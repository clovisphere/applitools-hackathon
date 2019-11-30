import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    """creates an instance of Chrome driver."""
    # initialize browser
    driver = webdriver.Chrome('../utils/chromedriver')
    driver.implicitly_wait(10)
    driver.get('https://demo.applitools.com/hackathon.html')
    yield driver
    driver.quit()


class TestUIElement:
    pass


class TestDataDriven:
    """For all Data Driven tests."""

    def test_login_without_providing_credentials(self, browser):
        browser.find_element_by_id('log-in').click()
        assert 'Both Username and Password must be present' in \
               browser.find_element_by_class_name('alert-warning').text

    def test_login_only_provide_username(self, browser):
        browser.find_element_by_id('username').send_keys('ada')
        browser.find_element_by_id('log-in').click()
        assert 'Password must be present' in \
               browser.find_element_by_class_name('alert-warning').text

    def test_login_only_provide_password(self, browser):
        browser.find_element_by_id('username').send_keys('ada')
        browser.find_element_by_id('log-in').click()
        assert 'Username must be present' in \
               browser.find_element_by_class_name('alert-warning').text
