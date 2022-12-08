*** Settings ***
Documentation		Here we are using single template to handle testcases by importing data from excel file
...		we have to run this command to install the DataDriver
...		pip install robotframework-datadriver

Library           ./StringLibrary.py
Library		DataDriver		./excel_data.xlsx	sheet_name=Sheet1


Test Template     Count words

*** Variables ***
@{list}		0	1	2	3	4	5

*** Test Cases ***    				#Expression    Expected

counting words						${arg1}		${arg2}		${arg3}	


									
*** Keywords ***
Count words
	[Arguments]		${arg1}		${arg2}		${arg3}
	counting_words	${arg1}		${arg2}
	Result should be    ${arg3}
