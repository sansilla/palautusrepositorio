*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kissa
    Set Password  kissa123
    Set Password Confirmation  kissa123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ki
    Set Password  kissa123
    Set Password Confirmation  kissa123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kissa
    Set Password  kissa1
    Set Password Confirmation  kissa1
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  kissa
    Set Password  kisssssa
    Set Password Confirmation  kisssssa
    Submit Credentials
    Register Should Fail With Message  Password must contain letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  kissa
    Set Password  kissa123
    Set Password Confirmation  kissa1234
    Submit Credentials
    Register Should Fail With Message  Password and confirmation must match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Fail With Message  Username already in use

Login After Successful Registration
    Set Username  kissa
    Set Password  kissa123
    Set Password Confirmation  kissa123
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  kissa
    Set Password  kissa123
    Click Button  Login
    Login Should Succeed


Login After Failed Registration
    Set Username  kissa
    Set Password  kissakissa
    Set Password Confirmation  kissakissa
    Submit Credentials
    Register Should Fail With Message  Password must contain letters and numbers
    Click Link  Login
    Set Username  kissa
    Set Password  kissakissa
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}