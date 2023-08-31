
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    import sys,os
    import numpy as np
    import array as arr
    import string
    import random,re
    import shutil
    from datetime import date
    from shutil import copyfile
    import zipfile
    import pandas as pd
    import logging
    import pyinputplus as pypi
    import random as rd
    import send2trash
    import PyPDF2
    from PyPDF2 import PdfFileReader,PdfFileWriter
    # import docx #not able to install
    # import csv
    import json,pickle
    import heapq #for finding the nth largest number in list
    # import readDocx #not able to install

except ModuleNotFoundError:
    print("you have to install the below packages to run")
    sys.exit("install all modules")

'''
https://silentinstallhq.com/python-3-9-silent-install-how-to-guide/
https://www.python.org/ftp/python/3.9.3/python-3.9.3-amd64.exe
python-3.9.3-amd64.exe /passive InstallAllUsers=1 PrependPath=1 TargetDir="C:\Python39"
'''


if 0:#pyinputplus usage similar to input with additional features
    if 0:#string input
        if 0:
            string = pypi.inputStr(prompt='enter the string',blank=True,blockRegexes='abcde')#blank=True allows the string
            print(string)
        if 0:
            string = pypi.inputStr(prompt='enter the string',blank=False,blockRegexes='abcde',allowRegexes="hjkl")#does not regexes of abcde
            print(string)
    if 0:#integer input
        if 0:
            num = pypi.inputInt(prompt='enter the number',default=10,limit=4)
            print(num)
        if 0:
            num = pypi.inputInt(prompt='enter the number',limit=4)#after 3 times if we provide wrong data,raises retrylimit error (limit=4)
            print(num)
        if 0:
            num = pypi.inputInt(prompt='enter the number',default=1,max=30,min=6,limit=4)#default will override min value condition, once limit is over
            print(num)
        if 0:
            num = pypi.inputInt(prompt='enter the number',default=10,timeout=6)#value has to give within 6 secondds,otherwise default will be taken
            print(num)
        if 0:
            num = pypi.inputInt(prompt='enter the number',default=10,limit=4,blockRegexes=[r'[13579]$'])#allows the integer not ends with 1,3,5,7,9
            print(num)
    if 0:#menu input
        if 0:
            value = pypi.inputMenu([1,2,3,4,5,6])#we cannot give numeric vlaues in the menu
            print(value)
        if 0:
            value = pypi.inputMenu(["1","2","3","4","5","6"])
            print(value)
        if 0:
            value = pypi.inputMenu(["abc","def","ghi","jkl","mno","pqr","stu","vwx","yz"])
            print(value)
        if 0:
            value = pypi.inputMenu(["abc","def","ghi","jkl","mno","pqr","stu","vwx","yz"],numbered=True)#we can give numbers instead of values
            print(value)
        if 0:
            value = pypi.inputMenu(["abc","def","ghi","jkl","mno","pqr","stu","vwx","yz"],numbered=True)
            print(value)
        if 0:
            value = pypi.inputMenu(["abc","def","ghi","jkl","mno","pqr","stu","vwx","yz"],lettered=True)
            print(value)
    if 0:#datetimeinput
        if 0:#%y year value has to be given in 2 digits. and  %y will take year value in 4 digits
            date = pypi.inputDatetime(prompt='enter the date and time',formats=('%m/%d/%y %H:%M:%S','%m.%d.%Y %H:%M:%S'))#we have to provide strftime formats only
            print(date)

if 0:
    a = arr.array('i',[1,2,3,4,5])
    # print(len(a))
    #adding elemenbts to array
    a.append(4)
    a.extend([5,6])
    a.insert(3, 10)
    # removing elements from array
    # print(a)
    a.pop()  #<--removes last element
    a.pop(5) #removes element from position
    a.remove(4)#removes the value from array
    # print(a)

    #concatination
    # print(a)
    b = arr.array('i',[7,4,7,4,5,7,6,54,4])
    c = arr.array('i')
    c = a+b
    # print(c)
    # slicing
    # print(a)
    # print(a[0:3])
    # print(a[0:-2:-1])
    # Looping through array
    # print(a)
    '''for i in a:
        print(i)

    for i in a[0:-2]:
        print(i)'''

    '''temp = 0
    while temp <a[4]:
        print(a[temp])
        temp+=1'''
# Hash tables and Hash maps
#nested dictionary
if 0:
    my_dict = {'emp_details':{'Dev':{'ID':'001','salary':'2000','post':'Lead'},
                              'ava':{'ID':'002','salary':'1000','post':'HR'}}}
    # print(my_dict)
    # print(my_dict.keys())
    # print(my_dict.values())
    # print(my_dict.items())
    my_dict1 = {'Dev':'001','chris':'002','joe':'003'}
    my_dict1.pop('Dev')
    # print(my_dict1)
    my_dict1.popitem()
    # print(my_dict1)
    del my_dict1['chris']
    # print(my_dict1)
    # converting dictionary to dataframe
    # import pandas as pd
    # df = pd.DataFrame(my_dict['emp_details'])
    # print(df)
if 0:
    #iterating over nested dictionary
    d = {'a':{'b':{'c':100}},'d':{'e':10}}

    def myprint(d):
        for k, v in d.items():
            if isinstance(v, dict):
                myprint(v)
            else:
                print("{0} : {1}".format(k, v))
    myprint(d)

# The simplest way to concatenate two dictionaries in python is by using the unpacking operator(**)
if 0:
    dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
    print(dict(**dict_1))

if 0:#merging 2 dictionaries with overriding of common key's value
    dict_1 = {'John': 15, 'Rick': 10, 'Misa' : 12 }
    dict_2 = {'Bonnie': 18,'Rick': 20,'Matt' : 16 }
    dict_3 = {'Stefan': 19, 'Riya': 14, 'Lora': 17}
    dict_4 = {**dict_1,**dict_2, **dict_3}
    print (dict_4)


if 0:#merging 2 dictionaries by Adding values of common keys
    dict_1 = {'Media/SFC': [495, 0, 0, 0, 0, 495], 'Media/VE': [274, 50, 0, 0, 0, 224]}
    dict_2 = {'Media/SFC': [495, 0, 0, 0, 0, 495], 'Media/VE': [274, 73, 0, 0, 0, 201]}

    def mergeDictionary(dict_1, dict_2):
       dict_3 = {**dict_1, **dict_2}
       print("dict_3",dict_3)
       for key, value in dict_3.items():
           if key in dict_1 and key in dict_2:
                   dict_3[key] =  dict_1[key]+value #here value will be dict2[key] because of override
       return dict_3

    dict_3 = mergeDictionary(dict_1, dict_2)
    print(dict_3)


# print(int(20*rd.random()))
# print(rd.random()+1)

# while else condition

random_value = int(20 *rd.random())
# print(rd.random())
# print(random_value)
user_selected = 0
# print(++user_selected) #it will work
# print(user_selected++)
'''
while random_value != user_selected:
    user_selected = int(input("enter the number"))
    if user_selected > 0:
        if random_value > user_selected:
            print(("number is large"))
        elif random_value < user_selected:
            print(("number is small"))
    else:
         print("Giving up")
         break
else:
    print("you guessed correct")'''
'''
fruits = ['mango','apple','grape']
for fruit in fruits:
    print("fruit name is",fruit)
else:
    print("printed all fruits")'''
# find fa'ctorial
'''num = int(input("enter the number"))
factorial = 1
if num <0:
    print("number should be positive")
elif num == 0:
    print("factrail = ",factorial)
else :
    for i in range(1,num+1):
        factorial = factorial *i
    print("factorial is ",factorial)'''


# Nested loops
'''balance = 67
chances = 3

print("welcome")
restart = 'Y'
while chances > 0:
    pin = int(input("enter the pin"))
    if pin == 1234:
        while restart not in ('n','N','no','NO'):
            print("check balance enter 1")
            print("withdraw 2")
            print("add amount 3")
            print("remove card 4")
            option = int(input("enter the option value"))
            if option == 1:
                print("your balance is ",balance)
                restart = input("would you like to continue?")
                if restart in ('n','N','no','NO'):
                    print("thank you")

            if option == 2:
                withdraw_amount = int(input("enter the amount in 100, 500 only"))
                if balance > withdraw_amount:
                    balance =- withdraw_amount
                    print("collect the cash")
                else:
                    print("balance is low")
            if option == 3:
                add_amount = int(input("enter the amount to add"))
                balnce=+add_amount
            if option == 4:
                print("thank you")
    elif pin != 1234:
        chances-=1
        print("wrong pin retry")
    if chances == 0:
        print("failed 3 times")
        break
'''
# finding pytharogous numbers: c2 = a2 + b2
'''from math import sqrt
n = int(input("enter the number"))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if (c**2 - c_square) == 0:
            print(a,b,c)'''
# Bulk people reservation
'''travel = input("yes or no")
while travel == 'yes':
    n = int(input("how many passangers"))
    for i in range(1,n+1):
        name = input("name")
        age = int(input("age"))
        gender = input("male or female")
        print(name,"\n",age,"\n",gender)
    travel = input("forgot any one")'''

if 0:
    i = 999999979758
    a = 0
    while True:
        for j in range(0,len(str(i))):
            a+=i%10
            i = i//10
        print(a)
        if a < 10:
            break
        else:
            i = a
            a = 0
    print(a)

if 0:
    # count the duplicated values in list
    l = [1,2,3,1,3,4,2,4,2,4,2,3,5,4,3,6,5,4,7,3,4,3,2,6]
    d = {}
    for i in l:
        d[i]=d.get(i,0)+1
    print(d)

if 0:
    #appending the values to list in dictionary
    Details = {"Destination": "China",
            "Nstionality": "Italian", "Age": [1]}
    Details["Age"] += [20, "Twenty"]
    print(Details)

    
# Pattern programs
# pyramid pattern
def pyramid(n):
    k = n
    for i in range(0,n):
        for j in range(0,k):
            print(" ",end="")
        k-= 1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
# pyramid(5)

def pyramid1(n):
    for i in range(0,n):
        print((n-i)*" ",(i+1)*"* ",end="\n")

# pyramid1(5)

# inverted pyramid:
def inverted_pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(" ",end="")
        for j in range(0,n-i):
            print("* ",end="")
        print("\r")

# inverted_pyramid(5)
def inverted_pyramid1(n):
    k = 2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(" ",end="")
        k+=1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
# inverted_pyramid1(5)

def inverted_pyramid2(n):
    for i in range(0,n):
        print(i*" ",(n-i)*"* ",end="\n")

# inverted_pyramid2(5)

# right start pattern
def right_start_pattern(n):
    for i in range(0,n+1):
        print("* "*i,end="")
        print("\r")

    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

# right_start_pattern(5)
def left_start_pattern(n):
    k = 2*n
    for i in range(0,n):
        for j in range(0,k-i-2):
            print(" ",end="")
        k-=1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    k+=1
    for i in range(n-1,-1,-1):
        for j in range(0,k-i):
            print(" ",end="")
        k+=1
        for j in range(0,i):
            print("* ",end="")
        print("\r")

# left_start_pattern(7)

# hour glass pattern
def hour_glass_pattern(n):
    for i in range(0,n):
        print(i*" ",(n-i)*"* ")
    for i in range(1,n+1):
        print((n-i)*" ",i*"* ")

# hour_glass_pattern(9)

# half pyramid pattern

def half_pyramid_pattern(n):
    for i in range(0,n):
        print(i*"* ")

# half_pyramid_pattern(6)

def half_pyramid_pattern1(n):
    for i in range(n,0,-1):
        print((i*2)*" ",(n-i)*" *")

# half_pyramid_pattern1(6)

def half_pyramid_pattern2(n):
    for i in range(0,n):
        print((i*2)*" ",(n-i)*"* ")

# half_pyramid_pattern2(6)

def half_pyramid_pattern3(n):
    for i in range(n,0,-1):
        print(i*"* ")

# half_pyramid_pattern3(6)

def half_pyramid_pattern4(n):
    x = 0
    for i in range(n,0,-1):
        x+=1
        print(i*str(x))

# half_pyramid_pattern4(6)

def half_pyramid_pattern5(n):
    for i in range(n,0,-1):
        for j in range(1,i):
            print(j,end=" ")
        print()

# half_pyramid_pattern5(6)

def half_pyramid_pattern6(n):
    x = 64
    for i in range(n,0,-1):
        x+=1
        print(i*chr(x))

# half_pyramid_pattern6(6)

def half_pyramid_pattern7(n):
    for i in range(n,0,-1):
        for j in range(1,i):
            print(chr(j+64),end=" ")
        print()

# half_pyramid_pattern7(6)

def diamond_pattern(n):
    for i in range(1,n+1):
        print((n-i)*" ",i*"* ")
    for i in range(1,n):
        print(i*" ",(n-i)*"* ")

# diamond_pattern(7)

# diamond star pattern
def diamond_start_pattern():
    for i in range(5):
        for j in range(5):
            if i+j == 2 or i-j == 2 or i+j == 6 or j -i == 2:
                print("*",end="")
            else:
                print(" ",end="")
        print()

# diamond_start_pattern()

def diamond_star_pattern1(n):
    for i in range(1,n+1):
        print((n-i)*" ","*",((i-2)*2)*" ",end="")
        if i!= 1:
            print("*",end="")
        print()
    for i in range(1,n):
        print(i*" ","*",(((n-i)-2)*2)*" ",end="")
        if (n-i)!= 1:
            print("*",end="")
        print()
