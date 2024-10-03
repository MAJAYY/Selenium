from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def click_on_the_button(self):
        return self.find(*ProductPageLocators.BUTTON_ADD_TO_CART).click()

    def item_name(self):
        return self.find(*ProductPageLocators.ITEM_NAME).text

    def item_added_name(self):
        return self.find(*ProductPageLocators.NAME_OFF_ITEM).text

    def item_price(self):
        return self.find(*ProductPageLocators.ITEM_PRICE).text

    def cart_value(self):
        return self.find(*ProductPageLocators.CART_VALUE).text

    def should_be_not_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ITEM_ADDED), \
            "Success message is presented, but should not be"

    def should_be_desappear(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ITEM_ADDED), \
            "Message didnt desappear"


