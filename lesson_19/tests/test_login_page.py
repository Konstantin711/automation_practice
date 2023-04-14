import pytest
from ..utilities.config_parser import get_test_data, get_errors


def test_make_login(open_login_page):
    login_page = open_login_page

    email, password = get_test_data()

    login_page.set_email(email).set_password(password)
    main_page = login_page.click_remember_checkbox().click_login_button()

    signed_user = main_page.get_signed_value()
    assert signed_user == email, 'Sign up is successful'


def test_login_with_empty_email(open_login_page):
    login_page = open_login_page

    _, password = get_test_data()
    status_expected, cause_expected, _ = get_errors()

    login_page.set_password(password)
    login_page.click_remember_checkbox().click_login_button()

    status = login_page.get_login_error_status()
    cause = login_page.get_login_error_cause()

    assert status == status_expected, 'Status is incorrect'
    assert cause == cause_expected, 'Cause is incorrect'


def test_login_with_empty_password(open_login_page):
    login_page = open_login_page

    email, _ = get_test_data()
    status_expected, _, cause_expected = get_errors()

    login_page.set_email(email)
    login_page.click_remember_checkbox().click_login_button()

    status = login_page.get_login_error_status()
    cause = login_page.get_login_error_cause()

    assert status == status_expected, 'Status is incorrect'
    assert cause == cause_expected, 'Cause is incorrect'
