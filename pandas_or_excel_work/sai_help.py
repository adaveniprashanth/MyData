import os
import pandas as pd
input_file_name = 'sai'
excel_file = input_file_name+'.xlsx'
cwd=os.getcwd()

df = pd.read_excel(excel_file,sheet_name='Sheet4')

first = list(df['first'])
second = list(df['second'])

first = [x.strip() for x in first if type(x) == str]
second = [x.strip() for x in second if type(x) == str]
first= list(set(first))
second = list(set(second))
counter = 0
for i in first:
    for j in second:
        if i ==j:
            counter+=1
            print(i,j)
        
print(counter)