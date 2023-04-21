from selenium.webdriver.common.by import By
from ..page_objects.base_page import BasePage


class RegisterResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    _register_result = (By.XPATH, "//div[@class='result']")
