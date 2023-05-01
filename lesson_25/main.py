from lesson_25.db_repository.store_repository import StoreRepository

if __name__ == '__main__':
    store = StoreRepository()
    # store.add_to_products(name='Samsung', price=800)
    # store.add_to_products(name='Iphone', price=1500)
    # store.add_to_products(name='Motorola', price=700)
    # store.add_to_products(name='Xiaomi', price=400)
    # store.add_to_products(name='Nokia', price=500)

    # store.add_to_orders(qty=5, product_id=2)
    # store.add_to_orders(qty=12, product_id=3)
    # store.add_to_orders(qty=33, product_id=4)
    # store.add_to_orders(qty=1, product_id=5)
    # store.add_to_orders(qty=32, product_id=6)

    res = store.custom_select()