import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.calculator
def test_calk():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html ")
    driver.text = driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.text = driver.find_element(By.CSS_SELECTOR, '#delay').send_keys("45")
    driver.text = driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.Button_seven = driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.Button_plus = driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.Button_eight = driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.Button_equals = driver.find_element(By.XPATH, "//span[text()='=']").click()


    driver.res = WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))).text
    assert driver.res == "15"

    driver.quit()
