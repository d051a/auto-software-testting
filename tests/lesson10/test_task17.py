import pytest
from config import LITECART_BASE_URL
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, \
    AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


@pytest.fixture
def driver(request):
    driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    yield driver
    request.addfinalizer(driver.quit)


def test_opening_link_in_new_window(driver, login_admin):
    add_new_country_page = LITECART_BASE_URL + 'admin/?app=catalog&doc=catalog&category_id=1'
    driver.get(add_new_country_page)

    items_links = []

    table = driver.find_element_by_class_name('dataTable')
    links = table.find_elements_by_css_selector('tr:not(.header):not(.footer) > td:nth-of-type(5) > a:nth-of-type(1)')
    for link in links:
        items_links.append(link.get_attribute('href'))

    for url in items_links:
        driver.get(url)
        for event in driver.get_log("browser"):
            print(event)