# diamond_star_pattern1(5)


def diamond_star_pattern2(n):
    for i in range(1,n+1):
        print((n-i)*" ","*",((i-2)*2)*" ",end="")
        if i!= 1:
            print("*",end="")
        print()
    for i in range(1,n):
        print(i*" ","*",(((n-i)-2)*2)*" ",end="")
        if (n-i)!= 1:
            print("* ",end="")
        print()

# diamond_star_pattern2(5)

# character pyramid
def character_pyramid(n):
    for i in range(0,n):
        print((n-i)*" ",i*(" "+chr(64+i)))
# character_pyramid(5)

def character_pyramid1(n):
    k = n
    c = 0
    for i in range(0,n):
        for j in range(0,k):
            print(" ",end="")
        k-= 1
        for j in range(0,i+1):
            c+=1
            print(chr(64+c)+" ",end="")
        print("\r")

# character_pyramid1(7)

def k_shaped_pattern(n):
    for i in range(0,n-1):
        print("*",(((n-i)-2)*2)*" ",end="")
        if (n-i)!= 1:
            print("* ",end="")
        print()

    for i in range(1,n+1):
        print("*",((i-2)*2)*" ",end="")
        if i!= 1:
            print("*",end="")
        print()

# k_shaped_pattern(7)

def character_diamond_star_pattern1(n):
    for i in range(1,n+1):
        print((n-i)*" ",chr(65),((i-2)*2)*" ",end="")
        if i!= 1:
            print(chr(65),end="")
        print()
    for i in range(1,n):
        print(i*" ",chr(65),(((n-i)-2)*2)*" ",end="")
        if (n-i)!= 1:
            print(chr(65),end="")
        print()
# character_diamond_star_pattern1(7)

def character_diamond_pattern(n):
    c = 0
    for i in range(1,n+1):
        print((n-i)*" ",i*(chr(65+c)+" "))
        c+=1
    c-=1
    for i in range(1,n):
        c-=1
        print(i*" ",(n-i)*(chr(65+c)+" "))

# character_diamond_pattern(7)

def character_diamond_pattern1(n):
    c = 0
    for i in range(1,n+1):
        print((n-i)*" ",end="")
        for j in range(0,i):
            print((chr(65+c)+" "),end="")
            c+=1
        print()

    for i in range(n,0,-1):
        print((n-i)*" ",end="")
        for j in range(0,i):
            c -= 1
            print(chr(65+c)+" ",end="")
        print()

# character_diamond_pattern1(7)
# import numpy as np
# a = np.arange(1,8,1)
# np.reshape(a,(7,1))
# b = np.arange(1,8,1)
# np.reshape(b,(7,1))
# print((a*b))
# print(np.shape(a*b))

# file = open('/home/pj/Desktop/python_files/helloworld3.py','r')
# print(file.read())# read whole file
# file.close()

# file = open('/home/pj/Desktop/python_files/helloworld3.py','r')
# print(file.read(3)) #reads 3 characters
# file.close()

# file = open('/home/pj/Desktop/python_files/helloworld3.py','r')
# print(file.readline())# read first line only
# print(file.readline(3)) #same as read(3)
# print(file.readlines(3)) #
# print(file.readlines()) #
# print(len(file.readlines())) #
# file.close()

# count the lines in file
# def file_count(fname):
#     with open(fname) as f:
#         for i, c in enumerate(f):
#             pass
#     return i+1
# print('Total number of lines in the text file: ', file_count('/home/pj/Desktop/python_files/helloworld3.py'))

# file = open('F:/python_files/demofile.txt','r')
# print(file.readlines()) #read lines separately
# file.close()

# file = open('F:/python_files/demofile.txt','r')
# for line in file: #line variable collects 1st line and moves pointer to 2nd line
#     # print(line)
#     print(file.readline())
# file.close()

# file = open('F:/python_files/demofile.txt','r')
# for i in file.readlines():
#     print(i)
# file.close()

# import os
# if os.path.exists("demofile1.txt"):
#     print("file already exist")
# else:
#     file = open('F:/python_files/demofile1.txt','x')#creates file if not exist
#     file.close()
# file = open('F:/python_files/demofile1.txt','w') # 'w' over writes content
# file.write("hello\n")
# file.close()

# file = open('F:/python_files/demofile1.txt','a') # 'a' appends at end
# file.write("world")
# file.close()

# Functions concepts
if 0:
    def func1(name):
        return f"hello {name}"
    def func2(name):
        return f"{name}, how are you ?"
    def func3(func4):
        return func4('Dear learner')
    
    print(func3(func1))#func1 passing as argument and assigning 'dear learer' 
    # to name in func1
    
    print(func3(func2))

# it is like below
# name='dear learner'
# print(f"hello{name}")

# Inner functions
if 0:
    def func():
        print("main function")
        def func1():
            print("first chils function")
        def func2():
            print("second child function")
        func1()
        func2()
    
    a = func #a assigned with address of object
    a()
if 0:
    def func(n):
        def func1():
            return "hello"
        def func2():
            return "world"
        if n == 1:
            return func1
        else:
            return func2
    
    a = func(1)
    b = func(2)
    print(a())
    print(b())
    
    c = func
    print(c(1)())


# Decorators way 1
if 0:
    def function1(function):
        def wrapper():
            print("hello")
            function()
            print("what are you doing?")
        print("wrapper",wrapper)
        return wrapper
    
    def function2():
        print("Learner")
    
    # print("function2",function2)
    # print("function1",function1)
    
    function2 = function1(function2) #wrapper statement
    
    print("function2",function2)
    function2()

if 0:
    # Decorators way 2 --> syntactic sugar
    def function1(function):
        def wrapper():
            print("hello")
            function()
            print("what are you doing?")
        return wrapper
    
    @function1
    def function2():
        print("Learner")
    
    function2()

'''
# ######
# The above is equivalent to the following code
def function2():
    print("Learner")
function2 = function1(function2)
############'''

'''
def fun1(name):
    print(f"{name}")
    return f"{name}"
a = fun1('hello')
print(a)'''
if 0:
    # Decorator with arguments
    def function1(function):
        def wrapper(*args,**kwargs):
            print("hello")
            function(*args,**kwargs)
            print("what are you doin?")
        return wrapper
    
    @function1
    def function2(name):
        print(f"{name}")
    
    function2("learner")


'''
# class without decorators
class Square:
    def __init__(self,val):
        self.set_side(val)

    def area(self):
        return self.get_side()**2
    def get_side(self):
        return self._side

    def set_side(self,value):
        print("setting the value")
        if value <= 0:
            print("error")
        else:
            self._side = value

s = Square(5)
print(s.get_side())
print(s.area())
'''
'''
# class with property
class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.get_side()**2
    def get_side(self):
        print("getting the value")
        return self._side

    def set_side(self,value):
        print("setting the value")
        if value <= 0:
            print("error")
        else:
            self._side = value
    side = property(get_side,set_side)

s = Square(5) #automatically calls set method
print(s.side)
# print(s.area())
'''

'''
# class with decorators

class Square:
    def __init__(self,side):
        self._side = side

    @property
    def side(self):
        print("getting value of side")
        return self._side
    @side.setter
    def side(self,value):
        print("setting value of side")
        self._side = value

    @property
    def area(self):
        print("getting value of area")
        return self._side**2

    @classmethod
    def unit_square(cls):
        return cls(1)

s = Square(5)
print(s.side)
print(s.area)
'''

# NEED TO KNOW ABOUT CLASSMETHOD and FUNCTOOLS library

# Lambda fuunctons/Anonymous functions



"""
Created on Sat Feb 13 10:45:40 2021

@author: pj
"""

# print("Learn python in 12 hours edureka")
'''
# Lambda functions
a = lambda x:x**2
# print(a(8))
'''
if 0:
    # Lambda within user-defined functions
    def new(x):
        return lambda y:x*y
    
    a = new(5) #a contains the address of lambda function
    print(a(8)) #passing the value to the lambda function

if 0:
    # lambda function within filter,map,reduce functions
    my_list = [1,2,3,4,5,6]
    
    # filter syntax filter(function,iterables)
    new_list = list(filter(lambda a:a%2 == 0,my_list))
    print(new_list) #contains only values satisfies the function
    
    # map syntax map(function,iterables)
    new_list1 = list(map(lambda a:a%2 == 0,my_list))
    print(new_list1)# return the list after satisfies condition
    
    my_list1 = [2,3,4,5,6]
    new_list1 = list(map(lambda a,b:a*b,my_list,my_list1))
    print(new_list1)
    
    # reduce syntax reduce(function,iterables,initial)
    # the function in reduce needs 2 parameters
    from functools import reduce
    my_data = range(1,7)
    summarized_value = reduce(lambda a,b :a*b,my_data)
    # print(summarized_value)


'''
# lamba for algebra 
s = lambda a,b:a**b
# print(s(2,3))

s= lambda a,b:(a+b)**2
print(s(2,3))'''

'''
# map,fileter and reduce within themselves
my_list = [1,2,3,7,75,3,8,3,5,43,5346,643,75,47,7]
map_in_filter = filter(lambda x: x*2>=100,map(lambda x:x+x,my_list))
print(list(map_in_filter))
l = map(lambda x:x+x,my_list)
map_in_filter1 = filter(lambda x: x*2>=100,l)
print(list(map_in_filter1))
filter_in_map = map(lambda x:x*2,filter(lambda x:x*3<100,my_list))
# print(list(filter_in_map))

from functools import reduce
filter_map_in_reduce = reduce(lambda x,y:x+y,map(lambda x:x*2,filter(lambda x: x*3 >=100,my_list)))
# print(filter_map_in_reduce)
'''

# Generators in python
# use of generator is one item can produce only when required
'''
def new(a):
    for x in a:
        yield x
l = [1,2,3,4,5]
b = new(l)
print(b) #returns address
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
# print(next(b))#returns error bcaz of end of list
'''

'''
def new1(a):
    while a <=3:
        yield a
        a+=1
c = new1(2)
print(next(c))
print(next(c))
# print(next(c))#produces stopiteration error
'''
if 0:
    def new2():
        n = 5
        yield n
        b = n*n
        yield b
    
    # v = new2()
    # print(next(v)) #returns n
    # print(next(v)) #returns b
    # print(next(v)) #returns stop iteration error
    
    li = [1,2,3,4,5]
    def new(l):
        for i in l:
            yield i
    v = new(li)
    for x in v:
        print(x)
    
    # if we use generator with loops we can avoid stopiteration error
    for x in v:
        print(x)

# s= 'asd'
# print("".join(reversed(s)))
# print(dir(s))

# print(list(reversed(s)))
if 0: #reverse the words in a string
    s = "fgh fhg fhjf hjg hk hk ljlk jlkjljkljk jk"
    l = s.split()
    print(s)
    d = " ".join(["".join(reversed(i)) for i in s.split()])
    # d = " ".join(["".join(list(reversed(i))) for i in s.split()])
    print(d)
    
# try/except/else/finally
if 0:
    b=4
    c=2
    try:
        a = b/c
    except ZeroDivisionError:
        print("number cannot divide with zero")
    except:
        print("error is there")
    else:
        print("code executed with out any errors")
    finally:
        print("The execution code has completed")

# default exception
if 0:
    try:
        f = open('adsasfd.txt')
    except ValueError:
        print("value error tried")
    except:#it has to be placed at last except
        print("default except block")


#Multiple ways of try/except logics
if 1:
    try:
        a = int(input("enter the number"))
        b = 9/a
        print("completed execution")
    except FileExistsError:
        print("error with FileExistsError")
    except ValueError:
        print("the value is not correct")
    except Exception as e:
        print("error in code")
        print(e)
    else:
        print("no error with try block")

if 0:
    try:
        a = int(input("enter the number"))
        b = 9/a
        print("completed execution")
    except (FileExistsError,ValueError,Exception,ZeroDivisionError):
        print("there is an error in code")
    else:
        print("no error with try block")

#raising an error
if 0:
    try:
        a = int(input(" enter the value"))
        if a < 10:
            raise ValueError("the value what you gave is less than the required value")
    except ValueError as e:
        print(e)
    else:
        print("you are right")

if 0:#printing prime numbers
    for i in range(2,25):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

if 0:#printing prime numbers
    print_primes = [x for x in range(2,25) if all(x%y !=0 for y in range(2,x))]
    print(print_primes)

    #priniting prime numbers:
    # Generator expressions
    a = range(8)
    b = [i+2 for i in a] #list comprehension
    print(b)
    
    c = (i+2 for i in a) # generator expression
    print(c) #prints generator address
    
    print(next(c))#generating one item
    
    print()
    #generating one after other
    for j in c:
        print(j)
    
    print()
    c = (i+2 for i in a) # generator expression
    print(min(c))
if 0:
    # Generator use cases
    # fibonacci series
    def fib():
        f,s = 0,1
        while True:
            yield f
            f,s = s,f+s
    for i in fib():
        if i >50:
            break
        print(i,end=" ")
    
    # numnber stream
    # a = (x for x in range(0,100)) #generator expression
    # for i in a:
    #     print(i)



