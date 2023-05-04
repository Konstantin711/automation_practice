import pymongo


class MongoConnector:
    def __init__(self, db_name: str = None, collection_name: str = None):
        self.__url = "mongodb://localhost:27017/"
        self.__db_name = db_name
        self.__collection_name = collection_name

    def _connection(self):
        connection = pymongo.MongoClient(self.__url)

        if self.__db_name is not None:
            db = connection[self.__db_name]
            if self.__collection_name is not None:
                collection: pymongo.collection.Collection = db[self.__collection_name]
                return collection
            else:
                raise Exception('Name for collection not set')
        else:
            raise Exception('Name for table not set')
