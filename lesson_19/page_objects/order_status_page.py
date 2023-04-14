from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage


class OrderStatus(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __page_title = (By.XPATH, "//div[@class='page-title']//h1[contains(text(), 'Thank')]")
    __order_status = (By.XPATH, "//div[@class='title']//strong")
    __continue_button = (By.XPATH, "//div[@class='buttons']//input[@value='Continue']")

    def get_page_title(self):
        title = self._wait_element(self.__page_title, type_of='visible_of')
        return title.text

    def get_order_status(self):
        status = self._wait_element(self.__order_status)
        return status.text

    def click_continue_button(self):
        from .main_page import MainPage
        self._wait_element(self.__continue_button).click()
        return MainPage(self._driver)
