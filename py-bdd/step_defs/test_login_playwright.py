import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

from pages.login_page_playwright import LoginPagePlaywright

# import all scenarios from the login file
scenarios("../features/login.feature")


# share test context between steps
@pytest.fixture
def login_context():
    return {}


@given("user is open the login page", target_fixture="login_page")
def open_login_page(page: Page, base_url: str):
    """open the login page"""
    login_page = LoginPagePlaywright(page, base_url)
    login_page.navigate()
    return login_page


@when(parsers.parse('user enters username "{username}"'))
def enter_username(login_page: LoginPagePlaywright, username):
    """enter username"""
    login_page.enter_username(username)


@when(parsers.parse('user enters password "{password}"'))
def enter_password(login_page: LoginPagePlaywright, password):
    """enter password"""
    login_page.enter_password(password)


@when("user clicks the login button")
def click_login_button(login_page: LoginPagePlaywright):
    """click the login button"""
    login_page.click_login()


@then("user should see the success login page")
def verify_successful_login(login_page: LoginPagePlaywright):
    """Validate successful login"""
    assert login_page.is_on_onboarding_page(), "user is not on the onboarding page"

    user_name = login_page.get_user_name()
    user_email = login_page.get_user_email()
    print(f"Logged in user (Playwright): {user_name}, {user_email}")


@then(parsers.parse('The page should display a message containing the Email "{email}"'))
def verify_success_message(login_page: LoginPagePlaywright, email):
    """Validate success message"""
    user_email = login_page.get_user_email()
    assert (
        email in user_email
    ), f"Excepted message '{email}' not in real message '{user_email}'"


@then(parsers.parse('The page should display a message containing the Name "{name}"'))
def verify_success_message(login_page: LoginPagePlaywright, name):
    """Validate success message"""
    name_message = login_page.get_user_name()
    assert (
        name in name_message
    ), f"Excepted message '{name}' not in real message '{name_message}'"
