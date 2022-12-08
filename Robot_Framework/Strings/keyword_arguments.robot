*** Settings ***
Documentation		This file is about how to use arguments in keywords

*** Test Cases ***
Tetscase Demo
	Arguments keyword demo	first_argument	second argument


*** Keywords ***
Arguments keyword demo
	[Arguments]		${arg1}		${arg2}
	log		${arg1}
	log 	${arg2}