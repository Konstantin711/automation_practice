from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.__wait = WebDriverWait(driver, 10, 1)
        self._driver = driver

    def _wait_element(self, locator: tuple, type_of=None):
        if type_of == 'presence':
            return self.__wait.until(EC.presence_of_element_located(locator))
        elif type_of == 'clickable':
            return self.__wait.until(EC.element_to_be_clickable(locator))
        elif type_of == 'visible':
            return self.__wait.until(EC.visibility_of_element_located(locator))
        elif type_of == 'all_elements_located':
            return self.__wait.until(EC.visibility_of_all_elements_located(locator))
        else:
            return self.__wait.until(EC.presence_of_element_located(locator))

    def _send_keys(self, locator: tuple, value: str, is_clear: bool = True):
        element = self._wait_element(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

