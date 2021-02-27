import pytest
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from config import LITECART_BASE_URL, USER_LOGIN, USER_PASSWORD


  
# LITECART_BASE_URL = 'http://192.168.56.200/litecart'

def test_login(driver):
    driver.get(LITECART_BASE_URL)
    driver.maximize_window()
    driver.find_element(By.NAME, "email").send_keys(USER_LOGIN)
    driver.find_element(By.NAME, "password").send_keys(USER_PASSWORD)
    driver.find_element(By.XPATH, "//button[@name='login']").send_keys(Keys.ENTER)
