#!/bin/sh

#escape sequences substitutions

#here \n is not replaced with its value
echo "hello world\n"

echo -e "hello world\n"

# -e enables the escape sequences
# -E disables the escape sequences (deafult is -E)

#command substitution --> by which the shell performs the operations and replaces their output in place of commands
#`command`

Date=`date`
echo "$Date"

UP=`date ; ls`
echo "uptime is $UP"

#variable substitution

echo "----variable substitution---"

var=10

echo $var #substitues the value of var

unset var #deleting the value of var

echo ${var:-"word"} #if var is null or unset, the word will be replaced but value of var will not change

echo $var

echo ${var:="words"} #if var is null or unset, it will assign the words to var

echo $var

unset var
echo ${var:?"message"} #if the value is null or unset, message will be printed 
echo $var
