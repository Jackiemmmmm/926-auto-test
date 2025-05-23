from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageSelenium:
    """Login page Page Object Model for Selenium"""

    # page URL path
    PATH = "/login"

    # page elements selectors
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Continue']")
    USER_NAME_TEXT = (By.XPATH, '//*[@id="radix-:ri:"]/div/span[1]')
    USER_EMAIL_TEXT = (By.XPATH, '//*[@id="radix-:ri:"]/div/span[2]')

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 10)

    def navigate(self):
        """Navigate to the login page"""
        self.driver.get(f"{self.base_url}{self.PATH}")
        return self

    def enter_username(self, username: str):
        """Enter text in the username field"""
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)
        return self

    def enter_password(self, password: str):
        """Enter text in the password field"""
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login(self):
        """Click login button and wait for navigation"""
        # Store current URL for comparison
        current_url = self.driver.current_url

        # Click the login button
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

        # Wait for URL to change
        self.wait.until(EC.url_changes(current_url))

        # Wait for onboarding URL if needed
        try:
            # Additional check that we're on the onboarding page
            self.wait.until(lambda driver: "/onboarding" in driver.current_url)
        except:
            pass

        return self

    def is_on_onboarding_page(self) -> bool:
        """Check if the current page is the onboarding page"""
        current_url = self.driver.current_url
        return "/onboarding" in current_url

    def get_message(self, message: str) -> str:
        """Get the message from the page containing the specified text"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(),'{message}')]")
                )
            )
            return element.text
        except:
            return ""

    def get_user_name(self) -> str:
        """Get the user name text"""
        try:
            user_name = self.wait.until(
                EC.visibility_of_element_located(self.USER_NAME_TEXT)
            )
            return user_name.text
        except:
            return ""

    def get_user_email(self) -> str:
        """Get the user email text"""
        try:
            user_email = self.wait.until(
                EC.visibility_of_element_located(self.USER_EMAIL_TEXT)
            )
            return user_email.text
        except:
            return ""
