import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Avtoriz:
    def __init__(self, driver: webdriver) -> webdriver:
        self._driver = driver
    @allure.step("Заполнить поле логи {login} и пароль {password}")
    def avtor(self,login: str,password: str) -> str:
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

class Shop:
    def __init__(self, driver: webdriver) -> webdriver:
        self._driver = driver 

    def make_shop(self):       
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_to(self):         
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


class Checkout:
    def __init__(self, driver:webdriver) -> webdriver:
        self._driver = driver 

    def chek(self):
        self._driver.get("https://www.saucedemo.com/cart.html") 
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()


class Cart:
    def __init__(self, driver:webdriver) -> webdriver:
        self._driver = driver
    @allure.step("Заполнить поле имя {name}, фамилия {last_name},индекс {code}")
    def main_post(self, name: str, last_name: str, code: str) -> str:
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(code)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()


class Total:
    def __init__(self, driver:webdriver) -> webdriver:
        self._driver = driver

    def _print_(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")
        print((self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text))
        total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return total