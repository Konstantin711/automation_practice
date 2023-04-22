from ..api_collections.base_api import BaseAPI


class LoginAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = 'some_url'

    def make_successful_login(self):
        pass

    def make_unsuccessful_login(self):
        pass
