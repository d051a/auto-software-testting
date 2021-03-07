from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from config import FILES_DIR
import time
import random
import os


def test_create_good(driver, login_admin):
    good_code = random.randint(1, 999999)
    good_name = f"good_{good_code}_full_name"
    quantity = '100'
    keywords = 'keyword1, keyword2'
    short_description = f"good_{good_code} description"
    full_description = f"good_{good_code} full description"
    image_path = os.path.join(FILES_DIR, 'image.jpg')
    head_title = f"good_{good_code} head title"
    meta_description = f"good_{good_code} meta description"
    purchase_price = '100'

    time.sleep(5)
    driver.find_element(By.XPATH, "//span[contains(text(), 'Catalog')]")
    driver.find_element(By.XPATH,"//span[contains(text(), 'Catalog')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(), ' Add New Product')]").click()
    driver.find_element(By.NAME, "status").click()
    driver.find_element(By.NAME, "name[en]").send_keys(good_name)
    driver.find_element(By.NAME, "code").send_keys(good_code)
    product_groups = driver.find_elements(By.NAME, "product_groups[]")
    for product in product_groups:
        product.click()
    driver.find_element(By.NAME, "quantity").clear()
    driver.find_element(By.NAME, "quantity").send_keys(quantity)
    driver.find_element(By.NAME, "new_images[]").send_keys(image_path)
    driver.find_element(By.NAME, "date_valid_from").click()
    driver.find_element(By.NAME, "date_valid_from").send_keys("2021-01-01")
    driver.find_element(By.NAME, "date_valid_to").click()
    driver.find_element(By.NAME, "date_valid_to").send_keys("2021-12-31")

    driver.find_element(By.LINK_TEXT, "Information").click()
    manufacturer_menu = driver.find_element(By.NAME, "manufacturer_id")
    manufacturer_menu = Select(manufacturer_menu)
    manufacturer_menu.select_by_visible_text('ACME Corp.')
    driver.find_element(By.NAME, "keywords").send_keys(keywords)
    driver.find_element(By.NAME, "short_description[en]").send_keys(short_description)
    driver.find_element(By.XPATH, "//div[@class='trumbowyg-editor']").send_keys(full_description)
    driver.find_element(By.NAME, "head_title[en]").send_keys(head_title)
    driver.find_element(By.NAME, "meta_description[en]").send_keys(meta_description)

    driver.find_element(By.LINK_TEXT, "Prices").click()
    driver.find_element(By.NAME, "purchase_price").clear()
    driver.find_element(By.NAME, "purchase_price").send_keys(purchase_price)
    curency_menu = driver.find_element(By.NAME, "purchase_price_currency_code")
    curency_menu = Select(curency_menu)
    curency_menu.select_by_visible_text('Euros')
    driver.find_element(By.XPATH, "//button[@name='save']").click()
    time.sleep(3)
    goods = [good.text for good in driver.find_elements(By.XPATH, "//table//tr[@class='row']/td[3]/a")]
    assert good_name in goods



