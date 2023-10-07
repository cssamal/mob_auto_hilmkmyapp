from pages.basepage import BasePage
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

log = Logger()._logger()

class NavMenu(BasePage):

    profile_menu = ('xpath', '//android.widget.ImageButton[@content-desc="التنقل إلى أعلى"]')
    menu_user_value = ('id', 'com.hilmk.hilmkMyApp:id/tvMenuUserIdValue')
    login_menu_element = ('id', 'com.hilmk.hilmkMyApp:id/menuLogin')
    register_user_element = ('id', 'com.hilmk.hilmkMyApp:id/menuRegister')
    navmenu_username_element = ('id', 'com.hilmk.hilmkMyApp:id/tvMenuUsername')
    navmenu_useremail_element = ('id', 'com.hilmk.hilmkMyApp:id/tvMenuEmail')
    navmenu_logout_element = ('id', 'com.hilmk.hilmkMyApp:id/menuLogout')
    navmenu_username_value = ('id', 'com.hilmk.hilmkMyApp:id/tvMenuUsernameValue')
    navmenu_useremail_value = ('id', 'com.hilmk.hilmkMyApp:id/tvMenuEmailValue')
        
    
    def __init__(self, driver):
        super().__init__(driver)

    def open_nav_menu(self):
        self.is_clickable(self.profile_menu)
        self.click_element(self.profile_menu)

    def verify_userid_value_present(self):
        self.is_visible(self.menu_user_value)

    def verify_login_icon_visible(self):
        self.is_visible(self.login_menu_element)

    def verify_username_invisible(self):
        self.is_invisible(self.navmenu_username_element)

    def verify_useremail_invisible(self):
        self.is_invisible(self.navmenu_useremail_element)

    def verify_logout_invisible(self):
        self.is_invisible(self.navmenu_logout_element)

    def verify_username_visible(self):
        self.is_visible(self.navmenu_username_element)

    def verify_useremail_visible(self):
        self.is_visible(self.navmenu_useremail_element)

    def verify_logout_visible(self):
        self.is_visible(self.navmenu_logout_element)

    def get_value_username(self):
        username = self.get_text(self.navmenu_username_value)
        return username

    def get_value_useremail(self):
        user_email = self.get_text(self.navmenu_useremail_value)
        return user_email    

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

    def tap_register_user(self):
        self.verify_register_user_option()
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(self.register_user_element)))).click()
        except Exception as e:
            log.debug(str(e))
        # return RegisterPage(self.driver)

    def tap_login(self):
        self.verify_login_icon_visible()
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(self.login_menu_element)))).click()
        except Exception as e:
            log.debug(str(e))
    
    def verify_loggedin_user_details(self, username, email):
        self.open_nav_menu()
        self.verify_username_visible()
        app_username = self.get_value_username()
        assert username == app_username
        app_useremail = self.get_value_useremail()
        assert email == app_useremail
        self.verify_useremail_visible()
        self.verify_logout_visible()

    def logout_user(self):
        self.verify_logout_visible()
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((self.appium_locator(self.navmenu_logout_element)))).click()
            time.sleep(5)
        except Exception as e:
            log.debug(str(e))

