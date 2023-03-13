if 0:#Assignment 3
    if 0:#question 10
        print(type(None))
    if 0:#question 13
        try:
            a = int(input("enter the data"))
            b = 8/a
            print(b)
        except Exception as e:
            print(e)
        else:
            print("try block executed successfully")

if 0:#Assignment_4
    if 0:#question 2
        spam = [2, 4, 6, 8, 10]
        spam.insert(2,'Hello')
        print(spam)
    if 0:#question 3
        spam = ['a', 'b', 'c', 'd']
        print(spam[int(int('3' * 2) / 11)])
        print(spam[-1]);print(spam[:2])
    if 0:#question 6
        bacon = [3.14, 'cat', 11, 'cat', True]
        print(bacon.index('cat'))
        bacon.append(99)
        print(bacon)
        bacon.remove('cat')
        print(bacon)
    if 0:#question 9
        l = [1,2,3,4]
        m = [3,45,8,4]
        l.append(89)
        print(l)
        l.extend(m)
        print(l);print(l+l);print(m*4)
    if 0:#question 11
        l = [1,2,3,4]
        l.pop()
        l.remove(1)
        print(l)
    if 0:#question 17
        import copy
        l=[0,1,2,3,4,[9,8,7,6,2,3]]
        m = copy.copy(l)
        n = copy.deepcopy(l)
        print("l=",l)
        l[5][2]='abcd'
        print("l=",l);print("m=",m);print("n=",n)
if 0:#Assignment_5
    if 0:#question 1
        spam = {}
        spam['abc']=1
        spam['foo']=42
        spam['color'] = 'black'
        print(spam.keys())
        print(spam.values())
if 1:#Assignment_6
    if 0:#question 6
        print('Hello, world!'[1])
        print('Hello, world!'[:5])
        print('Hello, world!'[3:])
    if 0:#question 7
        print('Hello'.upper())
        print('Hello'.upper().isupper())
        print('Hello'.upper().lower())
    if 0:#question 8
        print('Remember, remember, the fifth of July.'.split())
        print('-'.join('There can only one.'.split()))
    