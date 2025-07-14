from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_valid_search(driver):
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys('yashaka/selene')
    search_input.send_keys(Keys.RETURN)
    title = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'GitHub - yashaka/selene: User-oriented Web UI …')]")))
    assert title.is_displayed()

def test_invalid_search(driver):
    search_input = driver.find_element(By.NAME, 'q')
    searched_text = '489y8er9thu'
    search_input.send_keys(searched_text)
    search_input.send_keys(Keys.RETURN)
    result = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Не удалось найти ни одного результата для')]")))
    assert result.is_displayed()