import allure
import pytest


@allure.title('Valid login')
@pytest.mark.smoke
def test_valid_login(open_register_page, generate_test_data):
    register_page = open_register_page

    first_name, last_name, email, password = generate_test_data('valid')
    register_page.sign_gender_checkbox('male')
    register_page.fill_first_name_field(first_name)
    register_page.fill_last_name_field(last_name)
    register_page.fill_email_field(email)
    register_page.fill_password_field(password)
    register_page.fill_confirm_password_field(password)
    register_result = register_page.click_register_button()

    label = register_result.get_page_title(title_selector=register_result._register_result)
    assert label == 'Your registration completed', 'Registration is failed'


@allure.title('Check wrong email set')
@pytest.mark.smoke
def test_wrong_email_set(open_register_page, generate_test_data):
    register_page = open_register_page

    _, _, email, _ = generate_test_data('invalid')
    first_name, last_name, _, password = generate_test_data('valid')

    register_page.sign_gender_checkbox('female')
    register_page.fill_first_name_field(first_name)
    register_page.fill_last_name_field(last_name)
    register_page.fill_email_field(email)
    register_page.fill_password_field(password)
    register_page.fill_confirm_password_field(password)
    register_page.click_register_button()

    register_result = register_page.get_email_error()

    assert register_result == 'Wrong email', 'Message about invalid email is wrong'


@allure.title('Check wrong password field')
@pytest.mark.smoke
def test_wrong_password_set(open_register_page, generate_test_data):
    register_page = open_register_page

    first_name, last_name, email, password = generate_test_data('valid')
    _, _, _, wrong_password = generate_test_data('invalid')

    register_page.fill_first_name_field(first_name)
    register_page.fill_last_name_field(last_name)
    register_page.fill_email_field(email)
    register_page.fill_password_field(wrong_password).fill_confirm_password_field(wrong_password)
    register_page.click_register_button()

    password_error = register_page.get_password_error()

    assert password_error == 'The password should have at least 6 characters.', \
        'Password error field is wrong'


@allure.title('Check different passwords')
@pytest.mark.smoke
def test_set_different_passwords(open_register_page, generate_test_data):
    register_page = open_register_page

    first_name, last_name, email, password = generate_test_data('valid')
    _, _, _, wrong_password = generate_test_data('invalid')

    register_page.fill_first_name_field(first_name)
    register_page.fill_last_name_field(last_name)
    register_page.fill_email_field(email)
    register_page.fill_password_field(password).fill_confirm_password_field(wrong_password)
    register_page.click_register_button()

    repeat_password_error = register_page.get_repeat_password_error()

    assert repeat_password_error == 'The password and confirmation password do not match.', \
        'Repeat name error field is wrong'


@allure.title('Check empty name field')
@pytest.mark.smoke
def test_let_name_empty(open_register_page, generate_test_data):
    register_page = open_register_page

    _, last_name, email, password = generate_test_data('valid')

    register_page.fill_last_name_field(last_name)
    register_page.fill_email_field(email)
    register_page.fill_password_field(password).fill_confirm_password_field(password)
    register_page.click_register_button()

    error = register_page.get_first_name_error()

    assert error == 'First name is required.', 'First name error field is wrong'


@allure.title('Check last name empty')
@pytest.mark.regression
def test_let_last_name_empty(open_register_page, generate_test_data):
    register_page = open_register_page

    first_name, _, email, password = generate_test_data('valid')

    register_page.fill_first_name_field(first_name)
    register_page.fill_email_field(email)
    register_page.fill_password_field(password).fill_confirm_password_field(password)
    register_page.click_register_button()

    error = register_page.get_last_name_error()

    assert error == 'Last name is required.', 'Last name error field is wrong'


@allure.title('Check empty email field')
@pytest.mark.smoke
def test_let_email_empty(open_register_page, generate_test_data):
    register_page = open_register_page

    first_name, last_name, _, password = generate_test_data('valid')

    register_page.fill_first_name_field(first_name)
    register_page.fill_last_name_field(last_name)
    register_page.fill_password_field(password).fill_confirm_password_field(password)
    register_page.click_register_button()

    error = register_page.get_email_error()

    assert error == 'Email is required.', 'Email error field is wrong'


@allure.title('Check empty password field')
@pytest.mark.regression
def test_let_password_empty(open_register_page, generate_test_data):
    register_page = open_register_page

    first_name, last_name, email, password = generate_test_data('valid')

    register_page.fill_first_name_field(first_name)
    register_page.fill_last_name_field(last_name)
    register_page.fill_email_field(email)
    register_page.fill_confirm_password_field(password)
    register_page.click_register_button()

    error = register_page.get_password_error()

    assert error == 'Password is required.', 'Password error field is wrong'


@allure.title('Check repeat password field')
@pytest.mark.regression
def test_let_repeat_password_empty(open_register_page, generate_test_data):
    register_page = open_register_page

    first_name, last_name, email, password = generate_test_data('valid')

    register_page.fill_first_name_field(first_name)
    register_page.fill_last_name_field(last_name)
    register_page.fill_email_field(email)
    register_page.fill_password_field(password)
    register_page.click_register_button()

    error = register_page.get_repeat_password_error()

    assert error == 'Password is required.', 'Repeat password error field is wrong'
