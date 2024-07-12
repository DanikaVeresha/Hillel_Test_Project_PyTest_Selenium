"""
File with fixtures for tests
"""

import pytest

from selenium.webdriver import Chrome
from Web_tests.Helpers.user_data import UserData
from Web_tests.Pages.login_page import LoginPage
from Web_tests.Pages.user_account_page import AccountPage


@pytest.fixture()
def domain_part():
    return 'https://opensource-demo.orangehrmlive.com/'


@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def valid_user():
    return UserData('Admin', 'admin123')


@pytest.fixture(scope='session')
def invalid_user():
    return UserData(' Admin', 'ADMIN123')


@pytest.fixture()
def login_page(driver, domain_part):
    return LoginPage(driver).go_to_login_page(domain_part)


@pytest.fixture()
def account_page(driver, domain_part):
    return AccountPage(driver).go_to_account_page(domain_part)


@pytest.fixture()
def error_message():
    return 'Invalid credentials'




