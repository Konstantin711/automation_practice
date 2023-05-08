from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver import ChromiumEdge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from selenium import webdriver


def browsers_factory(browser: str):
    if browser.lower() == 'chrome':
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        return Chrome(service=Service(ChromeDriverManager().install()))
    elif browser.lower() == 'firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = Firefox(service=service)
        return driver
    elif browser.lower() == 'edge':
        return ChromiumEdge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        return Chrome(service=Service(ChromeDriverManager().install()))
