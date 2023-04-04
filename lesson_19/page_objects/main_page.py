from selenium.webdriver.common.by import By

from lesson_19.page_objects.account_page import AccountPage
from lesson_19.page_objects.base_page import BasePage
from lesson_19.page_objects.register_page import RegisterPage
from lesson_19.page_objects.cart_page import Cart
from lesson_19.page_objects.static_elements.header import Header
from lesson_19.page_objects.wishlist_page import Wishlist
from lesson_19.page_objects.search_page import SearchPage
from lesson_19.page_objects.static_elements.header_navigation import HeaderNavigation


class MainPage(BasePage, HeaderNavigation, Header):
    def __init_(self, driver):
        super(BasePage).__init__(driver)

    __register_page = (By.XPATH, "//a[@class='ico-register']")
    __all_cards = (By.XPATH, "//div[@class='details']")
    __search_field = (By.XPATH, "//input[@id='small-searchterms']")

    def get_header_link(self, url, action: str):
        page = self._wait_element(self._header_urls[url])
        if url not in self._header_urls.keys():
            raise Exception(f'Value can be any key in:{self._header_urls.keys()}')
        elif action.lower() == 'text':
            return page.text
        elif action.lower() == 'click':
            page.click()
            return self._header_pages[url](self._driver)
        else:
            raise Exception('Result should be "click" or "text" value')

    def send_keys_search(self, keys):
        self._send_keys(self.__search_field, keys)
        return self

    def get_navigation_link(self, url, result='text'):
        element = self._wait_element(self._urls[url])
        if result.lower() == 'text':
            return element.text
        elif result.lower() == 'click':
            element.click()
            return self._pages[url](self._driver)
        else:
            raise Exception('Result should be "click" or "text" value')

    def get_all_product_cards(self):
        cards = self._wait_element(self.__all_cards, type_of='all_elements_located')
        goods_cards = []
        for card in cards:
            desc, price = card.text.split('\n')
            link = card.find_element(By.XPATH, "//div[@class='add-info']//div[@class='buttons']//input[@type='button']")
            goods_cards.append((desc, price, link))
        return goods_cards
