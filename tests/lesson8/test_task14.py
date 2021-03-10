from config import LITECART_BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from contextlib import contextmanager


def get_new_window_handle(driver, main_window_handle):
    for window_handle in driver.window_handles:
        if window_handle != main_window_handle:
            return window_handle


@contextmanager
def wait_for_new_window(driver, timeout=10):
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))


def test_opening_link_in_new_window(driver, login_admin):
    add_new_country_page = LITECART_BASE_URL + 'admin/?app=countries&doc=edit_country'
    driver.get(add_new_country_page)
    page_info_links = driver.find_elements(By.XPATH, "//form//a[@target='_blank']")
    time.sleep(2)
    for page_info_link in page_info_links:
        main_window_handle = driver.current_window_handle
        with wait_for_new_window(driver):
            page_info_link.click()
        time.sleep(2)
        new_window_handle = get_new_window_handle(driver, main_window_handle)
        driver.switch_to.window(new_window_handle)
        driver.close()
        driver.switch_to.window(main_window_handle)


