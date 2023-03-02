#!/usr/bin/env python
# coding: utf-8

# In[3]:


notes = 5 
i = 1 
j = 1
while i < notes:
    print(i)
    i += 1
else :
    
    while j < 2 :
        print(i)
        j = j + 1 
    print("no 10 rs notes are available ")


# In[31]:


s = "my name is sudhanshu"


# In[32]:


s


# In[33]:


s[2:-6]


# In[15]:


s[3:10:2]


# In[22]:


s[::-1]


# In[23]:


s[2:-6]


# In[24]:


s = "sudh"


# In[28]:


s[0]


# In[34]:


s


# In[36]:


for i in s :
    if i == 's':
        print(" i got s as a string ")
    print(i)


# In[37]:


s 


# In[42]:


for i in s :
    if i == "n":
        continue 
    print(i)
else :
    if i == 'u':
        print("last char was u ")
    print("this is a else condtion ")


# In[53]:


s =  "ineuron"
ss = ""
for i in range(len(s)):
    if s[i] == "n":
        continue
    else :
        ss = ss + s[i]


# In[54]:


ss


# In[55]:


len(s)


# In[58]:


n = 7 
for i in range(0 ,n):
    for j in range(0 ,i +1):
        print("+ " , end = "")
    print("\r")
    


# In[59]:


def pattern(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           for j in range(0, i+1):
                print("*", end=" ")
           print("\r")
 
pattern(5)


# In[75]:


for i in range(7,0,-1):
    print(i)


# In[60]:


n = int(input('Enter number of rows required: '))

for i in range(n,0,-1):
    for j in range(n-i):
        print(' ', end='') 
    
    for j in range(2*i-1):
        print('*',end='') 
    print()


# In[77]:


for i in range(8, 0, -1):
    print(i)


# In[61]:


num = 5
m = 2 * num - 2
for i in range(num, -1, -1):
    for j in range(m, 0, -1):
        print(end=" ")
    m = m + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")


# In[80]:


" "*5


# In[ ]:





# In[78]:


n =9
i=0
while i < n :
    print(' '*(n-i-1) + '* '*(i+1))
    i +=1


# In[63]:


i=1
k=1 #for printing starts with the increament of 2

while i<=5:
    b=1
    while b<=5-i:
        print(' ',end='')
        b=b+1
        
    j=1
    while j<=k:
        print('*', end='')
        j=j+1
    print()
    
    k=k+2
    
    i=i+1


# In[64]:


userInput = int(input("Please enter the amount of rows: "))

row = 0
while(row < userInput):
    row += 1
    spaces = userInput - row

    spaces_counter = 0
    while(spaces_counter < spaces):
        print(" ", end='')
        spaces_counter += 1

    num_stars = 2*row-1
    while(num_stars > 0):
        print("*", end='')
        num_stars -= 1

    print()
print("**iNeuron-FSDS**")


# In[81]:


l = list()


# In[82]:


name = "sudh"
phno = 543535345
addr = "sdfsff"

name , phno , addr = "sudh " , 54353453,"fgfd"


# In[122]:


l = ["sudh" , 34535,"sfsfsafa", True, 45+8j , [3,5,6,"dfg"],6.787]

len(l)


# In[121]:


range(10)


# In[119]:


list(range(10))


# In[120]:


for  i in range(4,10):
    print(i)


# In[114]:


l[80 :3:1]


# In[107]:


for i in l :
    if type(i) == list:
        n = 0
        for  j in i :
            if type(j) == int :
                n = n + j
        print(n)
                
        print(type(j))


# In[88]:


type(l)


# In[94]:


l1 = []
type(l1)


# In[95]:


l2 = list()
type(l2)


# In[90]:


type(l1)


# In[85]:


l[0]


# In[86]:


l[1]


# In[87]:


l[2]


# In[ ]:




