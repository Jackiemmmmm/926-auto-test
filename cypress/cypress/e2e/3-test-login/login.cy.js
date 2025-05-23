import LoginPage from "../../pages/login-page";

describe("Login Functionality", () => {
  const loginPage = new LoginPage();

  beforeEach(() => {
    // Reset state and visit login page before each test
    cy.clearCookies();
    cy.clearLocalStorage();
    loginPage.visit();
  });

  it("Successfully logs in with valid credentials", () => {
    // Given a user is on the login page
    // Already handled by beforeEach

    // When user enters valid credentials and clicks login
    loginPage
      .enterUsername("jackie.tu@zerocap.com")
      .enterPassword("Q1w2e3r4.")
      .clickLogin();

    // Then user should be on the onboarding page
    loginPage.shouldBeOnOnboardingPage();

    // And the user email should be displayed
    loginPage.getUserEmail().should("contain", "jackie.tu@zerocap.com");

    // Log user information for debugging
    cy.log("Login successful");
    loginPage.getUserName().then(($name) => {
      loginPage.getUserEmail().then(($email) => {
        cy.log(`Logged in user: ${$name.text()}, ${$email.text()}`);
      });
    });
  });
});
