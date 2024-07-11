"""
Test cases for the login page <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
"""


# Test Case 1
def test_title_on_base_page(login_page):
    """
    1. Go to a valid URL
        <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    Check if the title of the page is <Login>
    """
    assert login_page.is_displayed_title_login_page(), \
        'The title of the page is not displayed'
    assert login_page.title_login_page.text == 'Login', \
        'The title of the page is not correct'


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
    Check that the user is logged in to the Dashboard page
    """
    login_page.is_displayed_objects()
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    assert account_page.is_displayed_title_page(), \
        'The title of the page is not displayed'
    assert account_page.title_page.text == 'Dashboard', \
        'The title of the page is not correct'


# Test Case 3
def test_URL_account_page_for_valid_user(driver, login_page, valid_user):
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
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index', \
        'The current URL does not match the valid URL'


# Test Case 4
def test_refresh_account_page_for_valid_user(driver, login_page, valid_user):
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
    After updating the account page, we check to see if we remain on the same page we were on.
    """
    login_page.is_displayed_objects()
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    login_page.refresh_page()
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index', \
        'The current URL does not match the valid URL'


# Test Case 5
def test_login_invalid_user(driver, login_page, invalid_user, error_message):
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
    Checking whether a correct error message is displayed
    """
    login_page.is_displayed_objects()
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(invalid_user)
    login_page.is_displayed_error_message()
    assert login_page.error_message.text == error_message, \
        'The correct error message is not displayed'


# Test Case 6
def test_URL_page_for_invalid_user(driver, login_page, invalid_user, error_message):
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
    We check that after entering incorrect user data we remain on the Login page
    """
    login_page.is_displayed_objects()
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(invalid_user)
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', \
        'The current URL does not match the valid URL'



