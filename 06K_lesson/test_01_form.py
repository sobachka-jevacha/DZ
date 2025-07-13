import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.form
def test_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.first_name = driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.address = driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.city = driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.zip_code = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys("")
    driver.country = driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.company = driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

    driver.submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    pole_z = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert pole_z == "alert py-2 alert-danger"

    poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
    for pole in poles:
        pole_class = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
        assert pole_class == "alert py-2 alert-success"