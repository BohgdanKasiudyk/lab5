import pytest
from selenium.webdriver import DesiredCapabilities

from page import Page
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = '/usr/bin/firefox'
    browser = webdriver.Firefox(capabilities=firefox_capabilities)
    browser.implicitly_wait(30)

    pytest.page = Page(browser, "https://hotline.ua/")
    try:
        yield browser
    finally:
        browser.quit()