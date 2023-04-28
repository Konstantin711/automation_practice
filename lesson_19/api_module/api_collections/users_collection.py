from ..api_collections.base_api import BaseAPI


class UsersAPI(BaseAPI):
    def __init__(self, config_data: dict):
        super().__init__(config_data)
        self.__all_users = f'users?page=%d'
        self.__single_user = f'users/%d'
        self.__create_user = 'users'

    def get_users_list(self, page_id: int = None, headers: dict = None, params: str = None):
        return self._get(url=self.__all_users % page_id, headers=headers, params=params)

    def get_single_user(self, user_id: int = None, headers: dict = None, params: str = None):
        return self._get(url=self.__single_user % user_id, headers=headers, params=params)

    def create_user(self, body: dict = None, headers: dict = None, params: str = None):
        return self._post(url=self.__create_user, headers=headers, params=params, body=body)

    def update_user(self, user_id: int = None, body: dict = None, headers: dict = None):
        return self._put(url=self.__single_user % user_id, headers=headers, body=body)

    def delete_user(self, user_id: int = None, headers: dict = None):
        return self._delete(url=self.__single_user % user_id, headers=headers)
