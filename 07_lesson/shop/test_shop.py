from time import sleep
import pytest
from shop_page import Avtoriz, Shop, Checkout, Cart, Total
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    avtoriz = Avtoriz(driver)
    avtoriz.avtor()
    shop = Shop(driver)
    shop.make_shop()
    sleep(4)
    shop.go_to()
    checkout = Checkout(driver)
    checkout.chek()
    cart = Cart(driver)
    sleep(10)
    cart.main_post()
    total = Total(driver)
    total._print_()