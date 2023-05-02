from lesson_26.connection_db import MongoConnector
import json


class MongoQueries(MongoConnector):
    def __init__(self, db_name: str = None, collection_name: str = None):
        super().__init__(db_name, collection_name)

        self.__collection = self._connection()

    def insert_document(self, document: dict):
        return self.__collection.insert_one(document)

    def insert_many_documents(self, documents: list):
        return self.__collection.insert_many(documents)

    def get_custom_fields(self, fields: dict):
        return self.__collection.find({}, fields)

    def get_all_data(self):
        return self.__collection.find()

    def get_document_by_field(self, query: dict):
        return self.__collection.find(query)

    def update_document_field(self, find_data: dict, field_to_update: str, new_value: str):
        set_data = f'{{"$set": {{ "{field_to_update}": "{new_value}"}}}}'
        return self.__collection.update_one(find_data, json.loads(set_data))
