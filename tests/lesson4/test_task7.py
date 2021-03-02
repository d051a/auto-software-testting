import time
from selenium.webdriver.common.by import By


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


def are_element_present(driver, *args):
    return len(driver.find_elements(*args)) == 1


def test_admin_panel_left_menu_items_h1_exists(driver, login_admin):
    left_menu = driver.find_element(By.XPATH, "//ul[@id='box-apps-menu']")
    menu_items = left_menu.find_elements(By.XPATH, ".//li")
    time.sleep(2)
    for menu_num, menu_item in enumerate(menu_items, start=1):
        menu_item_locator = f"//ul[@id='box-apps-menu']/li[{menu_num}]"
        admin_panel_left_menu_item = driver.find_element(By.XPATH, menu_item_locator)
        admin_panel_left_menu_item.click()
        assert are_elements_present(driver, By.XPATH, "//h1") is True

        admin_panel_left_menu_item = driver.find_element(By.XPATH, menu_item_locator)
        sub_menu_items = admin_panel_left_menu_item.find_elements(By.XPATH, "./ul/li")
        if sub_menu_items:
            for submenu_num, submenu_item in enumerate(sub_menu_items, start=1):
                submenu_item_locator = f"//ul[@id='box-apps-menu']/li[{menu_num}]/ul/li[{submenu_num}]"
                sub_menu = driver.find_element(By.XPATH, submenu_item_locator)
                sub_menu.click()
                assert are_elements_present(driver, By.XPATH, "//h1") is True