if 0:#class variables addition
    #not a good practice
    class test:
        pass
    test.name = 'test'
    t1=test   #assiging the class to the variable
    print(t1)
    print(type(t1))
    t1.name ='test1'
    t1.surname = 'newtest1'
    t1.numer = 1
    t2=test    #assiging the class to the variable
    t2.name ='test2'
    t2.surname = 'newtest2'
    t2.number = 2
    print(t1.name)
    print(t2.name)
    print(test.name) #all are same

if 0:
    class practice:
        pass
    practice.name = 'practice'
    t1=practice()#creating the instance of class
    print(t1)
    print(type(t1))
    t1.name ='test1'
    t1.surname = 'newtest1'
    t1.numer = 1
    t2=practice()
    t2.name ='test2'
    t2.surname = 'newtest2'
    t2.number = 2
    print(t1.name)
    print(t2.name)
    print(practice.name) #All are different




if 0:
    class Car():
        car_type = 'Sedan'    #class attribute wiil be same for all objects
        
        # constructor
        def __init__(self,name,milage,color,has_safety):
            print('my car is ready')
            self.name = name
            self.milage = milage   #  <--instance attributes differ for each object
            
            self._color = color  #<-- protected variable
            self.__has_safety = has_safety #private variable
        def __del__(self):
            print('object is deleted')
        
        #instance method with instance attributes
        def description(self):
            print("{} is the milage of {} looks good".format(self.name, self.milage))

        
        def max_speed(self,speed):
            print("{} is going with max speed of {}".format(self.name,speed))
        
        #encapsulation
        #instance method with protected  attribute 
        def car_color(self):
            print('{} is looks nice in {} color'.format(self.name,self._color))
        
        def has_safety(self):
            print('{} is {}'.format(self.name,self.__has_safety))
        
        def changeSafety(self,change_safety):
            self.__has_safety = change_safety
        
        
    
    # instantiate the Car class
    my_car = Car('my car',24,'black','no safe')
    
    # access the class attributes
    print('my car company is {}'.format(my_car.__class__.car_type))
    
    # access the instance attributes
    print('my car brand name is {} and milage is {}'.format(my_car.name,my_car.milage))
    
    # call our instance methods
    my_car.description()
    my_car.max_speed(120)
    
    #INHERITENCE 
    '''Inheritance is the procedure in which one class inherits the attributes and methods of another class.  The class whose properties and methods are inherited is known as Parent class. And the class that inherits 
    the properties from the parent class is the Child class.
    
    The interesting thing is, along with the inherited properties and methods, 
    a child class can have its own properties and methods.'''
    print('\ninheritence\n')
    
    class BMW(Car):  #child class
        def __init__(self, name, milage, color, has_safety):
            super().__init__(name, milage, color, has_safety)
            print('BMW is ready')
        def poly_function(self):
            print("This the description function of class BMW.")
    
    
    class AUDI(Car): #child class
        
        def audi_description(self):
            print('this is the description of car Audi')
        
        def poly_function(self):
            print("This the description function of class AUDI.")
        
    bmw = BMW('BMW_Series1',15,'blue','safe')

    
    # ENCAPSULATION
    '''Encapsulation  is a way to ensure security. Basically, it hides the data from the access of outsiders'''
    print('\n encapsulation\n')
    
    # accessing protected variable via class method 
    # my_car.car_color()
    # bmw.car_color()
    # audi.car_color()
    
    #accessing protected variable directly from outside
    print(my_car._color)
    my_car._color='blue'
    print(my_car._color)
    #accessing private variable via class method getter function
    my_car.has_safety()
    bmw.has_safety()
    
    # accessing private variable directly from outside
    # print(my_car.__has_safety)  #will give an error
    
    # Name mangling is a mechanism we use for accessing the class members from outside.
    print(my_car._Car__has_safety)    #mangled name
    
    my_car.has_safety()
    
    # changing the safety value directly
    my_car.__has_safety = 'safe'
    print('hello')
    my_car.has_safety()
    
    # using settter function
    my_car.changeSafety('safe')
    my_car.has_safety()

# accessing the private variable from child
if 0:
    class Parent:
        def __init__(self):
            self.__randomVariable = 'Test1'
            
    class Child(Parent):
        def __init__(self):
            super().__init__()
        def doSomething(self):
            self.__randomVariable = 'Test2'
            print(self.__randomVariable)
            
    p = Parent()
    # print(p.__randomValue)
    p._Parent__randomValue= 'tewst3'
    print(p._Parent__randomVariable)
    c = Child()
    print(c._Parent__randomVariable)
    # prints Test1, i.e. the value assigned in the parent class
    c.doSomething()
    # calling doSomething will execute the assignment in the subclass
    print(c._Parent__randomVariable)
    # still prints Test1, i.e. the private variable in the parent class
    # did not get reassigned in the method doSomething
    print(c._Child__randomVariable)
    # This one prints Test2, so in fact what happened is that a new
    # private attribute was created in the subclass.
    #accessing the parent method in child using super keyword.
    class P:
        def my_method(self):
            print('parent')

    class C(P):
        '''Child'''
        def my_method(self):
            print('child')


        def call_parent_method(self):
            super().my_method()

        
    child = C()
    child.call_parent_method()

# parent
# OOPS concepts
# classes and objects
# types of variables in class
# 1.class variable: it can be shared by all instances/objects
# 2.instance variable: it will specific to particualr object
# 3.data member: it is either class/instance variable holds data 
# associated with class and object
if 0:
    class Cars:
        # constructor which helps to assign value at object creation 
        #NO need give the word only 'self'. we can provide any name,
        #but we have to use that name only entire class definition
        
        def __init__(self,price,name,year):
            self.price= price
            self.year = year
            self.name=name
            
        # creating method
        def price_inc(self):
            self.price = int(self.price*1.15)
        
    honda = Cars(100000,'city',2015)
    honda.validity = 10
    
    tata = Cars(3000000,'indica',2013)
    
    print(honda.price)
    honda.price_inc()
    print(honda.price)
    # printing the parameters of object
    print(honda.__dict__)
    print(tata.__dict__)
    
    # OOPS concepts in python
    # 1.inheritence 2.Encapsulation 3.Abstraction
    
    # Inheritence
    
    # Inheriting the Cars to create Supercar class
    
    class SuperCar(Cars):
        
        # creating constructor uisng parent constructor
        def __init__(self,price,name,year,validity):
            Cars.__init__(self,price,year,name)
            self.validity = validity
    
    toyota = SuperCar(500000, 'indica', 2012,10)
    # print(help(toyota))
    print(toyota.price)
    toyota.price_inc()
    print(toyota.price)
    print(toyota.__dict__)


# Date 15/02/2021 from office laptop
if 0:  #DONT TRY
    class Cars:
        def __init__(self,name,year,price):
            self.name = name
            self.year=year
            self.price=price
    
        def price_inc(self):
            self.price *=1.15
    
    class SuperCar(Cars): #inheriting the cars class into supercar
        def __init__(self,name,year,price,validity):
            Cars.__init__(self,name,year,price) #inheriting the Cars constructor
            self.validity = validity
    
        def price_inc(self): #overwriting the method
            self.price *=2
    
    toyota = Cars("indica",2016,100000)
    honda = SuperCar("city", 2015, 400000,10)
    
    print(honda.__dict__)
    print(honda.validity)
    print(honda.price)
    honda.price_inc()
    
    print(honda.price)

# Types of inheritence

# 1.sinlge  2.multiple
# 3.multi level inheritence
# 4.Hierarchial and hybrid inheritence
#For MRO reference: 
#http://www.srikanthtechnologies.com/blog/python/mro.aspx#:~:text=Method%20Resolution%20Order%20(MRO)%20is,lets%20examine%20a%20few%20cases.
#https://stackoverflow.com/questions/27954695/what-is-a-sibling-class-in-python
if 0:
    # Sinlge inheritence
    
    class Cars:
        def __init__(self,name,year,price):
            self.name = name
            self.year=year
            self.price=price
    
        def price_inc(self):
            self.price *=1.15
    
    class SuperCar(Cars): #inheriting the cars class into supercar
        def __init__(self,name,year,price,validity):
            Cars.__init__(self,name,year,price) #inheriting the Cars constructor
            self.validity = validity
    
        def price_inc(self): #overwriting the method
            self.price *=2
    
    toyota = Cars("indica",2016,100000)
    honda = SuperCar("city", 2015, 400000,10)
    
    print(honda.__dict__)
    print(honda.validity)
    print(honda.price)
    honda.price_inc()
    
    print(honda.price)

if 0:
    # Multiple inheritence child will have 2 or more parents
    
    class Father:
        def func1(self):
            print("this is function 1")
        def func0(self):
            print("this is father function ")
    class Mother:
        def func2(self):
            print("this is function 2")
        def func0(self):
            print("this is mother function ")
    
    class Child1(Father,Mother):
        def func3(self):
            print("this is function 3")
    
    class Child2(Mother,Father):
        def func3(self):
            print("this is function 3")
    
    ob = Child1()
    ob.func1()
    ob.func2()
    ob.func3()
    ob.func0()
    
    ob = Child2()
    ob.func1()
    ob.func2()
    ob.func3()
    ob.func0()

if 0:
    # Multi level inheritence
    
    class Parent:
        def func1(self):
            print("this is function 1")
    class Child(Parent):
        def func2(self):
            print("this is function 2")
    class GrandChild(Child):
        def func3(self):
            print("this is function 3")
    
    ob = GrandChild()
    ob.func1()
    ob.func2()
    ob.func3()

if 0:
    # Heirarchial Inheritence it means parent have 2 or more childs
    
    class Parent:
        def func1(self):
            print("this is function 1")
    class Child1(Parent):
        def func2(self):
            print("this is function 2")
    class Child2(Parent):
        def func3(self):
            print("this is function 3")
    ob1 = Child1()
    ob1.func1()
    ob2 = Child2()
    ob2.func1()

if 0:
    # Hybrid inheritence it will have 2 or more types of inheritence

    class GrandFather:
        def func1(self):
            print("this is function 1")
    class Father(GrandFather):
        def func2(self):
            print("this is function 2")
    class Mother:
        def func4(self):
            print("this is function 4")
    class Child(Father,Mother):
        def func3(self):
            print("this is function 3")
    
    ob = Child()
    ob.func1()
    ob.func2()
    ob.func3()
    ob.func4()

if 0:
    # Suoer function --> by using this, 
                            # parent method calls in child method
    
    class Parent:
        def func1(self):
            print("this is function 1")
    
    class Child(Parent):
        def __init__(self):
            super().func1() #calling function from parent in child before object creation
            
        def func2(self):
            print("This is function 2")
    
    ob = Child()
    # ob.func2()

if 0:
    # Method overriding helps to change the functionality of parent class method
    
    class Parent:
        def func1(self):
            print("this ic parent function")
    class Child(Parent):
        def func1(self): #this method over written parent method
            print("this is child function")
    
    ob = Child()
    ob.func1()

if 0:
    # Hybrid inheritence it will have 2 or more types of inheritence
    class GrandFather:
        def func1(self):
            print("this is function 1")
    class Father(GrandFather):
        def func2(self):
            print("this is function 2")
    class Mother:
        def func4(self):
            print("this is function 4")
    class Child(Father,Mother):
        def func3(self):
            print("this is function 3")
    
    ob = Child()
    ob.func1()
    ob.func2()
    ob.func3()
    ob.func4()

if 0:
    # Suoer function --> by using this, parent method calls in child method
    
    class Parent:
        def func1(self):
            print("this is function 1")
    
    class Child(Parent):
        def func2(self):
            super().func1() #calling function from parent in child before object creation
            print("This is function 2")
    
    ob = Child()
    ob.func2()

if 0:
    # Method overriding helps to change the functionality of parent class method
    
    class Parent:
        def func1(self):
            print("this ic parent function")
    class Child(Parent):
        def func1(self): #this method over written parent method
            print("this is child function")
    
    ob = Child()
    ob.func1()

# DATA ABSTRACTION
'''We use Abstraction for hiding the internal details or implementations 
of a function and showing its functionalities only.
Any class with at least one abstract function is an abstract class.'''
if 0:
    print('\ndata abstraction\n')
    from abc import ABC,abstractmethod
    
    class House(ABC):
        def __init__(self,name):
            self.name = name
    
        def description(self):
            print("This the description function of {}".format(self.name))
        
        # using the decorator
        @abstractmethod
        def price(self,cost):
            pass
   
    
    '''Important thing is– you cannot create an object 
    for the abstract class with the abstract method.'''
    # house = House('my_house')   #will not work
    
    class first_house(House):
        def price(self,x):
            print('the house value is {}k'.format(x))
    
    class second_house(House):
        def price(self,y):
            print('the house value is {}k'.format(y))
            
    house1 = first_house('my_house1')
    print(house1.description())
    print(house1.price(20))
if 0:
    from abc import ABC, abstractmethod


    class AbstractClassExample(ABC):

        @abstractmethod
        def do_something(self):
            print("Some implementation!")


    class AnotherSubclass(AbstractClassExample):

        def do_something(self):
            super().do_something()  # still we can use the abstract method before overriding. But finally we have to override the method
            print("The enrichment from AnotherSubclass")


    x = AnotherSubclass()
    x.do_something()

# created at 16 feb 2021 in personal laptop

