#variables scope

#global scope
#global variables can be available anywehere in the test data

#test suite scope
#variables with test suite scope are available anywehere in the test suite where they are defined or imported

#test case scope
#variables with the test case scope are visible in a test case and in all user keywords in test uses

#local scope
#tes cases and user keywords have a local variable scope that is not seen by other tests and keywords


*** Settings ***


*** Variables ***
${GLOBAL}	this is a GLOBAL variable	#it can be access anywhere
${local_variable}	this is a local variable	#it can be access in this file only

*** Test Cases ***
Testcase demo1
	LOG		${GLOBAL}

Testcase demo2
	LOG		${GLOBAL}

Testcase demo3
	${local_variable1}=	Set Variable	this is local variable	#we are assigning the value to the local variable of test case
	LOG		${local_variable}
	LOG		${local_variable1}
	Log		${GLOBAL}

Testcase demo4
	LOG		${local_variable}
	log		${local_variable1}	#it will fail because the variable defined in only testcase scope 

Testcase demo5
	This is demo keyword1

Testcase demo6
	log		This is demo keyword2

*** Keywords ***
This is demo keyword1
	[Arguments]		${keyword_variable}=This is keyword variable
	log		${keyword_variable}

This is demo keyword2
	[Arguments]		${keyword_variable1}=This is keyword variable	#if both global and keyword variables have same name keyword_variable will have higher priority while accessing the keyword
	${keyword_variable1}
