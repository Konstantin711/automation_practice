import allure
import pytest


@allure.title('Change customer info')
@pytest.mark.regression
def test_change_customer_info(open_user_info_page, open_login_page, make_login):
    main_page = make_login

    with allure.step('Go to customer info'):
        main_page.click_header_link('customer_info')

        customer_info_page = open_user_info_page

        title = customer_info_page.get_title()
        assert title == 'My account - Customer info', 'Title is wrong'

    with allure.step('Set new data'):
        customer_info_page.set_first_name('New Name').set_last_name('Last Name').click_save_button()

        new_name = customer_info_page.get_first_name_value()
        new_last_name = customer_info_page.get_last_name_value()

        assert new_name == 'New Name' and new_last_name == 'Last Name', 'Values didn`t change'


@allure.title('Check error for empty name')
@pytest.mark.regression
def test_set_empty_name(open_user_info_page, open_login_page, make_login):
    user_info_page = open_user_info_page
    main_page = make_login

    with allure.step('Go to customer info page'):
        main_page.click_header_link('customer_info')

    with allure.step('Input data'):
        user_info_page.set_first_name('').set_last_name('Last Name').set_email('test@gmail.com').click_save_button()
        first_name_error = user_info_page.get_first_name_error()

        assert first_name_error == 'First name is required.', 'Error text is wrong'


@allure.title('Check error for last name')
@pytest.mark.smoke
def test_set_empty_last_name(open_user_info_page, open_login_page, make_login):
    user_info_page = open_user_info_page
    main_page = make_login

    with allure.step('Go to customer info page'):
        main_page.click_header_link('customer_info')

    with allure.step('Input data'):
        user_info_page.set_first_name('First Name').set_last_name('').set_email('test@gmail.com').click_save_button()
        last_name_error = user_info_page.get_last_name_error()

        assert last_name_error == 'Last name is required.', 'Error text is wrong'


@allure.title('Check error for email field')
@pytest.mark.smoke
def test_set_empty_email(open_user_info_page, open_login_page, make_login):
    user_info_page = open_user_info_page
    main_page = make_login

    with allure.step('Go to customer info page'):
        main_page.click_header_link('customer_info')

    with allure.step('Input data'):
        user_info_page.set_first_name('First Name').set_last_name('Last Name').set_email('').click_save_button()
        email_name_error = user_info_page.get_email_error()

        assert email_name_error == 'Email is required.', 'Error text is wrong'
