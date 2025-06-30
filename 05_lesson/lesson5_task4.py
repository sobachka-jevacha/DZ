from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/login')

input_1 = driver.find_element(By.ID, 'username')
input_1.send_keys('tomsmith')

input_2 = driver.find_element(By.ID, 'password')
input_2.send_keys('SuperSecretPassword!')

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

success_message = driver.find_element(By.ID, "flash").text.strip()
print(success_message)

driver.quit()
