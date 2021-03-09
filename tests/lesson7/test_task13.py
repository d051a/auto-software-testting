from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from config import LITECART_BASE_URL
import time


def add_good_to_basket(driver):
    good_locator = "//li[contains(@class, 'product')]"
    current_quantity = get_cart_items_quantity(driver)
    new_quantity_locator = f"//div[@id='cart']//span[@class='quantity' and contains(text(), '{current_quantity+1}')]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, good_locator)))
    goods_on_page = driver.find_elements(By.XPATH, good_locator)
    first_good = goods_on_page[0]
    first_good.click()
    size_select_menu = driver.find_elements(By.NAME, "options[Size]")
    if size_select_menu:
        size_select_menu = Select(driver.find_element(By.NAME, "options[Size]"))
        size_select_menu.select_by_value("Small")
    add_goods_to_basket_button = driver.find_element(By.NAME, "add_cart_product")
    add_goods_to_basket_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, new_quantity_locator)))
    driver.get(LITECART_BASE_URL)


def get_cart_items_quantity(driver):
    quantity_locator = "//div[@id='cart']//span[@class='quantity']"
    cart_items_quantity = driver.find_element(By.XPATH, quantity_locator)
    cart_items_quantity = int(cart_items_quantity.text)
    return cart_items_quantity


def remove_cart_item(driver):
    remove_button = driver.find_element(By.XPATH, "//button[@name='remove_cart_item']")
    removed_item_name = remove_button.find_element(By.XPATH, "./../..//strong").text
    remove_button.click()
    removed_item_in_table_locator = f"//div[@id='order_confirmation-wrapper']//td[@class='item' and contains(text(), '{removed_item_name}')]"
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, removed_item_in_table_locator)))


def get_order_summary_items(driver):
    items_names = driver.find_elements(By.XPATH, "//td[@class='item']")
    return items_names


def test_add_goods_to_basket(driver, login_customer):
    goods_count = 3
    for i in range(goods_count):
        add_good_to_basket(driver)
    driver.find_element(By.XPATH, "//div[@id='cart']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-checkout-summary")))
    for i in range(goods_count):
        remove_cart_item(driver)

