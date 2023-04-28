import requests


class BaseAPI:
    def __init__(self, config_data: dict):
        self.__requests = requests
        self.__base_url = config_data.api_link['url']
        self.__headers = {'content-type': 'application/json'}

    def _get(self, url: str, headers: dict = None, params: str = None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', params=params, headers=headers)
        return response

    def _post(self, url: str, body: dict = None, headers: dict = None, params: str = None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.post(f'{self.__base_url}{url}', data=body, params=params, headers=headers)
        return response

    def _put(self, url: str, body: dict = None, headers: dict = None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.put(f'{self.__base_url}{url}', data=body, headers=headers)
        return response

    def _patch(self, url, data: dict = None, headers: dict = None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.patch(f'{self.__base_url}{url}', data=data, headers=headers)
        return response

    def _delete(self, url: str, headers: dict = None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.delete(f'{self.__base_url}{url}', headers=headers)
        return response
