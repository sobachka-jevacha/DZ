from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

driver.quit()