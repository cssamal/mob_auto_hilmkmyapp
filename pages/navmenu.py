from pages.basepage import BasePage
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.registerpage import RegisterPage

log = Logger()._logger()

class NavMenu(BasePage):

    profile_menu = ('xpath', '//android.widget.ImageButton[@content-desc="التنقل إلى أعلى"]')
    menu_user_value = ('id', 'com.hilmk.hilmkMyApp:id/tvMenuUserIdValue')
    login_menu_element = ('id', 'com.hilmk.hilmkMyApp:id/menuLogin')
    register_user_element = ('id', 'com.hilmk.hilmkMyApp:id/menuRegister')
    navmenu_username_element = ('id', 'com.hilmk.hilmkMyApp:id/tvMenuUsername')
    navmenu_useremail_element = ('id', 'com.hilmk.hilmkMyApp:id/tvMenuEmail')
    navmenu_logout_element = ('id', 'com.hilmk.hilmkMyApp:id/menuLogout')
        
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_nav_menu(self):
        try:
            profileElement = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((self.appium_locator(self.profile_menu))))
            profileElement.click()
        except Exception as e:
            log.debug(str(e))

    def verify_userid_value_present(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(self.menu_user_value))))
        except Exception as e:
            log.debug(str(e))

    def verify_login_icon_visible(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(self.login_menu_element))))
        except Exception as e:
            log.debug(str(e))

    def verify_username_invisible(self):
        self.is_invisible(self.navmenu_username_element)

    def verify_useremail_invisible(self):
        self.is_invisible(self.navmenu_useremail_element)

    def verify_logout_invisible(self):
        self.is_invisible(self.navmenu_logout_element)

    def verify_is_anonymous_user(self):
        self.open_nav_menu()
        self.verify_userid_value_present()
        self.verify_login_icon_visible()
        self.verify_username_invisible()
        self.verify_useremail_invisible()
        self.verify_logout_invisible()

    def verify_register_user_option(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(self.register_user_element))))
        except Exception as e:
            log.debug(str(e))

    def perform_register_user(self):
        try:
            self.verify_register_user_option()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(self.register_user_element)))).click()
        except Exception as e:
            log.debug(str(e))
        return RegisterPage(self.driver)
