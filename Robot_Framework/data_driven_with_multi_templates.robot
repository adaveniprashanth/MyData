*** Settings ***
Documentation		Here we are using multiple templates to handle different types of testcases
#Test Template     Reverse Operate
Library           ./StringLibrary.py


*** Variables ***
${VALUE}               0
@{LIST}				abcd	abcd	abcdabcd


*** Test Cases ***    				#Expression    Expected

reverse         [Template]   	Reverse Operate
									 abcd	 		  dcba
									 12345	    	 54321
									 qwerty			ytrewq

add words		[Template]		Adding all words
									${LIST}[0]	${LIST}[1]	${LIST}[2]
									asdf	asdf	asdfasdf

counting words	[Template]		Count words
									abcdasbcd	a	2
									abcdasbcd	b	2
									abcdasbcd	c	2
									abcdasbcd	d	2
									abcdasbcd	s	1
									abcdasbcd	t	${VALUE}


*** Keywords ***
Reverse Operate
    [Arguments]    ${expression}    ${expected}
    string reverse    ${expression}
    Result should be    ${expected}

Adding all words
	[Arguments]    ${expression1}	${expression2}    ${expected}
	adding strings	${expression1}	${expression2}
	Result should be    ${expected}

Count words
	[Arguments]		${arg1}		${arg2}		${arg3}
	counting_words	${arg1}		${arg2}
	Result should be    ${arg3}

