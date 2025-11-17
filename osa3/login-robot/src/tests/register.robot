*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  kissa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ki  kissa123
    Output Should Contain  Username is fewer than 3 letters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ki55a  kissa123
    Output Should Contain  Username is allowed to contain lowercase letters only

Register With Valid Username And Too Short Password
    Input Credentials  kissa  kissa12
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kissa  kissapissa
    Output Should Contain  Password should include numbers

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input  kalle
    Input  kalle123
    Input New Command