*** Settings ***
Documentation     Login functionality test suite
Resource          ../resources/common.robot
Resource          ../resources/login_page.robot
Test Setup        Open Browser To Login Page
Test Teardown     Close Browser
Default Tags      login

*** Test Cases ***
Successfully Login With Valid Credentials
    [Documentation]    Verify that users can successfully login with valid credentials
    [Tags]    positive    smoke
    When Enter Username    ${VALID_USER}[username]
    And Enter Password    ${VALID_USER}[password]
    And Click Login Button
    Then User Should Be Successfully Logged In
    And Page Should Display User's Email    ${VALID_USER}[username]