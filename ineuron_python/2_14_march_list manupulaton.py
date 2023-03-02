#!/usr/bin/env python
# coding: utf-8
l  = ["sudh" , 234,45.56, [45,56,6,"c"] , True]
for i in l :
    print(i)

'''
l[0]
l[::-1]
for i in l :
    if type(i)== list :
        print("this is a list " ,i)
    else :
        print("no element is not a list ", i)
l 
l1= [345,2345, "ineuron" , "tech "]
l + l1
l * 2
len(l)
234  in l
print(max([2,3,4,5,45.56]))
max(["sdfs","sdfs" , 234])
max(["sudh" , "ineruon" , "AI","z"])
min(["fsdfa3434","fsd","fsdfaaaaaaaaa","a" , "A"])
min([2,3,4,5,0])
min("34345",234,234.345,"344")
l = [1,2,3,4]
l.append(6+6j)
l
l
l + "sudh"
l.append("sudh")
l
l = [1,2,3,4,5]
l.append("sudh")
l
l.insert(3,"ineuron")
l
l.insert(-1 , "test")
l
l
l.insert(-1 , "test2")
l
l
l.count("test")
l = [1,2,3,4]
l.append([3,4,7,89])
l
l.append([1,2,4,56])
l
l.extend([3,4,7,89,["sdfusdf",4,5]])
l
s = "test"
list(s)
l 
l.index(3)
l = [2,3,4,5,6,7]
l.pop(0)
l
l = [4,5,6,6,6,6,6,7,8,9]
l.remove(6)
l
l 
l.reverse()
l
l.sort()
l
l = [3,4,5,6,78,"sudh" , "ineuron" , 45.67]
l.sort()
l = [3,4,5,6,78 , 45.67]
l.sort()
l
l = [[1,2,3,4],[5,6,7,"hello",8],[8,7,66],2,6]
l.append([2,3,4])
l.append(8+6j)
l.append([5,6,7])
for i in l:  if type(i) == list:
    for j,v in enumerate(i):
      
      if type(v) == str:
        print("index of string: ",j)
        i[j]="hi"
    print(i[1])
print(l)
l=[[1,2,3],[4,5,6],[7,8,9,'xyz','xyz','xyz'],10, 'vishal', True]
# part1
l.insert(2,[11,12])
l.insert(-1,[13,14])
l.append(12+3j)
for i in l:
    if type(i) == list:
        for j in i:
            if type(j) == str:
                print(l.index(i))
l
l=[[1,2,3],[4,5,6],[7,8,9,'xyz'],10, 'vishal', True]
# part1
l.insert(2,[11,12])
l.insert(-1,[13,14])
l.append(12+3j)
print(l)
# part2
for i in l:
    if type(i) == list:
        for j in i:
            if type(j) == str:
                print(l.index(i))
#part3
for i in l:
    if type(i)==list:
        print(i.pop(2))
l = [[23,45],[6,7,'78S'],'ABC','REV']#Q1l.insert(2,['sdf','sdf'])
print(l)
l.insert(3,[11,12])
print(l)
l.insert(1,(2+3j))
print('After complex number- ',l)
l
#Q2
for i in l:
    if type(i) == list:
        for j in i:
            if type(j) == str:
                print('Found String in Neasted List at index={} : {}'.format(i,j))
                print('Removed',j)
                i.remove(j)print('List after remove ',l)
l=[[1,'2'],[10,11],[20,21],'3',4,5]
c=[1+2j,3+5j]# question 1
l.insert(1,c)
print(f'Updated list: {l}')print()
print()
l=[[1,'2'],[10,11],[20,21],'3',4,5]
c=[1+2j,3+5j]# question 1
l.insert(1,c)
print(f'Updated list: {l}')print()
print()# question 2
for i in l:
    if type(i)==str:
        print(f'String exist is {i}')
        a=l.index(i)
        print(f'Its position is: {a}')
print()
l.remove('3')
print(f'After removing {a} the new list is: {l}')print()
print()# question 3
print('The every second elemnt is:')
for i in l:
    if type(i)==list:
        
        print(i[1])l = [[23,45],[6,7,'78S'],'ABC','REV']#Q1l.insert(2,['sdf','sdf'])
print(l)
l.insert(3,[11,12])
print(l)
l.insert(1,(2+3j))
print('After complex number- ',l)#Q2
for i in l:
    if type(i) == list:
        for j in i:
            if type(j) == str:
                print('Found String in Neasted List at index={} : {}'.format(i,j))
                print('Removed',j)
                i.remove(j)print('List after remove ',l)#Q3
k=1
for i in l:
    if type(i) == list and len(i) >=2:
        print('Neasted List ',k)
        print('2nd element of it is=',i[1])
        k+=1
l = [[1,'a'],[3,4],[5,'b'],1,3,4,5,6]
# Append 2 more list and 1 complex number in between
l.insert(3,6j)
l.insert(4,[7,8])
l.insert(5,[9,0])
print (l)
for i in l:
    if type(i) == list:
        for t in i:
            if type(t) == str:
                print(t)
l1 = [[22,"mahendra",55,22.4],["dhoni",77,11,55,78.9],[77,88,99],2,5,8]l1.insert(2,[2,5,6])
l1.insert(4,[99,"pravin",88,True])
l1.insert(-1,6+4j)
l1
for i in l1:
    if type(i) == list :
        for j in i:
            if type(j) == str :
                print(i.index(j))
                i.remove(j)
l=[["gh",56],[89,"yhg"],["90",98],78,90.0]
for e in l:
    if type(e)==list:
        l.insert(l.index(e)+1,[78,90])
        l.insert(l.index(e)+2,[89,"90","90","90"])
        l.insert(l.index(e)+3,6+7j)
        break
print(l)
for i in l:
    if type(i)==list:
        for e in i:
            if type(e)==str:
                print(f"index of string in nested list of index number {l.index(i)} is {i.index(e)}")
                i.remove(e)
print("new list",l)
l=[["gh",56],[89,"yhg"],["90",98],78,90.0]
for e in l:
    if type(e)==list:
        l.insert(l.index(e)+1,[78,90])
        l.insert(l.index(e)+2,[89,"90"])
        l.insert(l.index(e)+3,6+7j)
        break
print(l)
for i in l:
    if type(i)==list:
        for e in i:
            if type(e)==str:
                print(f"index of string in nested list of index number {l.index(i)} is {i.index(e)}")
                i.remove(e)
print("new list",l)
for i in l:
    if type(i)==list:
        for e in i:
            if len(i)>1:
                i.pop(1)
print("final list",l)l1 = [[22,"mahendra",55,22.4],["dhoni",77,11,55,78.9],[77,88,99],2,5,8]l1.insert(2,[2,5,6])
l1.insert(4,[99,"pravin",88,True])
l1.insert(-1,6+4j)print(l1)for i in l1:
    if type(i) == list :
        for j in i:
            if type(j) == str :
                print(i.index(j))
                i.remove(j)
print(l1)for i in l1 :
    if type(i) == list :
        print(i[2], end = ",")
l = [[1,2,3],[4,5,6],[7,8,9],12,"Santosh"]
l.insert(2,[3,2,1,"test","test","test"])
l.insert(2,[6,5,4])
l.insert(0, 5 + 6j)
print("Q1")
print(l)
for i in range(len(l)):
    if type(l[i]) == list:
        for j in range(len(l[i])):
            if type(l[i][j]) == str:
                print(j)
                del l[i][j]
    if(type(l[i]) == str):
        print(j)
        del l[i]
print("Q2")
print(l)
print("Q3")
for i in range(len(l)):
    if type(l[i]) == list:
        print(l[i][1])
l=[[4,5,"Sameer","Sameer","Sameer"],[346,7,3426,76],[34657,"Jadhav",74557,45,6],23095,'ineuron']
l.append([67,67])
l.append([55,55])
l.insert(3,3+6j)
l
l=[[4,5,"Sameer","Sameer","Sameer"],[346,7,3426,76],[34657,"Jadhav",74557,45,6],23095,'ineuron']
l.append([67,67])
l.append([55,55])
l.insert(3,3+6j)
lfor i in l:
    if type(i)==list:
        for j in i:
            if type(j)== str:
                print (" got {} string at {} location".format(j,i))
                i.remove(j)
                print(i)
# This is 100% working l1 = [[1,2,3],[4,5,6],[7,8,9],'demo',12.5]
l2 = [11,12,'b','b','b']
l3 = [21,'t',223]
# 1)
l1.insert(1,l2)
l1.insert(2,l3)
print("Main List : ",l1)
# 2)for i in l1:
    if type(i)== list:
        for j in i:
            if type(j) == str:
                print("Index : ",i.index(j))
                i.remove(j)
                
# 3) 
for i in l1:
    if type(i)== list:
        print("Second Element : ",i[1])
l1
l1 = [[1,2,3],[4,5,6],[7,8,9],'demo',12.5]
l2 = [11,12,'b','b','b']
l3 = [21,'t',223]
# 1)
l1.insert(1,l2)
l1.insert(2,l3)
l1
l = [[1, 2, 3],
 [11, 12, 'b', 'b', 'b'],
 [21, 't', 223],
 [4, 5, 6],
 [7, 8, 9],
 'demo',
 12.5]
l = [[1, 2, 3],
 [11, 12, 'b', 'b', 'b'],
 [21, 't', 223],
 [4, 5, 6],
 [7, 8, 9],
 'demo',
 12.5]
for i in l:
    if type(i)==str:
        print("Ans 2: ",l.index(i))
        l.pop(l.index(i))
        print(l)
        print("string:",i)
#3b = [el[1] for el in l]
print(b)
l = [[1, 2, 3],
 [11, 12, 'b', 'b', 'b'],
 [21, 't', 223],
 [4, 5, 6],
 [7, 8, 9],
 'demo',
 12.5]li=[]
for i,j in enumerate(l):
    if type(j) == list:
        for k,d in enumerate(j):
            if type(d) == str:
                print('index of string in the list is ',k)
                l[i][k] = 'ccc'
            if k == 1:
                li.append(j[k])
print(l)
li
l
l = [[1, 2, 3],[11, 12, 'b', 'b', 'b'],[21, 't', 223],[4, 5, 6],[7, 8, 9],'demo',12.5]
for i in l:
    b=False
    if type(i) == list:
        a=False
        for j in i:
            if type(j)==str:
                i.remove(j)
                a=True
                break
        if a :
            print(l.index(i))
            l.remove(i)
l
l = [[1, 2, 3],
 [11, 12, 'b', 'b', 'b'],
 [21, 't', 223,44],
 [4, 5, 6],
 [7, 8, 9],
 'demo',
 12.5]#part 2
for sublist in l:
    if isinstance(sublist,list):
           for obj in sublist:
                if isinstance(obj,str):
                    print('Occurance found in sublist',sublist ,' at ',sublist.index(obj))
                    sublist.remove(obj)
                 
    print(sublist)#part 3for i in l:
    if type(i)== list:
        print(i[2])
l
l = []
for i in range(5):
    l.append(int(input()))
print(l)
# input()input()
list(input())
#2. Find the index of string element in the nested list and remove the string
l = [[1, 2, 3],
 [11, 12, 'b', 'b', 'b'],
 [21, 't', 223],
 [4, 5, 6],
 [7, 8, 9],
 'demo',
 12.5]for i in l:
    if type(i) == list:
        j=0
        while j < len(i):
            if type(i[j]) is str:
                print("Index of string {} is :".format(i[j]),j)
            j = j +1
        j=0
        while j < len(i):
            if type(i[j]) is str:
                print("The string in the nested list is '{}'".format(i[j]))
                i.remove(i[j])
                continue
            j = j +1
print("List after removal of string from nested list is\r",l,'')
l = [1,2,3,4,5]
l1 = []
for i in "sudh":
    l1.append(i)
    
l1
[[i] for i in "sudh"]
l = []
for i in range(10) :
    if i%2 ==0:
        l.append(i)
l
[i for i in range(10) if i %2 == 0 ]
8%3
8%2
l = []
for i in range(10):
    if i % 2 != 0:
        l.append("odd")
    else :
        l.append("even")
l
["odd" if i%2 != 0 else "even" for i in range(10)]
mat = []
for i in range(3):
    mat.append([])
    for j in range(3):
        mat[i].append(j)
mat
[[j for j in range(3)]for i in range(3)]
[i for i in range(8) if i % 2 == 0 if i % 3 == 0  ]
l = []
for i in range(8):
    if i % 2 == 0 :
        if i % 3 == 0 :
            l.append(i)
l
l = []
for i in range(10):
    l.append(i)
l
["yes " if i == 1  else "no" if i == 2 else "test " for i in l]
l 
res = []
for i in l :
    if i == 1 :
        res.append("yes")
    elif i ==2 :
        res.append("no")
    else :
        res.append("test")
res'''
