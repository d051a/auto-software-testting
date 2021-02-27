import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    webdriver.ChromeOptions
    yield driver
    request.addfinalizer(driver.quit)