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

    app_name = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/tvAppName')

    def __init__(self, driver):
        self.driver = driver

    def verify_app_name_displayed(self):
        try:
            appNameElement = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.app_name)))
        except Exception as e:
            log.debug(str(e))

    def is_visible(self, element):
        if WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((element))):
            log.info(f"{element} visible")
            return True
        else:
            log.info(f"{element} not found")
        return False
    
    def is_clickable(self, element):
        if WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((element))):
            log.info(f"{element} clickable")
            return True
        else:
            log.info(f"{element} not found")
        return False
    
    def click_element(self, locator):
        if locator[0] == 'id':
            try:
                log.info(f"clicking element={locator[1]} ")
                self.driver.find_element(locator[0], locator[1]).click()
                time.sleep(2)
            except Exception as e:
                log.debug(str(e))
        else:
            log.info("Expected locator type is not available")
    
    def send_text(self, locator, text):
        if locator[0] == 'id':
            try:
                log.info(f"Sending text={text} to element={locator[1]} ")
                self.driver.find_element(locator[0], locator[1]).send_keys(str(text))
                time.sleep(2)
            except Exception as e:
                log.debug(str(e))
        else:
            log.info("Expected locator type is not available")


