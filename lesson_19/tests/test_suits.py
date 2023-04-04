from lesson_19.utilities.config_parser import get_test_data
from lesson_19.page_objects.static_elements.header_navigation import HeaderNavigation

import time


def test_register_test(open_login_page, open_main_page):
    login_page = open_login_page
    email, password = get_test_data()

    main = login_page.set_email(email).set_password(password).click_button()
    main.get_account_page()


def test_main_page(open_main_page):
    main_page_driver = open_main_page

    # link_text = main_page_driver.get_books_link(url='books_url', result='text')
    # assert link_text == 'BOOKS', 'Text is wrong'

    cards = main_page_driver.get_all_product_cards()
    for card in cards:
        a, b, c = card

        c.click()
        time.sleep(5)


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
