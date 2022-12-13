import numpy as np
import pandas as pd
from numpy import newaxis
# For reference --> https://numpy.org/doc/stable/reference/index.html

# why numpy is fast?
# Vectorization describes the absence of any explicit looping, indexing, etc., in the code.
# Broadcasting is the term used to describe the implicit element-by-element behavior of operations
# numpy array class is called as ndarray
'''
Attributes of ndarray:
1.ndarray.ndim-->number of axes (dimensions) of the array
2.ndarray.shape --> This is a tuple of integers indicating the size of the array in each dimension.
and length of ndarray.shape is equals to ndarray.ndim
3.ndarray.size --> total number of elements of array. It is equal to  product of elements of ndarray.shape
4.ndarray.dtype --> it describes type of the elements in the array.
5.ndarray.itemsize -->  size in bytes of each element of the array
6.ndarray.data --> buffer containing the actual elements of the array.
'''
if 1:#Basics
    if 0: #Attribues of ndarray.
        a = np.arange(15).reshape(3, 5)
        print("array type is ",type(a))
        print("array is \n",a)
        print("no.of dimensions are ",a.ndim)
        print("no.of dimensions are ",len(a.shape))
        print("shape of array is ", a.shape)
        print("total elements are ", a.size)
        print("total elements are ", a.shape[0]*a.shape[1])
        print("type of elements in array is ",a.dtype)
        print("type of elements in array is ", a.dtype.name)
        print("size of each element is ",a.itemsize)
        # print("elements in array are ",list(a.data))#it will not work
    if 1:#Array creation types
        if 0: # from a regular Python list or tuple
            a = np.array([1,2,3])
            b = np.array((1.2,3.2,4))
            print(a,b)
        if 0:# array transforms sequences of sequences into two-dimensional arrays,and so on
            a= np.array([(1,2,3),[4,5,6]])
            print(a)
        if 0:#defining type of elements in array
            a = np.array([[1,2,3],[4,5,6]],dtype=np.int64)
            print(a)
            print(a.dtype)
        if 0:#zeros array, ones array, empty array(contanins random values)
            z = np.zeros([2,3],dtype=np.float16)
            o = np.ones([3,4],dtype=np.int32)
            e = np.empty([2,3])
            print(z)
            print(o)
            print(e)
        if 0:#using arange function
            # np.arange(start,stop,step)
            a = np.arange(10,30,5,dtype=np.int32)
            print(a)
            b = np.arange(1,5,0.5,dtype=np.float32)
            print(b)
        if 0:# using linspace
            # np.linspace(start,stop,no_of_elements)
            a = np.linspace(1,6,10)
            print(a)
            b = np.linspace(1, 6, 20)
            print(b)
        if 0:#using function
            def f(x,y):
                return (x+y)
            a = np.fromfunction(f,(5,5),dtype=np.int32)
            print(a)
            def f(x,y,z):
                return (x+y+z)
            a = np.fromfunction(f, (3,3,3), dtype=np.int32)
            print(a)
        if 0:#using the random function
            rg = np.random.default_rng(1)  # create instance of default random number generator
            a = rg.random((2,3))
            print(a)

        # we can also use othe methods:
        # they are array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace,
        # numpy.random.Generator.rand, numpy.random.Generator.randn, fromfunction, fromfile

    if 0:#printing the arrays
        # One-dimensional arrays are then printed as rows, bidimensionals as matrices
        # and tridimensionals as lists of matrices
        a = np.arange(5)
        print(a)
        b=np.arange(9).reshape(3,3)
        print(b)
        c = np.arange(27).reshape(3,3,3)
        print(c)
        #If an array is too large to be printed, NumPy automatically skips the central part of the array
        # and only prints the corners:
        # To disable this behaviour and force NumPy to print the entire array, you can change the printing options using
        # set_printoptions
        #np.set_printoptions(threshold=sys.maxsize)
    if 0:#Basic operations
        #Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
        a= np.arange(6)
        b=np.random.randint(6)
        c = a-b
        # print(c)
        d=np.arange(6).reshape(2,3)
        e = np.arange(6,12).reshape(2,3)
        #the product operator * operates elementwise in NumPy arrays
        f = d * e
        print("multplication operation\n",f)
        #The matrix product can be performed using the @ operator or the dot function
        m1 = np.arange(6).reshape(2,3)
        m2 = np.arange(6,12).reshape(3,2)
        g = m1 @ m2
        print("matrix multiplication")
        print(g)
        h = m1.dot(m2)
        print(h)
        # Some operations, such as += and *=, act in place to modify an existing array
        # rather than create a new one.
        a = np.arange(6).reshape(2,3)
        a+=3
        print(a)
        a*=5
        print(a)
        # Many unary operations, such as computing the sum of all the elements in the array
        print("total sum is \n",a.sum())
        print("column wise sum is \n",a.sum(axis=0)) #across rows
        print("row wise sum is \n", a.sum(axis=1))  # across columns
    if 0:#Universal functions like exp,sin,cos and etc.
        a = np.arange(2,8).reshape(2,3)
        print(np.sin(a))
        print(np.cos(a))
        print(np.log(a))#base e
        print(np.log2(a))  # base 2
        #other functions are :
        #all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj,
        # corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, invert, lexsort, max, maximum,
        # mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose,
        # var, vdot, vectorize, where
    if 1:#indexing,slicing and iterating
        if 0:#1-D Array
            a = np.arange(10)**3
            print(a[2])
            print(a[1:3])
            for i in a:
                print(i)
        if 0:#Multidimensional arrays can have one index per axis
            a = np.arange(25).reshape(5,5)
            b = np.arange(27).reshape(3, 3, 3)
            print(a)
            print(a[0,1])
            print(a[0, :])#printing single row
            print(a[:, 0])  # printing single column
            print(a[:3,1:4])#printing sub matrix
            #specail one
            print(a[-1])#it is equal to a[-1,:] i.e last row
            print(a[1,...])#... completes the remaining axes values with :
            print(b[1,...])
            print(b[...,2])
            #iterating
            print("iterating over array")
            #it is taking the outer dimensions as values
            for row in b:
                print(row)
                print()
            print("flat the array and print using flat or flatten methods")
            for i in b.flatten():
                print(i)
            # other methods are newaxis, ndenumerate, indices
    if 1:#shape manipulation
        #we can do the manipulation using array name or numpy function
        if 0:
            a = np.arange(0,12).reshape(3,4)
            print(a)
            print(a.reshape(4,3))#reshaping means converts to 1-D array and then changes to new shape
            print(a.ravel())
            print(a.flatten())
            print(a)
            print(a.T)
            print(a.transpose())
            a.resize(4,3)#reshapes creates new array and resize adjust itself i.e inplace changes
            print(a)
        if 0:
            b = np.arange(27).reshape(3,3,3)
            print(b)
            print(np.reshape(b,newshape=(9,3)))
            print(np.reshape(b, newshape=(9, -1)))
            print(np.ravel(b))
            print(np.transpose(b))
            print(np.transpose(b,axes=(1,2,0)))#axes wise transpose
            print(np.resize(b,new_shape=(3,9)))
            #print(np.resize(b, new_shape=(3, -1)))#it will no support negative values
        if 1:#stacking the array
            if 0:#for 2-D arrays
                a = np.arange(9).reshape(3,3)
                b = np.arange(9,18).reshape(3,3)
                #adding the array horizontally
                hstack = np.hstack((a,b))
                print(hstack)
                # adding the array vertically
                vstack = np.vstack([a, b])
                print(vstack)
            if 0:
                #The function column_stack stacks 1D arrays as columns into a 2D array.
                A= np.array([1,2,3,4])
                B= np.array([5,6,7,8])
                c = np.column_stack((A,B))#converts 1-D arrays to 2-D array. it is like hstack for 2-d arrays
                print(c)
                A = np.array([1,2])
                B = np.array([3, 4])
                C= np.hstack((A,B))
                print(C)
                D=np.vstack((A,B))
                print(D)
            if 0:#converts the 1-D array as 2-D array while doing calculation
                a = np.array([1,2,3,4])#1-D array
                print(a)
                print(a.shape)
                b = a[:,newaxis] #converts 1-D array to 2-D array
                print(b)
                print(b.shape)
                c = a[newaxis,:]
                print(c)
                print(c.shape)
            #The function column_stack stacks 1D arrays as columns into a 2D array.
            # It is equivalent to hstack only for 2D arrays

            #the function row_stack is equivalent to vstack for any input arrays.
            # In fact, row_stack is an alias for vstack
            if 0:
                print(np.column_stack is np.hstack)
                print(np.row_stack is np.vstack)
            # **************
            #Note: In general, for arrays with more than two dimensions,
            # hstack stacks along their second axes,
            # vstack stacks along their first axes,
            # and concatenate allows for an optional arguments
            # giving the number of the axis along which the concatenation should happen
            if 0:#splitting the array into smaller ones
                a= np.arange(24).reshape(2,12)
                print(a)
                print(np.hsplit(a,3))#splits the arrays into 3 arrays
                print(np.hsplit(a,(3,4)))#splits the array into 3 arrays splitting happens.
                #the 1st array is before 3 column,2nd array is 3 column itself and 3rd array is remain
                #it is like partition in string ex:--> s='new program'; s.partition('p')
                print(np.hsplit(a,(2,5)))
                #*************
                #vsplit splits along the vertical axis,
                # and array_split allows one to specify along which axis to split.
    if 1:#copy and view(shallow copy) of array
        #The 'view' method creates a new array object that points at the same data
        a = np.arange(12).reshape(3,4)
        if 0:
            b = a
            print(b)
            print(b is a)
            print(b.base is a)
            b=b.reshape(6,2)
            b[5,1]=1000
            print(a)
            print(b)
        if 0:
            c = a.view()
            print(c)
            print(c is a)
            print(c.base is a)
            c= c.reshape(2,6)
            print(a.shape)
            print(c.shape)
            c[0,4]=1000
            print(a)
        if 1:#Deep copy
            #The copy method makes a complete copy of the array and its data
            d = a.copy()
            d=d.reshape(4,3)
            print(a)
            print(d)
            d[3,1]=1000
            print(a)
            print(d)











