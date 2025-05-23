import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page_selenium import LoginPageSelenium

# import all scenarios from the login file
scenarios("../features/login.feature")


# share test context between steps
@pytest.fixture
def login_context():
    return {}


@given("user is open the login page", target_fixture="selenium_login_page")
def open_login_page(selenium_driver: WebDriver, base_url):
    """open the login page"""
    login_page = LoginPageSelenium(selenium_driver, base_url)
    login_page.navigate()
    return login_page


@when(parsers.parse('user enters username "{username}"'))
def enter_username(selenium_login_page: LoginPageSelenium, username):
    """enter username"""
    selenium_login_page.enter_username(username)


@when(parsers.parse('user enters password "{password}"'))
def enter_password(selenium_login_page: LoginPageSelenium, password):
    """enter password"""
    selenium_login_page.enter_password(password)


@when("user clicks the login button")
def click_login_button(selenium_login_page: LoginPageSelenium):
    """click the login button"""
    selenium_login_page.click_login()


@then("user should see the success login page")
def verify_successful_login(selenium_login_page: LoginPageSelenium):
    """Validate successful login"""
    assert (
        selenium_login_page.is_on_onboarding_page()
    ), "user is not on the onboarding page"

    # Get and print user name and email
    user_name = selenium_login_page.get_user_name()
    user_email = selenium_login_page.get_user_email()
    print(f"Logged in user (Selenium): {user_name}, {user_email}")


@then(parsers.parse('The page should display a message containing the Email "{email}"'))
def verify_email_displayed(selenium_login_page: LoginPageSelenium, email):
    """Validate the email is displayed on the page"""
    user_email = selenium_login_page.get_user_email()
    assert email in user_email, f"Expected email '{email}' not found in '{user_email}'"


@then(parsers.parse('The page should display a message containing the Name "{name}"'))
def verify_name_displayed(selenium_login_page: LoginPageSelenium, name):
    """Validate the name is displayed on the page"""
    user_name = selenium_login_page.get_user_name()
    assert name in user_name, f"Expected name '{name}' not found in '{user_name}'"