# time and datetime modules
'''
import datetime
# using the constructor
a = datetime.datetime(2021,2,16,19,35,56,678)
# print(a)

# current date and time
b = datetime.datetime.today()
print(b)
c = datetime.datetime.now()
print(c)
d = datetime.datetime.today()
print(d.year,d.month)

e = datetime.date(2021, 2, 16)
print(e)
f = datetime.time(23,45,56)
print(f)

b1 = datetime.timedelta(hours=34,minutes=45)
b2 = datetime.timedelta(hours=56,minutes=34)
b3 = b2-b1
print(b3)
print(type(b3))
'''

# Numpy



a = np.array([(1,2,3),(4,5,6)])
# print(a)
b = np.array([[1,2,3],[4,5,6]])
# print(b)

# numpy v/s List
'''
# 1. less memory
import time,sys
SIZE= 1000
l1 = range(SIZE)
n1 = np.arange(SIZE)
print(sys.getsizeof(5)*len(l1))
print(n1.size *n1.itemsize)

# 2.Faster than list
l2 = range(SIZE)
n2 = np.arange(SIZE)

start = time.time()
res1 = [(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

start = time.time()
res2 = n1+n2
print((time.time()-start)*1000)
'''

'''
n = np.array([1,2,3,4,5,6,7])
print(n.shape)
print(n)
n = np.array([[1,2,3,4,5,6,7]])
print(n.shape)
print(n)

a = np.array([(1,2,3),(4,5,6)])
print(a.shape)
a = a.reshape(3,2)
print(a.shape)

# multiply by taking each element but not matrix multiplication
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print(a*b)

print(np.vstack((a,b))) #adding vertically
print(np.hstack((a,b))) #adding horizontally
print(a.ravel()) #row array
'''
'''
import matplotlib.pyplot as plt
x = np.arange(0,3*np.pi,0.1)
y = np.tan(x)
plt.plot(x,y)
plt.show()

a = np.array([1,2,3])
print(np.exp(a)) #natural log i.e log with base e
print(np.log2(a))
print(np.log10(a))
'''

# Scipy

# Basic functions
'''
from scipy import cluster
# help(cluster)
# help()# give argument as scipy.cluster #use 'quit' to exit from this

import scipy
scipy.info(cluster)
scipy.source(cluster)
'''

# special functions

# from scipy import special
'''
a = special.exp10(2)
print(a)
print(special.exp2(3))
c = special.sindg(90)
print(c)
print(special.cosdg(90))
'''

# integration functions
'''
from scipy import integrate
i = integrate.quad(lambda x:special.exp10(x),0,1)
print(i)
e = lambda x,y: x*y
g = lambda x: 1
h = lambda x : -1
print(integrate.dblquad(e, 0, 2, g, h))
'''

# FFT and IFFT functions
'''
from scipy.fftpack import fft,ifft
x = np.array([1,2,3,4])
y = fft(x)
z = ifft(x)
print(y)
print(z)
'''

# Linear Algebra

'''
from scipy import linalg
a = np.array([(1,2),(4,5)])
b = linalg.inv(a)
print(b)
'''

# Interpolation functions
'''
import matplotlib.pyplot as plt
from scipy import interpolate
x = np.arange(5,20)
y = np.exp(x/3)
print(x)
print(y)
f = interpolate.interp1d(x, y)
f1 = interpolate.interp1d(x, y)
x1 = np.arange(6,12)
y1 = f(x1)
plt.plot(x,y,'o',x1,y1,'--')
plt.show()
'''
'''
import pandas as pd
xyz_web = {"day":[1,2,3,4,5,6],"visitors":[1000,7000,6000,1000,400,350],
           "bounce":[20,20,23,45,45,54]}
df = pd.DataFrame(xyz_web)
# print(df)

# slicing
# print(df.head(2))
# print(df.tail(2))

# merging
web1 = pd.DataFrame({"day":[1,2,3,4,5,6],"visitors":[1000,7000,6000,1000,400,350],
           "bounce":[20,20,23,45,45,54]})
web2 = pd.DataFrame({"day":[1,2,3,4,5,6],"visitors":[1000,7000,6000,1000,400,350],
           "bounce":[20,20,23,45,45,54]})

merge = pd.merge(web1, web2)
merge1 = pd.merge(web1, web2,on='day')
# print(merge1)

# joined
df1 = pd.DataFrame({"visitors":[1000,7000,6000,1000,400,350],
           "bounce":[20,20,23,45,45,54]},index = [1,2,3,4,5,7])
df2 = pd.DataFrame({"visitors1":[1000,7000,6000,1000,400,350],
           "bounce1":[20,20,23,45,45,54]},index = [1,3,4,5,6,8])
joined = df1.join(df2)
# print(joined)

# change index and column headers
import matplotlib.pyplot as plt
from matplotlib import style
df1 = pd.DataFrame({"days1":[1,2,3,4,5,6],"visitors1":[100,700,600,100,40,35],
           "bounce1":[20,20,23,45,45,54]})
df2 = pd.DataFrame({"days2":[1,2,3,4,5,6],"visitors2":[100,700,600,1000,40,35],
           "bounce2":[20,20,23,45,45,54]})

# print(df1)

# df1.set_index("day",inplace=True)
# print(df1)

style.use("fivethirtyeight")
# df1.plot()
# plt.show()
df1 = df1.rename(columns={"visitors":"users"})
# print(df1)

concat = pd.concat([df1,df2])
# print(concat)
'''
# created at 19 feb at office laptop
# python for statistics
'''
from statistics import mean,median,mode,variance
print(mean([1,2,2,2,1,3,4,1,5]))
print(median([1,1,1,2,2]))
print(mode([1,1,1,2,2]))
print(variance([1,1,1,2,2]))
'''

# matplotlib

# linear plot

# from matplotlib import pyplot as plt
'''
x = [5,6,7]
y = [3,4,2]

plt.plot(x,y)
plt.title('info')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
'''
'''
x = [5,6,7,4]
y = [3,4,2,3]

x2 = [7,4,5,8]
y2 = [4,3,2,4]

plt.plot(x,y,'g',label="line one",linewidth=5)
plt.plot(x2,y2,'c',label="line two",linewidth=5)

plt.title("my title")
plt.ylabel("y axis")
plt.xlabel("x axis")

plt.legend()
plt.grid(True,color='k')

plt.show()
'''

# bar graph
'''
x = [2,4,6,8]
y = [3,4,2,3]

x2 = [1,3,5,7]
y2 = [4,3,2,4]

plt.bar(x,y,label="line one")
plt.bar(x2,y2,label="line two",color="g")

plt.title("my title")
plt.ylabel("y axis")
plt.xlabel("x axis")

plt.legend()
plt.grid(True,color='k')
plt.show()
'''

# scatter plot
'''
x = [1,2,3,4,5,6,7,8]
y = [3,4,2,3,4,4,5,2]

plt.scatter(x, y, color='g',label='scatter1')
plt.legend()
plt.xlabel('xaxis')
plt.ylabel('y axis')
plt.show()
'''

# area plot
'''
days = [1,2,3,4,5]
sleep =   [6,5,8,9,4]
eating =  [5,6,6,7,8]
working = [7,4,5,7,3]
playing = [6,9,5,1,9]

plt.plot([],[],color='m',label='sleep',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='k',label='working',linewidth=5)
plt.plot([],[],color='r',label='playing',linewidth=5)

plt.stackplot(days, sleep,eating,working,playing,colors=['m','c','k','r'])
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('area plot')

plt.show()
'''

# Pie Plot
'''
slices = [5,4,6,3]
activities = ['play','eat','sleep','work']
cols = ['m','c','b','r']

plt.pie(slices,labels=activities,colors=cols,startangle=0,
        shadow=True,explode=(0,0.1,0,0),autopct='%1.1f%%')
plt.title("PIE PLOT")
plt.show()
'''
# subplots
'''
x1 = [2,4,6,8]
y1 = [3,4,2,3]
plt.subplot(211)
plt.bar(x1,y1,label="line one",width=0.8)

x = [1,2,3,4,5,6,7,8]
y = [3,4,2,3,4,4,5,2]
plt.subplot(212)
plt.scatter(x, y, color='g',label='scatter1')

plt.show()
'''
'''
import numpy as np
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0,5.0,0.1)
t2 = np.arange(0,5.0,0.02)
plt.subplot(211)
plt.plot(t1,f(t1),'go',t2,f(t2),linewidth=1)
plt.grid(False)

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),linewidth=1)
plt.show()
'''


#mp3 file speed control
'''
import wave

CHANNELS = 1
swidth = 2
Change_RATE = 2

spf = wave.open('Adai_Malai_Varum1.wav', 'rb')
RATE=spf.getframerate()
signal = spf.readframes(-1)

wf = wave.open('changed.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(swidth)
wf.setframerate(RATE*Change_RATE)
wf.writeframes(signal)
wf.close()

print(RATE)
# playing changed song
from pygame import mixer
mixer.init()
mixer.music.load("changed.wav")
# Setting loops=-1 to ensure that alarm only stops when user stops it!
mixer.music.set_volume(0.4)
mixer.music.play(loops=-1)
# Asking user to stop the alarm
input("Press ENTER to stop alarm")
mixer.music.stop()
'''

'''
change_rate = 1
from pygame import mixer
mixer.pre_init(44100*2)
mixer.init()
mixer.music.load("Adai_Malai_Varum1.wav")#supports .wav .ogg formats
# Setting loops=-1 to ensure that alarm only stops when user stops it!
mixer.music.set_volume(0.4)
mixer.music.play(loops=-1)
# Asking user to stop the alarm
input("Press ENTER to stop alarm")
mixer.music.stop()
'''


# created at 21 feb at personal laptop
# openCV Tutorial
# import cv2

'''
color_img = cv2.imread('./face_mask/image1.jpeg',1)
# print(color_img)
# print(type(color_img),color_img.shape)
gray_img = cv2.imread('./face_mask/image1.jpeg',0)
# print(gray_img)
# print(type(gray_img),gray_img.shape)
cv2.imshow('legend',gray_img)
# cv2.waitKey(0)# to provide delay <-- dont try these
# cv2.destroyAllWindows() <-- dont try these

# Resize of image
resized = cv2.resize(gray_img,(50,100))
# cv2.imshow('legend',resized)
# print(resized.shape)

resized1 = cv2.resize(gray_img,(int(gray_img.shape[1]/2),int(gray_img.shape[0]/2)))
# cv2.imshow('legend',resized1)

resized2 = cv2.resize(gray_img,(int(gray_img.shape[1]*2),int(gray_img.shape[0]*2)))
cv2.imshow('legend',resized2)
'''

# capturing the video
import time
'''
video= cv2.VideoCapture(0)
check,frame = video.read()
print(check)
# print(frame)
time.sleep(3)
cv2.imshow('frames',frame)
video.release()
'''

'''
video= cv2.VideoCapture(0)
a = 1
while True:
    a+=1    
    check,frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(a) #priniting no.of frames
video.release()
cv2.destroyAllWindows()
'''

# Motion detector
'''
import pandas as pd
from datetime import datetime
first_frame = None
status_list = [None,None]
times = []
pd.DataFrame(columns=['Start','End'])
video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray,(21,21),0)
    # gray = cv2.GaussianBlur(gray,(21,21),0)
    
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESHBINARY)[1]
    thresh_delta  = cv2.dilate(thresh_delta,None,iterations=0)
    (_,cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL(), cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status =1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)
        
    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
        
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
    
    cv2.imshow('frame',frame)
    cv2.imshow('capturing',gray)
    cv2.imshow('delta',delta_frame)
    cv2.imshow('thresh',thresh_delta)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(status_list)
print(times)
for i in range(0,len(times),2):
    df = df.append({'Start':times[i],'End':times[i+1]},ignore_index=True)
df.to_excel("times.xlsx")

video.release()
cv2.destroyAllWindows()
'''

if 0:
    # import the threading module
    import threading
    
    class thread(threading.Thread):
    	def __init__(self, thread_name, thread_ID):
    		threading.Thread.__init__(self)
    		self.thread_name = thread_name
    		self.thread_ID = thread_ID
    
    		# helper function to execute the threads
    	def run(self):
            # print(self.thread_name,self.thread_ID)
            print(self.thread_name +" "+ str(self.thread_ID));
    
    thread1 = thread("GFG", 1000)
    thread2 = thread("GeeksforGeeks", 2000);
    
    thread1.start()
    thread2.start()
    
    print("Exit")

if 0:
    # Function to take multiple arguments
    def add(datatype, *args):
    
    	# if datatype is int
    	# initialize answer as 0
    	if datatype =='int':
    		answer = 0
    		
    	# if datatype is str
    	# initialize answer as ''
    	if datatype =='str':
    		answer =''
    
    	# Traverse through the arguments
    	for x in args:
    
    		# This will do addition if the
    		# arguments are int. Or concatenation
    		# if the arguments are str
    		answer = answer + x
    
    	print(answer)
    
    # Integer
    add('int', 5, 6)
    
    # String
    add('str', 'Hi ', 'Geeks')
if 0:
    def addition(val1,val2):
        print(val1+val2)
    
    addition(1,2)
    addition('hi','world')

'''Abstract data types are like what kind of data structure can hold
 and what operations can be done on that data'''
