from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_input_field = (By.XPATH, "//input[@id='Q']")
    __advanced_checkbox = (By.XPATH, "//input[@id='As']")
    __search_button = (By.XPATH, "//div[@class='buttons']//input[@type='submit']")
    __sort_by_menu_option = (By.XPATH, "//select[@id='products-orderby']")
    __display_per_page_option = (By.XPATH, "//select[@id='products-pagesize']")
    __view_as_option = (By.XPATH, "//select[@id='products-viewmode']")
    _page_title = (By.XPATH, "//div[@class='page-title']//h1")
    __all_cards = (By.XPATH, "//div[@class='details']")

    def fill_search_field(self, email):
        self._send_keys(self.__search_input_field, email)
        return self

    def set_advanced_checkbox(self):
        checkbox = self._wait_element(self.__advanced_checkbox)
        checkbox.click()
        return self

    def click_search_button(self):
        button = self._wait_element(self.__search_button)
        button.click()
        return self

    def fill_sort_option(self, value):
        self._send_keys(self.__sort_by_menu_option, value, is_clear=False)
        return self

    def fill_display_per_page_option(self, value):
        self._send_keys(self.__display_per_page_option, value)
        return self

    def fill_view_as_option(self, value):
        self._send_keys(self.__view_as_option, value)
        return self

    def get_all_product_cards(self):
        cards = self._wait_element(self.__all_cards, type_of='all_elements_located')
        goods_cards = []
        for card in cards:
            desc, price = card.text.split('\n')
            goods_cards.append((desc, price))
        return goods_cards
