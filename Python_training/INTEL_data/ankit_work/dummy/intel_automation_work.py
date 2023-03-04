#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    import pandas as pd
    import sys,os
    import shutil
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
        return parent_child

    parent_child_combo = get_parent_child_pair()
    print(parent_child_combo)

    def get_instances_hierarchy():
        instances = []
        with open('PTL_hierarchy.txt','r') as f:
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
    f = open('final_result.txt','w')
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
    
    if 0:#missed modules
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
        with open('PTL_hierarchy.txt', 'r') as f:
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
    f = open('gtmctoremove1.txt','w')
    f.write("hier_spec = {\n")
    for c, i in enumerate(hier_structure.items()):
        string = "'/" + i[0] + "'" + ":" + ",\n".join(str(i[1]).split(", "))
        print(string)
        if c == length - 1:
            f.write(string)
        else:
            f.write(string + ",\n")
    f.close()











