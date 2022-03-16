from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
    

