import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from config import LITECART_BASE_URL


def test_good_page_compare(driver):
    driver.get(LITECART_BASE_URL)
    compaigns_section_locator = "//*[@id='box-campaigns']/div[@class='content']"
    first_good_locator = ".//li[@class='product column shadow hover-light'][1]"
    good_name_locator = ".//div[@class='name']"
    good_regular_price_locator = ".//*[@class='regular-price']"
    good_campaign_price_locator = ".//*[@class='campaign-price']"
    compaigns_section = driver.find_element(By.XPATH, compaigns_section_locator)
    first_good = compaigns_section.find_element(By.XPATH, first_good_locator)
    good_name = first_good.find_element(By.XPATH, good_name_locator).text
    good_regular_price = first_good.find_element(By.XPATH, good_regular_price_locator)
    good_campaign_price = first_good.find_element(By.XPATH, good_campaign_price_locator)
    good_regular_price_line_through = good_regular_price.value_of_css_property("text-decoration-line")
    good_regular_price_color = good_regular_price.value_of_css_property("color")
    good_regular_price_font_size = str(good_regular_price.value_of_css_property("font-size")).replace('px', '')
    good_campaign_price_font_weight = good_campaign_price.value_of_css_property("font-weight")
    good_campaign_price_color = good_campaign_price.value_of_css_property("color")
    good_campaign_price_font_size = str(good_campaign_price.value_of_css_property("font-size")).replace('px', '')
    good_regular_price = good_regular_price.text
    good_campaign_price = good_campaign_price.text

    assert Color.from_string(good_regular_price_color) == Color.from_string('rgba(119, 119, 119, 1)')
    assert good_regular_price_line_through == 'line-through'
    assert Color.from_string(good_campaign_price_color) == Color.from_string('rgba(204, 0, 0, 1)')
    assert good_campaign_price_font_weight == 'bold' or int(good_campaign_price_font_weight) >= 700
    assert float(good_campaign_price_font_size) > float(good_regular_price_font_size)

    first_good.click()

    good_h1_caption_locator = "//h1[@class='title']"
    good_page_good_name = driver.find_element(By.XPATH, good_h1_caption_locator).text
    good_page_regular_price = driver.find_element(By.XPATH, good_regular_price_locator)
    good_page_campaign_price = driver.find_element(By.XPATH, good_campaign_price_locator)
    good_page_regular_price_line_through = good_page_regular_price.value_of_css_property("text-decoration-line")
    good_page_regular_price_color = good_page_regular_price.value_of_css_property("color")
    good_page_regular_price_font_size = str(good_page_regular_price.value_of_css_property("font-size")).replace('px', '')
    good_page_campaign_price_font_weight = good_page_campaign_price.value_of_css_property("font-weight")
    good_page_campaign_price_color = good_page_campaign_price.value_of_css_property("color")
    good_page_campaign_price_font_size = str(good_page_campaign_price.value_of_css_property("font-size")).replace('px', '')

    assert good_name == good_page_good_name
    assert good_regular_price == good_page_regular_price.text
    assert good_campaign_price == good_page_campaign_price.text

    assert Color.from_string(good_page_regular_price_color) == Color.from_string('rgba(102, 102, 102, 1)')
    assert good_page_regular_price_line_through == 'line-through'
    assert Color.from_string(good_page_campaign_price_color) == Color.from_string('rgba(204, 0, 0, 1)')
    assert good_page_campaign_price_font_weight == 'bold' or int(good_page_campaign_price_font_weight) >= 700
    assert float(good_page_campaign_price_font_size) > float(good_page_regular_price_font_size)





