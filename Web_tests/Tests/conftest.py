"""
Open browser and close it after test
"""

import pytest

from selenium.webdriver import Chrome
from Web_tests.Helpers.url_base_page import URLPages as url
from Web_tests.Helpers.user_data import UserData as user
from Web_tests.Helpers.error_message import ErrorMessage as error
from Web_tests.Pages.login_page import LoginPage
from Web_tests.Pages.user_account_page import AccountPage


# TODO: Specify path to chromedriver there
service_path = '/usr/local/bin/chromedriver'


@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def url_base_page():
    return url('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


@pytest.fixture()
def url_account_page():
    return url('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')


@pytest.fixture(scope='session')
def valid_user():
    return user('Admin', 'admin123')


@pytest.fixture(scope='session')
def invalid_user():
    return user(' Admin', 'ADMIN123')


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver).login_page()


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver).account_page()


@pytest.fixture(scope='session')
def error_message():
    return error('Invalid credentials')


