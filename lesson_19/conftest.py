import pytest
import random

from .page_objects.customer_info_page import CustomerInfoPage
from .page_objects.register_page import RegisterPage
from .page_objects.search_page import SearchPage
from .page_objects.login_page import LoginPage
from .page_objects.main_page import MainPage
from .page_objects.computer_page import ComputerPage

from .utilities.config_parser import get_custom_urls, get_test_data
from .utilities.browsers_factory import browsers_factory


@pytest.fixture
def get_browser():
    driver = browsers_factory('chrome')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def send_request_to_custom_url(get_browser):
    driver = get_browser

    def wrapper(url):
        urls = get_custom_urls(url)
        driver.get(urls)
        return driver
    return wrapper


@pytest.fixture
def open_register_page(send_request_to_custom_url):
    return RegisterPage(send_request_to_custom_url('register_url'))


@pytest.fixture
def open_search_page(send_request_to_custom_url):
    return SearchPage(send_request_to_custom_url('search_url'))


@pytest.fixture
def open_login_page(send_request_to_custom_url):
    return LoginPage(send_request_to_custom_url('login_url'))


@pytest.fixture
def open_main_page(send_request_to_custom_url):
    return MainPage(send_request_to_custom_url('main_url'))


@pytest.fixture
def open_computers_page(send_request_to_custom_url):
    return ComputerPage(send_request_to_custom_url('computer_url'))


@pytest.fixture
def open_user_info_page(send_request_to_custom_url):
    return CustomerInfoPage(send_request_to_custom_url('customer_info_url'))


@pytest.fixture
def make_login(get_browser):
    login_page = LoginPage(get_browser)
    email, password = get_test_data()
    login_page.set_password(password).set_email(email).click_login_button()
    return MainPage(get_browser)


@pytest.fixture
def generate_test_data():
    def wrapper(data_type: str):
        if data_type.lower() == 'valid':
            first_name = f'TestFirstName{random.randint(00, 99)}'
            last_name = f'TestLastName{random.randint(00, 99)}'
            email = f'email{random.randint(00000, 99999)}@testmail.ua'
            password = random.randint(0000000, 9999999)
        elif data_type.lower() == 'invalid':
            first_name = '!@##@#$#@'
            last_name = '#@#$##@!@'
            email = f'email{random.randint(00000, 99999)}testmail.ua'
            password = random.randint(00000, 99999)
        else:
            raise Exception('data_type can be "valid" or "invalid" value')

        return first_name, last_name, email, password
    return wrapper
