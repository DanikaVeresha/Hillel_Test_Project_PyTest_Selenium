from selenium.webdriver.common.by import By
from Web_tests.Pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    TITLE_PAGE = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')

    # Find the elements ->
    @property
    def title_page(self):
        return self.find_element(AccountPage.TITLE_PAGE)

    # Open the page ->
    def account_page(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
        return self

    # Check if the elements are displayed ->
    def is_displayed_title_page(self):
        return self.title_page.is_displayed()
