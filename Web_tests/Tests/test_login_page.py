"""
Test cases for the login page <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
"""


def test_url_login_page(driver, login_page, domain_part):
    """
    1. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    Check if the current URL matches the valid URL login page
    """
    login_page.go_to_login_page(domain_part)
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', \
        'The current URL does not match the valid URL'


def test_title_on_base_page(login_page):
    """
    1. Go to a valid URL
        <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    Check if the title of the page is value <Login>
    """
    assert login_page.is_displayed_title_login_page(), \
        'The title of the page is not displayed'
    assert login_page.title_login_page.text == 'Login', \
        'The title of the page is not correct'


def test_go_to_account_page_without_user_registration(driver, account_page, domain_part):
    """
    1. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index>.
    We check that we cannot enter the account page without initial registration
    """
    account_page.go_to_account_page(domain_part)
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', \
        'The current URL does not match the valid URL'


def test_is_displayed_objects_on_login_page(login_page):
    """
    1. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    Check if the elements(username field, password field, login button) are displayed on the login page
    """
    assert login_page.is_displayed_objects(), \
        'The elements(username field, password field, login button) are not displayed'


def test_login_valid_user(login_page, valid_user, driver):
    """
    1. Navigate to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    2. Enter a valid username <Admin> in the username field.
    3. Enter a valid password <admin123> in the password field.
    4. Click the login button.
     Make sure the user is logged in and on the Dashboard page.
    """
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index', \
        'The current URL does not match the valid URL'


def test_title_account_page_after_user_registration(login_page, valid_user, account_page):
    """
    1. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    2. Enter a valid username <Admin> in the username field.
    3. Enter a valid password <admin123> in the password field.
    4. Press the login button.
    Check that the title of the page is value <Dashboard>
    """
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    assert account_page.is_displayed_title_account_page(), \
        'The title of the page is not displayed'
    assert account_page.title_page.text == 'Dashboard', \
        'The title of the page is not correct'


def test_refresh_account_page_for_valid_user(driver, login_page, valid_user):
    """
    1. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    2. Enter a valid username <Admin> in the username field.
    3. Enter a valid password <admin123> in the password field.
    4. Press the login button.
    5. Refresh the page.
    After updating the account page, we check to see if we remain on the same page we were on.
    """
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(valid_user)
    login_page.refresh_page()
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index', \
        'The current URL does not match the valid URL'


def test_login_invalid_user(driver, login_page, invalid_user):
    """
    1. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    2. Enter the incorrect username < Admin> in the username field.
    3. Enter the incorrect password <ADMIN123> in the password field.
    4. Press the login button.
    We check that after registering an invalid user we remain on the login page
    """
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(invalid_user)
    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', \
        'The current URL does not match the valid URL'


def test_correct_text_error_message_for_invalid_user(login_page, invalid_user, error_message):
    """
    1. Go to a valid URL <https://opensource-demo.orangehrmlive.com/web/index.php/auth/login>.
    2. Enter the incorrect username < Admin> in the username field.
    3. Enter the incorrect password <ADMIN123> in the password field.
    4. Press the login button.
    Checking whether the correct text of the error message is displayed
    """
    login_page.clear_fields()
    login_page.enter_user_data_and_click_to_login_button(invalid_user)
    assert login_page.is_displayed_error_message(), \
        'The error message is not displayed'
    assert login_page.error_message.text == error_message, \
        'The correct error message is not displayed'







