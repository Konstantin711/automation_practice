import pytest

from .page_objects.register_page import RegisterPage
from .page_objects.search_page import SearchPage
from .page_objects.login_page import LoginPage
from .page_objects.main_page import MainPage
from .page_objects.computer_page import ComputerPage

from .utilities.config_parser import get_custom_urls
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
