"""
This module contains the class LoginPage for the login page.
"""

from selenium.webdriver.common.by import By
from Web_tests.Pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.TAG_NAME, 'button')
    TITLE_LOGIN_PAGE = (By.TAG_NAME, 'h5')
    ERROR_MESSAGE_INVALID_CREDENTIALS = (By.TAG_NAME, 'p')

# Find the elements ->
    @property
    def username_field(self):
        return self.find_element(LoginPage.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.find_element(LoginPage.PASSWORD_FIELD)

    @property
    def login_button(self):
        return self.find_element(LoginPage.LOGIN_BUTTON)

    @property
    def title_login_page(self):
        return self.find_element(LoginPage.TITLE_LOGIN_PAGE)

    @property
    def error_message(self):
        return self.find_element(LoginPage.ERROR_MESSAGE_INVALID_CREDENTIALS)


# Open the page ->
    def go_to_login_page(self, domain):
        self.driver.get("".join([domain, 'web/index.php/auth/login']))
        return self


# Check if the elements are displayed ->
    def is_displayed_username_field(self):
        return self.username_field.is_displayed()

    def is_displayed_password_field(self):
        return self.password_field.is_displayed()

    def is_displayed_login_button(self):
        return self.login_button.is_displayed()

    def is_displayed_title_login_page(self):
        return self.title_login_page.is_displayed()

    def is_displayed_objects(self):
        self.is_displayed_username_field()
        self.is_displayed_password_field()
        self.is_displayed_login_button()
        self.is_displayed_title_login_page()
        return self

    def is_displayed_error_message(self):
        return self.error_message.is_displayed()


# Clear the fields ->
    def clear_username_field(self):
        return self.username_field.clear()

    def clear_password_field(self):
        return self.password_field.clear()

    def clear_fields(self):
        self.clear_username_field()
        self.clear_password_field()
        return self


# Enter the user data and click the button ->
    def enter_username(self, user):
        self.username_field.send_keys(user.username)
        return self

    def enter_password(self, user):
        self.password_field.send_keys(user.password)
        return self

    def click_login_button(self):
        self.login_button.click()

    def enter_user_data_and_click_to_login_button(self, user):
        self.enter_username(user)
        self.enter_password(user)
        self.click_login_button()





