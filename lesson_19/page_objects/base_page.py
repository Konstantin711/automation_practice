from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.__wait = WebDriverWait(driver, 10, 1)
        self._driver = driver

    def _wait_element(self, locator: tuple, type_of: str = None):
        if type_of == 'clickable':
            return self.__wait.until(EC.element_to_be_clickable(locator))
        elif type_of == 'visible':
            return self.__wait.until(EC.visibility_of_element_located(locator))
        elif type_of == 'all_elements_located':
            return self.__wait.until(EC.visibility_of_all_elements_located(locator))
        else:
            return self.__wait.until(EC.presence_of_element_located(locator))

    def _get_element_attribute(self, locator: tuple, attribute: str):
        return self._wait_element(locator).get_attribute(attribute)

    def _click_to_element(self, locator: tuple, type_of: str = 'Any'):
        return self._wait_element(locator, type_of).click()

    def _send_keys(self, locator: tuple, value: str, is_clear: bool = True):
        element = self._wait_element(locator, type_of='clickable')
        if is_clear:
            element.clear()
        element.send_keys(value)

    def hover_to_element(self, driver, hover_to: tuple, click_on: tuple):
        hover = ActionChains(driver)
        first_element = self._wait_element(hover_to)
        hover.move_to_element(first_element).perform()
        second_element = self._wait_element(click_on)
        hover.move_to_element(second_element).click().perform()

    def get_page_title(self, title_selector):
        return self._wait_element(title_selector).text
