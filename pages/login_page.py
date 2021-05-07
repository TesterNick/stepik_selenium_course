from .base_page import BasePage
from .locators import LoginPageLocators as Locators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login = "login"
        message = f'"{login}" is not in current url'
        assert login in self.browser.current_url, message

    def should_be_login_form(self):
        message = "Login form is not found"
        assert self.is_element_present(*Locators.LOGIN_FORM), message

    def should_be_register_form(self):
        message = "Register form is not found"
        assert self.is_element_present(*Locators.REGISTER_FORM), message
