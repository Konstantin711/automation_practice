from selenium.webdriver.common.by import By

from lesson_19.page_objects.apparel_shoes_page import ApparelShoesPage
from lesson_19.page_objects.books_page import BooksPage
from lesson_19.page_objects.cart_page import CartPage
from lesson_19.page_objects.computer_page import ComputerPage
from lesson_19.page_objects.customer_info_page import CustomerInfoPage
from lesson_19.page_objects.digital_page import DigitalPage
from lesson_19.page_objects.electronic_page import ElectronicPage
from lesson_19.page_objects.gift_cards_page import GiftCardPage
from lesson_19.page_objects.jewerly_page import JewerlyPage
from lesson_19.page_objects.main_page import MainPage
from lesson_19.page_objects.register_page import RegisterPage
from lesson_19.page_objects.search_page import SearchPage
from lesson_19.page_objects.wishlist_page import WishlistPage


class Header:
    _header_urls = {
        'customer_info': (By.XPATH, "//div[@class='header-links']//li//a[@href='/customer/info']"),
        'log_out': (By.XPATH, "//div[@class='header-links']//li//a[@href='/logout']"),
        'shopping_cart': (By.XPATH, "//div[@class='header-links']//li//a[@href='/cart']"),
        'wishlist': (By.XPATH, "//div[@class='header-links']//li//a[@href='/wishlist']"),
        'search_button': (By.XPATH, "//input[@value='Search']"),
        'register': (By.XPATH, "//div[@class='header-links']//li//a[@href='/register']"),
        'log_in': (By.XPATH, "//div[@class='header-links']//li//a[@href='/login']")
    }

    _header_pages = {
        'customer_info': CustomerInfoPage,
        'log_out': MainPage,
        'shopping_cart': CartPage,
        'wishlist': WishlistPage,
        'search_button': SearchPage,
        'register': RegisterPage,
        'log_in': MainPage,
    }