# single and double linked lists nodes creation
if 0:
    class SLLNode:
        def __init__(self,data):
            self.data = data
            self.next = None
        
        # get data for the current node
        def get_data(self):
            return self.data
        
        # set data for the current node
        def set_data(self,new_data):
            self.data = new_data
        
        # get the address for the next node
        def get_next(self):
            return self.next
        
        # dunder method helps to return the value in the next address
        def __repr__(self):
            return "SLL NOode object: data ={}".format(self.data)
        
        # set the next node address in current address
        def set_next(self,new_next):
            self.next = new_next
    
    if 0:
        node = SLLNode('apple')
        
        print(node.get_data()) #getting the value in node
        
        node.set_data('banana') #setting the value in node
        print(node.get_data())
        
        node2 = SLLNode('pizza')
        
        node.set_next(node2)#setting the next value of the node
        
        print(node2) #shows data instead of address
        print(node.get_next()) #getting the address of next node
    
    
    class DLLNode:
        def __init__(self,data):
            self.data = data
            self.next = None
            self.prev = None
        
        
        def get_data(self):
            return self.data
        
        
        def set_data(self,new_data):
            self.data = new_data
        
        
        def get_next(self):
            return self.next
        
        def get_prev(self): #getting the address of previous node
            return self.prev
        
        # dunder method helps to return the value in the next address
        def __repr__(self):
            return "SLL NOode object: data ={}".format(self.data)
        
        
        def set_next(self,new_next):
            self.next = new_next
            
        def set_prev(self,new_prev):
            self.prev = new_prev
    if 0:
        node0 = DLLNode(0)
        node1 = DLLNode(1)
        node2 = DLLNode(2)
        
        print(node1.get_prev())
        node1.set_prev(node0)
        print(node1.get_prev())

    class SLL: #LinkedList creation
        def __init__(self):
            self.head = None
        
        def __repr__(self):
            return "SLL object: data ={}".format(self.head)
        
        def isempty(self):
            return self.head is None
        
        def add_front(self):
            pass
        
        def size(self):
            pass
        
        def search(self):
            pass
        
        def remove(self,data):
            pass
        
    sll = SLL()
    print(sll.isempty())
    node1 = SLLNode(1)
    
    sll.head = node1
    print(sll.isempty())

if 0:        
    # Python program to demonstrate nested ternary operator
    a, b = 10, 20
    
    print ("Both a and b are equal" if a == b else "a is greater than b"
    		if a > b else "b is greater than a")

######## COLLECTIONS ############
if 0:
    if 0:
        # A Python program to show different
        # ways to create Counter
        from collections import Counter
        
        # With sequence of items
        print(Counter(['B','B','A','B','C','A','B',
        			'B','A','C']))
        
        # with dictionary
        print(Counter({'A':3, 'B':5, 'C':2}))
        
        # with keyword arguments
        print(Counter(A=3, B=5, C=2))
    
    if 0:
        # A Python program to demonstrate working of OrderedDict
        
        from collections import OrderedDict
        
        
        od = OrderedDict()
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4
        
        print('Before Deleting')
        for key, value in od.items():
        	print(key, value)
        	
        # deleting element
        od.pop('a')
        
        # Re-inserting the same
        od['a'] = 1
        
        print('\nAfter re-inserting')
        for key, value in od.items():
        	print(key, value)
    
    if 0:
        # Python program to demonstrate
        # defaultdict, 
        	
        	
        from collections import defaultdict
        	
        	
        # Defining the dict
        d = defaultdict(int)
        	
        L = [1, 2, 3, 4, 2, 4, 1, 2]
        	
        # Iterate through the list
        # for keeping the count
        for i in L:
        		
        	# The default value is 0
        	# so there is no need to
        	# enter the key first
        	d[i] += 1
        		
        print(d)
    if 0:
        # Python code to demonstrate ChainMap and
        # new_child()
        
        import collections
        
        # initializing dictionaries
        dic1 = { 'a' : 1, 'b' : 2 }
        dic2 = { 'b' : 3, 'c' : 4 }
        dic3 = { 'f' : 5 }
        
        # initializing ChainMap
        chain = collections.ChainMap(dic1, dic2)
        
        # printing chainMap
        print ("All the ChainMap contents are : ")
        print (chain)
        
        # using new_child() to add new dictionary
        # new child will be added at the beginning of list
        chain1 = chain.new_child(dic3)
        
        # printing chainMap
        print ("Displaying new ChainMap : ")
        print (chain1)
        print (chain1['a'])
    if 0:
        # Python code to demonstrate namedtuple()

        from collections import namedtuple
        
        # Declaring namedtuple()
        Student = namedtuple('Student',['name','age','DOB'])
        
        # Adding values
        S = Student('Nandini','19','2541997')
        
        # Access using index
        print ("The Student age using index is : ",end ="")
        print (S[1])
        
        # Access using name
        print ("The Student name using keyname is : ",end ="")
        print (S.name)
    
    if 0:
        # Python code to demonstrate namedtuple() and
        # _make(), _asdict()
        
        
        from collections import namedtuple
        
        # Declaring namedtuple()
        Student = namedtuple('Student',['name','age','DOB'])
        
        # Adding values
        S = Student('Nandini','19','2541997')
        
        # initializing iterable
        li = ['Manjeet', '19', '411997' ]
        
        # initializing dict
        di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }
        
        # using _make() to return namedtuple()
        print ("The namedtuple instance using iterable is : ")
        print (Student._make(li))
        
        # using _asdict() to return an OrderedDict()
        print ("The OrderedDict instance using namedtuple is : ")
        print (S._asdict())
        
if 0:
    # Python program to demonstrate
    # use of class method and static method.
    from datetime import date
    
    class Person:
    	def __init__(self, name, age):
    		self.name = name
    		self.age = age
    	
    	# a class method to create a Person object by birth year.
    	@classmethod
    	def fromBirthYear(cls, name, year):
    		return cls(name, date.today().year - year)
    	
    	# a static method to check if a Person is adult or not.
    	@staticmethod
    	def isAdult(age):
    		return age > 18
    
    person1 = Person('mayank', 21)
    person2 = Person.fromBirthYear('raju', 1996)
    
    print (person1.age)
    print (person2.age)
    
    # print the result
    print (Person.isAdult(22))
    
if 0:
    class Test:               #base class
        def method_one(self):
            print("Called method_one")
        
        @staticmethod
        def method_two():
            print ("Called method_two")
        
        @staticmethod
        def method_three():
            Test.method_two()
        
        # using classmethod decorator to edit the staticmethod
        
        @classmethod
        def method_four(cls):
            cls.method_two()
    
    
    class Test2(Test):  #derived class
        @staticmethod
        def method_two():
            print ("Test2")
    
    a_test = Test()
    a_test.method_one() #Called method_one
    a_test.method_two() #Called method_two
    a_test.method_three() #Called method_two
    a_test.method_four() #Called method_two
    print('hello')
    b_test = Test2()
    b_test.method_one() #Called method_one
    b_test.method_two() #Test2
    b_test.method_three() #Called method_two
    b_test.method_four() #Test2
    print('hello1')
    Test.method_two() #Called method_two
    Test.method_four() #Called method_two
    Test2.method_two() #Test2
    Test2.method_four() #Test2



# Sorting algorithms
# Bubble sort 
if 0:
    # Python3 program for Bubble Sort Algorithm Implementation
    def bubbleSort(arr):
    	
        n = len(arr)
        print(arr)
    
    	# For loop to traverse through all
    	# element in an array
        for i in range(n):
            
            for j in range(0, n - i - 1):
                	
    			# Range of the array is from 0 to n-i-1
    			# Swap the elements if the element found
                #is greater than the adjacent element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Driver code
    
    # Example to test the above code
    arr = [ 26, 21, 2, 1 ]
    
    bubbleSort(arr)
    
    print("Sorted array is:")
    for i in arr:
    	print("%d" % i)
# selection sort
if 0:
    # Selection Sort algorithm in Python
    def selectionSort(array):
    	size = len(array)
    	for s in range(size):
    		min_idx = s		
    		for i in range(s + 1, size):			
    			# For sorting in descending order
    			# for minimum element in each loop
    			if array[i] < array[min_idx]:
    				min_idx = i
    
    		# Arranging min at the correct position
    		(array[s], array[min_idx]) = (array[min_idx], array[s])
    
    # Driver code
    data = [ 7, 2, 1, 6 ]
    selectionSort(data)    
    print('Sorted Array in Ascending Order is :')
    print(data)
# Insertion sort
if 0:
    # Creating a function for insertion sort algorithm
    def insertion_sort(list1):    
    		# Outer loop to traverse on len(list1)
    		for i in range(1, len(list1)):    
    			a = list1[i]    
    			# Move elements of list1[0 to i-1],which are greater to one position
    			# ahead of their current position
    			j = i - 1
    		
    			while j >= 0 and a < list1[j]:
    				list1[j + 1] = list1[j]
    				j -= 1
    				
    			list1[j + 1] = a
    			
    		return list1
    			
    # Driver code
    list1 = [ 7, 2, 1, 6 ]
    print("The unsorted list is:", list1)
    print("The sorted new list is:", insertion_sort(list1))
# Binary search Tree

if 0:
    
    # insert operation in binary search tree
    # A utility class that represents an individual node in a BST
    
    class Node:
    	def __init__(self, key):
    		self.left = None
    		self.right = None
    		self.val = key
    
    # A utility function to insert
    # a new node with the given key
    
    
    def insert(root, key):
    	if root is None:
    		return Node(key)
    	else:
    		if root.val == key:
    			return root
    		elif root.val < key:
    			root.right = insert(root.right, key)
    		else:
    			root.left = insert(root.left, key)
    	return root
    
    # A utility function to search a given key in BST
    def search(root,key):
    	
    	# Base Cases: root is null or key is present at root
    	if root is None or root.val == key:
    		return root
    
    	# Key is greater than root's key
    	if root.val < key:
    		return search(root.right,key)
    
    	# Key is smaller than root's key
    	return search(root.left,key)
    
    # A utility function to do inorder tree traversal    
    def inorder(root):
    	if root:
    		inorder(root.left)
    		print(root.val)
    		inorder(root.right)
    def preorder(root):
        if root:
            print(root.val)
            preorder(root.left)
            preorder(root.right)
            
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.val)
    
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    
    # Print inoder traversal of the BST
    inorder(r)


"""
    ^           Matches the beginning of a line
    
    $           Matches the end of the line
    
    .           Matches any character
    
    \s          Matches whitespace
    
    \S          Matches any non-whitespace character
    
    *           Repeats a character zero or more times
    
    *?          Repeats a character zero or more times (non-greedy)
    
    +           Repeats a character one or more times
    
    +?          Repeats a character one or more times (non-greedy)
    
    [aeiou]     Matches a single character in the listed set
    
    [^XYZ]      Matches a single character not in the listed set
    
    [a-z0-9]    The set of characters can include a range
    
    (           Indicates where string extraction is to start
    
    )           Indicates where string extraction is to end
    
    \A          Returns a match if the specified characters are at the beginning of the string	"\AThe"	

    \b	        Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	

    \B	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
    \d	        Returns a match where the string contains digits (numbers from 0-9)	"\d"	

    \D	        Returns a match where the string DOES NOT contain digits	"\D"	

    \s	        Returns a match where the string contains a white space character	"\s"	

    \S	        Returns a match where the string DOES NOT contain a white space character	"\S"	

    \w	        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	

    \W	        Returns a match where the string DOES NOT contain any word characters	"\W"	

    \Z	        Returns a match if the specified characters are at the end of the string	"Spain\Z"
"""




"""
1	[Pp]ython--> Match "Python" or "python"
2	rub[ye]--> Match "ruby" or "rube"
3	[aeiou]--> Match any one lowercase vowel
4	[0-9]--> Match any digit; same as [0123456789]
5	[a-z]--> Match any lowercase ASCII letter
6	[A-Z]--> Match any uppercase ASCII letter
7	[a-zA-Z0-9]--> Match any of the above
8	[^aeiou]--> Match anything other than a lowercase vowel
9	[^0-9]--> Match anything other than a digit
"""
"""
Special Character Classes

1	.  --> Match any character except newline
2	\d  --> Match a digit: [0-9]
3	\D  --> Match a nondigit: [^0-9]
4	\s  --> Match a whitespace character: [ \t\r\n\f]
5	\S  --> Match nonwhitespace: [^ \t\r\n\f]
6	\w  --> Match a single word character: [A-Za-z0-9_]
7	\W  --> Match a nonword character: [^A-Za-z0-9_]
"""
"""
Repetition Cases

1	ruby?  --> Match "rub" or "ruby": the y is optional
2	ruby*  --> Match "rub" plus 0 or more ys
3	ruby+  --> Match "rub" plus 1 or more ys
4	\d{3}  --> Match exactly 3 digits
5	\d{3,}  --> Match 3 or more digits
6	\d{3,5}  --> Match 3, 4, or 5 digits
"""

"""
Nongreedy repetition :- This matches the smallest number of repetitions −

1	<.*>  --> Greedy repetition: matches "<python>perl>"
2	<.*?>  --> Nongreedy: matches "<python>" in "<python>perl>"
"""
"""
Grouping with Parentheses

1	\D\d+  --> No group: + repeats \d
2	(\D\d)+   --> Grouped: + repeats \D\d pair
3	([Pp]ython(, )?)+   --> Match "Python", "Python, python, python", etc.
"""

