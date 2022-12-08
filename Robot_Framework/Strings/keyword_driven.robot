*** Settings ***
Library           StringLibrary.py

Documentation		there are some sample commands to run the test case
...					ther are --> robot -d <folder to store results> <robot file name>
...					other one is --> robot -d <folder to store results> -v <scalar_variable_name>:<value to assign to it> <robot file name>
...					another one is --> robot -d <folder to store results> -v <scalar_variable_name1>:<value to assign to it> -v <scalar_variable_name1>:<value to assign to it> <robot file name>

*** Variables ***
${VALUE}               0	#defining the global variable BIG letters
${result}		result		#defining the local variable  small letters
@{list}		abcd	abcd	abcd	defg	abcdabcdabcddefg	#defining the list
@{list1}	a	b	c	d
&{dict}		string=abcd		result=dcba	#defining the dictionary
${operation}	1
@{original_list}	abcd	efgh	ijkl	mnop
@{reversed_list}	dcba	hgfe	lkji	ponm
@{numbers_list}		0	1	2	3

*** Test Cases ***
String addition1
    adding strings    abcd	abcd	abcd	defg
    Result should be    abcdabcdabcddefg

String addition2
    adding strings    @{list}[0:4]	#accessing the list items. more than one item
    Result should be    ${list}[4]	#accessing the single item from the list so we used $

Count words
	counting_words	abcdasbcd	a
	Result should be    2

Replace string
		String has to be replaced	#connecting to the keyword

String Reverse
    string reverse    ${dict.string}	#accessing the dictionary value
    Result should be    ${dict.${result}}

Index find
	index_find	abcd	a
	Result should be	${VALUE}

List conversion
	convert string to list

#using IF ELSE logic it is not working for comparing the strings but working for comparing the characters
If else demo for replace and reverse operation
	Run Keyword If	${operation} == 1		String has to be replaced	
	...		ELSE IF	 ${operation} == 2	Reversing the string
	...		ELSE	Log the details


#using the for loop logic
For loop demo using reverse logic
	FOR	 ${element}	 IN  @{numbers_list}
		string reverse	${original_list}[${element}]
		Result should be	${reversed_list}[${element}]
	END
checking the get count 
	${scalar}=	Set Variable	abcdcdcf
	${count}=	Get Count	${scalar}	a
	${count1}=	Get Count	${scalar}	d
	Should Be True		${count} == 1
	Should Be True		1<${count1}<5

*** Keywords ***
String has to be replaced
	replacing strings	abcdabcdef	ab	st
	Result should be    stcdstcdef

convert string to list
	convert to list		abcd
	List Result should be	@{list1}

Reversing the string
	string reverse    ${dict.string}	#accessing the dictionary value
    Result should be    ${dict.${result}}

Log the details
	Log		no operation performed