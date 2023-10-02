from pages.basepage import BasePage
import logging
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

log = Logger(__name__, logging.INFO)


class NavMenu(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    