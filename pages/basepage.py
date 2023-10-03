from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time


log = Logger()._logger()

class BasePage:
    """
    Page class for base or main page with locators and functions.
    """

    appName = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/tvAppName')

    def __init__(self, driver):
        self.driver = driver

    def verify_app_name_displayed(self):
        try:
            appNameElement = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appName)))
        except Exception as e:
            log.debug(str(e))



    