from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    TEXT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    TEXT_PRICE = (By.CSS_SELECTOR, "div.product_main> p.price_color")
    MASSAGE_TEXT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MASSAGE_TEXT_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)")
    BUTTON_ADD_BUCKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUCKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    BUCKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p > font > font")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BucketPageLocators():
    BUCKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BUCKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

#basket_formset > div