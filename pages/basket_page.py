from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BucketPageLocators

class BasketPage(BasePage): 
    def bucket_is_empty_text(self):
        assert self.browser.find_element(*BucketPageLocators.BUCKET_EMPTY).text == 'Your basket is empty. Continue shopping', "Bucket not empty"

    def bucket_is_empty_text(self):
        assert self.is_not_element_present(*BucketPageLocators.BUCKET_ITEMS), "Bucket not empty"


   