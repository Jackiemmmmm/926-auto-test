*** Settings ***
Documentation     Shared resources and settings
Library           SeleniumLibrary
Library           ../libraries/custom_keywords.py
Variables         ../variables/login_variables.py

*** Variables ***
${BROWSER}        Chrome
${TIMEOUT}        10
${LOGIN_URL}      http://localhost:5173/login

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}
    Wait Until Element Is Visible    ${USERNAME_FIELD}

Close Browser
    Capture Page Screenshot
    Close All Browsers