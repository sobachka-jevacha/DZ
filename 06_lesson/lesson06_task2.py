from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

tex = driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys('SkyPro')

blue_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(button)

driver.quit()
