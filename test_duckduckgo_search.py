from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_valid_search(driver):
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys('yashaka/selene')
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)
    title = driver.find_element(By.XPATH, "//span[contains(text(),'GitHub - yashaka/selene: User-oriented Web UI brow')]")
    assert title.is_displayed()

def test_invalid_search(driver):
    search_input = driver.find_element(By.NAME, 'q')
    searched_text = 'zqxwlypt gribnoffle mkzutrando bleenfark norvextil qlerzump'
    search_input.send_keys(searched_text)
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)
    result = driver.find_element(By.CSS_SELECTOR, "p[class='n3qkwFtJOg1QzF_265_r wZ4JdaHxSAhGy1HoNVja wN0KrcRQzChXFKiMHpCZ'] span")
    assert result.is_displayed()