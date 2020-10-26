from .base_page import BasePage
from .locators import ProductPageLocators
import time 

class ProductPage(BasePage):         
    def save_other_info(self):
        self.name = self.browser.find_element(*ProductPageLocators.TEXT_NAME).text
        self.price = self.browser.find_element(*ProductPageLocators.TEXT_PRICE).text

    def add_in_bucket(self):
    # метод для добавления в корзину
        button_add_bucket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BUCKET)
        button_add_bucket.click()

        # self.solve_quiz_and_get_code()

    def should_be_product_page(self):
        self.should_be_name_product()
        self.should_be_price_product()


    def should_be_name_product(self):
        #Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили
        text_name_el = self.get_elem(*ProductPageLocators.MASSAGE_TEXT_NAME)

        assert text_name_el, "Name product is not presented"
        
        assert text_name_el.text == f"{self.name} has been added to your basket.", "Product name does not match the desired one"

    def should_be_price_product(self):
        #Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        text_price_el = self.get_elem(*ProductPageLocators.MASSAGE_TEXT_PRICE)

        assert text_price_el, "Price product is not presented"
        assert text_price_el.text == f'Your basket total is now {self.price}', "Product price does not match the desired one"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MASSAGE_TEXT_NAME), \
       "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MASSAGE_TEXT_NAME), \
       "Success message is appear, but should disappear"
