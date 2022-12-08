*** Settings ***
Test Template     Reverse Operate   #applies the template to all the test cases in- the test suite
Library           ./StringLibrary.py

*** Variables ***
${VALUE}               0
@{LIST}				abcd	abcd	abcdabcd


*** Test Cases ***    #Expression    Expected
reverse1              	abcd		 dcba
reverse2           		12345	     54321
reverse3        		qwerty		 ytrewq


*** Keywords ***
Reverse Operate
    [Arguments]    ${expression}    ${expected}
    string reverse    ${expression}
    Result should be    ${expected}
