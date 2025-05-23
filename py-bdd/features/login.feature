Feature: the login functionality of the website
  as a website user
  I want to be able to log in to my account
  so that I can access my personal information and services

  Background:
    Given user is open the login page

  Scenario: Login with valid credentials
    When user enters username "jackie.tu@zerocap.com"
    And user enters password "Q1w2e3r4."
    And user clicks the login button
    Then user should see the success login page
    And The page should display a message containing the Email "jackie.tu@zerocap.com"
    And The page should display a message containing the Name "Tu Yucheng"
