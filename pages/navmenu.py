from pages.basepage import BasePage
import logging
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

log = Logger()._logger()

class NavMenu(BasePage):

    profileMenu = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="التنقل إلى أعلى"]')
    menuUserIDValue = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/tvMenuUserIdValue')
    loginMenuElement = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/menuLogin')
        
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_nav_menu(self):
        try:
            profileElement = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((self.profileMenu)))
            profileElement.click()
        except Exception as e:
            log.debug(str(e))

    def verify_userid_value_present(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.menuUserIDValue))).click()
        except Exception as e:
            log.debug(str(e))

    def verify_login_icon_visible(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.loginMenuElement))).click()
        except Exception as e:
            log.debug(str(e))

    def verify_is_anonymous_user(self):
        self.open_nav_menu()
        self.verify_userid_value_present()
        self.verify_login_icon_visible()