from .base_page import BasePage
from .locators import LoginPageLocators
from faker import Faker


class LoginPage(BasePage):
    def register_new_user(self):
        fake = Faker()
        email = fake.email()
        password = fake.password(length=9)
        email_field = self.find(*LoginPageLocators.INPUT_EMAIL)
        pass_field1 = self.find(*LoginPageLocators.INPUT_PASSWORD1)
        pass_field2 = self.find(*LoginPageLocators.INPUT_PASSWORD2)
        btn_submit = self.find(*LoginPageLocators.REGISTRATION_BUTTON)
        email_field.send_keys(email)
        pass_field1.send_keys(password)
        pass_field2.send_keys(password)
        btn_submit.click()



