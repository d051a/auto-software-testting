from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LITECART_BASE_URL, USER_LOGIN, USER_PASSWORD


def test_login(driver):
    driver.get(LITECART_BASE_URL)
    driver.maximize_window()
    driver.find_element(By.NAME, "email").send_keys(USER_LOGIN)
    driver.find_element(By.NAME, "password").send_keys(USER_PASSWORD)
    driver.find_element(By.XPATH, "//button[@name='login']").send_keys(Keys.ENTER)
