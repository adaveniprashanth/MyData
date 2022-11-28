#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array as arr
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
#iterating over nested dictionary
d = {'a':{'b':{'c':100}},'d':{'e':10}}

def myprint(d):
    for k, v in d.items():
        if isinstance(v, dict):
            myprint(v)
        else:
            print("{0} : {1}".format(k, v))
myprint(d)

import random as rd
# print(int(20*rd.random()))
# print(rd.random()+1)

# while else condition

random_value = int(20 * rd.random())
# print(rd.random())
# print(random_value)
user_selected = 0
# print(++user_selected)
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
    
    # reduce syntax reduce(function,iterables)
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
if 0:
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


if 0:
    class Car():
    
        car_type = 'Sedan'    #class attribute wiil be same for all objects
        
        
        # constructor
        def __init__(self,name,milage,color,has_safety):
            print('my car is ready')
            self.name = name
            self.milage = milage   #  <--instance attributes differ for each object
            
            self._color = color  #<-- protected variable
            self.__has_safety = has_safety
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
    
    #accessing protected variable via class method 
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
    
    #accessing private variable directly from outside
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
    '''Parent'''
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
# classews and objects
# types of variables in class
# 1.class variable: it can be shared by all instances/objects
# 2.instance variable: it will specific to particualr object
# 3.data member: it is either class/instance variable holds data 
# associated with class and object
if 0:
    class Cars:
        
        # constructor which helps to assign value at object creation 
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

import numpy as np

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
import cv2

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
    
    
    class T2(Test):  #derived class
        @staticmethod
        def method_two():
            print ("T2")
    
    a_test = Test()
    a_test.method_one()
    a_test.method_two()
    a_test.method_three()
    a_test.method_four()
    print('hello')
    b_test = T2()
    b_test.method_one()
    b_test.method_two()
    b_test.method_three()
    a_test.method_four()
    print('hello1')
    Test.method_two()
    Test.method_four()
    T2.method_two()
    T2.method_four()



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
    
    # A utility class that represents
    # an individual node in a BST
    
    
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

# Regular expression methods 
import re
if 0:
    import re
    xx = "guru99,education is fun"
    r1 = re.findall(r"^\w+", xx)
    print((re.split(r'\s','we are splitting the words')))
    print((re.split(r's','split the words')))

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
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
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
    # Grredy match means search for the longer range
    # Non-Grredy match means search for the short range
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
