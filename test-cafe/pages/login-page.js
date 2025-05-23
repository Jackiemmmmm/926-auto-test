import { Selector, t } from "testcafe";
import XPathSelector from "../tests/x-path-selector";

class LoginPage {
  // Page elements selectors
  usernameInput = Selector("#username");
  passwordInput = Selector("#password");
  loginButton = Selector('button[type="submit"]');
  userNameText = Selector("#radix-\\:ri\\: div span").nth(0);
  userEmailText = Selector("#radix-\\:ri\\: div span").nth(1);

  /**
   * Navigate to the login page
   */
  async visit() {
    const loginButton = XPathSelector(
      '//*[@id="root"]/div[1]/main/section[1]/div/div/div[2]/a[1]'
    );
    await t.click(loginButton);
    return this;
  }

  /**
   * Enter text in the username field
   * @param {string} username - Username to enter
   */
  async enterUsername(username) {
    await t.typeText(this.usernameInput, username, { replace: true });
    return this;
  }

  /**
   * Enter text in the password field
   * @param {string} password - Password to enter
   */
  async enterPassword(password) {
    await t.typeText(this.passwordInput, password, { replace: true });
    return this;
  }

  /**
   * Click login button and wait for navigation
   */
  async clickLogin() {
    await t.click(this.loginButton);
    await t.expect(t.eval(() => window.location.href)).contains("/onboarding");

    return this;
  }

  /**
   * Check if the current page is the onboarding page
   */
  async shouldBeOnOnboardingPage() {
    await t.expect(t.eval(() => window.location.href)).contains("/onboarding", {
      timeout: 5000,
    });
    return this;
  }

  /**
   * Check if the page contains a specific message
   * @param {string} message - Message to check for
   */
  async shouldContainMessage(message) {
    const messageElement = Selector("body").withText(message);
    await t.expect(messageElement.exists).ok({ timeout: 5000 });
    return this;
  }

  /**
   * Get the user name from the page
   */
  async getUserName() {
    return await this.userNameText.innerText;
  }

  /**
   * Get the user email from the page
   */
  async getUserEmail() {
    return await this.userEmailText.innerText;
  }

  /**
   * Login with provided credentials
   * @param {string} username - Username to use
   * @param {string} password - Password to use
   */
  async login(username, password) {
    await this.enterUsername(username);
    await this.enterPassword(password);
    await this.clickLogin();
    return this;
  }
}

export default new LoginPage();
