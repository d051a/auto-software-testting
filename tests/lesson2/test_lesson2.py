from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


def test_untitled(driver):
    find_string = 'test'
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.find_element(By.NAME, "q").send_keys(find_string)
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.title_is(f"{find_string} - Поиск в Google"))