
import numpy as np
import pandas as pd
import sys,time
import matplotlib.pyplot as plt
from matplotlib import pylab

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

if 0:
    df = pd.DataFrame({'a':[1,2,0,3,9,4,3,2,3,2,8,4,8,5,5,5,6,4,4,6,6]})
    # print(df)
    # print(df.loc[df['a'].shift() != df['a']])#shift will delete consecutive repeated numbers

    df1 = pd.DataFrame({'a': [1, 2, 0, 3, 9, 9, 2, 2, 2, 2, 8, 8, 8, 5, 5, 5, 4, 4, 4, 6, 6]})
    print(df1)
    print(df1.loc[df1['a'].shift() != df1['a']])

if 0:
    x = np.linspace(0, 10, 25)
    y = x * x + 2
    if 0:#creating a graph
        # print(x)
        # print(y)
        # print(np.array([x,y]).reshape(25,2).reshape(2,25))
        pylab.plot(x,y,'b')
        plt.show()
    if 0:#creating the sub graph by splitting the plot area into parts
        pylab.subplot(1,2,1)#splitting the area in to 1 row and 2 columns and plotting at 1st column
        pylab.plot(x, y, 'b')
        plt.show()
    if 0:
        pylab.subplot(1, 2, 2)  # splitting the area in to 1 row and 2 columns and plotting at 2nd column
        pylab.plot(x, y, 'b')
        plt.show()
    if 0:# splitting the area in to 2 row and 2 columns and plotting at 1st row and 2nd column
        pylab.subplot(2, 2, 2)
        pylab.plot(x, y, 'g')
        plt.show()
    if 0:# splitting the area in to 2 row and 2 columns and plotting at 1st row and 2nd column
        pylab.subplot(2, 2, 3)
        pylab.plot(x, y, 'g--')
        plt.show()
    if 0:#plotting sub graphs at a time
        pylab.subplot(2, 2, 3)
        pylab.plot(x, y, 'g--')
        pylab.subplot(2, 2, 2)
        pylab.plot(x, y, 'b')
        plt.show()
    if 0:#plotting sub graphs in single graph
        pylab.subplot(2, 2, 2)
        pylab.plot(x, y, 'g--')
        pylab.subplot(2, 2, 2)
        pylab.plot(y, x, 'b*')
        plt.show()
if 1:
    x = np.linspace(0, 10, 25)
    y = x * x + 2
    if 0:#adjusting the sides of a graph
        fig = plt.figure()
        axis =fig.add_axes([0.1,0.1,0.5,0.5])#left,bottom,width,height
        axis.plot(x,y,'r')
        plt.show()
    if 0:#plotting 2 subgraphs
        fig,axis = plt.subplots(nrows=1,ncols=2)
        axis[0].plot(x,y,'r')
        axis[1].plot(x, y, 'b')
        plt.show()
    if 0:
        fig = plt.figure()
        #adjusting the graph size
        axis1 = fig.add_axes([0.1,0.1,0.8,0.8])
        axis2 = fig.add_axes([0.2,0.5,0.5,0.5])
        #providing the data to the graph
        axis1.plot(x,y,'r')
        axis2.plot(x, y, 'g*')
        plt.show()
    if 0:#this one looks same as below one also
        fig = plt.figure(figsize=(16,9))
        fig.add_subplot()
        plt.plot(x,y,'r')
        plt.show()
    if 0:
        fig = plt.figure(figsize=(16, 9))
        # fig.add_subplot()
        plt.plot(x, y, 'r')
        plt.show()
    if 0:
        fig,axis = plt.subplots(nrows=1,ncols=2)
        axis[0].set_title('title')
        axis[0].set_xlabel('x value')
        axis[0].set_ylabel('y value')
        axis[0].plot(x, y, 'r')
        axis[0].legend(['numpy data'])

        axis[1].set_title('graph')
        axis[1].set_xlabel('x data')
        axis[1].set_ylabel('y data')
        axis[1].plot(x, y, 'g*')
        axis[1].legend(['pandas data'])

        plt.show()
    if 0:
        fig,axis = plt.subplots()
        #adding the x axis,y axis and name of graph
        axis.set_xlabel('x value')
        axis.set_ylabel('y value')
        axis.set_title('data')
        axis.plot(x,x**2,'b')
        axis.plot(x, x ** 3, 'r')
        #adding the legends
        axis.legend(['y = x**2','y=x**3'],loc=2)
        plt.show()

if 0:
    x =np.arange(10)
    fig,axis = plt.subplots()
    if 0:#setting the lables and title for the graph
        axis.set_xlabel('x value')
        axis.set_ylabel('y value')
        axis.set_title('x operations')
        axis.plot(x,x+1)
        axis.plot(x, x + 2)
        axis.plot(x, x + 3)
        plt.show()
    if 0:#adding the legend to the graph
        axis.plot(x, x + 1)
        axis.plot(x, x + 2)
        axis.plot(x, x + 3)
        axis.legend(['y=x+1', 'y=x+2', 'y=x+3'], loc=2)#location of legends corners/sides i.e. loc
        plt.show()
    if 0:#adding colors to the lines
        axis.plot(x,x+1,color='red')
        axis.plot(x,x + 2,color='#112233')
        axis.plot(x, x + 3,color='#FFaa00')
        plt.show()
    if 0:#applying the transparency for the lines
        axis.plot(x, x + 1,alpha=0.5)
        axis.plot(x, x + 2,alpha=0.3)
        axis.plot(x, x + 3, alpha=0.8)
        plt.show()
    if 0:#applying the thickness
        axis.plot(x, x + 1,color='blue', linewidth=0.25)
        axis.plot(x, x + 2,color='blue',linewidth=0.5)
        axis.plot(x, x + 3,color='blue',lw=0.9)
        plt.show()
    if 0:#applying the line style
        axis.plot(x, x + 1,linestyle='--')
        axis.plot(x, x + 2, linestyle='dotted')
        axis.plot(x, x + 3, linestyle='-.')
        line, = axis.plot(x, x + 4, linestyle='-.')
        line.set_dashes([5,10,15,3])
        line1, = axis.plot(x, x + 5, linestyle='-.')
        line1.set_dashes([5, 8, 13, 18])
        plt.show()
    if 0:#applying the marker for lines
        axis.plot(x,x+1,marker='o')
        axis.plot(x, x + 2, marker='+')
        axis.plot(x, x + 3, marker='s')
        axis.plot(x, x + 4, marker='1')
        axis.plot(x, x + 5, marker='2')
        axis.plot(x, x + 6, marker='3')
        axis.plot(x, x + 7, marker='4')
        axis.plot(x, x + 8, marker='o',markersize=10)
        axis.plot(x, x + 9, marker='s', markerfacecolor='red')
        plt.show()
if 0:
    x = np.arange(10)
    fig,axis = plt.subplots(1,2,figsize=(10,5))
    if 1:#applying the grids and limits
        axis[0].plot(x,x**2)
        axis[0].plot(x, x ** 3)
        axis[0].grid(True)
        axis[1].plot(x,x**2,x,x**3,marker='o')
        axis[1].set_xlim([1,5])
        axis[1].set_ylim([1, 40])
        plt.show()

# if 1:#other 2-D graphs
    # df = pd.DataFrame('a':)



