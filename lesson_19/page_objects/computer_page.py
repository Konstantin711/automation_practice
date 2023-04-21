from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage
from .computer_product_page import ComputerProductPage


class ComputerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _page_title = (By.XPATH, "//div[@class='page-title']//h1")
    __all_cards = (By.XPATH, "//div[@class='add-info']//div[@class='buttons']//input[@type='button']")
    __cards = (By.XPATH, "//div[@class='details']")
    __login_page_url = (By.XPATH, "//a[@href='/login']")

    description = ''
    price = ''

    def add_product_to_cart(self, product_index: int):
        """Add product to cart at Computer Page"""
        cards = self._wait_element(self.__cards, type_of='all_elements_located')

        for index, card in enumerate(cards):
            if index == product_index:
                self.description, self.price = card.text.split('\n')
                try:
                    card.find_element(By.CSS_SELECTOR, "input").click()
                    return ComputerProductPage(self._driver)
                except:
                    raise Exception('Button is absent in current card')
