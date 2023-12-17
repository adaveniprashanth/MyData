#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 07:11:31 2020

@author: pj
"""
#For reference--> https://numpy.org/doc/stable/reference/index.html
import numpy as np
if 1:  #Numpy arrays
    if 0: #array initialization
    
        arr = np.array([[0, 1, 2], [3, 4, 5]],
                       dtype=np.float32)  #manually casting to float
        # print(repr(arr))
        
        # example of np.array upcasting.
        arr = np.array([0,1,2.])
        print(repr(arr))
        print(arr.dtype)
    
    if 0: # Copying
        a = np.array([0,1,2])
        b = np.array([3,4,5])
        c = a #reffered to same object
        d= b.copy() # it will create  a new object
        print(" A format is {}:".format(repr(a)))
        c[0] = 9
        print(" A format is {}:".format(repr(a)))
        print(" B format is {}:".format(repr(b)))
        d[0]=7
        print(" B format is {}:".format(repr(b)))
    
    if 0: # Casting
        arr = np.array([1,2,3])
        print(arr.dtype)
        arr = arr.astype(np.float64) #casting to np.float64
        print(arr.dtype)
        
    if 0: # NaN, it will be like a placeholder
        arr = np.array([np.nan,1,2])
        print(arr)
        print(arr.dtype)
        arr1 = np.array([np.nan, 'abc'])
        print(arr1)
        print(arr1.dtype)
        #np.nan cannot handle integer type
        # arr2 = np.array([np.nan,2,3],dtype=np.int32)
    
    if 0: #Infinity
        print(np.inf > 100000000)
        print(-np.inf < -100000000)
        
        arr = np.array([np.inf, 2, 3])
        print(repr(arr))
        
        arr1 = np.array([-np.inf, -2])
        print(repr(arr1))
        #inf value will not work on integer tpye
        # arr2 = np.array([np.inf, 2,3],dtype=np.int64)
    if 0: # using lists to create numpy array
        l1= [0,1,2]
        l2 = [3,4,5]
        arr = np.array([l1,l2],dtype=np.int32)
        print(repr(arr))
        print(type(l1))
if 1:#Numpy baiscs
    if 0: #Numpy basics  #Ranged data
        #np.arange(start,stop,step,dtype)
        a = np.arange(24) #ranged data #default is int64 
        print(a)
        print(a.dtype)
        print(a.shape)
        b = np.arange(24,dtype=np.float32)
        # print(repr(b))
        # print(b.dtype)
        b = np.arange(24.1)
        print(repr(b))
        # print(b.dtype)
        c = np.arange(0,12,2)
        print(c)
        c = np.arange(0,12.1,2)
        print(c)
        
    if 0: #linspaced data like stpe data
        #np.linspace(start,stop,num,endpoint,dtype)
        #num <-- no.of values b/w start and stop
        #endpoint=False  <-- Don't consider stop in range values 
        lin1 = np.linspace(0,24)
        print(lin1)
        lin2= np.linspace(0,24,dtype=np.int32) #defaults is  float64
        print(lin2)
        lin3 = np.linspace(0,24,num=6)
        print(lin3)
        lin4 = np.linspace(0,24,num=6,endpoint=False)
        print(lin4)
    
    if 0: #reshaping the data
        #np.reshape(val,(dimension sizes))
        reshaped = np.reshape(np.arange(24),(4,3,2)) #reshaping the ranged data
        # print(reshaped)
        reshaped1=np.reshape(np.arange(24),(-1,2,2)) #-1 is 6 to fit 24 values in array
        # print(reshaped1)
        flattened = reshaped.flatten() # making it as 1-D array
        # print(flattened.shape)
    
    if 0: #Transposed array/exchange dimension sizes
        # np.transpose(array,axes=dimnsion positions) (0,1,2)
        #axes is used to exchange dimension sizes
        reshaped = np.reshape(np.arange(24),(4,3,2))
        print(reshaped.shape)
        transposed = np.transpose(reshaped) #transpose
        # print(transposed.shape)
        changed_axes = np.transpose(transposed, axes=(1,2,0))
        # print(changed_axes)
        # print(changed_axes.shape)
        
    if 0: #zero/ ones column/row matrices
        #np.zeros(row_size,column_size)
        #np.zeros_like(array_with diff.sizes)
        z = np.zeros(5,dtype=np.int32)  #default is float64
        print(z)    
        z1 = np.zeros((5,1),dtype=np.int32)
        print(z1)
        print(np.transpose(z1))
        o = np.ones_like(np.transpose(z))
        print(o)
        print(o.shape)
    
if 1:#Math operations
    if 0: #matrix creations
        arr= np.array([[-0.5,0.8,-0.1],[0.0,-1.2,1.3]])
        # print(repr(arr))
        arr2 = np.array([[1,2],[3,4],[5,6]])
        # print(repr(arr2))
    
    if 0: #arithmetic operations
        arr= np.array([[1,2,3],[4,5,6]])
        arr2 = np.array([[1,2],[3,4],[5,6]])
        multiplied = arr * np.pi
        # print(multiplied)
        added = arr+multiplied
        # print(added)
        added1 = arr2+1
        print(added1)
        squared = added ** 2
        # print("squared is {}".format(squared))
        powered = np.power(3,arr) #np.power(base,power)
        print("powered is {}".format(powered))
        powered1 = np.power(np.array([[1,2],[3,4]]),np.array([[5,6],[7,8]]))
        print(powered1)
    
    if 0: #exp and log operations
        arr= np.array([[1,2,3],[4,5,6]])
        arr2 = np.array([[1,2],[3,4],[5,6]])
        exponential = np.exp(arr)
        print(exponential)
        logged = np.log(arr2) #log with base e
        print(logged)
        logged10 = np.log10(arr2) #log with base 10
        print(logged10)
        
    if 0: #multiplication operations
        a= np.array([1,2,3])
        a1 = np.array([4,5,6])
        # when both are 1-D arrays, output is dot product.
        print(np.matmul(a,a1))
        arr= np.array([[1,2,3],[4,5,6]])
        arr2 = np.array([[1,2],[3,4],[5,6]])
        matmul1 = np.matmul(arr,arr2)
        print(matmul1)
        matmul2 = np.matmul(arr2,arr)
        print(matmul2)
    
    if 0: #function usage
        farenheat = np.array([[100,200,300],[400,500,600]])
        def ftc(temps):
            return (5/9)*(temps-32)
        celcius = ftc(farenheat)
        print(celcius)
        
if 1: #Random operations
    if 0:#Random integers
        #np.random.randint(lower,high,size=shape,dtype)
        a = np.random.randint(5)
        print(a)
        b = np.random.randint(1,high=10) # low to (n-1)
        print(b)
        arr1 = np.random.randint(1, high=10,size=(1,5))
        print(repr(arr1))
        arr2 = np.random.randint(1, high=10,size=(2,5))
        print(repr(arr2))
        arr3 = np.random.randint(1, high=10,size=(2,5,3))
        print(repr(arr3))
        print(np.arange(30).reshape(2,5,3))

    if 0: #Distribution functions
        #np.random.randint(low,high,size=shape) <--uniform
        # print(np.random.uniform())
        uniform = np.random.uniform(0,24,size=6)
        #print(uniform)
        
        #np.random.normal(loc,scale,size=shape)
        #              ||
        #              ||
        #np.random.normal(mean,deviation,size=shape)
        # print(np.random.normal())
        random_norm = np.random.normal(2.0,3.5,size=(10,5))
        #print(random_norm)
        
        #own choice distribution
        #np.random.choice(array,p=[total sum = 1],size=shape)
        choices = ['a','b','c','d']
        choice1 = np.random.choice(choices,p=[0.5,0.1,0.2,0.2])
        print(choice1)
        choice2 = np.random.choice(choices,p=[0.5,0.1,0.2,0.2],size=(2,2))
        print(choice2)
    
    if 0:#Utility functions
        #np.random.seed(0) <-- to fix the value of random function output
        # print(np.random.randint(1,high=10,size=(3,3,3))) # O/P changes for 1st execution
        # print(np.random.seed(2)) <-- to freeze the O/P of random functions
        # print(np.random.randint(1,high=10,size=(3,3,3))) # O/P fixed
        
        #np.random.shuffle(array) <-- for more than 1-D shuffles 1-D only 
        arr = [1,2,3,4,5]
        np.random.shuffle(arr)
        print(arr)
        arr2 = np.arange(27).reshape(3,3,3)
        print(arr2)
        np.random.shuffle(arr2)
        print(arr2)

if 1:#Indexing 
    if 0:#array slicing
        arr1= np.arange(3)
        # print(arr1)
        arr2 = np.arange(9).reshape(3,3)
        # print(arr2)
        arr3 = np.arange(27).reshape(3,3,3)
        # print(arr3)
        
        # print(arr2[:,2:])     #<--check this
        # print(type(arr2[:,2:]))
        # print(arr2[:, -1])    # and this also
        # print(type(arr2[:, -1]))
        # print(arr2[:,2:][0])
        # print(type(arr2[:,2:][0]))
        # print(arr2[:, -1][1])  #at last dimension  we are giving value instead of slicing
        # print(type(arr2[:, -1][1]))
        # print(arr2[:, -2:-1])
        
        print(type(arr3[:,:,-2][0][0]))
        print(arr3[:,:,-2])
        print(arr3[:,:,-2][0])
        print(arr3[:,:,-2][0][0])
    if 0: #argmin and argmax  <-- returns index value
        arr2 = np.array(
       [[3, 9, 4],
        [2, 1, 4],
        [7, 8, 7]])
        print(arr2)
        
        arr3 = np.array(
      [[[3, 9, 4],
        [2, 1, 4],
        [7, 8, 7]],

       [[4, 6, 4],
        [3, 2, 6],
        [3, 9, 7]],

       [[9, 2, 4],
        [6, 8, 7],
        [1, 3, 8]]])
        
        # print(np.argmin(arr2)) # returns min value index
        # print(np.argmin(arr2,axis = 0))  #returns the min. value index from upper dimension
        # print(np.argmin(arr2,axis = 1))  #returns the min. value index from (upper-1) dimension
        
        print(np.argmin(arr3))
        print(np.argmin(arr3,axis=0))# taking elements from the index posistion of result and comparing ex: min(3,4,9) position is 0
        print()
        print(np.argmin(arr3,axis=1))# taking elements from the index posistion of result and comparing ex: min(3,2,7) position is 1
        print()
        print(np.argmin(arr3,axis=2))# taking elements from the index posistion of result and comparing ex: min(3,9,4) position is 0
        print()
        print(np.argmin(arr3,axis=-1))# taking elements from the index posistion of result and comparing here axis =-1 means last dimension
    
if 1: #Filtering
    if 0:#Filtering data
        arr1 = np.random.randint(-3,high=5,size=(3,3))
        # print("random integers array\n {}".format(arr1))
        
        arr2 = np.array([[ 4, -2, -2],
                         [ 2, -1,  1],
                         [ 0,  1,  1]])
        print(arr2)
        print(repr(arr2 >2))#checks every element with the condition
        # print(arr2 == 0)
        # print(arr2 != 0)
        # print(~(arr2 == 0)) # ==  <==> ~(!=)
        
        # arr = np.array([[0, 2, np.nan],
        #         [1, np.nan, -6],
        #         [np.nan, -2, 1]])
        # print("checking np.nan is present\n {}".format(np.isnan(arr)))
    
    
    if 0:#Filtering in numpy --> np.where(filter_condition, True_replacements, False_replacements)
        
        print(repr(np.where([True, False, True]))) #checks positions  of True values and returns a tuple of 1-D array indices values.
        
        # arr1 = np.random.randint(-3,high=5,size=(3,3))
        # print("random integers array\n {}".format(arr1))
        
        arr = np.array([[ 2,  3,  2],[-2,  1,  4],[ 1, -2, 0]])
        print(arr)
        np_filter = arr > 0
        print(np_filter) # 2-D array
        a = np.where(np_filter) # returns tuple with True value indices w.r.to dimensions
        print(a)
        x_ind,y_ind = np.where(np_filter)
        print(arr[x_ind,y_ind])# printing values whihc satisfies the filter condition
        
        np_filter = np.array([[True, False], [False, True]])
        positives = np.array([[1, 2], [3, 4]])
        negatives = np.array([[-2, -5], [-1, -8]])
        a = np.where(np_filter, positives, negatives) # returns array with values where True filter positions replace with positive values and vice versa.
        print(a) # +ve array values and -ve array values replace based on filter values
        
        np_filter = np.array([[True, False], [False, True]])
        positives = np.array([[1, 2], [3, 4]])
        print(repr(np.where(np_filter, positives, -1)))
    
    if 0:#use of np.any(condition), np.all(condition)
        arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
        print(repr(arr > 0))
        print(np.any(arr > 0)) #returns True if any one value satisfies
        print(np.all(arr > 0)) #returns False if any one value not satisfies
    
    if 0:#axis-wise Filtering
        arr = np.array([
                [-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])
        # print(np.any(arr > 0, axis=0))# checking upper dimension values 
        # print(np.any(arr > 0, axis=1))#checking upper-1 dimension values 
        # print(np.any(arr > 0, axis=-1))
        
        #code to find rows at least have one +ve value in it
        np_filter = np.any(arr >0, axis=1)
        print(np_filter) #finding whihch rows have at least one +ve value
        print(np.where(np_filter))# finding rows positions
        print(arr[np.where(np_filter)])# printing rows wihc have at least one +ve value
    
    if 0: #function usage
        data = np.arange(9,18).reshape(3,3)
        print(data.shape)
        def coin_flip_filter(data):
            coin_flips = np.random.randint(2,size=data.shape) #probability
            bool_coin_flips = coin_flips.astype(np.bool) #condition
            one_replace = np.where(bool_coin_flips,data,1)
            return one_replace
        a = coin_flip_filter(data)
        print(a)
if 1: #Statistics
    if 0:#Analysis #array.min(axis_value)  #array.max(axis_value)
        # arr = np.random.randint(-3,high=50,size=(3,3))
        # print(arr)
        arr1 = np.array([
            [19, 18, 13],
            [42, -2,  6],
            [30, 11,  5]])
        print(arr1)
        
        print(arr1.min())#returns the min.value in the whole array
        print(arr1.max())
        print(arr1.min(axis=0))#returns the min.values in the upper dimensions
        print(arr1.max(axis=1))#returns the min.values in the upper-1 dimensions
    if 0:#statistical methods #np.mean(array,axis_value) #np.var(array,axis_value)
        arr1 = np.array([
            [19, 18, 13],
            [42, -2,  6],
            [30, 11,  5]])
        print(arr1)
        
        print(np.mean(arr1)) # returns the mean value of total array elements
        print(np.var(arr1))
        print(np.median(arr1))#Note that np.median applied without axis takes the median of the flattened array. i.e center value of flattered array.
        
        print(np.median(arr1,axis=1))
        print(np.mean(arr1,axis=0))
if 1: #Aggregation
    if 0:#Summation
        arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])
        print(np.sum(arr)) #sum of total elements of whole array
        print(repr(np.sum(arr, axis=0)))#sum of elements of columns
        print(repr(np.sum(arr, axis=1)))#sum of elements of rows
        print()
        print(repr(np.cumsum(arr)))
        print(repr(np.cumsum(arr, axis=0)))
        print(repr(np.cumsum(arr, axis=1)))
    
    if 0:#Concatenation like combining multiple arrays into one array
            #np.concatenate(list of arrays,axis) i.e [arr1,arr2,arr3]
        arr1 = np.array([[0, 72, 3],
                 [1, 3, -60],
                 [-3, -2, 4]])
        arr2 = np.array([[-15, 6, 1],
                 [8, 9, -4],
                 [5, -21, 18]])
        
        print(repr(np.concatenate([arr1, arr2]))) #default axis = 0 it means adding arrays vertically
        print(repr(np.concatenate([arr1, arr2], axis=1)))#adding arrays horizontally
        print(repr(np.concatenate([arr2, arr1], axis=1)))
if 1:#saving data
    if 0:#Saving
        arr = np.random.uniform(0,9,size=(3,3,3))
        np.save('array.npy',arr)#saving the array in "array.npy" file
        np.save('array1',arr)# not mandatory for format
        
        #now loading
        load_arr = np.load('array.npy')#format is compulsary
        print(load_arr)
        load_arr1 = np.load('array1.npy')
        print("\nloaded array is \n{}".format(load_arr1))

# Kaggle questions --> https://www.kaggle.com/code/utsav15/100-numpy-exercises
if 1: #Create a 2d array with 1 on the border and 0 inside
    if 0:
        Z = np.ones((10, 10))
        Z[1:-1, 1:-1] = 0
        print(Z)
    if 0: #need to work on this
        z=np.zeros((10,10))
        z[0:,0]=1
        z[-1,-1:]=1
        print(z)

if 0: #How to add a border (filled with 0's) around an existing array?
    if 1:
        a = np.ones((5, 5))
        a = np.pad(a, pad_width=1, mode='constant', constant_values=0)
        print(a)
    if 0:
        a=np.ones((5,5))
        a=np.pad(a,pad_width=2,mode='constant',constant_values=[1,2])
        print(a)

if 0:
    print(0 * np.nan)
    print(np.nan == np.nan)
    print(np.inf > np.nan)
    print(np.nan - np.nan)
    print(np.nan in set([np.nan]))
    print(0.3 == 3 * 0.1)
    print(0.3)
    print(3*0.1)

if 1: #Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
    if 0:
        a = np.diag(1 + np.arange(4), k=1)  # moving the values just above the diagonal
        print(a)
    if 0:
        a = np.diag(1 + np.arange(4),k=-1)#moving the values just below the diagonal
        print(a)
    if 0:
        a = np.diag(1+np.arange(4)) #adding value to the elemnets
        print(a)
    if 0:
        a=np.diag(np.arange(4))
        print(a)

if 1: #Create a 8x8 matrix and fill it with a checkerboard pattern
    if 1:
        if 0:
            a = np.zeros((8, 8))
            a[1::2,::2]=1
            a[::2,1::2]=1
            print(a)
        if 0:
            a = np.zeros((8, 8))
            a[1::2,::2]=1
            print(a)
        if 0:
            a = np.zeros((8, 8))
            a[1::2]=1
            print(a)
        if 0:
            a=np.zeros((8,8))
            print(a)
    if 0:
        if 1:
            a=np.ones((8,8))
            a[1::2,::2]=0
            a[::2,1::2] =0
            print(a)
        if 0:
            a=np.ones((8,8))
            a[1::2,::2]=0
            print(a)
        if 0:
            a=np.ones((8,8))
            print(a)

if 0: #Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
    if 1:
        a=np.arange(6*7*8).reshape((6,7,8))
        index=np.unravel_index(10,a.shape)#getting the position of 100(any value) in array
        print(index)
    if 0:
        a=np.arange(6*7*8).reshape((6,7,8))
        print(a)

#Create a checkerboard 8x8 matrix using the tile function
if 1:
    if 1:
        a=np.tile(np.array([[1,0],[0,1]]),(4,4))
        print(a)
    if 0:
        a=np.tile(np.array([[1,0],[0,1]]),(2,2))
        print(a)
    if 0:
        a=np.tile(np.array([[1,0],[0,1]]),(2,1))
        print(a)
    if 0:
        a=np.tile(np.array([[1,0],[0,1]]),(1,1))
        print(a)

if 0: #Normalize a 5x5 random matrix
    # normalization = (val-mean)/std
    if 0:
        a=np.arange(25).reshape((5,5))
        norm = (a-a.mean())/a.std()
        print(norm)
    if 0:
        a=np.arange(25).reshape((5,5))
        difference = a-a.mean()
        print(difference)
    if 0:
        a=np.arange(25).reshape((5,5))
        print(a)

if 0: #Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
    if 0:
        res= np.dot(np.ones((5,3)),np.ones((3,2)))
        print(res)
    if 1:
        res = np.ones((5,3)) @ np.ones((3,2))
        print(res)

if 0: # Given a 1D array, negate all elements which are between 3 and 8, in place.
    if 0:
        a=np.arange(11)
        a[(3<=a) & (a<=8)]*=-1
        print(a)
    if 0:
        a=np.arange(11)
        a[3<a]*=-1
        print(a)
    if 0:
        a=np.arange(11)
        a*=-1
        print(a)

if 0:
    if 0:
        print(sum(range(5), -1)) #here -1 will be added to the sum
        from numpy import *
        print(sum(range(5), -1)) #here -1 will be used for axis value handling
    if 1:
        from numpy import *
        a =sum(range(5))
        print(a)
    if 1:
        a =sum(range(5))
        print(a)

if 0:
    if 0:
        a = np.arange(5)
        print(a)
        print(a**a)
    if 0:
        a=np.arange(-5,5)
        print(a)
        print(a ** a) #negative powers are not allowed

if 0: #RuntimeWarning
    print(np.array(0) / np.array(0))
    print(np.array(0) // np.array(0))
    print(np.array([np.nan]).astype(int).astype(float))

if 0: #How to find common values between two arrays?
    if 1:
        a=np.arange(0,10).reshape((2,5))
        b=np.arange(5,15).reshape((2,5))
        res= np.intersect1d
        print(res)
    if 0:
        a=np.arange(0,10)
        b=np.arange(5,15)
        res= np.intersect1d(a,b)
        print(res)

if 0:
    defaults = np.seterr(all="ignore")#ignoring the all warnings
    print(np.sqrt(-1) == np.emath.sqrt(-1))

if 0: #How to get the dates of yesterday, today and tomorrow?
    today=np.datetime64('today','D')
    print(today)
    yesterday = np.datetime64('today','D')-np.timedelta64(1,'D')
    print(yesterday)
    tomorrow = np.datetime64('today','D')+np.timedelta64(1,'D')
    print(tomorrow)

if 0: #How to get all the dates corresponding to the month of July 2016?
    dates=np.arange('2016-07','2016-08',dtype='datetime64[D]')
    print(dates)

if 0: #How to compute ((A+B)*(-A/2)) in place (without copy)?
    A=np.ones(3)*1
    B=np.ones(3)*2
    C = np.ones(3) * 3
    print(A)
    np.add(A,B,out=B)
    np.divide(A, 2, out=A)
    np.negative(A, out=A)
    np.multiply(A, B, out=A)
    print(A)

if 0: #Extract the integer part of a random array using 5 different methods
    a=np.random.uniform(0,10,10)
    print(a)

if 0:# Create a 5x5 matrix with row values ranging from 0 to 4
    if 0:
        a= np.zeros((5,5))
        a+=np.arange(5)
        print(a)
    if 0:
        a= np.zeros((5,5))
        a+=5
        print(a)
    if 0:
        a= np.zeros((5,5))
        print(a)

if 0:#Consider a generator function that generates 10 integers and use it to build an array
    def gen():
        for i in range(10):
            yield i
    if 0:
        a=np.fromiter(gen(),dtype=np.int64,count=-1)
        print(a)

    if 0:
        a=np.fromiter(gen(),dtype=np.int64)
        print(a)

if 0:#Create a vector of size 10 with values ranging from 0 to 1, both excluded
    if 0:
        a=np.linspace(0,1,11,endpoint=False)[1:]#removing the first value
        print(a)
        print(a.shape)
    if 0:
        a=np.linspace(0,1,11,endpoint=False)#removing the last value i.e 1
        print(a)
        print(a.shape)
    if 0:
        a=np.linspace(0,1,11) #array with 11 values
        print(a)
        print(a.shape)
    if 0:
        a=np.linspace(0,1)#array with 50values
        print(a)
        print(a.shape)

if 0:#Create a random vector of size 10 and sort it
    if 0:
        a=np.random.random(10)
        a.sort()
        print(a)
    if 0:
        a=np.random.random(10)
        print(a)
    if 0:
        a=np.random.random()
        print(a)

if 0:#How to sum a small array faster than np.sum?
    if 1:
        a=np.arange(10)
        a=np.add.reduce(a)
        print(a)

if 0:#Consider two random array A and B, check if they are equal
    if 1:
        a = np.random.randint(0, 2, 5)
        b = np.random.randint(0, 2, 5)
        print(a)
        print(b)
        res= np.array_equal(a,b)#Checking both the shape and the element values, no tolerance (values have to be exactly equal)
        print(res)
    if 0:
        a = np.random.randint(0, 2, 5)
        b = np.random.randint(0, 2, 5)
        print(a)
        print(b)
        res= np.allclose(a,b)#check identical shape of the arrays and a tolerance for the comparison of values
        print(res)

    if 1:
        a = np.random.randint(0, 2, 5)
        b = np.random.randint(0, 2, 5)
        print(a)
        print(b)
        print(a == b)  # values comparision

if 0:#Make an array immutable (read-only)
    a=np.arange(10).reshape((2,5))
    print(a)
    a[0,1]=100
    print(a)
    a.flags.writeable=False #making it as read-only
    a[:,1]=400
    print(a)

if 0:#Consider a 10x2 matrix representing cartesian coordinates, convert them to polar coordinates
    if 1:
        a=np.arange(20).reshape((10,2))
        x=a[:,0];y=a[:,1]
        r= np.sqrt(x**2+y**2)
        t=np.arctan2(y,x)
        print(r)
        print(t)
    if 0:
        a=np.arange(20).reshape((10,2))
        x=a[:,0];y=a[:,1]
        print(x);print(y)
    if 0:
        a=np.arange(20).reshape((10,2))
        print(a)

#Create random vector of size 10 and replace the maximum value by 0
if 0:
    if 1:
        a = np.random.random(10)
        print(a)
        v = np.argmax(a)
        a[v]=0
        print(a)
    if 0:
        a=np.random.random(10)
        v=np.argmax(a)#position of max value
        print(a)
        print(v)
    if 0:
        a=np.random.random(10)
        print(a)

# Create a structured array with x and y coordinates covering the [0,1]x[0,1] area
if 0:
    if 0:
        a=np.zeros((5,5),[('x',float),('y',float)])
        a['x'],a['y']=np.meshgrid(np.linspace(0,1,5),np.linspace(0,1,5))
        print(a)
    if 0:
        a,b=np.meshgrid(np.linspace(0,1,5),np.linspace(0,1,5))
        print(a)
        print(b)
    if 0:
        a=np.zeros((5,5),[('x',float),('y',float)])
        print(a)
    if 0:
        a=np.zeros((5,5))
        print(a)

# Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))
if 0:
    if 0:
        a=np.arange(8)
        b = a+0.5
        c=1/np.subtract.outer(a,b)
        print(np.linalg.det(c))
    if 0:
        a=np.arange(5)
        b = a+2
        c=1/np.subtract.outer(a,b)
        print(c)
    if 0:
        a=np.arange(5)
        b = a+2
        print(a)
        print(b)
        c=np.outer(a,b)
        print(c)
    if 0:
        a=np.arange(5)
        b = a+2
        c=1/np.subtract(a,b)
        print(c)
    if 0:
        a=np.arange(5)
        b = a+2
        c=np.subtract(a,b)
        print(c)

# Print the minimum and maximum representable value for each numpy scalar type
if 0:
    #for integers
    for d in [np.int8,np.int32,np.int64]:
        print(d)
        print(np.iinfo(d).min)#min value for this type
        print(np.iinfo(d).max)#max value for this type

    # for float values
    for d in [np.float32,np.float64]:
        print(d)
        print(np.finfo(d).min)  # min value for this type
        print(np.finfo(d).max)  # max value for this type

#  How to print all the values of an array?
if 0:
    if 0:
        np.set_printoptions(threshold=np.inf)#making to display all values in the array
        a=np.arange(16*16).reshape((16,16))
        print(a)
    if 0:
        a=np.arange(16*16).reshape((16,16))
        print(a)

# How to find the closest value (to a given scalar) in a vector?
if 0:
    if 1:
        a=np.arange(100)
        v= np.random.randint(100)
        index=np.abs(a-v).argmin()
        print(a[index])
        print(v)
    if 0:
        a=np.arange(100)
        v= np.random.randint(100)
        res=np.abs(a-v)
        print(res)
        print(v)
    if 0:
        a=np.arange(100)
        v= np.random.randint(100)
        print(v)

# Create a structured array representing a position (x,y) and a color (r,g,b)
if 0:
    if 0:
        a = np.zeros(10,[('position',[('x',float),('y',float)]),('color',[('r',float),('g',float),('b',float)])])
        print(a)
    if 0:
        a=np.zeros(10)
        print(a)

# Consider a random vector with shape (100,2) representing coordinates, find point by point distances
if 0:
    if 0:
        a=np.arange(10).reshape((5,2))
        x,y=np.atleast_2d(a[:,0],a[:,1])
        distance=np.sqrt((x-x.T)**2+(y-y.T)**2)
        print(distance)
    if 0:
        a=np.arange(20).reshape((10,2))
        b,c=np.atleast_2d(a[:,0],a[:,1])
        print(b,b.shape)
        print(c)

# How to convert a float (32 bits) array into an integer (32 bits) in place?
if 0:
    if 1:
        a = np.arange(10, dtype=np.float32)
        a.astype(np.int32,copy=False) #inplace means replacing the value at its place
        print(a)

    if 0:
        a=np.arange(10,dtype=np.float32)
        b=a.astype(np.int32)
        print(a)
        print(b)

if 0:
    from io import StringIO
    if 0:
        s= StringIO("""1,2,3,4\n
                        6,,7,8\n
                        , , 10,11\n """)
        a=np.genfromtxt(s,delimiter=",")
        print(a)
    if 0:
        s= StringIO("""1,2,3,4,5\n
                        6,,7,8,9\n
                        , , 10,11\n """)
        print(type(s))

#  What is the equivalent of enumerate for numpy arrays?
if 0:
    if 1:
        a = np.arange(9).reshape((3, 3))
        for index in np.ndindex(a.shape):
            print(index,a[index])
    if 0:
        a=np.arange(9).reshape((3,3))
        for index,value in np.ndenumerate(a):
            print(index,value)
    if 0:
        a=np.arange(9).reshape((3,3))
        print(a)

# How to randomly place p elements in a 2D array?
if 0:
    if 0:
        a=np.zeros((5,5))
        np.put(a,np.random.choice(range(5*5),5),1)#replacing at 5 locations with 1
        print(a)
    if 0:
        print(np.random.choice(range(5*5),3))#collecting the 3 random values between 0 to 24
    if 0:
        print(np.random.choice(range(5*5)))
    if 0:
        a=np.zeros((5,5))
        print(a)

# Subtract the mean of each row of a matrix
if 0:
    if 0:
        a=np.arange(30).reshape((5,6))
        mean_value=a-np.mean(a,keepdims=True)
        print(mean_value)
    if 0:#mean of all rows
        a=np.arange(30).reshape((5,6))
        mean_value=np.mean(a,axis=1)
        print(mean_value)
    if 0:#mean of all columns
        a=np.arange(30).reshape((5,6))
        mean_value=np.mean(a,axis=0)
        print(mean_value)
    if 0:#mean of total array
        a=np.arange(30).reshape((5,6))
        mean_value=np.mean(a)
        print(mean_value)
    if 0:
        a=np.arange(30).reshape((5,6))
        print(a)

#  How to sort an array by the nth column?
if 0:
    if 0:
        a = np.random.randint(1, 25, (4, 4))
        print(a)
        print(a[a[:,1].argsort()])
    if 0:
        a = np.random.randint(1, 25, (4, 4))
        print(a)
        print(a[[0,3,2,1]])
    if 0:
        a=np.random.randint(1,25,(4,4))
        print(a)
        print(a[:, 1])
        print(a[:,1].argsort())

    if 0:
        a=np.random.randint(1,25,(4,4))
        print(a)
        print(a.argsort())#argsort will returns the index after sorting but it will not sort the array
    if 0:
        a=np.random.randint(1,10,(3,3))
        print(a)
        a.sort(axis=1)#sorted based on rows
        print(a)
    if 0:
        a=np.random.randint(1,10,(3,3))
        a.sort()#sorted based on columns
        print(a)
    if 0:
        a=np.random.randint(1,10,(3,3))
        print(a)

# How to tell if a given 2D array has null columns?i.e column having all 0's
if 0:
    if 0:
        a=np.random.randint(0,2,(3,10))
        print(a)
        print(~a.any(axis=0))#checks for any column having 0's
        print((~a.any(axis=0)).any())
    if 0:
        a=np.random.randint(0,2,(3,10))
        print(a)
        print(a.any(axis=0))
        print(~a.any(axis=0))
    if 0:
        a=np.random.randint(0,3,(3,10))
        print(a)
        print(a.any(axis=0))#checking any column is having all 0's
    if 0:
        a=np.random.randint(0,3,(3,10))
        print(a)

# Find the nearest value from a given value in an array
if 0:
    if 1:
        a = np.random.uniform(0, 1, (2, 4))
        print(a)
        given_value=0.7
        print(np.abs(a - given_value))
        print(np.abs(a-given_value).argmin())
        print(a.flat[np.abs(a-given_value).argmin()])
    if 0:
        a=np.random.uniform(0,1,(2,4))
        print(a)
        print(a.flatten())
        print(a.flat[2])#gives the index2 item after the falttering the array
    if 0:
        a=np.random.uniform(0,1,10)
        print(a)
        print(np.abs(a-0.5))
        print(np.abs(a - 0.5).argmin())
    if 0:
        a=np.random.uniform(0,1,10)
        print(a)
        print(np.abs(a-0.5))
    if 0:
        a=np.random.uniform(0,1,10)
        print(a)

# Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator?
if 0:
    if 1:
        a=np.arange(3).reshape(1,3)
        b = np.arange(3).reshape(3,1)
        it =np.nditer([a,b,None])#create an iterator
        print(it)
        for x,y,z in it:
            z[...]=x+y
        print(it.operands)
        print(it.operands[0])
        print(it.operands[1])
        print(it.operands[2])
    if 0:
        a=np.arange(3).reshape(1,3)
        b = np.arange(3).reshape(3,1)
        it =np.nditer([a,b,None])
        print(it)
        for x,y,z in it:
            z[...]=x+y
        print(it.operands)
    if 0:
        a=np.arange(3).reshape(1,3)
        b = np.arange(3).reshape(3,1)
        it =np.nditer([a,b,None])
        for x,y,z in it:
            z[...]=x+y
    if 0:
        a=np.arange(3).reshape(1,3)
        b = np.arange(3).reshape(3,1)
        it =np.nditer([a,b,None])
        for x,y,z in it:
            print(x,y,z)
    if 0:
        a=np.arange(3).reshape(1,3)
        b = np.arange(3).reshape(3,1)
        it =np.nditer([a,b,None])
        for i in it:
            print(i)
    if 0:
        a=np.arange(3).reshape(1,3)
        b = np.arange(3).reshape(3,1)
        print(a)

# Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)?
# i.e count the elemnts in a vector of the array indexes and add 1 to the count
if 0:
    if 1:
        ones_array = np.ones(10, dtype=np.int64)
        print(ones_array)
        random_array= np.random.randint(0, len(ones_array), 20)
        print(random_array)
        count_of_occurances=np.bincount(random_array,minlength=len(ones_array))
        print(count_of_occurances)
        count_of_occurances+=ones_array
        print(count_of_occurances)
    if 0:
        ones_array = np.ones(10, dtype=np.int64)
        random_array= np.random.randint(0, len(ones_array), 20)
        print(random_array)
        count_of_occurances = np.bincount(random_array,minlength=20)
        print(count_of_occurances)
        count_of_occurances = np.bincount(random_array, minlength=15)
        print(count_of_occurances)
        count_of_occurances = np.bincount(random_array, minlength=5)
        print(count_of_occurances)
    if 0:
        b=np.random.randint(0,10,20)
        print(b)
        c=np.bincount(b)#Each bin gives the number of occurrences of its index value in `x`.
        print(c)
    if 0:
        a=np.ones(10,dtype=np.int64)
        print(a)
        b=np.random.randint(0,len(a),20)
        print(b)

# Considering a four dimensions array, how to get sum over the last two axis at once?
if 0:
    if 1:
        array=np.arange(3*4*3*4).reshape((3,4,3,4))
        print(array)
        print(array.sum(axis=(-2,-1)))
    if 0:
        array=np.arange(3*4*3*4).reshape((3,4,3,4))
        print(array)
        print(array.sum())
    if 0:
        array=np.random.randint(0,10,(3,4,3,4))
        print(array)

# How to get the diagonal of a dot product?
if 0:
    if 1:
        a = np.arange(9).reshape((3, 3))
        b = np.arange(9).reshape((3, 3))
        dot_product=np.dot(a, b)
        print(dot_product)
        print(np.diag(dot_product))
    if 0:
        a=np.arange(9).reshape((3,3))
        print(a)
        print(np.diag(a))
    if 0:
        a=np.arange(9).reshape((3,3))
        b = np.arange(9).reshape((3, 3))
        print(a)
        print(np.dot(a,b))

# Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value?
if 0:
    if 1:
        array = np.arange(5)+1
        consecutive_position = 3
        zeros_vector = np.zeros(len(array) + (len(array) - 1) * (consecutive_position))
        zeros_vector[::consecutive_position+1]=array
        print(zeros_vector)
    if 0:
        array=np.arange(5)
        print(array)
        consecutive_position=3
        zeros_vector=np.zeros(len(array) + (len(array)-1)*(consecutive_position))
        total= len(array) + (len(array)-1)*(consecutive_position)
        print(total)
        print(zeros_vector)

# Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)?
if 0:
    A = np.ones((5, 5, 3))
    B = 2 * np.ones((5, 5))
    print(A * B[:, :, None])#last axis is None

# How to swap two rows of an array?
if 0:
    if 0:
        a=np.arange(20).reshape((4,5))
        print(a)
        a[[0,1]]=a[[1,0]]
        print(a)
    if 0:
        a=np.arange(20).reshape((4,5))
        print(a)
        print(a[0])
        print(a[[0,1]])
    if 0:
        a=np.arange(20).reshape((4,5))
        print(a)

# How to swap two columns of an array?
if 0:
    if 0:
        a=np.arange(20).reshape((4,5))
        print(a)
        a[:,[0,1]]=a[:,[1,0]]
        print(a)
    if 0:
        a=np.arange(20).reshape((4,5))
        print(a)
        print(a[:,[0,1]])
    if 0:
        a=np.arange(20).reshape((4,5))
        print(a)

# Given an array C that is a bincount, how to produce an array A such that np.bincount(A) == C?
if 0:
    if 1:
        a=np.random.randint(0,10,(10))
        print(a)
        bincount=np.bincount(a)
        print(bincount)
        result=np.repeat(np.arange(len(a)),bincount)
        print(result)
    if 0:
        a=np.random.randint(0,10,(10))
        print(a)
        bincount=np.bincount(a)
        print(bincount)
    if 0:
        a=np.arange(10)
        print(a)
        c=np.repeat(np.arange(len(a)),a)
        print(c)
    if 0:
        a=np.arange(5)
        repeat_count=[1,2,1,2,3]
        c=np.repeat(a,repeat_count)#repeat the values in array with how many times given in repeat_count array
        print(c)
    if 0:
        a=np.random.randint(0,10,(2,5))
        print(a)
        c=np.bincount(a.flatten())
        print(c)

# How to negate a boolean, or to change the sign of a float inplace?
if 0:
    if 0:
        Z = np.random.randint(0, 10, 10)
        print(Z)
        np.logical_not(Z, out=Z)
        print(Z)
    if 0:
        Z = np.random.uniform(1,10, 10)
        print(Z)
        np.negative(Z, out=Z)
        print(Z)

# Consider an array Z = [1,2,3,4,5,6,7,8,9,10], how to generate an array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [7,8,9,10]]?
if 0:
    from numpy.lib import stride_tricks
    if 0:
        a = np.arange(1, 11).reshape((2, 5))
        b=stride_tricks.as_strided(a,(7,4),(4,4))
        print(b)
    if 1:
        a = np.arange(1, 11).reshape((2, 5))
        b=stride_tricks.as_strided(a,(7,3),(1,2))
        print(b)
    if 0:
        a = np.arange(1, 11).reshape((2, 5))
        b=stride_tricks.as_strided(a,(7,3),(1,1))
        print(b)
    if 0:
        a = np.arange(1, 11).reshape((2, 5))
        b=stride_tricks.as_strided(a,(7,3),(1,4))
        print(b)
    if 0:
        a=np.arange(1,11).reshape((2,5))
        print(a)

# How to find the most frequent value in an array?
if 0:
    if 1:
        a=np.random.randint(1,10,20)
        print(a)
        bincount=np.bincount(a,minlength=15)
        print(bincount)
        frequent_value=bincount.argmax()
        print(frequent_value)
    if 0:
        a=np.random.randint(1,10,20)
        print(a)
        bincount=np.bincount(a,minlength=15)
        print(bincount)
    if 0:
        a=np.random.randint(1,10,(2,5))
        print(a)

# How to get the n largest values of an array
if 0:
    if 1:
        a = np.arange(20)
        np.random.shuffle(a)
        b=np.argsort(a)
        print(a)
        print(b)
        n=5
        print(b[-n:])
        print(a[b[-n:]])
    if 0:
        a = np.arange(20)
        np.random.shuffle(a)
        b=np.argsort(a)
        print(b)
        n=5
        print(b[-n:])
    if 0:
        a = np.arange(20)
        np.random.shuffle(a)
        b=np.argsort(a)#Returns the indices that would sort an array.
        print(a)
        print(b)
        print(a[b[0]])
    if 0:
        a = np.arange(20)
        np.random.shuffle(a)
        print(a)
    if 0:
        a = np.arange(20).reshape((4, 5))
        np.random.shuffle(a)
        print(a)
    if 0:
        a=np.arange(20).reshape((4,5))
        print(a)









