from lesson_19.utilities.config_parser import get_test_data
import time


def test_register_test(open_login_page, open_main_page):
    login_page = open_login_page
    email, password = get_test_data()

    main = login_page.set_email(email).set_password(password).click_button()
    main.get_account_page()


def test_register_page(open_register_page):
    register_page = open_register_page
    register_page.fill_first_name_field('Name')
    register_page.click_register_button()


def test_search_page(open_search_page):
    search_page = open_search_page

    search_page.fill_search_field('computer')
    search_page.click_search_button()
    search_page.fill_sort_option('Created on')
    time.sleep(5)
