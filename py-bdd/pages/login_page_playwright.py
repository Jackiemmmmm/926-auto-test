from playwright.sync_api import Page


class LoginPagePlaywright:
    """Login page Page Object Model"""

    # page URL path
    PATH = "/login"

    # page elements selectors
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    USER_NAME_TEXT = "#radix-\\:ri\\: div span:nth-child(1)"
    USER_EMAIL_TEXT = "#radix-\\:ri\\: div span:nth-child(2)"

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        

    def navigate(self):
        """Navigate to the login page"""
        self.page.goto(f"{self.base_url}{self.PATH}")
        return self

    def enter_username(self, username: str):
        """text in the username field"""
        self.page.fill(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        """text in the password field"""
        self.page.fill(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        """login button"""
        self.page.click(self.LOGIN_BUTTON)
        self.page.wait_for_url("**/onboarding**", timeout=5000)
        return self

    def is_on_onboarding_page(self) -> bool:
        """check if the current page is the onboarding page"""
        current_url = self.page.url
        return "/onboarding" in current_url

    def get_message(self, message: str) -> str:
        """get the message from the page"""
        return self.page.get_by_text(message).inner_text()

    def get_user_name(self) -> str:
        """Get the user name text"""
        try:
            return self.page.locator(self.USER_NAME_TEXT).text_content()
        except:
            return ""

    def get_user_email(self) -> str:
        """Get the user email text"""
        try:
            return self.page.locator(self.USER_EMAIL_TEXT).text_content()
        except:
            return ""
