
#for reference -->
# https://pynative.com/python-yaml/#:~:text=We%20can%20read%20the%20YAML,Deserializing%20YAML%20into%20a%20Python.
#string operations
'''
in split operation, it will split the string based on separator
It will split the string wherever the separator presents

in partition operation, it will return the part before the separator,separator and part after the separaton.
and also that it will split the string only at first occurance of separator.
'''
import pyinputplus as pypi

s = "my@name@is@prashanth"
if 0:
    print(s.split('@'))
    print(s.split("@",1))
    print(s.partition("@"))
    print(s.center(30,'&'))
    print(s.center(10,'&'))
if 0:
    print('abc\tabc'.expandtabs())
    print('my name is {}'.format('prashanth'))
    print('my name is {} {}'.format('prashanth','kumar'))
    print('my name is {1} {0}'.format('kumar','prashanth'))
if 0:
    print(s.isprintable())
    #print(help(s.isprintable))
    print('abc123'.isalnum())
    print('abc@'.isalpha())
    print('abc_'.isalpha())
    print('abcdef'.isalpha())
    print(*list(s))


'''
in insert operation, the object will be inserted at given position by moving the object
 to right side of the list. The position my be +ve or -ve value
NOTE: By using insert method you cannot insert the element at last position 
if you dont know the length of list, but we can use append method
'''
l = [1,2,'avba','fDF',4,5,'ewfdsc34']
if 0:
    print(l)
    l.insert(0,'ffds')#moving 0 positioned value to right side
    print(l)
    l.insert(-1,'dsaf')#moving _ positioned value to right side
    print(l)
    l.insert(-2,'iufew')
    print(l)
if 1:
    if 0:
        m = [[2,3,4,4,52,42,5],[2,6,75,47,54,65],[35,5,5,46,4,36,3]]
        print(m)
        print(m[::-1])
        print([i[::-1] for i in m[::-1]])

    if 0:
        #l=[1,2,3,4,5,3,2,3,[3,2,3,2,3,2,3]]#not working because the values will shift by removing 3 before nested list
        l=[1,2,3,4,5,3,2,[3,2,3,2,3,2,3]]#working
        #l=[4,5,6,5,7,8,9,[4,5,6,7,7,5]]#for testing others
        for i in l:
            #print()#use this line for debugging
            if i == 3:l.remove(3)
            if type(i)==list:
                for j in i:
                    if j == 3:i.remove(j)
            #print(i,"\n",l)
        print("final result",l)



if 0:
    #print(help(l.extend))
    for i in (1,2,3,4):
        print(i)

if 0:
    def test():
        return 'abc',[1,2,3,4],{2,3,4},{1:2,3:4}

    _,_,_,a=test()#using plcae holders
    print(a)
    print(_)
if 0:
    for i in range(2,5):
        for j in range(2,i):
            if i%j!=0:
                continue
            else:
                print(i)

'''
Note: to use next() function on iterable object, 
we have to convert the iterable object to iterator object.
:. we can use iter() function to convert iterable to object to iterator object.
:.for loop internally converts the iterable object into iterator object
:. no need to convert generator object to iterator object by using with next() function 
'''
if 1:
    if 0:
        a = 'pras'
        b = iter(a)
        print(next(b));print(next(b))
        print(next(b));print(next(b))
        #print(next(b))
    if 0:
        a = range(10)
        b = iter(a)
        print(next(b))
        print(next(b));print(next(b))
    if 0:
        def gencubes(n):
            for i in range(n):
                yield i**3
        v = gencubes(5)
        print(type(v));print(next(v))
        print(next(v));print(next(v))
    if 0:
        def fibonacci(n):
            a,b=0,1
            for i in range(n):
                yield a
                a,b=b,a+b

        v = fibonacci(5)
        print(next(v));print(next(v))
        print(next(v));print(next(v))
    if 0:
        a = range(8)
        c = (i + 2 for i in a)
        print(type(c))
if 0:
    if 0:
        a = lambda x: x**2
        print(a(3))
    if 0:
        b = lambda x,y,z:x+y+z
        l1=list(range(5))
        l2 = list(range(10,20));l3 = list(range(20,30))
        res = list(map(b,l1,l2,l3))
        print(res)
    if 0:
        from functools import reduce
        a = lambda x,y:x*y
        b = reduce(a,[1,1,1,1,1],2)
        print(b)
    if 0:
        a = lambda x:x%2 == 0
        l1 = list(range(10))
        b = list(filter(a,l1))
        print(b)

