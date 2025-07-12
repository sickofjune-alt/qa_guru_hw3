import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://duckduckgo.com/')
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()

