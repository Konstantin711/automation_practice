from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage


class CustomerInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __page_title = (By.XPATH, "//div[@class='page-title']//h1")
    __gender = {
        'male': (By.XPATH, "//input[@id='gender-male']"),
        'female': (By.XPATH, "//input[@id='gender-female']")
    }

    __first_name = (By.XPATH, "//input[@id='FirstName']")
    __first_name_error = (By.XPATH, "//span[@for='FirstName']")
    __last_name = (By.XPATH, "//input[@id='LastName']")
    __last_name_error = (By.XPATH, "//span[@for='LastName']")
    __email = (By.XPATH, "//input[@id='Email']")
    __email_error = (By.XPATH, "//span[@for='Email']")
    __save_button = (By.XPATH, "//div[@class='buttons']//input[@type='submit']")

    def get_title(self):
        title = self._wait_element(self.__page_title)
        return title.text

    def set_gender(self, gender: str):
        if gender == 'male':
            self._click_to_element(self.__gender['male'])
        elif gender == 'female':
            self._wait_element(self.__gender['female'])
        else:
            raise Exception('Gender can be : male or female')
        return self

    def set_first_name(self, first_name: str):
        self._send_keys(self.__first_name, first_name)
        return self

    def get_first_name_value(self):
        return self._get_element_attribute(self.__first_name, 'value')

    def set_last_name(self, last_name):
        self._send_keys(self.__last_name, last_name)
        return self

    def get_last_name_value(self):
        return self._get_element_attribute(self.__last_name, 'value')

    def set_email(self, email):
        self._send_keys(self.__email, email)
        return self

    def click_save_button(self):
        self._click_to_element(self.__save_button)
        return self

    def get_first_name_error(self):
        error = self._wait_element(self.__first_name_error)
        return error.text

    def get_last_name_error(self):
        error = self._wait_element(self.__last_name_error)
        return error.text

    def get_email_error(self):
        error = self._wait_element(self.__email_error)
        return error.text

