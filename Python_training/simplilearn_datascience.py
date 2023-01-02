
import numpy as np
import pandas as pd
import sys,time
import matplotlib.pyplot as plt


if 0:
    #checking the size comparision of numpy array and list
    if 1:
        # List size
        a = 5
        l = range(1000)
        print(sys.getsizeof(a)*len(l))
    if 1:
        #numpy occupies
        c = np.arange(1000)
        print(c.size)
        print(c.itemsize)
        print(c.size*c.itemsize)

if 0:#checking the time comparision of list and numpy array
    size = 1000000   #Don't take small size
    if 1:#list time
        start = time.time()
        l1= range(size)
        l2 = range(size)
        res = [(x+y) for x,y in zip(l1,l2)]
        print(res)
        print("time taken to compute is", (time.time() - start)*1000)
    if 1:#array time
        start = time.time()
        a1 = np.arange(size)
        a2 = np.arange(size)
        res = a1+a2
        print(res)
        print("time taken to compute is", (time.time() - start)*1000)

if 0:#Features
    if 0:
        a = np.arange(6).reshape(3,2)
        print("array is \n",a)
        print("dimensions",a.ndim)
        print("size of element is ",a.itemsize)
        print("shape is ",a.shape)
        print("datatype is ",a.dtype)
    if 1:
        a = np.arange(6,dtype=np.float64).reshape(3,2)
        print("array is \n", a)
        print("item size is",a.itemsize)

if 0:#types of arrays creation
    z = np.zeros((3,4))
    # print(z)
    o = np.ones((4,3))
    # print(o)
    a = np.arange(5)
    # print(a)
    r = np.random.randn(10)
    # print(r)
    # print(r.shape)
    r = np.random.randn(2,10)
    # print(r)
    # print(r.shape)
    c = np.char.add(['hello','world'],['abc','def'])
    # print(c)
    c = np.char.multiply('hello',3)
    # print(c)
    c = np.char.upper('hello')
    # print(c)
    c = np.char.split('hello world how are you?')
    # print(c)
    c = np.char.splitlines('hello world\nhow are you?')
    # print(c)
    #strip works at the end/beginning
    c = np.char.strip(['ahello','worald','how','are','you?'],'a')
    # print(c)
    #split and join
    c = np.char.join(['-',':'],['YMD','HMS'])
    # print(c)
    c = np.char.replace('hello world how are you?','are','were')
    # print(c)


if 0:#pandas information
    print(pd.__version__)

if 0:#pandas Series creation types
    a = [0,1,2,3,4]
    s1 = pd.Series(a)
    # print(s1)
    #Re naming the index with default values
    order = ['a','b','c','d','e']
    s2 = pd.Series(a,index=order)
    # print(s2)
    n = np.random.randn(5)
    s3 = pd.Series(n,index=order)
    # print(s3)
    d = {1:'a',2:'b',3:'c','d':4,'e':5,'f':6}
    s4 = pd.Series(d)
    # print(s4)
    #modifying the index of series
    s1.index = ['A','B','C','D','E']
    # print(s1)
    #using the method on series
    s5 = pd.Series(['a','b','c',np.nan,'abc','def','COW','DOG'])
    print(s5.str.upper())

if 0:#UPDATE on Series
    a = [0, 1, 2, 3, 4]
    s1 = pd.Series(a)
    order = ['a', 'b', 'c', 'd', 'e']
    s2 = pd.Series(a, index=order)
    # print(s1[:])
    # print(s1[1:])
    # print(s1[:3])
    # Appending the series
    s3 = s1.append(s2) #it is about to expire
    print(s3)
    print(s3.drop('a'))#it is not deleting inplace
    print(s3)

if 0:#Operations on Series
    s1 = pd.Series([2,3,4,1,5,6,7])
    s2 = pd.Series([0,3,4,6,2,5])
    # print(s1.add(s2))
    # print(s1.sub(s2))
    # print(s1.mul(s2))
    # print(s1.div(s2))
    print(s1.median())#middle element after sort if odd elements
    print(s2.median())#avg. of middle elements after sort if length is even
    # print(s1.max())
    # print(s1.min())
    # print("min. value index",s1.argmin())
    # print("max. value index",s1.argmax())

if 0:#DataFrame creation
    dates = pd.date_range('today',periods=6)
    # print(dates)
    np_arr = np.random.randn(6,4)
    # print(np_arr)
    columns = ['a','b','c','d']
    df1 = pd.DataFrame(np_arr,index=dates,columns=columns)
    # print(df1)
    d = {'animal':['dog','cat','horse','donkey','lion','elephant','mouse'],
         'age':[3,2,0,12,23,np.nan,1],
         'visit':['no','yes','yes','no','no','yes','no']}
    labels = ['a','b','c','d','e','f','g']
    df2 = pd.DataFrame(d,index=labels)
    # print(df2)
    # print(df2.head())#printing the first 5
    # print(df2.head(2))#printing the first 2
    # print(df2.tail())#printing the last 5
    # print(df2.tail(2))#printing the last 2

    #printing the row and column names
    # print(df2.index)
    # print(df2.columns)

    #printing the data in np array
    # print(df2.values)

    # printing the statistical data
    # print(df2.describe())

    #transpose the data
    # print(np.transpose(np_arr))
    # print(df2.T)

    #sorting the data
    # print(df2.sort_values(by=['age','animal']))
if 0:#operations
    d = {'animal': ['dog', 'cat', 'horse', 'donkey', 'lion', 'elephant', 'mouse'],
         'age': [3, 2, 0, 12, 23, np.nan, 1],
         'visit': ['no', 'yes', 'yes', 'no', 'no', 'yes', 'no']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    df2 = pd.DataFrame(d, index=labels)
    # slicing the data by rows/columns
    # print(df2[1:4])#slicing by rows
    # print(df2[['age']])#slicing by columns
    # print(df2.iloc[1:3])#slicing by index range
    # print(df2.loc['a':'d'])#slicing by index names
    df2.loc['a','age']=9

    # finding the false/nan values from dataframe
    # print(df2.isnull())
    # print(df2.isna())

    #operations
    # print(df2.mean())
    # print(df2['age'].mean())
    # print(df2['age'].argmin())
    # print(df2['age'].argmax())
    # print(df2.sum())
    #handling the missing values in dataframe
    df3 = df2.copy()
    # print(df3)
    # print(df3.fillna(6))#filling the nan value with 6
    # print(df3.dropna())#drop the rows which are having nan values
if 0:
    d = {'animal': ['dog', 'cat', 'horse', 'donkey', 'lion', 'elephant', 'mouse'],
         'age': [3, 2, 0, 12, 23, np.nan, 1],
         'visit': ['no', 'yes', 'yes', 'no', 'no', 'yes', 'no']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    df3 = pd.DataFrame(d, index=labels)
    print(df3)
    df3.to_csv('animal.csv')
    df4 = pd.read_csv('animal.csv')
    # print(df4)
    df3.to_excel('animal.xlsx',sheet_name='Sheet1')
    df4 = pd.read_excel('animal.xlsx',sheet_name='Sheet1',index_col=None,na_values=['NA'])
    print(df4)

if 0:#plotting
    s1 = pd.Series(np.random.randn(6),index=pd.date_range('today',periods=6))
    print(s1)
    s1.plot()
    plt.show()

if 0:
    df = pd.DataFrame(np.random.randn(50,4),columns=['a','b','c','d'],index=pd.date_range('today',periods=50))
    df.plot()
    plt.show()

