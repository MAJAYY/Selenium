from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_CART_IS_EMPTY), "Нет сообщения о пустой корзине"

    def should_cart_is_not_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_CART), "Нет локатара о товарах в корзине"

