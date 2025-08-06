import allure
import pytest
from calc_page2 import Calculator
from selenium import webdriver


@pytest.fixture
# Фикстура открывает браузер и переходит на страницу калькулятора.
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

@allure.feature("Функциональность калькулятора")
@allure.title("Сложение чисел")
@allure.description("Тестирует базовую функциональность калькулятора при выполнении операции сложения.")
@allure.severity("BLOCKER")
def test_calculator(driver):
    with allure.step("Открыть калькулятор"):
        calculator = Calculator(driver)
    with allure.step("Ввести значение задержки"):
        calculator.delay()
    with allure.step("Нажать цифру ('7')"):
        calculator.button('7')
    with allure.step("Нажать ('+')"):
        calculator.button('+')
    with allure.step("Нажать цифру ('8')"):
        calculator.button('8')
    with allure.step("Нажать ('=')"):
        calculator.button('=')
    with allure.step("Проверить ожидание"):
        calculator.wait()
    with allure.step("Проверка результата"):
        res = calculator.result()
        assert res == "15"