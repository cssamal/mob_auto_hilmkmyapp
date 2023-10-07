import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.basepage import BasePage
from pages.navmenu import NavMenu
from pages.registerpage import RegisterPage

@pytest.mark.registered
@pytest.mark.usefixtures("appium_service", "appium_driver")
class TestRegisterUser:
    def test_success_register_user(self):
        basePage = BasePage(self.driver)
        basePage.verify_app_name_displayed()
        navMenu = NavMenu(self.driver)
        navMenu.verify_is_anonymous_user()
        navMenu.perform_register_user()
        registerPage = RegisterPage(self.driver)
        registerPage.verify_register_user('testcsg', 'testcsg@gmail.com', '12345678')
