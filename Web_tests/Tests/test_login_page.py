import pytest


# Test Case 1
def test_URL_base_page(driver, url_base_page):
    """
    1. Open the Chrome browser.
    2. Go to a valid URL
        <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    Check if the current page URL matches the valid URL
        <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    """
    driver.get(url_base_page.url)
    assert driver.current_url == url_base_page.url, 'The current URL does not match the valid URL'


# Test Case 2
def test_login_valid_user(login_page, account_page, valid_user):
    """
    1. Open the Chrome browser.
    2. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    3. On the basic page we see the <Login> header.
    4. On the page we see a field for entering a username.
    5. On the page we see a field for entering a password.
    6. We see the login button.
    7. The username and password fields are empty.
    8. Enter a valid username <Admin> and password <admin123>.
    9. Press the login button.
    Check if the <Dashboard> header is visible on the account page.
    """
    login_page.is_displayed_objects()
    login_page.clier_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    assert account_page.is_displayed_title_page(), 'The title of the page is not displayed'


# Test Case 3
def test_URL_account_page_for_registered_user(driver, login_page, url_account_page, valid_user):
    """
    1. Open the Chrome browser.
    2. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    3. We see the <Login> header on the page.
    4. On the basic page we see a field for entering a username.
    5. We see a field for entering a password.
    6. We see the login button.
    7. The username and password fields are empty.
    8. Enter a valid username <Admin> and password <admin123>.
    9. Press the login button.
    Check if the current URL matches a valid URL
        <https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index>.
    """
    login_page.is_displayed_objects()
    login_page.clier_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    assert driver.current_url == url_account_page.url, 'The current URL does not match the valid URL'


# Test Case 4
def test_login_invalid_user(login_page, invalid_user):
    """
    1. Open the Chrome browser.
    2. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    3. We see the <Login> header on the page.
    4. We see a field for entering a username.
    5. We see a field for entering a password.
    6. We see the login button.
    7. The username and password fields are empty.
    8. Enter the incorrect username < Admin> and password <ADMIN123>.
    9. Press the login button.
    Checking whether an error message about entering incorrect data is displayed
    """
    login_page.is_displayed_objects()
    login_page.clier_fields()
    login_page.enter_user_data_and_click_to_login_button(invalid_user)
    assert login_page.is_displayed_error_message_invalid_credentials(), \
        'The error message is not displayed'


# Test Case 5
def test_error_message_invalid_credentials(login_page, invalid_user, error_message):
    """
    1. Open the Chrome browser.
    2. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    3. We see the <Login> header on the page.
    4. We see a field for entering a username.
    5. We see a field for entering a password.
    6. We see the login button.
    7. The username and password fields are empty.
    8. Enter the incorrect username < Admin> and password <ADMIN123>.
    9. Press the login button.
    We check whether the text of the error message about entering incorrect data matches
    """
    login_page.is_displayed_objects()
    login_page.clier_fields()
    login_page.enter_user_data_and_click_to_login_button(invalid_user)
    assert login_page.error_message_invalid_credentials.text == error_message.error_message, \
        'The error message is not correct'


# Test Case 6
def test_refresh_account_page(driver, login_page, valid_user, url_account_page):
    """
    1. Open the Chrome browser.
    2. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    3. We see the <Login> header on the page.
    4. We see a field for entering a username.
    5. We see a field for entering a password.
    6. We see the login button.
    7. The username and password fields are empty.
    8. Enter a valid username <Admin> and password <admin123>.
    9. Press the login button.
    10. Refresh the page.
    We check that we remain on the same page we were on before refreshing
    """
    login_page.is_displayed_objects()
    login_page.clier_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    login_page.refresh_page()
    assert driver.current_url == url_account_page.url, \
        'The current URL does not match the valid URL'
