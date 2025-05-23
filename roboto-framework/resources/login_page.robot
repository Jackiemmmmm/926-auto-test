*** Settings ***
Documentation     Login page keywords
Library           SeleniumLibrary
Variables         ../variables/login_variables.py

*** Keywords ***
Enter Username
    [Arguments]    ${username}
    Clear Element Text    ${USERNAME_FIELD}
    Input Text    ${USERNAME_FIELD}    ${username}

Enter Password
    [Arguments]    ${password}
    Clear Element Text    ${PASSWORD_FIELD}
    Input Text    ${PASSWORD_FIELD}    ${password}

Click Login Button
    Click Button    ${LOGIN_BUTTON}

User Should Be Successfully Logged In
    Wait Until Location Contains    /onboarding    timeout=${TIMEOUT}
    Location Should Contain    /onboarding

Page Should Display User's Email
    [Arguments]    ${expected_email}
    Wait Until Element Is Visible    ${USER_EMAIL_FIELD}    timeout=${TIMEOUT}
    Element Should Contain    ${USER_EMAIL_FIELD}    ${expected_email}

Error Message Should Be Displayed
    [Arguments]    ${expected_message}
    Wait Until Page Contains    ${expected_message}    timeout=${TIMEOUT}
    Page Should Contain    ${expected_message}

When Enter Username
    [Arguments]    ${username}
    Enter Username    ${username}

And Enter Password
    [Arguments]    ${password}
    Enter Password    ${password}

And Click Login Button
    Click Login Button

Then User Should Be Successfully Logged In
    User Should Be Successfully Logged In

And Page Should Display User's Email
    [Arguments]    ${expected_email}
    Page Should Display User's Email    ${expected_email}

Then Error Message Should Be Displayed
    [Arguments]    ${expected_message}
    Error Message Should Be Displayed    ${expected_message}