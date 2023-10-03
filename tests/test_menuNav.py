import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.basepage import BasePage
from pages.navmenu import NavMenu

@pytest.mark.usefixtures("appium_service", "appium_driver")
class TestAnonymousUser:
    def test_nav_menu_open(self):
        basePage = BasePage(self.driver)
        basePage.verify_app_name_displayed()
        navMenu = NavMenu(self.driver)
        navMenu.verify_is_anonymous_user()
