from pages.basepage import BasePage
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
import time

log = Logger()._logger()

class RegisterPage(BasePage):

    register_msg_element = ('id', 'com.hilmk.hilmkMyApp:id/tvRegisterMessage')
    username_element = ('id', 'com.hilmk.hilmkMyApp:id/etUsername')
    email_element = ('id', 'com.hilmk.hilmkMyApp:id/etEmail')
    password_element = ('id', 'com.hilmk.hilmkMyApp:id/etPassword')
    confirm_password_element = ('id', 'com.hilmk.hilmkMyApp:id/etConfirmPassword')
    terms_agreement_checkbox_element = ('id', 'com.hilmk.hilmkMyApp:id/cbTermsAgreement')
    register_button = ('id', 'com.hilmk.hilmkMyApp:id/btnRegister')

    def __init__(self, driver):
        super().__init__(driver)
    
    def set_username(self, username):
        self.is_clickable(self.username_element)
        self.send_text(locator=self.username_element, text=username) 
    
    def set_email(self, email):
        self.is_clickable(self.email_element)
        self.send_text(locator=self.email_element, text=email) 

    def set_password(self, password):
        self.is_clickable(self.password_element)
        self.send_text(locator=self.password_element, text=password) 
    
    def set_confirm_password(self, password):
        self.is_clickable(self.confirm_password_element)
        self.send_text(locator=self.confirm_password_element, text=password) 

    def check_terms_checkbox(self):
        self.is_visible(self.terms_agreement_checkbox_element)
        self.click_element(locator=self.terms_agreement_checkbox_element)

    def click_register_button(self):
        self.is_visible(self.terms_agreement_checkbox_element)
        self.click_element(locator=self.register_button)
    
    def verify_register_user(self, username, email, password):
        self.is_visible(self.register_msg_element)
        self.set_username(username=username)
        self.set_email(email=email)
        self.set_password(password=password)
        self.set_confirm_password(password=password)
        self.check_terms_checkbox()
        # self.click_register_button()
        # basepage = BasePage(self.driver)
        # assert basepage.verify_app_name_displayed()
    