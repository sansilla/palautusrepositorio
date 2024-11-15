*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Starting Page

*** Variables ***
${SERVER}        localhost:5001
${DELAY}         0.5 seconds
${HOME_URL}      http://${SERVER}
${LOGIN_URL}     http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${BROWSER}       chrome
${HEADLESS}      false

*** Test Cases ***
Click Login Link
    Click Link  Login
    Login Page Should Be Open

Click Register Link
    Click Link  Register new user
    Register Page Should Be Open

*** Keywords ***

Register Page Should Be Open
    Title Should Be  Register

Reset Application And Go To Starting Page
    Reset Application
    Go To  ${HOME_URL}