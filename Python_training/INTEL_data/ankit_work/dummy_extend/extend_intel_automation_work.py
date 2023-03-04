#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    import pandas as pd
    import sys,os
    import yaml
    from yaml.loader import SafeLoader
    import json,re
except ModuleNotFoundError:
    sys.exit("install all modules")

if 1:
    def get_parent_child_pair():
        print("pandas activity")
        parent_child = []
        df = pd.read_excel('module_parent_structure.xlsx',sheet_name=['module_parent'])#accessing sheet by names
        module_list = list(df['module_parent']['#Module'])
        parent_list = list(df['module_parent']['Parent'])

        for parent,child in zip(parent_list,module_list):
            if parent == 'None':
                continue
            parent_child.append([parent,child])
        
        '''
        file_input=open('excel_data.txt','r')
        all_lines=file_input.readlines()
        file_input.close()
        for line in all_lines:
            data=line.strip().split("\t")
            if data[0] == 'None':
                continue
            parent_child.append(data)
        '''

        return parent_child
    
    parent_child_combo = get_parent_child_pair()
    
    #print(parent_child_combo)

    def get_instances_hierarchy():
        instances = []
        with open('PTL_hierarchy1.txt','r') as f:
            for i in f:
                values = i.strip().split()
                instances.append((int(values[0]),values[-1]))
        return instances

    instance_hierarchy = get_instances_hierarchy()
    # print(instance_hierarchy)

    final_child_path = []
    missed_in_hierarchy = []
    def find_path_values(instance_hierarchy1,parent_child_combo1):
        for parent,child in parent_child_combo1:
            d = {}
            counter = 0
            instance_present = True
            for position,instance in instance_hierarchy1:
                d[position]=instance
                if instance == child:
                    counter = position
                    break
            else:
                instance_present = False

            new_dict = d.copy()
            for k in d.keys():
                if k > counter:
                    new_dict.pop(k)
            if not instance_present:
                print(child,"is not present in hierarchy")
                missed_in_hierarchy.append(child)
            else:
                final_child_path.append([parent, new_dict])

    find_path_values(instance_hierarchy,parent_child_combo)


    final_path = []
    def create_child_path(final_child_path1):
        for i in final_child_path1:
            path =''
            for j in range(2,len(i[1])):
                path = path + "/"+i[1][j]
            # print("parent","child_path")
            # print(i[0],path)
            final_path.append((i[0],path))
        return final_path

    final_path = create_child_path(final_child_path)
    # print(final_path)

    hier_structure = {}
    def create_hierarchy(final_path1):
        for i in final_path1:
            if i[0] not in hier_structure.keys():
                hier_structure[i[0]]=[i[1]]
            else:
                hier_structure[i[0]]+=[i[1]]
    create_hierarchy(final_path)

    # print(hier_structure)
    length = len(hier_structure)
    f = open('extend_final_result.txt','w')
    f.write("hier_spec = {\n")
    for c,i in enumerate(hier_structure.items()):
        string = "'/"+i[0]+"'"+":"+",\n".join(str(i[1]).split(", "))
        print(string)
        if c == length-1:
            f.write(string)
        else:
            f.write(string + ",\n")
    f.write("\n}")
    f.close()
    if 1:#missed modules
        f1 = open("missed_modules.txt",'w')
        f1.write("\nmissed modules in hierarchy are\n")
        for c,i in enumerate(missed_in_hierarchy):
            f1.write(i+",")
            if c%4 == 0:
                f1.write("\n")
        f1.close()
    


# gtmctoremove1  code to fetch dfx_insert1 and dfx_tieoff1 modules
if 1:
    def get_instances_hierarchy():
        instances = []
        with open('PTL_hierarchy1.txt', 'r') as f:
            for i in f:
                values = i.strip().split()
                instances.append((int(values[0]), values[-1]))
        return instances


    instance_hierarchy = get_instances_hierarchy()

    print(instance_hierarchy)


    final_child_path = []
    missed_in_hierarchy = []
    def find_path_values(instance_hierarchy1):
        length = len(instance_hierarchy1)
        counting = 0
        childs = ['dfx_tieoff1','dfx_insert1']
        childs_count = 0
        while True:
            parent = 'gtmctoremove1'
            child = childs[childs_count]
            d = {}
            childs_count+=1

            for position, instance in instance_hierarchy1:
                counting += 1
                d[position] = instance
                if instance == child:
                    counter = position
                    new_dict = d.copy()
                    for k in d.keys():
                        if k > counter:
                            new_dict.pop(k)
                    final_child_path.append([parent, new_dict])

            if counting == length and childs_count == len(childs):
                break
            counting = 0

    find_path_values(instance_hierarchy)
    print(final_child_path)

    final_path = []
    def create_child_path(final_child_path1):
        for i in final_child_path1:
            path =''
            for j in range(2,len(i[1])):
                path = path + "/"+i[1][j]
            final_path.append((i[0],path))
        return final_path

    final_path = create_child_path(final_child_path)
    # print(final_path)

    hier_structure = {}
    def create_hierarchy(final_path1):
        for i in final_path1:
            if i[0] not in hier_structure.keys():
                hier_structure[i[0]] = [i[1]]
            else:
                hier_structure[i[0]] += [i[1]]

    create_hierarchy(final_path)

    print(hier_structure)
    length = len(hier_structure)
    f = open('extend_gtmctoremove.txt','w')
    f.write("hier_spec = {\n")
    for c, i in enumerate(hier_structure.items()):
        string = "'/" + i[0] + "'" + ":" + ",\n".join(str(i[1]).split(", "))
        print(string)
        if c == length - 1:
            f.write(string)
        else:
            f.write(string + ",\n")
    f.close()



