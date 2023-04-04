from selenium.webdriver.common.by import By

from lesson_19.page_objects.base_page import BasePage
from lesson_19.page_objects.register_result_page import RegisterResultPage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __gender_male_checkbox = (By.XPATH, "//input[@id='gender-male']")
    __gender_female_checkbox = (By.XPATH, "//input[@id='gender-female']")
    __first_name_field = (By.XPATH, "//input[@id='FirstName']")
    __last_name_field = (By.XPATH, "//input[@id='LastName']")
    __email_field = (By.XPATH, "//input[@id='Email']")
    __password_field = (By.XPATH, "//input[@id='Password']")
    __confirm_password_field = (By.XPATH, "//input[@id='ConfirmPassword']")
    __register_button = (By.XPATH, "//input[@id='register-button']")

    def sign_gender_checkbox(self, gender):
        if gender == 'male':
            element = self._wait_element(self.__gender_male_checkbox)
            element.click()
        else:
            element = self._wait_element(self.__gender_female_checkbox)
            element.click()
        return self

    def fill_first_name_field(self, first_name):
        self._send_keys(self.__first_name_field, first_name)
        return self

    def fill_last_name_field(self, last_name):
        self._send_keys(self.__last_name_field, last_name)
        return self

    def fill_email_field(self, email):
        self._send_keys(self.__email_field, email)
        return self

    def fill_password_field(self, password):
        self._send_keys(self.__password_field, password)
        return self

    def fill_confirm_password_field(self, password):
        self._send_keys(self.__confirm_password_field, password)
        return self

    def click_register_button(self):
        elem = self._wait_element(self.__register_button)
        elem.click()
        return RegisterResultPage(self._driver)
