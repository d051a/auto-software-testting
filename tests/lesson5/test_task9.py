import time
from selenium.webdriver.common.by import By
from config import LITECART_BASE_URL
from selenium.webdriver.support.select import Select


def test_admin_panel_countries_sorting(driver, login_admin):
    table_rows_locator = "//table[@class='dataTable']//tr[@class='row']"
    table_td_with_country_name = "./td[5]"
    table_td_with_country_name_url = "./td[5]/a"
    table_td_with_country_zones = "./td[6]"

    admin_panel_countries_page = LITECART_BASE_URL + 'admin/?app=countries'
    driver.get(admin_panel_countries_page)

    table_tr_countries_list = driver.find_elements(By.XPATH, table_rows_locator)
    countries_names = [country_name.find_element(By.XPATH, table_td_with_country_name).get_attribute("textContent")
                       for country_name in table_tr_countries_list]
    sorted_countries_names = sorted(countries_names)
    assert countries_names == sorted_countries_names

    countries_with_multiply_zones = [country_name.find_element(By.XPATH, table_td_with_country_name_url).get_attribute("textContent")
                                     for country_name in table_tr_countries_list
                                     if int(country_name.find_element(By.XPATH, table_td_with_country_zones).get_attribute("textContent")) > 0]

    for country_name in countries_with_multiply_zones:
        table_rows_with_zones_locator = "//table[@class='dataTable']//tr"
        table_td_with_zone_name_locator = "./td[3]"
        country_with_miltiply_zones_link_locator = f"//td/a[contains(text(), '{country_name}')]"

        driver.get(admin_panel_countries_page)
        country_with_miltiply_zones_link = driver.find_element(By.XPATH, country_with_miltiply_zones_link_locator)
        country_with_miltiply_zones_link.click()

        table_tr_countries_list = driver.find_elements(By.XPATH, table_rows_with_zones_locator)
        countries_names = [country_name.find_element(By.XPATH, table_td_with_zone_name_locator).get_attribute("textContent")
                           for country_name in table_tr_countries_list[1:-1]]
        sorted_countries_names = sorted(countries_names)
        assert countries_names == sorted_countries_names


def test_admin_panel_zones_sorting(driver, login_admin):
    table_rows_locator = "//table[@class='dataTable']//tr[@class='row']"
    table_td_with_country_name = "./td[3]"

    admin_panel_countries_page = LITECART_BASE_URL + 'admin/?app=geo_zones'
    driver.get(admin_panel_countries_page)

    table_tr_countries_list = driver.find_elements(By.XPATH,table_rows_locator)
    countries_names = [country_name.find_element(By.XPATH, table_td_with_country_name).get_attribute("textContent")
                       for country_name in table_tr_countries_list]

    for country_name in countries_names:
        zones_names = []
        country_link_locator = f"//td/a[contains(text(), '{country_name}')]"
        table_rows_with_zones_locator = "//table[@class='dataTable']//tr"
        driver.get(admin_panel_countries_page)
        country_link = driver.find_element(By.XPATH, country_link_locator)
        country_link.click()

        table_tr_zones_list = driver.find_elements(By.XPATH, table_rows_with_zones_locator)
        for table_row in table_tr_zones_list[1:-1]:
            td_with_zone_name_locator = "./td[3]/select"
            select_with_zone = Select(table_row.find_element(By.XPATH, td_with_zone_name_locator))
            zone_name = select_with_zone.first_selected_option.text
            zones_names.append(zone_name)
        sorted_zones_names = sorted(zones_names)
        assert zones_names == sorted_zones_names






