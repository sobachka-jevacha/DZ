import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.calculator
def test_calk():
    driver = webdriver.Chrome()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_field = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay_field.clear()
    delay_field.send_keys("45")
    
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    assert result, "Результат не равен 15"
    
    driver.quit()
