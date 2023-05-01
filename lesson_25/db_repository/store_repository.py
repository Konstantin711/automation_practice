from ..models.store_tables import Products as p
from ..models.store_tables import Orders as o
from sqlalchemy.orm import join
from ..session import session
from sqlalchemy import insert, select


class StoreRepository:
    def __init__(self):
        self.__session = session

    def add_to_products(self, name, price):
        insert_data = insert(P).values(name=name, price=price)
        self.__session.execute(insert_data)
        self.__session.commit()

    def add_to_orders(self, qty, product_id):
        insert_data = insert(O).values(quantity=qty, product_id=product_id)
        self.__session.execute(insert_data)
        self.__session.commit()

    def custom_select(self):
        join_cond = p.c.id == o.c.product_id

        stmt = select(
            p.c.name,
            p.c.price,
            o.c.quantity,
            (p.c.price * o.c.quantity).label('total')
        ).select_from(join(p, o, join_cond, isouter=True))

        return self.__session.execute(stmt).fetchall()
