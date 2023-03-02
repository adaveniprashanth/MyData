import subprocess
from subprocess import Popen

path_to_output_file = 'contents.txt'

myoutput = open(path_to_output_file,'w+')

# file 'foo bar' doesn't exist
p = Popen(["python", "yaml_converter.py"], stdout=myoutput, stderr=myoutput, universal_newlines=True)

output, errors = p.communicate()

print(output)