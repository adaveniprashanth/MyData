#!/usr/bin/env python


class StringMethods(object):   
    def __init__(self):
        self._expression = ''
    
    def add_strings(self,*args):
        a = ''
        for i in args:
            a = a+i
        return a
    def added_strings(self,args):
        a = ''
        for i in args:
            a = a+i
        return a
    
    def count_words(self,string,s):
        c = string.count(s)
        return str(c)
    
    def replace_string(self,s,sub,replace):
        replaces = s.replace(sub,replace)
        return replaces
    
    def reverse_string(self,string):
        return string[::-1]
    
    def find_index(self,string,i):
        return str(string.find(i))
    
    def convert_list(self,string):
        return list(string)

# needed in run_command in stringlibrary file
'''
s = StringMethods()
def finding_index(string,value):
    #print(s.find_index(string,value))
    return s.find_index(string,value)

def add_strings(*args):
    s.add_strings(*args)

def replaced_string(string,sub,replace):
    return replace_string(string,sub,replace)
#For reference: https://www.simplilearn.com/tutorials/python-tutorial/subprocess-in-python

if __name__ == '__main__':
    actions = {'find-index':finding_index,'add-words': add_strings,'replace-string': replaced_string,
               'reverse-string':StringMethods.reverse_string, 'count-words': StringMethods.count_words}
'''