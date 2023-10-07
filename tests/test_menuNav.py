import pytest
from pages.basepage import BasePage
from pages.navmenu import NavMenu

@pytest.mark.anonymous
@pytest.mark.usefixtures("appium_service", "appium_driver")
class TestAnonymousUser:
    def test_anonymous_user(self):
        basePage = BasePage(self.driver)
        basePage.verify_app_name_displayed()
        navMenu = NavMenu(self.driver)
        navMenu.verify_is_anonymous_user()
