import os
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


@pytest.fixture
def browser():
    """creates an instance of Chrome driver."""
    # initialize browser
    driver = webdriver.Chrome(os.path.join(ROOT, 'resources/chromedriver'))
    driver.implicitly_wait(10)
    driver.get('https://demo.applitools.com/hackathon.html')
    yield driver
    driver.quit()


class TestUIElement:
    def test_ensure_the_login_page_looks_okay(self, browser):
        """Using functional (automated) testing for this can be tedious and 
        cumbersome as it requires one to validate or write assertions 
        for every single element on a page. Since we are mostly validating that 
        everything on the page (log-in) appears as expected or intended, it's a task better suited
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
        username.clear()  # to clear any pre-populated text in input field
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
            assert True  # Surely, there's a better way:-)
        except NoSuchElementException:
            # no element found.. this means we can't or didn't login, we can safely assert FALSE
            assert False


class TestTableSort:

    def is_logged_in(self, browser):
        browser.find_element_by_id('username').send_keys('ada')
        browser.find_element_by_id('password').send_keys('lovelace')
        browser.find_element_by_id('log-in').click()
        return True if browser.find_element_by_class_name('top-menu-controls') else False

    def _get_table_data(self, browser):
        """Saves content of table in a list of lists - where each row is a list."""
        data = []
        table = browser.find_element_by_css_selector('table')
        for row in table.find_elements_by_css_selector('tbody'):
            content = []
            for col in row.find_elements_by_css_selector('td'):
                content.append(col.text)
            data.append(content)
        return data

    def test_view_recent_transactions(self, browser):
        if self.is_logged_in(browser):
            original = self._get_table_data(browser)
            browser.find_element_by_id('amount').click()
            assert self._get_table_data(browser).sort() == original.sort()
        else:
            assert False


class TestCanvasChart(TestTableSort):
    pass


class DynamicContentTest(TestTableSort):
    pass
