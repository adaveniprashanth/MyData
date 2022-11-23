#!/bin/sh

echo "conditional statements"
#single if else logic
echo "if-else logic"
a=1
if [ $a -eq 0 ]
then
	echo "a value is 0"
else
	echo "a value is 1"
fi

#if else ladder
echo "if-else ladder"
echo "enter the a value"
read a
if [ $a -le 10 ]
then
	echo "av values is less than 10"
elif [ $a -gt 10 -a $a -le 20 ]
then
	echo "a value is between 10 and 20"
elif [ $a -gt 20 -a $a -le 30 ]
then
	echo "a value is between 20 and 30"
else
	echo "a value is greater than 30"
fi

echo "case esac statement"
#case esac  statements
echo "enter any fruit name"
echo "1.mango 2.apple 3.orange"

read fruit

case "$fruit" in
	"apple") echo "you gave apple and it is costly item."
	     ;;
	"mango")
		echo "you gave mango and it is king of fruits"
	     ;;
	"orange")
		echo "you gave orange and it can be colour and fruit name also"
	     ;;
	*)  #it will take other than -f and -d
      echo "not a valid one"
esac

#another example

option="${1}" 
case ${option} in 
   -f) FILE="${2}" 
      echo "File name is $FILE"
      ;; 
   -d) DIR="${2}" 
      echo "Dir name is $DIR"
      ;; 
   *)  #it will take other than -f and -d
      echo "`basename ${0}`:usage: [-f file] | [-d directory]" #basename will gives only filename
      exit 1 # Command to come out of the program with status 1
      ;; 
esac

echo "loops"

echo "for loop"
NUMS="0 1 2 3 4 5 6 7 8 9"
for var in $NUMS
do
	echo $var
done
for var in  0 1 2 3 4 5 6 7 8 9
do
	echo -n $var
done
echo ""

for var in {1..10}
do
	echo "$var"
done


echo "while loop"
a=0
while [ $a -lt 10 ]
do
	echo $a
	a=`expr $a + 1`
done

echo "until loop"

a=0
until [ ! $a -lt 10 ]
do
	echo $a
	a=`expr $a + 1`
done

echo "select loop"
select DRINK in tea cofee water juice appe all none
do
   case $DRINK in
      tea|cofee|water|all) 
         echo "Go to canteen"
         ;;
      juice|appe)
         echo "Available at home"
      ;;
      none) 
         break 
      ;;
      *) echo "ERROR: Invalid selection" 
      ;;
   esac
done

echo "nested loop"

echo "nested while loop"
a=0
while [ $a -lt 10 ]
do
	b=$a
	while [ $b -ge 0 ]
	do
		echo -n $b
		b=`expr $b - 1`
	done
	echo 
	a=`expr $a + 1`
done

echo "nested for loop"

for var in 0 1 2 3 4 5 6 7 8 9
do
	echo $var
	b=$var
	for var1 in 0 1 2 3 4 5 6 7 8 9
	do
		if [ ! $var1 -le $b ]
		then
			echo -n $var1
		fi

	done
	echo
done

echo "loop controls break and continue"

echo "break usage"

for var in 1 2 3 4 5 6 7 8 9
do
	if [ $var -gt 5 ]
	then
		break
	fi
	echo -n "$var "
done
echo
echo "continue usage"

for var in 1 2 3 4 5 6 7 8 9
do
	if [ $var -eq 5 ]
	then
		continue
	fi
	echo -n "$var "
done
echo

#break and continue at a time
echo "break and continue at a time"
for var in {0..20}
do
	num=$((var * var))
	#num=`expr $var * $var`
	if [ $var -gt 15 ]
	then
		break
	fi
	if [ $num -gt 100 -a $num -lt 150 ]
	then
		continue
	fi
	echo "square of $var is $num"
done

#finding the even numbers from the list of values
for var in {1..10}
do
	q=`expr $var % 2`
	if [ $q -eq 0 ]
	then
		echo "$var is even"
		continue
	fi
	echo "$var is odd number"
done
c=1
for var in ls pwd ls pwd
do
	q=`expr $c % 2`
	if [ $q -eq 0 ]
	then
		$var > abc.txt
	fi
	c=`expr $c + 1`
done
