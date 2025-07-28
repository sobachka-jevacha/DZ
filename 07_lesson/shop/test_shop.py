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
    shop.go_to()
    checkout = Checkout(driver)
    checkout.chek()
    cart = Cart(driver)
    cart.main_post()
    total = Total(driver)
    res = total._print_()
    assert res == "Total: $58.29"