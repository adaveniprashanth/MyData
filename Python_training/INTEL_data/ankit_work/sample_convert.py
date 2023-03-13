#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import pyyaml module
import yaml
from yaml.loader import SafeLoader
import json,time
import re,sys,subprocess
import logging
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)


target_and_dependecies=[]
# Open the file and load the file
with open('trkset_components.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    #print(data.items())
    yaml_dictionary=data['TRKSET_DEFAULT_DEFINITION']['TRKSET_COMPONENTS']

#printing yaml_dictionary
if 0:
    for i,j in yaml_dictionary.items():print(i,'=',j)

#collecting all targets and dependencies under same wrapper
target_dependencies_dict={}
for k,v in yaml_dictionary.items():
    #print(v)
    if k not in target_dependencies_dict.keys():
        target_dependencies_dict[k]=[]
    else:
        target_dependencies_dict[k]=target_dependencies_dict[k]
    
    if 'target'in v.keys() and v['target'] is not None:
        if type(v['target']) is not list:
            a=[]
            a.append(v['target'])
            target_dependencies_dict[k]+=a
        else:
            target_dependencies_dict[k]+=v['target']
    
    if 'dependencies'in v.keys() and v['dependencies'] is not None:
        if type(v['dependencies']) is not list:
            a=[]
            a.append(v['dependencies'])
            target_dependencies_dict[k]+=a
        else:
            target_dependencies_dict[k]+=v['dependencies']

#printing all targets and dependencies under same wrapper
if 0:
    for i,j in target_dependencies_dict.items():
        print(i,'=',j)

#collecting all targets and dependencies together
all_targets=[]
for k,v in target_dependencies_dict.items():
    all_targets+=v

summarized_targets= list(set(all_targets))
#print(summarized_targets)

target_wrapper_dict={}
for i in summarized_targets:
    target_wrapper_dict[i]=[]
    for k,v in target_dependencies_dict.items():
        if i in v:
            target_wrapper_dict[i]+=[k]

#printing all targets associate with wrappers
if 0:
    for i,j in target_wrapper_dict.items():
        print(i,'=',j)



'''
for k,v in yaml_dictionary.items():
    pass
    #print(k,"=",v)
    if 'target' in yaml_dictionary[k].keys():
        if d[k]['target'] != None:
            target_and_dependecies.append([k,yaml_dictionary[k]['target']])
        #print(yaml_dictionary[k]['target'],k)
    if 'dependencies' in yaml_dictionary[k].keys():
        target_and_dependecies.append([k,yaml_dictionary[k]['dependencies']])
        #print(yaml_dictionary[k]['dependencies'],k)
        #logging.info(yaml_dictionary[k]['dependencies'])
        #print(k,"=",v)

#print(target_and_dependecies)
'''

'''
new_dict = {}
for i in target_and_dependecies:
    if i[0] in new_dict.keys():
        if type(i[1]) is not list:
            a=[]
            a.append(i[1])
            new_dict[i[0]]+=a
        elif type(i[1]) is list:
            new_dict[i[0]]+=i[1]
    elif i[0] not in new_dict.keys():
        if type(i[1]) is not list:
            a=[]
            a.append(i[1])
            new_dict[i[0]] = a
        elif type(i[1]) is list:
            new_dict[i[0]] = i[1]

for item in new_dict.items():
    pass
    #print(list(item))
'''




#creating the dictionary form the file
f = open('extend_final_result.txt','r')
all_data = f.read()
f.close()
val=all_data.split("{")[1].split("}")[0].replace("'","\"")
final_result=json.loads("{"+val+"}")    

#printing the hierarchy from ditionary
if 0:
    for i,j in final_result.items():
        print(i,'=',j)


'''
def updated_list(k,list1,key,list2):
    new_list = list1.copy()
    for item1 in list1:
        for item2 in list2:
            #if item2 in item1:
            if re.search(item2+'[\d]+',item1):
                splits= item1.split("/")
                splits=splits[0:-1]+[key]
                string="/".join(splits)
                new_list.append(string)    
    return new_list
'''



def append_list(list1,key,list2):
    b=list1.copy()
    empty_list=list1.copy()

    for i in range(len(list1)):
        for substr in list2:
            if re.search(substr+'[\d]+',list1[i]):
                splits = list1[i].split("/")[0:-1]
                splits.append(key)
                string="/".join(splits)
                b.append(string)
                empty_list+=b
                empty_list=list(set(empty_list))
                #f.write(str(empty_list).strip()+"\n")
    return empty_list


final_dict = {}
f=open('result.txt','w')
for final_result_key,final_result_value in final_result.items():
    f.write(final_result_key+":"+str(final_result_value)+"\n")
    temp_list=[]
    for key,value in target_wrapper_dict.items():
        #temp_list=updated_list(final_result_key,final_result_value,key,value)
        temp_list=append_list(final_result_value,key,value)
        final_dict[final_result_key]=temp_list
        
    f.write(final_result_key+":"+str(temp_list)+"\n")
    f.write("\n")

f.close()




'''
def append_list(list1,key,list2):
    b=list1.copy()
    empty_list=list1.copy()

    for i in range(len(list1)):
        for substr in list2:
            if re.search(substr+'[\d]+',list1[i]):
                splits = list1[i].split("/")[0:-1]
                splits.append(key)
                string="/".join(splits)
                b.append(string)
                empty_list+=b
                empty_list=list(set(empty_list))
                #f.write(str(empty_list).strip()+"\n")
    return empty_list
    

final_dict = {}
f=open('result.txt','w')
for final_result_key,final_result_value in final_result.items():
    for new_dict_key,new_dict_value in new_dict.items():
        #final_result_value,new_dict_value = append_list(final_result_value,new_dict_value)
        if final_result_key not in final_dict.keys():
            final_dict[final_result_key]=append_list(final_result_value,new_dict_key,new_dict_value)
        else:
            final_dict[final_result_key]+=append_list(final_result_value,new_dict_key,new_dict_value)
        
        #for i in new_dict_value:
        #    for j in final_result_value:
for k,v in final_dict.items():
    final_dict[k]=list(set(final_dict[k]))
f.write(str(final_dict).replace("],","],\n")+"\n")
f.close()                
'''

#logging module example
'''
logger = logging.getLogger("test")
logger.setLevel(level=logging.DEBUG)
logFileFormatter = logging.Formatter(fmt='%(name)s - %(levelname)s - %(message)s')
fileHandler = logging.FileHandler(filename='test.log')
fileHandler.setFormatter(logFileFormatter)
fileHandler.setLevel(level=logging.DEBUG)
logger.addHandler(fileHandler)
'''

'''
root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='test.log')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
'''

'''
# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

'''

'''
if re.search('vmx_sl_vid[\d]+','/smvdbox0/smmfxvdenc1/vmx_sl_vid11'):
    print("present")
else:
    print("not present")
'''