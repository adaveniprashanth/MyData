#!/bin/sh

#defing the function

Hello() {
	echo "hello learner"
}

#calling the function

Hello

#***************
#passing the parameters to the function

hello() {

	echo "hello $1 $2"
}

#calling the function by passing parameters

hello dear learner

#*************

#capturing the return value from function


func() {
	echo "passed values are $1 $2"
	echo -n "sum of $1 and $2 is "
	echo `expr $1 + $2`
	return $(($1 + $2)) # return $1 + $2 will not work
}

func 10 20

#capturing the return value
ret="$?"
echo "returned value from function is $ret"

#nested functions

function_one() {
	echo "this is the first function"
	function_two
}

function_two() {
	echo "this is the second function"
}

#calling the function
function_one
