from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*Locators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_correct_product_name_in_success_message(self):
        expected_name = self.browser.find_element(*Locators.BOOK_TITLE).text
        actual_name = self.browser.find_element(*Locators.ADDED_BOOK_TITLE).text
        assert actual_name == expected_name, "Wrong book added to basket"

    def should_be_basket_total_equals_book_price(self):
        price = self.browser.find_element(*Locators.BOOK_PRICE).text
        basket_total = self.browser.find_element(*Locators.BASKET_TOTAL).text
        assert basket_total == price, "Wrong basket total"
