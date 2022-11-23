#!/bin/sh

echo "enter 2 numbers"
read a b

var1=`expr $a+$b`  #it will give 10+20 as output
echo "it will give $a+$b as $var1"

#one type of operation
sum=$((a+b)) #this is valid
echo "sum is $sum"

sum1=$(( $a + $b )) #this is also valid
echo "sum = $sum1"

#other type of operation
#there must be spaces before/after the operator
echo "arithmatic operators"

var=`expr $a + $b` #it will give 30 as output
echo "$a + $b = $var"

var=`expr $a - $b`
echo "$a - $b = $var"

mul=$((a*b))
echo "$a * $b = $mul"

div=`expr $a / $b`
echo "$a / $b = $div"

modulo=$((a%b))
echo "$a % $b = $modulo"

#comparing two variable values
echo "if output is 1 means the logic is correct"
compare=`expr $a == $b`
echo " result of $a == $b is $compare"
compare1=`expr $a != $b`
echo "result of $a != $b is $compare1"

echo "incrementing $a by 10"
((a+=10))
echo $a

echo "incrementing $b by 10"
b=`expr $b + 10`
echo $b
c=$a
echo "c value is $c"

echo -n "c == a is " #-n will be used to remove the end separator "\n"

[ $c == $a ] #need to give space while using [ ]
echo "$?"

echo "a!=c"
[ $c != $a ]
echo "$?" #to check the return status of previous command

echo "relational operators" #these will work only on numaric not on strings

#read a b
echo "a is $a and b is $b"
echo "a equals(-eq) b"
[ $a -eq $b ]
echo "$?"
echo "a not equals(-ne) b"
[ $a -ne $b ]
echo "$?"

echo "a greater than(-gt) b"
[ $a -gt $b ]
echo "$?"

echo "a less than(-lt) b"
[ $a -lt $b ]
echo "$?"

echo "a greater than or equal(-ge) b"
[ $a -ge $b ]
echo "$?"

echo "a lesser than or equal(-le) b"
[ $a -le $b ]
echo "$?"

echo "boolean operators"

echo "a is $a and b is $b"
#not operator
res=`expr  $a != $b`
echo "result of ![a ==b ] is $res"
res=$((!false))
echo "result of !false is $res"
#echo "$?"

echo "a or b"
[ $a -le 20 -o $b -lt 20 ]
echo "$?"

echo "a is $a and b is $b"

#not working below line
#res=`expr [ $a -eq 10 ] -o [ $b -le 20 ]`
#echo "the result of a== 10 or b <= 20 is $res"

[ $a -eq 10 -a $b -le 20 ]
echo "$?"
#need to learn this also
echo "checking"
#res=[ $a -eq 10 -o $b -eq 20 ]
#echo "$res"

str1="abcdef"
str2="abcdef"
str3="ghijkl"
str4=""
echo "string1 is $str1"
echo "string2 is $str2"
echo "string3 is $str3"

echo "string operators"

echo "equality of strings"
result=`expr $str1 = $str2`
echo "result of string1 = string2 is $result"

echo "not equality of strings"
#res=`expr [ $str1 != $str3 ]`#it will not work
result=`expr $str1 != $str3`
echo "result of $str1 != $str3 is $result"

#echo "checking for empty string i.e length is zero"
#need to learn this one
#result=`expr -z $str1`
#result=`expr -n $str1`

echo "file test operators"
#we have to use if else logic to check file operators
echo "absolute path for a file"
path=$(realpath shell_operations.sh)
echo 'absolute path is ' $path

echo "directory path of a file"
dir_path=$(dirname $path)
echo "directory of a file is\n $dir_path"
filename="shelloperations.sh"
echo "printing the result"

if [ -b $path ]
then
	echo "file is block file"
else
	echo "file is not block file"
fi

if [ -c $path ]
then
	echo "file is character file"
else
	echo "file is not character file"
fi

if [ -d $path ]
then
	echo "file is directory"
else
	echo "file is not directory"
fi

if [ -f $path ]
then
	echo "file is normal file"
else
	echo "file is not normal file"
fi

#[ -g $path] to check whether file group user id bit set or not. if set result is true.
#[ -k $path ] to check file sticky bit is set or not.
#[ -p $path ] toch eck whether is it  named pipe or not.
#[ -t $path ] to check whether the given file is file descriptor and it is open or not.
#[ -u $path ] to check whether file user group bit is set or not.
#[ -r $path ] to check whether file is readble or not.
#[ -w $path ] to check whether file is writable or not.
#[ -x $path ] to check whether file is executable or not.
#[ -s $path ] to check whether file size is > 0 or not.
#[ -e $path ] to check whether file/directory is exist or not.

