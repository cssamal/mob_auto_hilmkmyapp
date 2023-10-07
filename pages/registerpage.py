from pages.basepage import BasePage
from pages.navmenu import NavMenu
from utils.logger import Logger

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
        self.send_text(element=self.username_element, text=username) 
    
    def set_email(self, email):
        self.is_clickable(self.email_element)
        self.send_text(element=self.email_element, text=email) 

    def set_password(self, password):
        self.is_clickable(self.password_element)
        self.send_text(element=self.password_element, text=password) 
    
    def set_confirm_password(self, password):
        self.is_clickable(self.confirm_password_element)
        self.send_text(element=self.confirm_password_element, text=password) 

    def check_terms_checkbox(self):
        self.is_visible(self.terms_agreement_checkbox_element)
        self.click_element(element=self.terms_agreement_checkbox_element)

    def click_register_button(self):
        self.is_visible(self.register_button)
        self.click_element(element=self.register_button)
    
    def verify_register_user(self, username, email, password):
        navMenu = NavMenu(self.driver)
        navMenu.tap_register_user()
        # self.is_visible(self.register_msg_element)
        # self.set_username(username=username)
        # self.set_email(email=email)
        # self.set_password(password=password)
        # self.set_confirm_password(password=password)
        # self.check_terms_checkbox()
        # self.click_register_button()
        # basepage = BasePage(self.driver)
        navMenu.verify_username_visible()
        app_username = navMenu.get_value_username()
        assert username == app_username
        app_useremail = navMenu.get_value_useremail()
        assert email == app_useremail
        navMenu.verify_useremail_visible()
        navMenu.verify_logout_visible()


    