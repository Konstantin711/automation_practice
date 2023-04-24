from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage
from .login_page import LoginPage
from .search_page import SearchPage
from ..page_objects.static_elements.header_element import Header
from ..page_objects.static_elements.header_navigation import HeaderNavigation
from .computer_page import ComputerPage


class MainPage(BasePage, HeaderNavigation, Header):
    def __init_(self, driver):
        super(BasePage).__init__(driver)

    __all_cards = (By.XPATH, "//div[@class='details']")
    __search_field = (By.XPATH, "//input[@id='small-searchterms']")
    __log_out = (By.XPATH, "//div[@class='header-links']//li//a[@href='/logout']")
    __log_in = (By.XPATH, "//div[@class='header-links']//li//a[@href='/login']")
    __signed_user = (By.XPATH, "//div[@class='header-links']//ul//li//a[@href='/customer/info']")

    __computers_url = (By.XPATH, "//ul[@class='top-menu']//a[contains(text(), 'Computers')]")
    __desktops_url = (By.XPATH, "//div[@class='header-menu']//ul[@class='top-menu']"
                                "//ul//li//a[contains(text(),'Desktops')]")

    def get_header_link_text(self, url):
        if url not in self._header_urls.keys():
            raise Exception(f'Value can be any key in:{self._header_urls.keys()}')
        return self._wait_element(self._header_urls[url]).text

    def click_header_link(self, url):
        if url not in self._header_urls.keys():
            raise Exception(f'Value can be any key in:{self._header_urls.keys()}')
        self._click_to_element(self._header_urls[url])
        return self._header_pages[url](self._driver)

    def click_login(self):
        self._click_to_element(self.__log_in)
        return LoginPage(self._driver)

    def make_logout(self):
        self._click_to_element(self.__log_out)
        return MainPage(self._driver)

    def get_signed_value(self):
        name = self._wait_element(self.__signed_user)
        return name.text

    def get_unsigned_value(self):
        name = self._wait_element(self._header_urls['register'])
        return name.text

    def send_keys_search(self, keys: str):
        self._send_keys(self.__search_field, keys)
        return self

    def click_search_button(self):
        self._click_to_element(self._header_urls['search_button'])
        return SearchPage(self._driver)

    def get_navigation_link_text(self, url):
        if url not in self._urls.keys():
            raise Exception(f'Value can be any key in:{self._urls.keys()}')
        return self._wait_element(self._urls[url]).text

    def get_navigation_link(self, url):
        if url not in self._urls.keys():
            raise Exception(f'Value can be any key in:{self._urls.keys()}')
        self._click_to_element(self._urls[url])
        return self._pages[url](self._driver)

    def get_all_product_cards(self):
        cards = self._wait_element(self.__all_cards, type_of='all_elements_located')
        goods_cards = [(card.text.split('\n')) for card in cards]

        return goods_cards

    def open_computer_page(self):
        self.hover_to_element(self._driver, hover_to=self.__computers_url, click_on=self.__desktops_url)
        return ComputerPage(self._driver)
