from lesson_19.utilities.config_parser import get_test_data


def test_first_test(open_login_page, open_main_page):
    login_page = open_login_page
    email, password = get_test_data()

    main = login_page.set_email(email).set_password(password).click_button()
    main.get_account_page()


def test_main_page(open_main_page):
    main_page = open_main_page

    main_page.send_keys_search('computer')
    main_page.click_search_button()

