import json
from http import HTTPStatus

import allure

from ...api_module.api_collections.login_collection import LoginAPI


@allure.title('Check successful login')
def test_successful_login(config_data):
    register_api = LoginAPI(config_data)
    credentials = dict({'email': 'eve.holt@reqres.in', 'password': 'pistol'})
    response = register_api.make_login(body=json.dumps(credentials))

    assert response.status_code == HTTPStatus.OK, 'Status code is wrong'


@allure.title('Check unsuccessful login')
def test_unsuccessful_login(config_data):
    register_api = LoginAPI(config_data)

    credentials = dict({'email': 'eve.holt@reqres.in'})
    response = register_api.make_login(body=json.dumps(credentials))

    assert response.status_code == HTTPStatus.BAD_REQUEST, 'Status code is wrong'

    error_text = response.json()
    assert error_text['error'] == 'Missing password'
