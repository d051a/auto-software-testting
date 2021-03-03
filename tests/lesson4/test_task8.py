from selenium.webdriver.common.by import By


def test_good_item_sticker_exist(driver, login_customer):
    goods_category1_link_locator = "//li[@class='category-1']"
    goods_list_locator = "//li[contains(@class,'product')]"
    sticker_locator = ".//div[contains(@class, 'sticker')]"

    goods_category1_link = driver.find_element(By.XPATH, goods_category1_link_locator)
    goods_category1_link.click()
    goods_list = driver.find_elements(By.XPATH, goods_list_locator)
    for good in goods_list:
        stickers_count = len(good.find_elements(By.XPATH, sticker_locator))
        assert stickers_count == 1



