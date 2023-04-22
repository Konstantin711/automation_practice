import requests


class BaseAPI:
    def __init__(self):
        self.__requests = requests
        self.__base_url = 'dase_url'
        self._headers = {}

    def _get(self, url: str, header: dict = None, params: str = None):
        pass

    def _post(self):
        pass

    def _put(self):
        pass

    def _patch(self):
        pass

    def _delete(self):
        pass