"""
Backreferences :- This matches a previously matched group again −

1	([Pp])ython&\1ails  --> Match python&pails or Python&Pails
2	(['"])[^\1]*\1  --> Single or double-quoted string. \1 matches whatever the 1st group matched. \2 matches whatever the 2nd group matched, etc.
"""
"""
Alternatives

1	python|perl  --> Match "python" or "perl"
2	rub(y|le))  --> Match "ruby" or "ruble"
3	Python(!+|\?)  --> "Python" followed by one or more ! or one ?
"""

"""
Anchors :- This needs to specify match position.
1	^Python  --> Match "Python" at the start of a string or internal line
2	Python$  --> Match "Python" at the end of a string or line
3	\APython  --> Match "Python" at the start of a string
4	Python\Z  --> Match "Python" at the end of a string
5	\bPython\b  --> Match "Python" at a word boundary
6	\brub\B  --> \B is nonword boundary: match "rub" in "rube" and "ruby" but not alone
7	Python(?=!)  --> Match "Python", if followed by an exclamation point.
8	Python(?!!)  --> Match "Python", if not followed by an exclamation point.
"""


# Regular expression methods 
import re
if 0:#search method will searches the entire string and return if any match found
    a = re.search('\d','asabnm2323')
    print(a)

if 0:#match method will search from the starting,if match found retirn the value,otherwise returns None
    a = re.match('as','asabasnm2323')
    print(a)
    print(a.group())
    b = re.match('\d','asd13adas')
    print(b)
    b = re.match('asd\d','asd13adas')
    print(b)
    print(b.group())


if 0:#raw string will remove the property of "\". it will be consider as a literal only.
    import re
    xx = "guru99,education is fun"
    r1 = re.findall(r"^\w+", xx)
    print((re.split(r'\s','we are splitting the words')))
    print((re.split(r's','split the words')))
    print((re.split(r'\\s','we are \\splitting the words')))
    print((re.split( '\\s','we are \\splitting the words')))
    print((re.split( '\\s','we are \ splitting the words')))

if 0:
    list = ["guru99 get", "guru99 give", "guru Selenium"]
    for element in list:
        z = re.match("(g\w+)\W(g\w+)", element)
    if z:
        print((z.groups()))
if 0:
    patterns = ['software testing', 'guru99']
    text = 'software testing is fun?'
    for pattern in patterns:
        print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
        if re.search(pattern, text):
            print('found a match!')
    else:
        print('no match')
if 0:
    abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
    emails = re.findall(r'[\w.]+@[\w.]+', abc)
    for email in emails:
        print(email)

if 0:
    txt = "The rain in Spain"
    x = re.findall("ai", txt)
    print(x)
      
    txt = "The rain in Spain"
    x = re.search("\s", txt)  
    print("The first white-space character is located in position:", x.start())
    
    txt = "The rain in Spain"
    x = re.split("\s", txt)
    print(x)
    
    txt = "The rain in Spain"
    x = re.sub("\s", "9", txt)
    print(x)
    
    txt = "The rain in Spain"
    x = re.search(r"\bS\w+", txt)
    print(x.span())
    print(x.string)
    print(x.group())
    
# Using_python_to_access_web_data
import re
if 0:
    str1 = '/*apples are @red & green'
    print(re.split('/\* @ &',str1))
    # print(m)

if 0:
    a='Beautiful, is; better*than\nugly'
    # re.split('; |, |\*|\n',a)
    str1 = '/*apples are @red & green'
    print(re.split('[/\*@&]',str1))
    m = re.split('[/\*@&]',str1)
    print("".join(m))
    print(re.split(r'[/*@&]',str1))
    m = re.split(r'[/*@&]',str1)
    print("".join(m))

if 0:#putting comment in search pattern and making it exceptional using re.X or re.VERBOSE
    target_str = "Jessa is a Python developer, and her salary is 8000"

    # re.X to add indentation  and comment in regex
    result = re.search(r"""(^\w{2,}) # match 5-letter word at the start
                            .+(\d{4}$) # match 4-digit number at the end """, target_str, re.X)
    # Fiver-letter word
    print(result.group(1))
    # Output 'Jessa'

    # 4-digit number
    print(result.group(2))
    # Output 8000

if 0:#making the . to accept newline character also as a literal by using re.S or re.DOTALL
    # string with newline character
    target_str = "ML\nand AI"

    # Match any character
    result = re.search(r".+", target_str)
    print("Without using re.S flag:", result.group())
    # Output 'ML'

    # With re.S flag
    result = re.search(r".+", target_str, re.S)
    print("With re.S flag:", result.group())
    # Output 'ML\nand AI'

    # With re.DOTALL flag
    result = re.search(r".+", target_str, re.DOTALL)
    print("With re.DOTALL flag:", result.group())
    # Output 'ML\nand AI'


if 0:  # preparing
    while True:
        v = input("enter the data")
        if v == 'done':
            break
        m = re.search("F*r", v)
        # works --> For,Foor,FFor,f#$%$r,f r
        # not works abc,12vfhgf123
        # m = re.search("^F*r", v)
        # works For,Fffr,a##ffr
        # not works FFRR,Fff,a####ff
        if m:
            print("matches")
        else:
            print("not matched")
if 0:  # preparing
    while True:
        v = input("enter the data")
        if v == 'done':
            break
        m = re.findall("F*r", v)#returns the list with matches
        # works dfas3gdf, hjghjg56gff6fgfg435
        # not works gfdgfg, ghghgff, ytrywd
        # m = re.findall("^[0-9]+", v)
        # works 1fgh, 223323hjbjhhh
        # not works ars1, @arsds1hbb23
        print(m)

if 0:  # preparing
    while True:
        v = input("enter the data")
        if v == 'done':
            break
        # m = re.findall("[AEIOU]+", v)#returns the list with matches
        # works fggAfgghEg,AfhghgEYhjgghg
        # not works dfas3gdf, hjghjg56gff6fgfg435
        m = re.findall("^[AEIOU]+", v)  # returns the list with matches
        # works Adfs,AEGFGFG,
        # not works dAEGGHJ,aeifghAaghggEf
        print(m)
if 0:
    v = 'From:prashanth : raj : abc'
    # Greedy match means search for the longer range
    # Non-Greedy match means search for the short range
    print("main string", v)
    m = re.findall('^F.*:', v)  # <--greedy
    print("greedy search", m)
    m = re.findall('^F.*?:', v)  # <--Non-greedy
    print("Non-greedy search", m)
if 0:
    while True:
        v = input("enter the data")
        if v == 'done':
            break
        # m = re.findall('\s+@\s+',v)
        # workd abc @ ghjabc,hjfsd @ vvhvg
        # not works  abc@ghj, ancbxh@fghfh
        m =re.findall('\S+@\S+',v)
        # works abc@ghj, ancbxh@fghfh
        # not works abc @ ghjabc,hjfsd @ vvhvg
        print(m)
if 0:
    # Python program to sort a list of
    # tuples by the second Item using sort()
    
    # Function to sort hte list by second item of tuple
    def Sort_Tuple(tup):
    
    	# reverse = None (Sorts in Ascending order)
    	# key is set to sort using second element of
    	# sublist lambda has been used
    	tup.sort(key = lambda x: x[1],reverse=True)
    	return tup
    
    # Driver Code
    tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
    
    # printing the sorted list of tuples
    print(Sort_Tuple(tup))
if 0:
    # Python code to sort a list of tuples
    # according to given key.
    
    # get the last key.
    def last(n):
    	return n[m]
    
    # function to sort the tuple
    def sort1(tuples):
    
    	# We pass used defined function last
    	# as a parameter.
    	return sorted(tuples, key = last)
    
    # driver code
    a = ((23, 45, 20), (25, 44, 39), (89, 40, 23))
    m = 2
    print("Sorted:"),
    print(sort1(a))

if 0:
    import re


    match = re.search(r'portal', 'GeeksforGeeks: A computer science \
    				portal for geeks')
    print(match)
    print(match.group())
    if match:
        print('success')
    print('Start Index:', match.start())
    print('End Index:', match.end())
if 0:
    loat = 2.154327
    format_float = "{:.2f}".format(loat)
    print(format_float)

# singleton class
if 0:
    class SingletonClass:
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(SingletonClass, cls).__new__(cls)
            return cls.instance
    singleton = SingletonClass()
    new_singleton = SingletonClass()
    
    print(singleton is new_singleton)

    singleton.singl_variable = "Singleton Variable"
    print(new_singleton.singl_variable)

# design patterns
# 1.Creational Design patterns
# 2.Structural Design patterns
# 3.Behavioral Design patterns

'''Creational Design patterns: These design patterns are all about 
class instantiation or object creation. These patterns can be further 
categorized into Class-creational patterns and object-creational patterns.
 While class-creation patterns use inheritance effectively in the 
 instantiation process, object-creation patterns use delegation'''
 
'''
These design patterns are about organizing different classes and objects 
to form larger structures and provide new functionality. 
'''

'''
Behavioral patterns are about identifying common communication patterns 
between objects and realizing these patterns. '''

#Creational Design patterns
# 1.Factory method
# 2.Abstract Factory method


if 0: #Creational Design patterns

    if 0: # Without Factory Method
        class FrenchLocalizer:
        	def __init__(self):
        		self.translations = {"car": "voiture", "bike": "bicyclette",
        							"cycle":"cyclette"}
        	def localize(self, msg):
        		return self.translations.get(msg, msg)
        
        class SpanishLocalizer:
        	"""it simply returns the spanish version"""
        	def __init__(self):
        		self.translations = {"car": "coche", "bike": "bicicleta",
        							"cycle":"ciclo"}
        	def localize(self, msg):
        		"""change the message using translations"""
        		return self.translations.get(msg, msg)
        
        class EnglishLocalizer:
        	"""Simply return the same message"""
        	def localize(self, msg):
        		return msg
        
           	# main method to call others
        f = FrenchLocalizer()
        e = EnglishLocalizer()
        s = SpanishLocalizer()
           
        # list of strings
        message = ["car", "bike", "cycle"]
           
        for msg in message:
           	print(e.localize(msg))
           	print(s.localize(msg))
           	print(f.localize(msg))
    if 0: # With Factory Method
        '''
        It allows an interface or a class to create an object, 
        but lets subclasses decide which class or object to instantiate.
        '''
        class FrenchLocalizer:
        	def __init__(self):
        		self.translations = {"car": "voiture", "bike": "bicyclette",
        							"cycle":"cyclette"}
        	def localize(self, msg):
        		return self.translations.get(msg, msg)
        
        class SpanishLocalizer:
        	def __init__(self):
        		self.translations = {"car": "coche", "bike": "bicicleta",
        							"cycle":"ciclo"}
        	def localize(self, msg):
        		return self.translations.get(msg, msg)
        
        class EnglishLocalizer:
        	def localize(self, msg):
        		return msg
        
        def Factory(language ="English"):
        
        	"""Factory Method"""
        	localizers = {
        		"French": FrenchLocalizer,
        		"English": EnglishLocalizer,
        		"Spanish": SpanishLocalizer,
        	}
        
        	return localizers[language]()
        
        
        
        f = Factory("French")
        e = Factory("English")
        s = Factory("Spanish")
        
        message = ["car", "bike", "cycle"]
        
        for msg in message:
        	print(f.localize(msg))
        	print(e.localize(msg))
        	print(s.localize(msg))
    
    if 0: #without abstract afctory method 
        class DSA:
        	def price(self):
        		return 11000
        
        	def __str__(self):
        		return "DSA"
        
        class STL:
        	def price(self):
        		return 8000
        
        	def __str__(self):
        		return "STL"
        
        class SDE:
        	def price(self):
        		return 15000
        
        	def __str__(self):
        		return 'SDE'
        
        sde = SDE() # object for SDE class
        dsa = DSA() # object for DSA class
        stl = STL() # object for STL class
        
        print(f'Name of the course is {sde} and its price is {sde.price()}')
        print(f'Name of the course is {dsa} and its price is {dsa.price()}')
        print(f'Name of the course is {stl} and its price is {stl.price()}')
    
    if 0: #with abstract factory method
        '''allows you to produce the families of related objects 
        without specifying their concrete classes.'''

        class DSA:
        	def Fee(self):
        		return 11000
        
        	def __str__(self):
        		return "DSA"
        
        class STL:
        	def Fee(self):
        		return 8000
        
        	def __str__(self):
        		return "STL"
        
        class SDE:
        	def Fee(self):
        		return 15000
        
        	def __str__(self):
        		return 'SDE'
        
        
        class Course_At_CSE:
        
            def __init__(self, courses_factory = None):
                """course factory is out abstract factory"""
                
                self.course_factory = courses_factory
        
            def show_course(self):
                """creates and shows courses using the abstract factory"""
        
                course = self.course_factory()
                print(f'We have a course named {course}')
                print(f'its price is {course.Fee()}')
        
        
       	course = Course_At_CSE(SDE)
       	course.show_course()
    if 0:#builder method  DO NOT UNDERSTAND
        class Course:

        	def __init__(self):
        		self.Fee()
        		self.available_batches()
        
        	def Fee(self):
        		pass
        
        	def available_batches(self):
        		pass
        
        	def __repr__(self):
        		return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)
        
        # concrete course
        class DSA(Course):
        
        	def Fee(self):
        		self.fee = 8000
        
        	def available_batches(self):
        		self.batches = 5
        
        	def __str__(self):
        		return "DSA"
        
        # concrete course
        class SDE(Course):
            
        	def Fee(self):
        		self.fee = 10000
        
        	def available_batches(self):
        		self.batches = 4
        
        	def __str__(self):
        		return "SDE"
        
        # concrete course
        class STL(Course):
        
        	"""Class for Standard Template Library"""
        
        	def Fee(self):
        		self.fee = 5000
        
        	def available_batches(self):
        		self.batches = 7
        
        	def __str__(self):
        		return "STL"
        
        
        # Complex course
        class Complexcourse:
            def Fee(self):
                self.fee = 7000
            def available_batches(self):
                self.batches = 6
            def __repr__(self):
                return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)
            
        
        # construct course
        def construct_course(cls):
        
        	course = cls()
        	course.Fee()
        	course.available_batches()
        
        	return course # return the course object
        
        dsa = DSA() # object for DSA course
        sde = SDE() # object for SDE course
        stl = STL() # object for STL course
        
        complex_course = construct_course(Complexcourse)
        print(complex_course)
    if 1: #Singleton method
        class Borg:

        	# state shared by each instance
        	__shared_state = dict()
        
        	# constructor method
        	def __init__(self):
        
        		self.__dict__ = self.__shared_state
        		self.state = 'GeeksforGeeks'
        
        	def __str__(self):
        
        		return self.state
        
        
        person1 = Borg() 
        person2 = Borg()
        person3 = Borg()
        
        person1.state = 'DataStructures' # person1 changed the state
        person2.state = 'Algorithms'	 # person2 changed the state
        
        print(person1) # output --> Algorithms
        print(person2) # output --> Algorithms
        print(person1 is person2)
        
        person3.state = 'Geeks' # person3 changed the
        						# the shared state
        print(person1) # output --> Geeks
        print(person2) # output --> Geeks
        print(person3) # output --> Geeks

