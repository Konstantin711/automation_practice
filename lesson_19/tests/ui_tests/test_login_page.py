import allure
import pytest


@allure.title('Positive login')
@pytest.mark.smoke
def test_make_login(open_login_page, config_data):
    login_page = open_login_page

    email = config_data.test_data['email']
    password = config_data.test_data['password']

    with allure.step('Make login'):
        login_page.set_email(email).set_password(password)
        main_page = login_page.click_remember_checkbox().click_login_button()

        signed_user = main_page.get_signed_value()
        assert signed_user == email, 'Sign up is successful'


@allure.title('Check error for email field')
@pytest.mark.smoke
def test_login_with_empty_email(open_login_page, config_data):
    login_page = open_login_page

    password = config_data.test_data['password']

    status_expected = config_data.login_errors['status']
    cause_expected = config_data.login_errors['no_customer_found']

    with allure.step('Make login'):
        login_page.set_password(password)
        login_page.click_remember_checkbox().click_login_button()

        status = login_page.get_login_error_status()
        cause = login_page.get_login_error_cause()

        assert status == status_expected, 'Status is incorrect'
        assert cause == cause_expected, 'Cause is incorrect'


@allure.title('Check error for password field')
@pytest.mark.smoke
def test_login_with_empty_password(open_login_page, config_data):
    login_page = open_login_page

    email = config_data.test_data['email']
    status_expected = config_data.login_errors['status']
    cause_expected = config_data.login_errors['wrong_password']

    with allure.step('Make login'):
        login_page.set_email(email)
        login_page.click_remember_checkbox().click_login_button()

        status = login_page.get_login_error_status()
        cause = login_page.get_login_error_cause()

        assert status == status_expected, 'Status is incorrect'
        assert cause == cause_expected, 'Cause is incorrect'
