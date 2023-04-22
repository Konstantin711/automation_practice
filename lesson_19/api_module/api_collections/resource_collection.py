from ..api_collections.base_api import BaseAPI


class ResourceAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = 'some_url'

    def get_list_resource(self):
        pass

    def get_single_resource(self):
        pass

    def get_unexist_resource(self):
        pass
