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
    # app_name locator helps us verify we have landed on home screen next to splash screen
    app_name = ('id', 'com.hilmk.hilmkMyApp:id/tvAppName')

    def __init__(self, driver):
        self.driver = driver

    def verify_app_name_displayed(self):
        try:
            appNameElement = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(self.app_name))))
        except Exception as e:
            log.debug(str(e))

    def appium_locator(self, element):
        if element[0] == 'id':
            return((AppiumBy.ID, element[1]))
        if element[0] == 'xpath':
            return((AppiumBy.XPATH, element[1]))


    def is_visible(self, element):
        if WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(element)))):
            log.info(f"{element} visible")
            return True
        else:
            log.info(f"{element} not found")
        return False
    
    def is_invisible(self, element):
        if WebDriverWait(self.driver, 30).until(EC.invisibility_of_element((self.appium_locator(element)))):
            log.info(f"{element} not visible")
            return True
        else:
            log.info(f"{element} not found")
        return False

    def is_clickable(self, element):
        if WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((self.appium_locator(element)))):
            log.info(f"{element} clickable")
            return True
        else:
            log.info(f"{element} not found")
        return False
    
    def click_element(self, element):
        try:
            log.info(f"clicking element={element[1]}")
            self.driver.find_element(element[0], element[1]).click()
            time.sleep(2)
        except Exception as e:
            log.debug(str(e))
    
    def send_text(self, element, text):
        if element[0] == 'id':
            try:
                log.info(f"Sending text={text} to element={element[1]} ")
                self.driver.find_element(element[0], element[1]).send_keys(str(text))
                time.sleep(2)
            except Exception as e:
                log.debug(str(e))
        else:
            log.info("Expected locator type is not available")
    
    def get_text(self, element):
        self.is_visible(element)
        try:
            text = self.driver.find_element(element[0], element[1]).get_attribute('text')
            log.info(f"Got the text value text={text} for element={element[1]} ")
            time.sleep(2)
            return text
        except Exception as e:
            log.debug(str(e))

    def is_checked(self, element):
        if self.driver.find_element(element[0], element[1]).get_attribute('checked') == 'true':
            log.info(f"Checkbox selected for element={element[1]} ")
            time.sleep(2)
            return True
        else:
            log.info(f"Checkbox not selected for element={element[1]} ")
            return False


