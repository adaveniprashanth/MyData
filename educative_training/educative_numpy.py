#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 07:11:31 2020

@author: pj
"""
#For reference--> https://numpy.org/doc/stable/reference/index.html
import numpy as np
if 1:  #Numpy arrays
    if 1: #array initialization
    
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
        print(uniform)
        
        #np.random.normal(loc,scale,size=shape)
        #              ||
        #              ||
        #np.random.normal(mean,deviation,size=shape)
        # print(np.random.normal())
        random_norm = np.random.normal(2.0,3.5,size=(10,5))
        print(random_norm)
        
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
        print(arr3)
        
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




