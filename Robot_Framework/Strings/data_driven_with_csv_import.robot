*** Settings ***
Documentation		Here we are using single template to handle testcases by importing data from csv file
...		we have to run this command to install the DataDriver
...		pip install robotframework-datadriver


Library           ./StringLibrary.py
Library		DataDriver		./csv_data1.csv


Test Template     Reverse Operate

*** Variables ***


*** Test Cases ***    				#Expression    Expected

reverse operation				${expression}	${expected}

*** Keywords ***
Reverse Operate
    [Arguments]    ${expression}    ${expected}
    string reverse    ${expression}
    Result should be    ${expected}
