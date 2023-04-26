import json
from http import HTTPStatus


from ...api_module.api_collections.register_collection import RegisterAPI


def test_successful_register(config_data):
    register_api = RegisterAPI(config_data)
    credentials = dict({'email': 'eve.holt@reqres.in', 'password': 'pistol'})
    response = register_api.make_register(body=json.dumps(credentials))

    assert response.status_code == HTTPStatus.OK, 'Status code is wrong'


def test_unsuccessful_register(config_data):
    register_api = RegisterAPI(config_data)

    credentials = dict({'email': 'eve.holt@reqres.in'})
    response = register_api.make_register(body=json.dumps(credentials))

    assert response.status_code == HTTPStatus.BAD_REQUEST, 'Status code is wrong'

    error_text = response.json()
    assert error_text['error'] == 'Missing password'
