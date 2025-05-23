import LoginPage from "../pages/login-page";

fixture("Getting Started")
  .page("http://localhost:5173")
  .beforeEach(async (t) => {
    // 在每个测试前清除缓存和本地存储
    await t.eval(() => {
      window.localStorage.clear();
      window.sessionStorage.clear();

      // 清除cookie的替代方案
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i];
        const eqPos = cookie.indexOf("=");
        const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
      }
    });
  });

test("Successfully logs in with valid credentials", async (t) => {
  // Given a user is on the login page

  await LoginPage.visit();
  // When user enters valid credentials and clicks login
  await LoginPage.enterUsername("jackie.tu@zerocap.com");
  await LoginPage.enterPassword("Q1w2e3r4.");
  await LoginPage.clickLogin();

  // Then user should be on the onboarding page
  await LoginPage.shouldBeOnOnboardingPage();

  // And the user email should be displayed
  const userEmail = await LoginPage.getUserEmail();
  await t.expect(userEmail).contains("jackie.tu@zerocap.com");

  // Log user information for debugging
  const userName = await LoginPage.getUserName();
  console.log(`Logged in user: ${userName}, ${userEmail}`);
});
