import pytest

from lesson_19.page_objects.main_page import MainPage
from page_objects.login_page import LoginPage

from lesson_19.utilities.config_parser import get_app_data
from lesson_19.utilities.browsers_factory import browsers_factory


@pytest.fixture
def get_browser():
    driver = browsers_factory('chrome')
    driver.maximize_window()
    driver.get(get_app_data())
    yield driver
    driver.quit()


@pytest.fixture
def open_login_page(get_browser):
    return LoginPage(get_browser)


@pytest.fixture
def open_main_page(get_browser):
    return MainPage(get_browser)
