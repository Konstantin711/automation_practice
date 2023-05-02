"""
Implement baseMongo client with base methods like insert_one, insert_many, fint_one, find ...
implement one collection class, this class should inherit from the baseDB class and use its
functions to communicate with DB. Add main.py file where you use your code and print the result of this code.
"""

from lesson_26.mongo_queries import MongoQueries


documents = [
  {"name": "Amy", "address": "Apple st 652"},
  {"name": "Hannah", "address": "Mountain 21"},
  {"name": "Viola", "address": "Sideway 1633"}
]

document = {"name": "Peter2", "address": "Lowstreet 27"}
collection = MongoQueries('testDB', 'testCollection')

collection.insert_document(document)
collection.insert_many_documents(documents)

documents_custom_fields = collection.get_custom_fields({"_id": 0, "address": 1})
for document in documents:
    print(document)

documents_all = collection.get_all_data()
for document in documents_all:
    print(document)

one_document = collection.get_document_by_field({'name': 'Amy'})

updated_document = collection.update_document_field(find_data={'name': 'Hannah'},
                                                    field_to_update='address',
                                                    new_value='Updated Street')
