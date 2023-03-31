from selenium.webdriver.common.by import By
from lesson_19.page_objects.main_page import MainPage
from lesson_19.page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email = (By.CSS_SELECTOR, '#Email')
    __password = (By.CSS_SELECTOR, '#Password')
    __log_in = (By.XPATH, "//input[@class='button-1 login-button']")

    def set_email(self, email: str):
        email_field = self._wait_element(self.__email, type_of='clickable')
        email_field.clear()
        email_field.send_keys(email)
        return self

    def set_password(self, password: str):
        password_field = self._wait_element(self.__password, type_of='visible')
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_button(self):
        button = self._wait_element(self.__log_in)
        button.click()
        return MainPage(self._driver)