if 0:
    '''magic triplets'''

    items = [10, 3, -4, 1, -6, 9]
    items.sort()
    length = len(items)
    l = []
    # Magic triplet is a group of three numbers whose sum is zero.
    for i in range(length):
        print("i",i)
        firstelement =items[i]
        # now we have to find the remaining numbers
        needed_sum = -firstelement

        ptr1 =i+1  #moving from left
        ptr2 = length-1 #moving from right
        while(ptr1 < ptr2):
            total = items[ptr1]+items[ptr2]
            print(items)
            print(items[ptr1],items[ptr2],total,firstelement)
            if(total  == needed_sum):
                l.append([firstelement,items[ptr1],items[ptr2]])
                print(l)
                ptr1+=1 #moving one step forward
            elif (total > needed_sum):
                ptr2-=1
            else:
                ptr1+=1

    print(l)

#printing the 2 biggest values from the list

integers = [1, 16, 3, 39, 26, 4, 8, 16]

# get 2 largest values
largest_integers = heapq.nlargest(2, integers)  # [39, 26]

largest_integer = largest_integers[0]  # 39
second_largest_integer = largest_integers[1]  # 26
'''
if 0:
    def fun1(a=10,b,c):
        pass

    a=20
    b=10
    c=5

    fun1(b,c) #it will not work because default assigned values are present at the first in function definition
'''
if 0:
    def fun1(b,c,a=10):
        pass

    a=20
    b=10
    c=5

    fun1(b,c) #it will work because default assigned values are present at the last in function definition

if 0:
    new_list = [2,3,2,1,4,3,1,2,4]
    test={}
    for i in new_list:
        k = 0
        for j in new_list:
            if i == j:
                k += 1
        test[i] = k    
    print(test)
if 0:
    l = [2,32,23,3,4,53,233,242,532,5,325,223]
    maximum = None
    for i in l:
        if maximum is None or maximum < i:
            maximum = i
    print(maximum)
if 0:
    # Program to generate a random number between 0 and 9

    # importing the random module
    import random

    print(random.randint(0,9))
if 0:
    pass
    #ssh keys
    '''SHA256:B+biL17G5f2TD9EffwJeEOnRGEm/OfH/yyHe0ITLOWc adaveniprashanth@gmail.com  for adaveniprashanth@gmail.com
    SHA256:WI+2OY8aP+gCTTwWYPAUa3bSJPmuTkETXyZlv1o5GWk prashanthx.adaveni@intel.com  for  prashanthx.adaveni@intel.com
    f328e45a48c643e802e1b5cb68fdfbe441688b02		branch 'master' of https://github.com/adaveniprashanth/MyData'''

if 0:#working
    import pywhatkit as kit
    number = '+919113890660'
    kit.sendwhatmsg(number,'hello',11,31)

