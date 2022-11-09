from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()

    def check_item_added_to_basket(self):
        self.check_item_name_added_to_basket()
        self.cost_should_be_equal_price()

    def check_item_name_added_to_basket(self):
        title_of_item = self.browser.find_element(*ProductPageLocators.TITLE_OF_THE_ITEM).text
        message_after_add = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADD_ITEM).text
        assert title_of_item == message_after_add, 'Book titles do not match'

    def cost_should_be_equal_price(self):
        price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert price_item == basket_total, 'Basket cost value does not match book price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but ' \
                                                                                  'should not be '

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message not disappeared, but ' \
                                                                          'should be '
