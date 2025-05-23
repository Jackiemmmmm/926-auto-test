class LoginPage {
  // Page URL path
  path = "http://localhost:5173/login";

  // Page elements selectors
  selectors = {
    usernameInput: "#username",
    passwordInput: "#password",
    loginButton: 'button[type="submit"]',
    userNameText: "#radix-\\:ri\\: div span:nth-child(1)",
    userEmailText: "#radix-\\:ri\\: div span:nth-child(2)",
  };

  /**
   * Navigate to the login page
   */
  visit() {
    cy.visit(this.path);
    return this;
  }

  /**
   * Enter text in the username field
   * @param {string} username - Username to enter
   */
  enterUsername(username) {
    cy.get(this.selectors.usernameInput).clear().type(username);
    return this;
  }

  /**
   * Enter text in the password field
   * @param {string} password - Password to enter
   */
  enterPassword(password) {
    cy.get(this.selectors.passwordInput).clear().type(password);
    return this;
  }

  /**
   * Click login button and wait for navigation
   */
  clickLogin() {
    // Click the login button
    cy.get(this.selectors.loginButton).click();

    // Wait for URL to change to onboarding
    cy.url().should("include", "/onboarding");

    return this;
  }

  /**
   * Check if the current page is the onboarding page
   */
  shouldBeOnOnboardingPage() {
    cy.url().should("include", "/onboarding");
    return this;
  }

  /**
   * Check if the page contains a specific message
   * @param {string} message - Message to check for
   */
  shouldContainMessage(message) {
    cy.contains(message).should("be.visible");
    return this;
  }

  /**
   * Get the user name from the page
   */
  getUserName() {
    return cy.get(this.selectors.userNameText);
  }

  /**
   * Get the user email from the page
   */
  getUserEmail() {
    return cy.get(this.selectors.userEmailText);
  }

  /**
   * Login with provided credentials
   * @param {string} username - Username to use
   * @param {string} password - Password to use
   */
  login(username, password) {
    this.enterUsername(username);
    this.enterPassword(password);
    this.clickLogin();
    return this;
  }
}

export default LoginPage;
