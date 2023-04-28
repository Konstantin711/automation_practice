from ..api_collections.base_api import BaseAPI


class RegisterAPI(BaseAPI):
    def __init__(self, config_data: dict):
        super().__init__(config_data)
        self.__register = 'register'

    def make_register(self, headers: dict = None, body: str = None, params: str = None):
        return self._post(url=self.__register, headers=headers, params=params, body=body)
