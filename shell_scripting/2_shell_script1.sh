#!/bin/sh
#the above line is called shebang because of we are having hash(#) and bang(!)
#python analogy

echo "hello what is your name?"  #it will be like print() method in pyton

#read PERSON #it will be like input in python

#echo "hi $PERSON"

# we have 3 types of variables:
#1. local variables 2.Environmental variables 3.shell variables

#defining the variables

NAME="Raju" #we can treat it like normal string assignment i.e  a = 'abc' it is called scalar variable because it is holding one value at a time.
echo $NAME

#readonly NAME  #converting the variable to immutable i.e fixed value so we cannot update this variable value
#NAME='Ramesh'  #it will throw error because it is readonly we can't edit

PERSON='raju'
echo  $PERSON
unset PERSON  #deleting the variable
echo $PERSON #iyt will throw error because we deleted the variable
echo "hello what is your name?"  #it will be like print() method in pyton
#echo "hi $PERSON"
echo $NAME
echo  $PERSON
echo $PERSON #it will throw error because we deleted the variable
echo "file name: $0"
echo "first parameter: $1"
echo "second parameter: $2"
echo "quoted values: $@"
echo "quoted values: $*"  #this will gives strings separeated by space( )
echo "no.of parameters: $#"
echo "exit status: $?"
echo "to print the current process number $$"
echo "$! will print the process number of last background command"

#python analogy

echo "hello what is your name?"  #it will be like print() method in pyton

#read PERSON #it will be like input in python

#echo "hi $PERSON"

# we have 3 types of variables:
#1. local variables 2.Environmental variables 3.shell variables

#defining the variables

NAME="Raju" #we can treat it like normal string assignment i.e  a = 'abc'
echo $NAME

#readonly NAME  #converting the variable to mutable i.e fixed value
#NAME='Ramesh'  #it will throw error because it is readonly we can't edit

PERSON='raju'
echo  $PERSON
unset PERSON  #deleting the variable
echo $PERSON #iyt will throw error because we deleted the variable
#!/bin/sh

#special variables
# $0 captures the file name while running the file
# $1...9 captures the command line arguments
# $@  captures the quoted values
# $*  captures the quoted values
# $# returnes the no.of parameters
# $?  returnes the exit status of last used command i.e fail/pass

echo "file name: $0"
echo "first parameter: $1"
echo "second parameter: $2"
echo "quoted values: $@"
echo "quoted values: $*"  #this will gives strings separeated by space( )
echo "no.of parameters: $#"
echo "exit status: $?"

#run this file  like this ./<file_name>  'abc' def


# $0 captures the file name while running the file
#run this file  like this ./<file_name>  'abc' def

#using arrays in shell

my_name=('first' 'second' 'third')
NAME[0]='one'
NAME[1]='two'
NAME[2]='three'
NAME[3]='four'
NAME[4]='five'

#printing one item from array
echo "printing array values"
echo "first item in my_name array ${my_name[0]}"
echo "first item in NAME array ${NAME[0]}"
my_array=(1 2 3)
echo "first item is ${my_array[0]}"

echo "prnting all values from NAME array is ${NAME[*]}"
echo "prnting all values from my_name array is ${my_name[@]}"
