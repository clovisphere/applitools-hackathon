import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys 

@pytest.fixture
def browser():
    """creates an instance of Chrome driver."""
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

class TestUIElement:
    pass
