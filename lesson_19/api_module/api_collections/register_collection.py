from ..api_collections.base_api import BaseAPI


class RegisterAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = 'some_url'

    def make_successful_register(self):
        pass

    def make_unsuccessful_register(self):
        pass