if 0:
    class person:
        def __init__(self,a,b,c):
            self.a=a
            self.b = b
            self.c = c

        def __str__(self):#to override object details
            return "first is {},second is {} and third is {}".format(self.a,self.b,self.c)
    p = person(1,2,3)
    print(p)
if 0:
    class grandafather:
        def MethodA(self):
            print("MethodA of Class0")

    class father(grandafather):
        def MethodA(self):
            super(father, self).MethodA()
            print("MethodA of ClassA")

    class mother(grandafather):
        def MethodA(self):
            print("MethodA of ClassB")

    class ClassC(father, mother):
        def MethodA(self):
            super(ClassC, self).MethodA()

    ClassC().MethodA()
    print(ClassC.__mro__)

#stringIO operations on string
'''
stringIO operations will be convert the string to file logic i.e we can perform file type operations
on string
'''
if 0:
    from io import StringIO
    s = 'prashanth'
    s1 = StringIO(s)
    a = s1.read()
    b = s1.read()
    s1.seek(0)
    c = s1.read()
    print(a)
    print(b)
    print(c)
    s1.write("faSEGFragr")
    s1.seek(0)
    print(s1.read())

'''
try/except logic handles only run time errors.
'''
#Multiple ways of try/except logics

if 0:
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

# raise the exception
#just for fun
if 0:
    while True:
        try:
            a = input(" are you donkey? yes or no?")
            if a.lower() != 'yes':
                raise ValueError("you have not selected correct answer")
        except ValueError as e:
            print("you are wrong",e)
        else:
            print("you are right")
            break

if 0:
    try:
        a = int(input(" enter the value"))
        if a < 10:
            raise ValueError("the value what you gave is less than the required value")
    except ValueError as e:
        print(e)
    else:
        print("you are right")

#raising the ZeroDivisionError
if 0:
    try:
        v = int(input("eneter the value"))
        if v == 2:
            raise ZeroDivisionError("here i am considering 2 as 0")
        print(56/v)
    except ZeroDivisionError as e:
        print(e)
if 0:
    # default exception
    try:
        f = open('adsasfd.txt')
    except ValueError:
        print("value error tried")
    except:#it has to be placed at last except
        print("default except block")

# The simplest way to concatenate two dictionaries in python is by using the unpacking operator(**)
if 0:
    dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
    print(dict(**dict_1))
if 0:#merging 2 dictionaries
    dict_1 = {'Media/SFC': [495, 0, 0, 0, 0, 495], 'Media/VE': [274, 50, 0, 0, 0, 224]}
    dict_2 = {'Media/SFC': [495, 0, 0, 0, 0, 495], 'Media/VE': [274, 73, 0, 0, 0, 201]}

    def mergeDictionary(dict_1, dict_2):
       dict_3 = {**dict_1, **dict_2}
       print("dict_3",dict_3)
       for key, value in dict_3.items():
           if key in dict_1 and key in dict_2:
                   dict_3[key] =  dict_1[key]+value
       return dict_3

    dict_3 = mergeDictionary(dict_1, dict_2)
    print(dict_3)

"""
hi
hello
[Tuesday 12:50 PM] Adaveni, PrashanthX
https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe

[Tuesday 12:51 PM] Adaveni, PrashanthX
python-3.8.3-amd64.exe /passive InstallAllUsers=1 PrependPath=1 TargetDir="C:\Python38"

python-3.8.3-amd64

https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.7/npp.8.4.7.Installer.x64.exe

https://www.programiz.com/python-programming

print("hello")
x=9
print(x)
z= x+y+z
https://-string-methods/

s = 'i am practicing the coding for my future'
1.print only 'coding'
2.print ['i', 'am', 'practicing', 'the', 'coding', 'for', 'my', 'future']
3.print i@am@practicing@the@coding@for@my@future
4. find the index value of future
5. reaplace 'a' with 'w'
6.reverse the string
7.count how many 'a' in string
nums="1,2.786"
print(nums)
"""

if 0:#creating the temporary file and deleting after completing the work
    import pandas as pd
    import tempfile
    fo = tempfile.NamedTemporaryFile()
    df =pd.read_excel('My_daily_status.xlsx',sheet_name='Sheet1')
    #print(df)
    print(fo.name+".csv")
    df.to_csv(fo.name+".csv",index=False)
    df1 = pd.read_csv(fo.name+".csv")
    print(df1)

    fo.close()