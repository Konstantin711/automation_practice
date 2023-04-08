from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage


class RegisterResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __register_result = (By.XPATH, "//div[@class='result']")

    def get_page_title(self):
        label = self._wait_element(self.__register_result)
        return label.text
