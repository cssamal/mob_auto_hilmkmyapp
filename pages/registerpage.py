from pages.basepage import BasePage
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

log = Logger()._logger()

class RegisterPage(BasePage):

    register_msg_element = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/tvRegisterMessage')
    username_element = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/etUsername')
    email_element = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/etEmail')
    password_element = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/etPassword')
    confirm_password_element = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/etConfirmPassword')
    terms_agreement_checkbox_element = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/cbTermsAgreement')
    register_button = (AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/btnRegister')

    def __init__(self, driver):
        super().__init__(driver)
    
    def set_username(self, username):
        try:
            self.is_visible(self.username_element)
            self.driver.find_element(self.username_element).send_keys(str(username))
        except Exception as e:
            log.debug(str(e))
    
    def set_email(self, email):
        try:
            self.is_visible(self.email_element)
            self.driver.find_element(self.email_element).send_keys(str(email))
        except Exception as e:
            log.debug(str(e))

    def set_password(self, password):
        try:
            self.is_visible(self.password_element)
            self.driver.find_element(self.password_element).send_keys(str(password))
        except Exception as e:
            log.debug(str(e))
    
    def set_confirm_password(self, password):
        try:
            self.is_visible(self.confirm_password_element)
            self.driver.find_element(self.confirm_password_element).send_keys(str(password))
        except Exception as e:
            log.debug(str(e))

    def check_terms_checkbox(self):
        try:
            self.is_visible(self.terms_agreement_checkbox_element)
            self.driver.find_element(self.terms_agreement_checkbox_element).click()
        except Exception as e:
            log.debug(str(e))

    def click_register_button(self):
        try:
            self.is_visible(self.register_button)
            self.driver.find_element(self.register_button).click()
        except Exception as e:
            log.debug(str(e))
    
    def verify_register_user(self, username, email, password):
        self.is_visible(self.register_msg_element)
        self.set_username(username=username)
        self.set_email(email=email)
        self.set_password(password=password)
        self.set_confirm_password(password=password)
        self.check_terms_checkbox()
        self.click_register_button()
        basepage = BasePage(self.driver)
        assert basepage.verify_app_name_displayed()
    