if 0:
    #zip the folder after create folder structure
    with open("abc.txt",'w') as f1:
        for i in range(100):
            f1.write("diff -r the new file\n")
            f1.write("Only in the new file\n")
            f1.write("abc  is the new file again\n")

    f0 = open('abc_copy.txt','w')
    with open("abc.txt",'r') as f1:
        read_content = f1.readline()
    if read_content.startswith('diff -r'):
        f0.write(read_content)
    f0.close()
    today = date.today()
    d1 = today.strftime('%Y%m%d')
    if not os.path.isdir(os.path.join(os.getcwd(),'smedia_top/source/includes')):
        os.makedirs('smedia_top/source/includes')
    if not os.path.isdir(os.path.join(os.getcwd(),'smedia_top/source/rtl/src')):
        os.makedirs('smedia_top/source/rtl/src')

    copyfile('abc.txt','smedia_top/source/includes/abc.txt')#we have to provide file name also in detination if we use copyfile



    def zipdir(path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file),os.path.relpath(os.path.join(root, file),os.path.join(path, '..')))


    with zipfile.ZipFile('hotpatch_'+d1+'.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('smedia_top/', zipf)
if 0:#unzipping the zipped folder
    os.system("unzip "+'hotpatch_'+d1+'.zip')



# 7550006035

if 0:
    last_drop = '/nfs/site/disks/lnl_soc_regress_001/ashish/soc_package/LNL_IPX_UPLOAD/RTL1p0_refresh/xe2lpm_media_common-22ww44e-package'
    current_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/WW51_SOC_LNL_A0_PROD/IPX_UPLOAD/xe2lpm_media_common-22ww53e-package'
    log_file = 'log.txt'
    if os.path.isfile(os.path.join(os.getcwd(), log_file)):
        os.remove(os.path.join(os.getcwd(), log_file))
    reference_include = os.path.join(last_drop, 'smedia_top/source/includes')
    source_include = os.path.join(current_drop, 'smedia_top/source/includes')
    if os.path.isfile(os.path.join(os.getcwd(), log_file)):
        os.system("diff -r " + source_include + " " + reference_include + " >> log.txt")
    else:
        os.system("diff -r " + source_include + " " + reference_include + " > log.txt")
    reference_rtl = os.path.join(last_drop, 'smedia_top/source/rtl/src')
    source_rtl = os.path.join(current_drop, 'smedia_top/source/rtl/src')

    if os.path.isfile(os.path.join(os.getcwd(), log_file)):
        os.system("diff -r " + source_rtl + " " + reference_rtl + " >> log.txt")
    else:
        os.system("diff -r " + source_rtl + " " + reference_rtl + " > log.txt")

    includes_folder = 'smedia_top/source/includes'
    if not os.path.isdir(os.path.join(os.getcwd(), includes_folder)):
        os.makedirs(includes_folder)
    rtl_folder = 'smedia_top/source/rtl/src'
    if not os.path.isdir(os.path.join(os.getcwd(), rtl_folder)):
        os.makedirs(rtl_folder)

    new_file = open('updated_log.txt', 'w')
    with open(log_file, 'r') as f1:
        content = f1.readlines()
    for i in content:
        if i.startswith('diff -r'):
            new_file.write(i.split(" ")[2].split("/")[-1] + " present in both drops\n")
            if rtl_folder in i.split(" ")[2]:
                copyfile(i.split(" ")[2], rtl_folder + "/" + i.split(" ")[2].split("/")[-1])
            if includes_folder in i.split(" ")[2]:
                copyfile(i.split(" ")[2], includes_folder + "/" + i.split(" ")[2].split("/")[-1])
        elif i.startswith('Only in'):
            if current_drop in i:
                new_file.write(i.strip().replace(": ", "/").split("/")[-1] + " present in current drop\n")
                if rtl_folder in i:
                    copyfile(i.strip().replace(": ", "/").split(" ")[2],
                             rtl_folder + "/" + i.strip().replace(": ", "/").split("/")[-1])
                elif includes_folder in i:
                    print(i)
                    copyfile(i.strip().replace(": ", "/").split(" ")[2],
                     includes_folder + "/" + i.strip().replace(": ", "/").split("/")[-1])
            elif last_drop in i:
                new_file.write(i.strip().replace(": ", "/").split("/")[-1] + " present in last drop\n")

    new_file.close()

'''python test.py 
-f 'ww53_prashanth' 
-p '/nfs/site/disks/lnl_soc_disk_001/krenangi/WW51_SOC_LNL_A0_PROD_snapshot_plusbios' 
-r '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/WW51_SOC_LNL_A0_PROD/IPX_UPLOAD/xe2lpm_media_common-22ww53e-package'''

if 0:
    from datetime import date
    today = date.today()
    d1 = today.strftime("%Y%m%d")
    print("d1 =", d1)



if 0:#working
    import smtplib

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("adaveniprashanth@gmail.com", "fmvlojxwjtbnicpx")

    # fmvlojxwjtbnicpx <-- app password

    # message to be sent
    message = "Message_you_need_to_send"

    # sending the mail
    s.sendmail("adaveniprashanth@gmail.com", "adaveniprashanth@gmail.com", message)

    # terminating the session
    s.quit()

if 0:#need to test
    # Python code to illustrate Sending mail with attachments from your Gmail account
    # libraries to be imported
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "EMAIL address of the sender"
    toaddr = "EMAIL address of the receiver"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Subject of the Mail"

    # string to store the body of the mail
    body = "Body_of_the_mail"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    #file should be in same folder
    filename = "File_name_with_extension"
    attachment = open("Path of the file", "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "Password_of_the_sender")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

if 0:
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import base64

    """Create a message for an email.
    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.
    Returns:
        An object containing a base64url encoded email object.
      """
    def create_message(sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    """Send an email message.
    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.
    Returns:
        Sent Message.
      """
    def send_message(service, user_id, message):
        try:
            message = (service.users().messages().send(userId=user_id, body=message)
                       .execute())
            print('Message Id: {}'.format(message['id']))
            return message
        except:
            print ('An error occurred')

    #Sender is the sender email, to is the receiver email, subject is the email subject, and notification is the email body message. All the text is str object.
    def notification(sender, to, subject, notification):
        SCOPES = 'https://mail.google.com/'
        message = create_message(sender, to, subject, notification)
        creds = None
        if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
                #We use login if no valid credentials
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow =   InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        service = build('gmail', 'v1', credentials=creds)
        send_message(service, sender, message)

if 0:
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent   from Python"
    sender_email = "mydata232@gmail.com"
    receiver_email = "mydata232@gmail.com"
    password = input("Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    '''
    filename = "document.pdf"  # In same directory as script
    
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    
    # Add attachment to message and convert message to string
    message.attach(part)
    '''
    text = message.as_string()


    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


# 7550006035
# 04440146969
# kani.

if 0:
    l = [1,2,3,4,5,6,7,8,9,10,11]#gives False
    m = [1,2,3,4,5,7,8,9,10]#gives False
    n = [1,2,3,4,5,6,7,8,9,10]#gives True

    k = 10

    check = True
    for i in range(1,k+1):
        if i not in l:
            check = False
    for i in l:
        if i > k:
            check = False

    print(check)

# finding the word in list
if 0:
    l = ['sa2e','ab1c','as2d','as11e','b1ca','ads11','a2cb']
    digits1 = []; digits2 = []; res = []
    import re
    for i in l:
        count = len(re.findall('[0-9]',i))
        if count == 1:  digits1.append(i)
        elif count == 2:  digits2.append(i)
    print(digits1,digits2)
    for i in digits1:
        m=[]
        a = re.findall('[0-9]',i)
        for i in digits1:
            if a[0] in i:
                m.append(i); digits1.remove(i)
        if len(digits1) ==1: m.extend(digits1)
        res.append(m)
    res.append(digits2)

    print(res)


if 0:
    def left_start_pattern(n):
        k = 2*n
        for i in range(0,n):
            m = 1
            for j in range(0,k-i-2):
                print(" ",end="")
            k-=1
            for j in range(0,i+1):
                print(str(m)+" ",end="")
                m+=2
            print("\r")

    left_start_pattern(4)


if 0:
    s = "max_length"
    check = True
    for i in s:
        if i.isupper() and not i == '_':
            check=False

    if check:
        print(check,len(s.split('_')))
    else:
        check=False
        print(check, len(s.split('_')))



if 0:
    # use of logging module
    # logging.basicConfig(filename='sample.log', format='%(asctime)s | %(levelname)s: %(message)s', level=logging.NOTSET)
    logging.basicConfig(filename='sample.log',filemode='w', level=logging.NOTSET)
    logging.debug('Here you have some information for debugging.')
    logging.info('Everything is normal. Relax!')
    logging.warning('Something unexpected but not important happend.')
    logging.error('Something unexpected and important happened.')
    logging.critical('OMG!!! A critical error happend and the code cannot run!')

if 0:
    #logging module example
    pass
    #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
'''
logger = logging.getLogger("test")
logger.setLevel(level=logging.DEBUG)
logFileFormatter = logging.Formatter(fmt='%(name)s - %(levelname)s - %(message)s')
fileHandler = logging.FileHandler(filename='test.log')
fileHandler.setFormatter(logFileFormatter)
fileHandler.setLevel(level=logging.DEBUG)
logger.addHandler(fileHandler)
'''

'''
root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='test.log')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
'''

'''
# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

'''

'''
if re.search('vmx_sl_vid[\d]+','/smvdbox0/smmfxvdenc1/vmx_sl_vid11'):
    print("present")
else:
    print("not present")
'''




if 0:
    smedia=''
    import glob
    for file in glob.glob(os.path.join(os.getcwd(),'sm*')):
        smedia = file
        print(file)
    print("sm", os.path.basename(smedia))
    logging.info(os.path.basename(smedia))
    logging.debug(os.getcwd())

    a = 5
    b = 0

    try:
        c = a / b
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)


if 0:
    v = input("enter the students count")
    t = input("enter the students ranks")
    length = len(t.split())
    reminder = length%3
    if reminder > 0: extra_classes = 1
    else: extra_classes = 0
    total_classes = (length//3)+extra_classes
    print(total_classes)



if 0:
    import yaml

    f = open('//sc6-samba.sc.intel.com/nfs/site/disks/xe3_clips_storage/hello.py','r')
    print(f.readlines())

# adding the values in list in dcitionary
if 0:
    Details = {"Destination": "China",
               "Nstionality": "Italian", "Age": []}
    Details["Age"] += [20, "Twenty"]
    print(Details)

if 0:
    # count the duplicated values in list
    l = [1,2,3,1,3,4,2,4,2,4,2,3,5,4,3,6,5,4,7,1,3,4,3,2,6]
    d = {}
    for i in l:
        d[i]=d.get(i,0)+1
    print(d)



def copy_files():
    destination = '/nfs/site/disks/xe3_clips_storage/Decoder/MFX/MPEG'
    f = open(output_file,'r')
    l = f.readlines()
    print(os.getcwd())
    for i in l[0:2]:
        clipname = i.strip().split("\\")[-1]
        print(clipname)
        dest_path = destination+"/"+clipname
        source = i.strip()
        print(source)
        print(dest_path)
        # shutil.copyfile(source,dest_path)

if 0:#copy/delete files/folders
    if 0:
        print(os.listdir('abc'))#to list all the directories/files in it
        os.rename('abc/abc.txt','abc/xyz.txt')#to rename the file
    if 0:#copy files/folders
        os.mkdir('def')#to create a folder
        #os.rmdir('def')#to delete an empty directory
        shutil.copy('abc/abc.txt','def')#copying the file from one folder to other folder
        shutil.copyfile('abc/abc.txt','def/abc.txt')#copying the file from one folder to other folder but we have to provide the file name in destination
        #shutil.copytree('abc','def/abc')#to copy the fodler structure from one folder to other folder
        #shutil.rmtree('def/abc')
    if 0:# delete file/folders
        os.rmdir('def')#to delete an empty directory
        os.remove('def/abc.txt')#to delete a file
        os.unlink('def/abc.txt')#linux form of deleting the file
        shutil.rmtree('def/abc')#to delete the directory with files/folders having in it.
        #send2trash.send2trash('abc/abc.txt')#deleting the file and sending it to recycle bin
        #os.remove('def/abc.txt')#deleting the file permannently shift+delete
    
if 0:#zipping/unzipping the files/folders
    if 0:#zipping the files/folders
        zip_file = zipfile.ZipFile('abc.zip','w')
        zip_file.write('abc/abc.txt')#add file names only. not the folders
        zip_file.close()
        
        shutil.make_archive('archive','zip','abc')#zipping the folder using shutil module. we can zip only folders using this.

    if 0:#unzipping/extracting the files/folders
        zip_file = zipfile.ZipFile('abc.zip','r')
        files = zip_file.namelist()
        print(files) #printing the file names in the zipped folder
        zip_file.printdir()#print all the files in zipped file
        #zip_file.extractall("extract_zipped")#extracting the zipped files to files to extract_zipped folder
        zip_file.close()
        
        #shutil.unpack_archive('archive.zip','archive')
if 0:#reading/writing into zipped file
    if 0:#reading the data
        zip_file = zipfile.ZipFile('abc.zip','r')#reading the zip file
        lines = zip_file.read('abc/abc.txt').split(b"\n")#bytes type of "\n"
        print(lines)
        zip_file.close()
    if 0:#another way
        zip_file = zipfile.ZipFile('abc.zip','r')#reading the zip file
        data = zip_file.open('abc/abc.txt','r')
        for i in data:
            print(i)
        data.close()
        zip_file.close()
    if 0:#appending into the zip file
        zip_file = zipfile.ZipFile('abc.zip','a')#we are adding the new member to zip file, so we have to use append method
        data = zip_file.open('abc/abc.txt','w')#adding a new file to archive file
        data.write(b"writing the data into the file after zipping")
        data.close()
        zip_file.close()
    if 0:#writing into the zip file
        zip_file = zipfile.ZipFile('abc.zip','w')#we are adding the new member to zip file, so we have to use append method
        data = zip_file.open('abc/abc.txt','w')#adding a new file to archive file
        data.write(b"writing the data into the file after zipping")
        data.close()
        zip_file.close()

#Handling the pdf files.
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger
if 0:
    if 0:#getting the document details
        filename= 'NLP_overview.pdf'
        f = open(filename,'rb')
        pdf_reader = PdfFileReader(f)#creating the pdf read object
        pdf_file_info = pdf_reader.getDocumentInfo()
        total_pages = pdf_reader.getNumPages()
        f.close()
        print("total pages",total_pages)
        author = pdf_file_info.author
        creator = pdf_file_info.creator
        producer = pdf_file_info.producer
        subject = pdf_file_info.subject
        title = pdf_file_info.title
        print("author",author)
        print("creator",creator)
        print("producer",producer)
        print("subject",subject)
        print("title",title)
    if 0:#extracting the data from pdf file# NOT WORKING
        filename= 'NLP_overview.pdf'
        f = open(filename,'rb')
        pdf_reader = PdfFileReader(f)#creating the pdf read object
        page  =pdf_reader.getPage(1)#getting the page from pdf
        #print(page)
        text = page.extractText()
        print(text)
        f.close()
    if 0:#rotating the files in pdf file. but not rotate the pdf file
        filename= 'NLP_overview.pdf'
        f = open(filename,'rb')
        f1 = open('rotated_'+filename,'wb')
        pdf_reader = PdfFileReader(f)
        pdf_writer = PdfFileWriter()#creating the object for writing
        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            page.rotateClockwise(180)
            pdf_writer.addPage(page)#adding the data to the object
            pdf_writer.write(f1)
        f1.close()
        f.close()
    if 0:#merging the pdf files
        file1='NLP_1.pdf'
        file2='NLP_2.pdf'
        file3='NLP_3.pdf'
        pdf_merger = PdfFileMerger()#creating the object of file merger
        pdf_merger.append(PdfFileReader(open(file1,'rb')))
        pdf_merger.append(PdfFileReader(open(file2,'rb')))
        pdf_merger.append(PdfFileReader(open(file3,'rb')))
        output = open("merged_output.pdf",'wb')
        pdf_merger.write(output)
        output.close()
    if 0:#merging the files in other method
        pdf_merger = PdfFileMerger()#creating the object
        for i in range(1,10):
            pdf_merger.append(PdfFileReader('NLP_'+str(i)+'.pdf','rb'))
        output = open('combined_merged.pdf','wb')
        pdf_merger.write(output)
        output.close()
    if 0:#separating the pages from pdf
        filename ='NLP_1.pdf'
        pdf_reader = PdfFileReader(filename)
        page = pdf_reader.getPage(0)#getting the required page
        
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(page)#adding the page. not the file
        
        output = open("separated.pdf",'wb')
        pdf_writer.write(output)
        output.close()
    if 0:#encryption of a file
        file = 'NLP_1.pdf'
        password = '1234'
        pdf_reader = PdfFileReader(file)
        pages = pdf_reader.getNumPages()
        pdf_writer = PdfFileWriter()
        for page_number in range(pages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
            pdf_writer.encrypt(user_pwd=password,owner_pwd=None,use_128bit=True)
        output = open('encrypted.pdf','wb')
        pdf_writer.write(output)
        output.close()
    if 0:#watermark the pdf
        input_file = 'NLP_1.pdf'
        watermark_file = 'NLP_2.pdf'
        
        input_pdf_reader = PdfFileReader(open(input_file,'rb'))#creating the object for input file
        watermark_pdf_reader = PdfFileReader(open(watermark_file,'rb'))#creating the object for watermark file
        
        watermark_page = watermark_pdf_reader.getPage(0)#getting the watermark page
        input_pdf_page = input_pdf_reader.getPage(0)#getting the first page from input file
        
        input_pdf_page.mergePage(watermark_page)#merging the watermark page with input file page
        
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(input_pdf_page)#adding the merged watermark page with pdf writer
        output = open('watermark.pdf','wb')
        pdf_writer.write(output)
        output.close()
#handling with documents
#A Run object is a contiguous run of text with the same style. A new Run object is needed whenever the text style changes.
#paragraph objectw ill be added to end of the document, but run object will be added at the end of the paragraph object
#adding heading is also considered as a paragraph

if 0:
    if 0:#saving the data into document
        new_document=docx.Document() #creating the document object
        new_document.add_heading('Heading one with style1',0)#adding the heading to document with heading1 style
        new_document.add_paragraph('This is the first paragraph in the document') #adding a paragraph
        
        new_document.add_heading('Heading one with style2',1)#adding the heading to document with heading1 style
        para = new_document.add_paragraph('This is the second paragraph in the document',style='Body Text') #adding with style
        para.add_run('adding the run object to the paragraph object')#adding the run object to para object
        new_document.add_heading('Heading one with style3',2)#adding the heading to document with heading1 style
        new_document.add_paragraph('This is the third paragraph in the document',style='Quote')
        new_document.add_paragraph('This is the third paragraph in the document',style='macro')
        new_document.add_paragraph('this is a Computer Science portal for guys.',style = 'Title')
        new_document.add_paragraph('this is a Computer Science portal for guys.',style = 'Subtitle')
        new_document.add_paragraph('this is a Computer Science portal for guys.',style = 'No Spacing')
        
        
        new_document.save('new_testing.docx') #saving the documnet
    if 0:#reading the data from documnet
        file=docx.Document('testing.docx')
        print(len(file.paragraphs)) #counting the paragraphs in document
        
        print(len(file.paragraphs[0].runs))#count the styles used in paragraph
        
        #printing the text in document based on styles
        for i in range(len(file.paragraphs[0].runs)):
            print(file.paragraphs[0].runs[i].text)
        
        #printing the full text from the document using paragraphs
        for para in file.paragraphs:
            print(para.text)
if 0:#handling the csv data
    if 0:#writing the data into csv file
        f = open('csv_file.csv','w',newline='')#if we do not give newline='', it will create an empty row in csv file
        writer = csv.writer(f)#creating the object for csv writer
        writer.writerow(["No","name","place"])#writing each row into the file
        writer.writerow([1,"asd","asd"])
        writer.writerow([2,"abc","abc"])
        #writing multiple rows at a time
        writer.writerows([[3,"qwert","qwert"],[4,"yuiop","yuiop"],[5,"hjkl","hjkl"],
                            [6,"zxcv","zxcv"]])
        f.close()
    
    if 0:#reading the csv file as a line
        f = open("csv_file.csv","r")
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            print(row)
        f.close()
    if 0:#reading the csv file as a dictionary
        f = open("csv_file.csv","r")
        reader = csv.DictReader(f,delimiter=',')
        for row in reader:
            print(row)
        f.close()
if 1:#JSON(Java Script Object Notation) data handling
    if 0:#python data to JSON 
        d ={'a':1,"b":"my name",2:"my place"}
        # Serializing json
        json_data = json.dumps(d)
        print(type(json_data))	
        
        json_object = json.dumps(d, indent = 4)
        print(json_object)
        print(type(json_object))
        
    if 0:#storing json data into file
        d ={'a':1,"b":"my name",2:"my place"}
        fp = open("json_data.json","w")
        json_data = json.dump(d,fp)
        fp.close()
    if 0:#convert json to python data
        data = """{
            "Name": "Jennifer Smith",
            "Contact Number": 7867567898,"Email": "jen123@gmail.com","Hobbies":["Reading", "Sketching", "Horse Riding"]
            }"""
        #data = """{'a':1,'b':2}"""#it will not work because the key is ecnlosed in dingle quote
        # parse data:
        res = json.loads( data )
        # the result is a Python dictionary:
        print( res )
        print( type(res ))
    if 0:#convert json data from file to python
        f = open('json_data.json','r')
        data = json.load(f)
        print(data)

    if 0: #pickling
        import pickle
        # Input Data
        my_data = {'BMW', 'Audi', 'Toyota', 'Benz'}

        # Pickle the input
        with open("demo.pickle", "wb") as file_handle:
            pickle.dump(my_data, file_handle, pickle.HIGHEST_PROTOCOL)

        # Unpickle the above pickled file
        with open("demo.pickle", "rb") as file_handle:
            res = pickle.load(file_handle)
            print(my_data)  # display the output
    
    
    
    
    
        
    
    