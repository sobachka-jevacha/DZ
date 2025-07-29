import pytest
from calc_page import Calculator
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator = Calculator(driver)
    calculator.delay()
    calculator.button('7')
    calculator.button('+')
    calculator.button('8')
    calculator.button('=')
    calculator.wait()
    res = calculator.result()
    assert res == "15"