#updated structure with yaml file values.
if 1:
    f1=open('temp_file.txt','w')
    # Open the file and load the file
    with open('trkset_components.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
        yaml_dict=data['TRKSET_DEFAULT_DEFINITION']['TRKSET_COMPONENTS']

    #printing yaml data after converting to dictionary
    if 0:
        for k,v in yaml_dict.items():
            f1.write(k+":"+str(v)+"\n")
            print(k,":",v)

    target_and_dependecies=[]
    wrapper_target_depends_dict={}
    for k,v in yaml_dict.items():

        if k not in wrapper_target_depends_dict.keys():
            wrapper_target_depends_dict[k]=[]
        else:
            wrapper_target_depends_dict[k]=wrapper_target_depends_dict[k]
        
        if 'target' in yaml_dict[k].keys():
            if yaml_dict[k]['target'] != None:
                target_and_dependecies.append([k,yaml_dict[k]['target']])
                
                if type(yaml_dict[k]['target']) is not list:
                    wrapper_target_depends_dict[k]+=[yaml_dict[k]['target']]
                elif type(yaml_dict[k]['target']) is list:
                    wrapper_target_depends_dict[k]+=yaml_dict[k]['target']
                    
        if 'dependencies' in yaml_dict[k].keys():
            if yaml_dict[k]['dependencies'] != None:
                target_and_dependecies.append([k,yaml_dict[k]['dependencies']])
                
                if type(yaml_dict[k]['dependencies']) is not list:
                    wrapper_target_depends_dict[k]+=[yaml_dict[k]['dependencies']]
                elif type(yaml_dict[k]['dependencies']) is list:
                    wrapper_target_depends_dict[k]+=yaml_dict[k]['dependencies']

    #printing targets and dependencies
    if 0:
        f1.write("printing targets and dependencies\n")
        for k,v in target_and_dependecies:
            f1.write(k+":"+str(v)+"\n")

    #printing wrappers,targets and dependencies
    if 0:
        f1.write("printing wrappers,targets and dependencies\n")
        for k,v in wrapper_target_depends_dict.items():
            f1.write(k+":"+str(v)+"\n")


    f = open('extend_final_result.txt','r')
    all_data = f.read()
    f.close()
    val=all_data.split("{")[1].split("}")[0].replace("'","\"")
    final_result=json.loads("{"+val+"}")    

    #printing the final_result 
    if 0:
        f1.write("printing the final_result\n")
        for k,v in final_result.items():
            f1.write(k+":"+str(v)+"\n")

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

    #printing the new dict
    if 0:
        f1.write("printing the new dict\n")
        for k,v in new_dict.items():
            f1.write(k+":"+str(v)+"\n")


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

    total_dict={}
    for k,v in final_result.items():
        dummy_list=v.copy()
        for key,value in wrapper_target_depends_dict.items():
            if len(value)>=0:
                for i in value:
                    string="@".join(v)
                    res=re.subn(i+'[\d]+',key,string)[0].split("@")
                    if re.subn(i+'[\d]+',key,string)[1] >= 1:
                        f1.write(k+"=>"+i+" : "+key+"\n")
                    #print(res)
                    dummy_list+=res
        for data in v:
            if data in dummy_list:
                dummy_list.remove(data)
        total_dict[k]=list(set(dummy_list))
        f1.write(k+":"+str(v)+"\n")
        f1.write(k+":"+str(list(set(dummy_list)))+"\n")


    length = len(total_dict)
    f2 = open('total_final_result.txt','w')
    f2.write("hier_spec = {\n")
    for c,i in enumerate(total_dict.items()):
        string = i[0]+"'"+":"+",\n".join(str(i[1]).split(", "))
        print(string)
        if c == length-1:
            f2.write(string)
        else:
            f2.write(string + ",\n")
    f2.write("\n}")
    f2.close()

    f1.close()