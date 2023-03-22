import re
import pyinputplus
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
if 0:#Assignment_6
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
    if 0:#question 9
        s = "abcdefgh"
        print(s.rjust(20,'*'))
        print(s.ljust(20,'*'))
        print(s.center(20,'*'))

if 0:#Assignment_7
    if 0:#question 3
        a = re.search('\d','asabnm2323')#searches entire string and returns if any match found
        print(a)
    if 0:#question 4
        a = re.match('as','asabasnm2323')#searches from beginning, and returns if match found other wise returns None
        print(a)
        print(a.group())
        b = re.match('\d','asd13adas')
        print(b)
        b = re.match('asd\d','asd13adas')
        print(b)
        print(b.group())
    if 0:#question 5
        a = re.search(r'(\d\d\d)-(\d\d\d-\d\d\d\d)','abc123-456-7890')
        print(a.group())
        b = re.search(r'(\d\d\d)-(\d\d\d-\d\d\d\d)','abc-456-7890')
        print(b)
    if 0:#question 6
        #raw string will remove the property of "\". it will be consider as a literal only.
        print((re.split(r'\\s','we are \\splitting the words')))
        print((re.split( '\\s','we are \\splitting the words')))
        print((re.split( '\\s','we are \ splitting the words')))

        a = re.search('\(','dsag(afsdsfds)')
        print(a)
    if 0:#question 7
        pass
        a = re.findall('abc','dabccdcabc')
        print(a)
        b = re.findall('(abc)(cdc)','dabccdcabc')
        print(b)
        c = re.findall('(abc)\w*(cdc)','dabccdcabc')
        print(c)
    if 0:#question 9
        a = re.findall('ca|bc','abcbacbabcbabcbabcbabcbabcbacb')
        print(a)
        a = re.findall('c[a|b]a','abcbacbabcbabcaabcbabcbabcaacb')
        print(a)

        #question 17
    if 0:#making the . to accept newline character also as a literal by using re.S or re.DOTALL
        # string with newline character
        target_str = "ML\nand AI"

        # Match any character
        result = re.search(r".+", target_str)
        print("Without using re.S flag:", result.group())
        # Output 'ML'

        # With re.S flag
        result = re.search(r".+", target_str, re.S)
        print("With re.S flag:", result.group())
        # Output 'ML\nand AI'

        # With re.DOTALL flag
        result = re.search(r".+", target_str, re.DOTALL)
        print("With re.DOTALL flag:", result.group())
        # Output 'ML\nand AI'
        
    if 0:
        pass
        pattern = re.compile(r'\d+')
        print(pattern.sub('X', '11 drummers, 10 pipers, five rings, 4 hen'))
        
        #question 19
    if 0:#putting comment in search pattern and making it exceptional using re.X or re.VERBOSE
        target_str = "Jessa is a Python developer, and her salary is 8000"

        # re.X to add indentation  and comment in regex
        result = re.search(r"""(^\w{2,}) # match 5-letter word at the start
                                .+(\d{4}$) # match 4-digit number at the end """, target_str, re.X)
        # Fiver-letter word
        print(result.group(1))
        # Output 'Jessa'

        # 4-digit number
        print(result.group(2))
        # Output 8000
    if 0:#question 20
        a = '42'
        a = '1,234'
        a = '1234'
        a = '6,368,745'
        a = '12,34,567'
        print(re.findall('^\d{1,3}(,\d{3})*$',a))
    if 0:#question 21
        a = 'Haruto Watanabe'
        a = 'Alice Watanabe'
        a = 'RoboCop Watanabe'
        a = 'haruto Watanabe'
        a = 'Mr. Watanabe'
        a = 'Watanabe'
        a = 'Haruto watanabe'
        print(re.findall('[A-Z][A-Za-z]+ Watanabe',a))
    if 0:#question 22
        a = 'Alice eats apples.'
        a = 'Bob pets cats.'
        a = 'Carol throws baseballs.'
        a = 'Alice throws Apples.'
        a = 'BOB EATS CATS.'
        a = 'RoboCop eats apples.'
        a = 'ALICE THROWS FOOTBALLS.'
        a = 'Carol eats 7 cats.'
        print(re.findall('(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',a,re.IGNORECASE))
if 1:#Assignment_8
    pass