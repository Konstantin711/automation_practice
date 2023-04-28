from http import HTTPStatus

import allure
import pytest
from ...api_module.api_collections.users_collection import UsersAPI
from ...data_objects.person_data import PersonData


@allure.title('Check len of users on page')
@pytest.mark.parametrize('page_id', [1, 2, 3])
def test_len_users_on_page(config_data, page_id):
    user_api = UsersAPI(config_data)
    response = user_api.get_users_list(page_id=page_id).json()

    if page_id == 3:
        assert len(response['data']) == 0, 'Quantity of elements is wrong'
    else:
        assert len(response['data']) == 6, 'Quantity of elements is wrong'


@allure.title('Check single user data')
def test_single_user(config_data, person_data):
    user_api = UsersAPI(config_data)

    expected_person = person_data
    response = user_api.get_single_user(user_id=1).json()
    current_person = PersonData(**response)

    assert expected_person == current_person, 'Person data is wrong'


@allure.title('Check new user creation')
def test_create_new_user(config_data):
    user_api = UsersAPI(config_data)

    data = PersonData(id='555',
                      first_name='Homer',
                      last_name='Simpson',
                      email='homer122@gmail.com')
    response = user_api.create_user(body=data.get_json())
    assert response.status_code == HTTPStatus.CREATED, 'Status code is wrong'

    created_user = PersonData(**response.json())
    assert data == created_user, 'Person data is wrong'


@allure.title('Check user data update')
def test_update_user(config_data):
    user_api = UsersAPI(config_data)
    data = PersonData(id='555',
                      first_name='Barny',
                      last_name='Gamble',
                      email='barny@gmail.com')
    response = user_api.update_user(body=data.get_json(), user_id=2)
    assert response.status_code == HTTPStatus.OK, 'Status code is wrong'

    updated_user = PersonData(**response.json())
    assert data == updated_user, 'Person data is wrong'


@allure.title('Check user deletion')
def test_delete_user(config_data):
    user_api = UsersAPI(config_data)
    response = user_api.delete_user(user_id=2)

    assert response.status_code == HTTPStatus.NO_CONTENT, 'Status code is wrong'
