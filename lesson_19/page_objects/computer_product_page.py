from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage
from .cart_page import CartPage


class ComputerProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __product_title = (By.XPATH, "//div[@class='product-name']//h1")
    __cart_page = (By.XPATH, "//li[@id='topcartlink']//a[@href='/cart']")
    __processor_radio_buttons = {
        'slow': (By.XPATH, "//label[contains(text(), 'Slow')]"),
        'medium': (By.XPATH, "//label[contains(text(), 'Medium')]"),
        'fast': (By.XPATH, "//label[contains(text(), 'Fast')]")
    }
    __ram_radio_buttons = {
        '8_gb': (By.XPATH, "//label[contains(text(), '8 GB') or contains(text(), '8GB')]"),
        '2_gb': (By.XPATH, "//label[contains(text(), '2 GB') or contains(text(), '2GB')]"),
        '4_gb': (By.XPATH, "//label[contains(text(), '4 GB') or contains(text(), '4GB')]")
    }
    __hdd_radio_buttons = {
        '320_gb': (By.XPATH, "//label[contains(text(), '320 GB')]"),
        '400_gb': (By.XPATH, "//label[contains(text(), '400 GB')]")
    }
    __software = {
        'image_viewer': (By.XPATH, "//label[contains(text(), 'Image Viewer')]"),
        'office_suite': (By.XPATH, "//label[contains(text(), 'Office Suite  [+100.00]')]"),
        'other_office_suite': (By.XPATH, "//label[contains(text(), 'Other Office Suite  [+40.00]')]")
    }
    __price = (By.XPATH, "//span[@itemprop='price']")
    __qty = (By.XPATH, "//input[@class='qty-input']")
    __add_to_cart = (By.XPATH, "//div[@class='add-to-cart']//input[@type='button']")

    def set_processor_radio(self, value: str):
        if value.lower() in self.__processor_radio_buttons.keys():
            radio = self._wait_element(self.__processor_radio_buttons[value.lower()])
            radio.click()
        else:
            raise Exception(f'Value can be: {self.__processor_radio_buttons.keys()}')
        return self

    def set_ram_radio(self, value: str):
        if value.lower() in self.__ram_radio_buttons.keys():
            radio = self._wait_element(self.__ram_radio_buttons[value.lower()])
            radio.click()
        else:
            raise Exception(f'Value can be: {self.__ram_radio_buttons.keys()}')
        return self

    def set_hdd_radio(self, value: str):
        if value.lower() in self.__hdd_radio_buttons.keys():
            radio = self._wait_element(self.__hdd_radio_buttons[value.lower()])
            radio.click()
        else:
            raise Exception(f'Value can be: {self.__hdd_radio_buttons.keys()}')
        return self

    def set_additional_options(self, values: list):
        for value in values:
            if value.lower() not in self.__software.keys():
                raise Exception(f'Value can be: {self.__software.keys()}')
            checkbox = self._wait_element(self.__software[value.lower()])
            checkbox.click()
        return self

    def get_product_title(self):
        title = self._wait_element(self.__product_title, type_of='visible')
        return title.text

    def get_current_price(self):
        price = self._wait_element(self.__price)
        return price.text

    def set_qty(self, value: str):
        self._send_keys(self.__qty, value)
        return self

    def add_to_cart(self):
        button = self._wait_element(self.__add_to_cart, type_of='clickable')
        button.click()
        return self

    def go_to_cart_page(self):
        page = self._wait_element(self.__cart_page, type_of='clickable')
        page.click()

        return CartPage(self._driver)

