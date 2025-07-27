import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Avtoriz:
    def __init__(self, driver):
        self._driver = driver

    def avtor(self):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

class Shop:
    def __init__(self, driver):
        self._driver = driver 

    def make_shop(self):       
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_to(self):         
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


class Checkout:
    def __init__(self, driver):
        self._driver = driver 

    def chek(self):
        self._driver.get("https://www.saucedemo.com/cart.html") 
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()


class Cart:
    def __init__(self, driver):
        self._driver = driver

    def main_post(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Мария")
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Асадуллаева")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("603053")
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()


class Total:
    def __init__(self, driver):
        self._driver = driver

    def _print_(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")
        print((self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text))
        total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        assert total == 'Total: $58.29'
