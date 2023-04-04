import pytest

from lesson_19.page_objects.main_page import MainPage
from lesson_19.page_objects.login_page import LoginPage
from lesson_19.page_objects.register_page import RegisterPage
from lesson_19.page_objects.search_page import SearchPage

from lesson_19.utilities.config_parser import get_site_urls
from lesson_19.utilities.browsers_factory import browsers_factory


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
        urls = get_site_urls(url)
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
def open_login_page(get_browser):
    return LoginPage(get_browser)


@pytest.fixture
def open_main_page(send_request_to_custom_url):
    return MainPage(send_request_to_custom_url('main_url'))
