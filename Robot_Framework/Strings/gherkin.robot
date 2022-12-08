*** Settings ***
Library           StringLibrary.py

*** Test Cases ***
Reverse1
    Given user given value
    Then result is "dcba"


Reverse2
	When user types "qwerty"
	Then result is "ytrewq"
	
*** Keywords ***
user given value
    String reverse    abcd

User types "${expression}"
    string reverse    ${expression}


Result is "${result}"
    Result should be    ${result}
