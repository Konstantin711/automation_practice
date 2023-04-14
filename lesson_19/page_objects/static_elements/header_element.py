from selenium.webdriver.common.by import By

from ..customer_info_page import CustomerInfoPage
from ..register_page import RegisterPage
from ..search_page import SearchPage
from ..wishlist_page import WishlistPage
from ..cart_page import CartPage


class Header:
    _header_urls = {
        'customer_info': (By.XPATH, "//div[@class='header-links']//li//a[@href='/customer/info']"),
        'shopping_cart': (By.XPATH, "//div[@class='header-links']//li//a[@href='/cart']"),
        'wishlist': (By.XPATH, "//div[@class='header-links']//li//a[@href='/wishlist']"),
        'search_button': (By.XPATH, "//input[@value='Search']"),
        'register': (By.XPATH, "//div[@class='header-links']//li//a[@href='/register']")
    }

    _header_pages = {
        'customer_info': CustomerInfoPage,
        'shopping_cart': CartPage,
        'wishlist': WishlistPage,
        'search_button': SearchPage,
        'register': RegisterPage,
    }

