# video lecture 10
# 6th_march_while_loop
# *** in while-else logic, else block execute only when while loop doesnt execute break condition
# In other words, else block execute only when while loop completes all iterations
import logging,sys,re
if 0:
    a = 0
    b = 10.
    while (a< 20):
        a+=1
        print(a)
        if a >= b:
            print("breaking in loop")
            break
    else:
        print("while loop has not broken")


# *** in for-else logic, else block execute only when loop doesnt execute break condition
# In other words, else block execute only when for loop completes all iterations
if 0:
    b = 5
    for i in range(20):
        print(i)
        if i>=b:
            print("break executed")
            break
    else:
        print("break not executed in for loop")


# video lecture 11
# for reference --> 7th march live class notebook for loop while and range function.py
# 7th_march_for loop
# *** in traversal logic, if we travel forward, end has to be added with -1 or if we travel reverse end has
# to be added with +1

if 0:
    #    012345678901
    l = 'master prashanth'
    print("test1",l[2:6])
    print("test2",l[6:2:-1])
    print("test3",l[2:-6])
    print("test4",l[2:-20:-1])
    print(l[-1:10:-3])

if 0:
    rows = 7
    columns = 7
    for i in range(rows):
        print(" "*(i)+"* "*(rows-i))

if 0:
    rows = 7
    columns = 7
    for i in range(rows):
        print(" "*i+(str(i)+" ")*(rows-i))

if 0:
    rows = 5
    columns =(2*rows-1) #  2n-1 formula
    i = 0
    while i<=rows:
        print(" "*(columns-2*i)+"* "*(2*i-1))
        i+=1

if 0: #the code is same as the previous one
    n=9
    i=0
    while i < n:
        print(' '*(n-i-1)+"* "*(i+1))
        i+=2

print(help(re.match))



