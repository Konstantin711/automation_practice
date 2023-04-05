from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage


class BooksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __page_title = (By.XPATH, "//div[@class='page-title']//h1")

    def get_page_title(self):
        title = self._wait_element(self.__page_title)
        return title.text
