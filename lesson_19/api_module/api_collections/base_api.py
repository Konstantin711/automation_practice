import json
import os

import requests


def config_data():
    __CONFIG_PATH = os.path.abspath('../configurations/api_config.json')

    with open(__CONFIG_PATH, 'r') as file:
        json_obj = json.loads(file.read())

    return json_obj
    # return JsonParser(**json_obj)


class BaseAPI:
    def __init__(self):
        self.__requests = requests
        self.__base_url = 'dase_url'
        self.__headers = {}

    def _get(self, url: str, headers: dict = None, params: str = None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', params=params, headers=headers)
        return response

    def _post(self, url: str, body: dict = None, headers: dict = None, params: str = None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.post(f'{self.__base_url}{url}', json=body, params=params, headers=headers)
        return response

    def _put(self, url: str, data: dict = None, headers: dict = None):
        if headers is None:
            headers = self.__headers
        response = self.__requests.put(f'{self.__base_url}{url}', data=data, headers=headers)
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
