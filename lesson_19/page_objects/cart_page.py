from selenium.webdriver.common.by import By

from .order_status_page import OrderStatus
from ..page_objects.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _page_title = (By.XPATH, "//div[@class='page-title']//h1")
    __product_attributes = {
        'title': (By.XPATH, "//td[@class='product']//a[@class='product-name']"),
        'all_data': (By.XPATH, "//td[@class='product']//div[@class='attributes']")
    }
    __price = (By.XPATH, "//span[@class='product-unit-price']")
    __qty = (By.XPATH, "//input[@class='qty-input']")
    __total_price = (By.XPATH, "//span[@class='product-subtotal']")
    __country = (By.XPATH, "//select[@id='CountryId']")
    __zip = (By.XPATH, "//input[@id='ZipPostalCode']")
    __agree_checkbox = (By.XPATH, "//input[@id='termsofservice']")
    __checkout_button = (By.XPATH, "//button[@id='checkout']")

    __continue_billing_button = (By.XPATH, "//div[@id='billing-buttons-container']//input[@title='Continue']")

    __in_store_pickup_checkbox = (By.XPATH, "//input[@id='PickUpInStore']")
    __continue_shipping_button = (By.XPATH, "//div[@id='shipping-buttons-container']//input[@title='Continue']")

    __shipping_methods = {
        'ground': (By.XPATH, "//input[@id='shippingoption_0']"),
        'next_day_air': (By.XPATH, "//input[@id='shippingoption_1']"),
        'second_day_air': (By.XPATH, "//input[@id='shippingoption_2']"),
        'continue_button': (By.XPATH, "//div[@id='shipping-method-buttons-container']//input[@value='Continue']")
    }

    __payment_methods = {
        'cash': (By.XPATH, "//input[@id='paymentmethod_0']"),
        'check': (By.XPATH, "//input[@id='paymentmethod_1']"),
        'credit_card': (By.XPATH, "//input[@id='paymentmethod_2']"),
        'purchase': (By.XPATH, "//input[@id='paymentmethod_3']"),
        'continue_button': (By.XPATH, "//div[@id='payment-method-buttons-container']//input[@value='Continue']")
    }

    __payment_information_button = (By.XPATH, "//div[@id='payment-info-buttons-container']//input[@value='Continue']")
    __final_confirm = (By.XPATH, "//div[@id='confirm-order-buttons-container']//input[@value='Confirm']")

    def get_price(self):
        price = self._wait_element(self.__price)
        return price.text

    def get_qty(self):
        return self._get_element_attribute(self.__qty, 'value')

    def get_total_price(self):
        total_price = self._wait_element(self.__total_price)
        return total_price.text

    def set_country(self, country):
        self._send_keys(self.__country, country, is_clear=False)
        return self

    def set_zip(self, zip_code):
        self._send_keys(self.__zip, zip_code)
        return self

    def set_agree_checkbox(self):
        self._click_to_element(self.__agree_checkbox)
        return self

    def click_checkout_button(self):
        self._click_to_element(self.__checkout_button)
        return self

    def click_billing_button(self):
        self._click_to_element(self.__continue_billing_button, type_of='clickable')
        return self

    def set_in_store_pickup_checkbox(self):
        self._click_to_element(self.__in_store_pickup_checkbox)
        return self

    def click_shipping_address_button(self):
        self._click_to_element(self.__continue_shipping_button, type_of='clickable')
        return self

    def set_shipping_method(self, method):
        self._click_to_element(self.__shipping_methods[method])
        self._click_to_element(self.__shipping_methods['continue_button'])
        return self

    def set_payment_method(self, method):
        self._click_to_element(self.__payment_methods[method])
        self._click_to_element(self.__payment_methods['continue_button'])
        return self

    def click_payment_information_button(self):
        self._click_to_element(self.__payment_information_button, type_of='clickable')
        return self

    def click_final_button(self):
        self._click_to_element(self.__final_confirm, type_of='clickable')
        return OrderStatus(self._driver)
