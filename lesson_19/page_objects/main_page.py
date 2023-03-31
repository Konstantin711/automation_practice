from selenium.webdriver.common.by import By

from lesson_19.page_objects.account_page import AccountPage
from lesson_19.page_objects.base_page import BasePage
from lesson_19.page_objects.register_page import RegisterPage
from lesson_19.page_objects.cart_page import Cart
from lesson_19.page_objects.wishlist_page import Wishlist
from lesson_19.page_objects.search_page import SearchPage
from lesson_19.page_objects.books_page import BooksPage
from lesson_19.page_objects.computer_page import ComputerPage


class MainPage(BasePage):
    def __init_(self, driver):
        super().__init__(driver)

    __register_page = (By.XPATH, "//a[@class='ico-register']")
    __account_page = (By.XPATH, "//a[@class='account' and text() != 'My account']")
    __log_in_page = (By.XPATH, "//a[@class='ico-login']")
    __cart = (By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']")
    __wishlist = (By.XPATH, "//div[@class='header-links-wrapper']//li//a[@class='ico-wishlist']")
    __search_field = (By.XPATH, "//input[@id='small-searchterms']")
    __search_button = (By.XPATH, "//input[@value='Search']")
    __books_url = (By.XPATH, "//ul[@class='top-menu']//a[contains(text(), 'Books')]")
    __computers_url = (By.XPATH, "//ul[@class='top-menu']//a[contains(text(), 'Computers')]")

    def click_register_page(self):
        page = self._wait_element(self.__register_page)
        page.click()
        return RegisterPage

    def get_account_page(self):
        page = self._wait_element(self.__account_page)
        page.click()
        return AccountPage

    def click_log_out(self):
        page = self._wait_element(self.__log_in_page)
        page.click()
        return MainPage(self._driver)

    def get_cart_page(self):
        page = self._wait_element(self.__cart)
        page.click()
        return Cart(self._driver)

    def get_wishlist_page(self):
        page = self._wait_element(self.__wishlist)
        page.click()
        return Wishlist(self._driver)

    def send_keys_search(self, keys):
        self._send_keys(self.__search_field, keys)

    def click_search_button(self):
        self._wait_element(self.__search_button).click()
        return SearchPage(self._driver)

    def get_books_page(self):
        page = self._wait_element(self.__books_url)
        page.click()
        return BooksPage(self._driver)

    def get_computers_page(self):
        page = self._wait_element(self.__computers_url)
        page.click()
        return ComputerPage(self._driver)
