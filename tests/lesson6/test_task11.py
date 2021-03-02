from selenium.webdriver.common.by import By
from config import LITECART_BASE_URL
from selenium.webdriver.common.keys import Keys
import time
import random


def test_register_user(driver):
    new_user_register_page = LITECART_BASE_URL + 'create_account'
    user_firstname = "Firstname"
    user_lastname = "Lastname"
    user_address1 = "simple address 1 d. 2 kv. 345"
    user_postcode = "12345"
    user_city = "City"
    user_country = "United States"
    user_email = f"username{random.randint(1, 999999)}@mail.ru"
    user_phone = "9261321221"
    user_password = "password"
    driver.get(new_user_register_page)

    driver.find_element(By.NAME, "firstname").send_keys(user_firstname)
    driver.find_element(By.NAME, "lastname").send_keys(user_lastname)
    driver.find_element(By.NAME, "address1").send_keys(user_address1)
    driver.find_element(By.NAME, "postcode").send_keys(user_postcode)
    driver.find_element(By.NAME, "city").send_keys(user_city)
    driver.find_element(By.XPATH, "//span[contains(@class, 'select2 select2-container')]").click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(user_country)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    driver.find_element(By.NAME, "email").send_keys(user_email)
    driver.find_element(By.NAME, "phone").send_keys(user_phone)
    driver.find_element(By.NAME, "password").send_keys(user_password)
    driver.find_element(By.NAME, "confirmed_password").send_keys(user_password)
    driver.find_element(By.NAME, "create_account").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    driver.find_element(By.NAME, "email").send_keys(user_email)
    driver.find_element(By.NAME, "password").send_keys(user_password)
    driver.find_element(By.XPATH, "//button[@name='login']").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Logout").click()

