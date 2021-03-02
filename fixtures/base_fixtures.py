from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import LITECART_BASE_URL, ADMIN_LOGIN, ADMIN_PASSWORD, USER_LOGIN, USER_PASSWORD


@pytest.fixture
def driver(request):
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    # driver.implicitly_wait(5)
    yield driver
    request.addfinalizer(driver.quit)


@pytest.fixture
def login_customer(driver):
    driver.get(LITECART_BASE_URL)
    driver.maximize_window()
    driver.find_element(By.NAME, "email").send_keys(USER_LOGIN)
    driver.find_element(By.NAME, "password").send_keys(USER_PASSWORD)
    driver.find_element(By.XPATH, "//button[@name='login']").send_keys(Keys.ENTER)


@pytest.fixture
def login_admin(driver):
    admin_panel_url = LITECART_BASE_URL + 'admin'
    driver.get(admin_panel_url)
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys(ADMIN_LOGIN)
    driver.find_element(By.NAME, "password").send_keys(ADMIN_PASSWORD)
    driver.find_element(By.XPATH, "//button[@name='login']").send_keys(Keys.ENTER)


