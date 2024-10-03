import time

import pytest
from Pages.product_page import ProductPage
from Pages.basket_page import BasketPage
from Pages.login_page import LoginPage


@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                              "/?promo=offer7", marks=pytest.mark.xfail),
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.click_on_the_button()
    page.solve_quiz_and_get_code()
    title = page.item_name()
    price = page.item_price()
    added_title = page.item_added_name()
    calc = page.cart_value()
    assert title == added_title
    assert price == calc


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, url="http://selenium1py"
                                                                                    ".pythonanywhere.com"
                                                                                    "/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, url)
    page.open()
    page.click_on_the_button()
    page.should_be_not_success_message()


def test_guest_cant_see_success_message(browser, url="http://selenium1py"
                                                                                    ".pythonanywhere.com"
                                                                                    "/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_not_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, url="http://selenium1py"
                                                                                    ".pythonanywhere.com"
                                                                                    "/catalogue/coders-at-work_207/"):
    page = ProductPage(browser, url)
    page.open()
    page.click_on_the_button()
    page.should_be_desappear()


@pytest.mark.xfail
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, url="http://selenium1py"
                                                                                    ".pythonanywhere.com"
                                                                                    "/catalogue/coders-at-work_207/"):
    page = BasketPage(browser, url)
    page.open()
    page.go_to_cart_page()
    page.should_cart_is_not_empty()


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, url="http://selenium1py.pythonanywhere.com/accounts/login/")
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, url="http://selenium1py"
                                                         ".pythonanywhere.com"
                                                         "/catalogue/coders-at-work_207/"):
        page = ProductPage(browser, url)
        page.open()
        page.should_be_not_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, url="http://selenium1py.pythonanywhere.com/catalogue"
                                                               "/coders-at-work_207/?promo=offer0"):
        page = ProductPage(browser, url)
        page.open()
        page.click_on_the_button()
        page.solve_quiz_and_get_code()
        title = page.item_name()
        price = page.item_price()
        added_title = page.item_added_name()
        calc = page.cart_value()
        assert title == added_title
        assert price == calc

