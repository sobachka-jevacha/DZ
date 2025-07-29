import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator():
    def __init__(self, driver):
        self._driver = driver

    def delay(self):
        delay_field = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_field.clear()
        delay_field.send_keys('45')

    def button(self, numbers):
        button = self._driver.find_element(By.XPATH, f"//span[text()= '{numbers}']")
        button.click()

    def wait(self):
        WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))      

    def result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
