import pytest
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium import webdriver
import os

CURRENT_DIR = os.getcwd()
APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()

@pytest.fixture(scope='function')
def appium_driver(request):
    desired_caps = {
        "platformName": "Android",
        "version": "11.0",
        "app": os.path.join(CURRENT_DIR, "app-debug.apk"),
        "realDevice": True,
        "automationName": "uiautomator2"
    }

    caps_options = UiAutomator2Options().load_capabilities(desired_caps)

    driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=caps_options)

    request.cls.driver = driver
    driver.implicitly_wait(20)
    yield driver
    driver.quit()



