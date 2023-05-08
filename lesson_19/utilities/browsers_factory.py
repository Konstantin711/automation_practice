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
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        return Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser.lower() == 'firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = Firefox(service=service)
        return driver
    elif browser.lower() == 'edge':
        return ChromiumEdge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        return Chrome(service=Service(ChromeDriverManager().install()))
