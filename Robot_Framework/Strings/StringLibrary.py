from stringmethods import StringMethods
import os.path
import subprocess
import sys

class StringLibrary(object):
    def __init__(self):
        self._string = StringMethods()
        self._sut_path = os.path.join(os.path.dirname(__file__),'stringmethods.py')#need for run_command used in pipe logic
        self._result = ''
    
    def adding_strings(self, *args):
        self._result = self._string.add_strings(*args)
    
    def strings_adding(self, args):
        self._result = self._string.added_strings(args)
    
    def counting_words(self,string,s):
        self._result = self._string.count_words(string,s)
    
    def replacing_strings(self,string,sub,replace):
        self._result = self._string.replace_string(string,sub,replace)
        
    def string_reverse(self, original):
        self._result = self._string.reverse_string(original)
    
    
    def index_find(self,string,value):
        self._result = self._string.find_index(string,value)
    
    def convert_to_list(self,string):
        self._result = self._string.convert_list(string)
    
    def result_should_be(self, expected):
        if expected != self._result:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (self._result, expected))
    
    def list_result_should_be(self, *expected):
        if list(expected) != self._result:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (self._result, expected))
    


'''    
    #these will work based on the subprocess
    #NOW these are not working
    def index_finding(self,string,value):
        self._run_command('find-index', string, value)

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(args)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        self._result = process.communicate()

'''
