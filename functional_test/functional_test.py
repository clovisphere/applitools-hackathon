import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


ROOT = os.path.dirname(os.path.dirname(__file__))

@pytest.fixture
def browser():
    """creates an instance of Chrome driver."""
    # initialize browser
    driver = webdriver.Chrome(os.path.join(ROOT, 'utils/chromedriver')) # TODO: this can be removed if latest driver is already installed.
    driver.implicitly_wait(10)
    driver.get('https://demo.applitools.com/hackathon.html')
    yield driver
    driver.quit()


class TestUIElement:
    def test_ensure_the_login_page_looks_okay(self, browser):
        """Using functional (automated) testing for this can be tedious and 
        cumbersome as it requires one to validate or write assertions 
        for every single element on a page. Since we are mostly validating that 
        everything on the page (log-in) appears as expected or intented, it's a task better suited 
        for a visual UI testing tool i.e applitools. 
        """


class TestDataDriven:
    """For all Data-Driven tests."""
    def test_login_without_providing_credentials(self, browser):
        browser.find_element_by_id('log-in').click()
        assert 'Both Username and Password must be present' in \
               browser.find_element_by_class_name('alert-warning').text

    def test_login_only_provide_username(self, browser):
        username = browser.find_element_by_id('username')
        username.clear() # to clear any pre-populated text in input field
        username.send_keys('ada')
        browser.find_element_by_id('log-in').click()
        assert 'Password must be present' in \
               browser.find_element_by_class_name('alert-warning').text

    def test_login_only_provide_password(self, browser):
        password = browser.find_element_by_id('password')
        password.clear()
        password.send_keys('lovelace')
        browser.find_element_by_id('log-in').click()
        assert 'Username must be present' in \
               browser.find_element_by_class_name('alert-warning').text

    def test_login_with_valid_credentials(self, browser):
        browser.find_element_by_id('username').send_keys('ada')
        browser.find_element_by_id('password').send_keys('lovelace')
        browser.find_element_by_id('log-in').click()
        
        # if element exists then we know we have successfully logged in
        try:
            browser.find_element_by_class_name('top-menu-controls')
            assert True  # we could probably do better:-)
        except NoSuchElementException:
            # no element found.. this then means we can't or didn't login
            assert False






