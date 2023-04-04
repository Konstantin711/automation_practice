from selenium.webdriver.common.by import By
from lesson_19.page_objects.main_page import MainPage
from lesson_19.page_objects.base_page import BasePage
from lesson_19.page_objects.register_page import RegisterPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_field = (By.XPATH, "//input[@id='Email']")
    __password_field = (By.XPATH, "//input[@id='Password']")
    __log_in_button = (By.XPATH, "//input[@class='button-1 login-button']")
    __register_button = (By.XPATH, "//div[@class='buttons']//input[@class='button-1 register-button']")

    def set_email(self, email: str):
        email_field = self._wait_element(self.__email_field, type_of='clickable')
        email_field.clear()
        email_field.send_keys(email)
        return self

    def set_password(self, password: str):
        password_field = self._wait_element(self.__password_field, type_of='visible')
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login_button(self):
        button = self._wait_element(self.__log_in_button)
        button.click()
        return MainPage(self._driver)

    def click_register_button(self):
        button = self._wait_element(self.__register_button)
        button.click()
        return RegisterPage(self._driver)
