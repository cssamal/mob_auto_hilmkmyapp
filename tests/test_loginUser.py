import pytest
from pages.loginpage import LoginPage

@pytest.mark.loggedin
@pytest.mark.usefixtures("appium_service", "appium_driver")
class TestUserLogin:
    def test_success_user_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.login_user('testcss', 'testcss@gmail.com', '12345678')
