from ..api_collections.base_api import BaseAPI


class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = 'some_url'

    def get_users_list(self):
        pass

    def get_single_user(self):
        pass

    def get_unexist_user(self):
        pass

    def create_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass