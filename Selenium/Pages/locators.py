from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "wqe")  # Неправильный локатор
    BUTTON_GO_TO_CART = (By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1")
    ITEM_PRICE = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    MESSAGE_ITEM_ADDED = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")
    NAME_OFF_ITEM = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    CART_VALUE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")


class BasketPageLocators:
    MESSAGE_CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    ITEMS_IN_CART = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]/div/h2")


class LoginPageLocators:
    INPUT_EMAIL = (By.ID, "id_registration-email")
    INPUT_PASSWORD1 = (By.ID, "id_registration-password1")
    INPUT_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")


