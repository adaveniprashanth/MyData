'''
1.Array Data structure:
    In an array, elements in memory are arranged in continuous memory. 
    All the elements of an array are of the same type
'''
if 1:
    import array
    arr = array.array('i', [1, 2, 3,2,3,4,2])
    print(arr)
    print(arr.pop(2)) #removes item from 3nd index
    arr.remove(1) # removes 1
    arr.append(4) #append 4 at end
    arr.insert(2,5) #insert 5 at 2nd index
    print(arr.index(4)) #find the index of 2
    print(arr.reverse()) #reverse the index
