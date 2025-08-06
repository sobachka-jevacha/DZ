import allure
import pytest
from shop_page2 import Avtoriz, Shop, Checkout, Cart, Total
from selenium import webdriver


@pytest.fixture
# Фикстура открывает браузер и переходит на страницу калькулятора.
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@allure.feature("Функциональность магазина")
@allure.description("Тестирует базовую функциональность магазина.")
@allure.severity("BLOCKER")
@allure.title("Тестироапние интернет-магазина")
def test_shop(driver):
    with allure.step("Авторизация"):
        avtoriz = Avtoriz(driver)
        avtoriz.avtor(login="standard_user", password="secret_sauce")
    with allure.step("Добавление товара в корзину"):
        shop = Shop(driver)
        shop.make_shop()
        shop.go_to()
    with allure.step("Проверка содержимого корзины"):
        checkout = Checkout(driver)
        checkout.chek()
    with allure.step("Заполнение данных покупателя"):
        cart = Cart(driver)
        cart.main_post(name="Мария", last_name="Асадуллаева", code="603053")
    with allure.step("Проверка итога"):
        total = Total(driver)
        res = total._print_()
        assert res == "Total: $58.29"