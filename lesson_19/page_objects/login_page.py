from selenium.webdriver.common.by import By

from .password_recovery_page import PasswordRecovery
from ..page_objects.base_page import BasePage
from ..page_objects.register_page import RegisterPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_field = (By.XPATH, "//input[@id='Email']")
    __password_field = (By.XPATH, "//input[@id='Password']")
    __log_in_button = (By.XPATH, "//input[@class='button-1 login-button']")
    __register_button = (By.XPATH, "//div[@class='buttons']//input[@class='button-1 register-button']")
    __remember_checkbox = (By.XPATH, "//input[@id='RememberMe']")
    __forgot_password = (By.XPATH, "//span[@class='forgot-password']//a")

    __login_error_status = (By.XPATH, "//div[@class='validation-summary-errors']//span")
    __login_error_cause = (By.XPATH, "//div[@class='validation-summary-errors']//ul//li")

    def set_email(self, email: str):
        self._send_keys(self.__email_field, email)
        return self

    def set_password(self, password: str):
        self._send_keys(self.__password_field, password)
        return self

    def click_login_button(self):
        self._click_to_element(self.__log_in_button)

        from ..page_objects.main_page import MainPage
        return MainPage(self._driver)

    def click_register_button(self):
        self._click_to_element(self.__register_button)
        return RegisterPage(self._driver)

    def click_remember_checkbox(self):
        self._click_to_element(self.__remember_checkbox)
        return self

    def click_forgot_password(self):
        self._click_to_element(self.__forgot_password)
        return PasswordRecovery(self._driver)

    def get_login_error_status(self):
        error = self._wait_element(self.__login_error_status)
        return error.text

    def get_login_error_cause(self):
        cause = self._wait_element(self.__login_error_cause)
        return cause.text
