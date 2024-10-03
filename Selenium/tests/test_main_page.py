from Pages.main_page import MainPage
from Pages.basket_page import BasketPage

url = "http://selenium1py.pythonanywhere.com/ru/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, url)
    page.open()
    page.go_to_cart_page()
    page.should_cart_is_empty()
