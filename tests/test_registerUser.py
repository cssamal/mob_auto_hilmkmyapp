import pytest
from pages.registerpage import RegisterPage

@pytest.mark.register
@pytest.mark.usefixtures("appium_service", "appium_driver")
class TestRegisterUser:
    def test_success_register_user(self):
        registerPage = RegisterPage(self.driver)
        registerPage.verify_register_user('testcss', 'testcss@gmail.com', '12345678')
