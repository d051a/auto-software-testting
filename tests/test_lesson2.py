import pytest
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_untitled(driver):
    find_string = 'test'
    driver.get("https://www.google.com/")
    driver.set_window_size(1440, 877)
    driver.find_element(By.NAME, "q").send_keys(find_string)
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.title_is(f"{find_string} - Поиск в Google"))