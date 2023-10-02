import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.usefixtures("appium_service", "appium_driver")
class TestNavMenu:
    def test_nav_menu_open(self):
        appNameElement = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/tvAppName')))
        profileMenuElement = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="التنقل إلى أعلى"]')))
        profileMenuElement.click()
        menuUserIDValueElement = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/tvMenuUserIdValue')))
        
        loginMenuElement = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.hilmk.hilmkMyApp:id/menuLogin')))
        
        assert menuUserIDValueElement, loginMenuElement
        
