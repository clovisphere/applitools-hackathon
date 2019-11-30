import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

@pytest.fixture
def browser():
    """creates an instance of Chrome driver."""
    # used to maximize window
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    # initialize browser
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.get('https://demo.applitools.com/hackathon.html')
    yield driver
    driver.quit()

class TestUIElement:
    pass

class TestDataDriven:
    def test_login_without_providing_credentials(self, browser):
        browser.find_element_by_id('log-in').click()
        assert 'Both Username and Password must be present' in browser.find_element_by_class_name('alert-warning').text
