import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.shop
def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.first_name = driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.last_name = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.button = driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    driver.Sauce_Labs_Backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.Sauce_Labs_Bolt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.Sauce_Labs_Onesie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.basket = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.checkout = driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.first_name = driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Мария")
    driver.last_name = driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Асадуллаева")
    driver.zip = driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("603053")
    driver.сontinue = driver.find_element(By.CSS_SELECTOR, "#continue").click()

    print((driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text))

    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    assert total == 'Total: $58.29'

    driver.quit()
