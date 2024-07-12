"""
This module contains the AccountPage class for the user account page.
"""
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from Web_tests.Pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    TITLE_PAGE = (By.TAG_NAME, 'h6')

# Find the elements ->
    @property
    def title_page(self):
        return self.find_element(AccountPage.TITLE_PAGE)

# Open the page ->
    def go_to_account_page(self, domain):
        self.driver.get(urljoin(domain, 'web/index.php/dashboard/index'))
        return self

# Check if the elements are displayed ->
    def is_displayed_title_account_page(self):
        return self.title_page.is_displayed()
