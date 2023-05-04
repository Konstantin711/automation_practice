from sqlalchemy import Column, MetaData, Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from ..session import engine

meta = MetaData()


Products = Table(
    'products',
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("price", Integer)
)

Orders = Table(
    'orders',
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("quantity", Integer),
    Column("product_id", Integer, ForeignKey("products.id"), nullable=False)
)

meta.create_all(engine)
