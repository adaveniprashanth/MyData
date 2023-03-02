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
        df = pd.read_excel('Logistic.xlsx',sheet_name=['module_parent'])#accessing sheet by names
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
    '''f.write("\nmissed modules in hirerarchy are\n")
    for c,i in enumerate(missed_in_hierarchy):
        f.write(i+",")
        if c%4 == 0:
            f.write("\n")'''
    f.close()


# gtmctoremove1  code to fetch dfx_insert1 and dfx_tieoff1 modules
if 0:
    def get_instances_hierarchy():
        instances = []
        with open('extend_gtmctoremove1.txt', 'r') as f:
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
    f = open('final.txt','w')
    f.write("hier_spec = {\n")
    for c, i in enumerate(hier_structure.items()):
        string = "'/" + i[0] + "'" + ":" + ",\n".join(str(i[1]).split(", "))
        print(string)
        if c == length - 1:
            f.write(string)
        else:
            f.write(string + ",\n")
    f.close()









if 0:
    # count the duplicated values in list
    l = [1,2,3,1,3,4,2,4,2,4,2,3,5,4,3,6,5,4,7,3,4,3,2,6]
    d = {}
    for i in l:
        d[i]=d.get(i,0)+1
    print(d)

# MP2 gsf files path creation
if 0:
    input_file = 'Decoder_MP2_50_tests'
    output_file = input_file + 'clip_paths.txt'
    excel_file = input_file + '.xls'
    df = pd.read_excel(excel_file)
    subcategories =list(df['SubCategory'])
    print(os.getcwd())
    os.chdir("../../../../../")
    current_path = os.getcwd()
    print("cwd",current_path)
    local_path = 'Perforce_folder/genGraphics/validation/tests/main/media'

    f1 = open(output_file,'w')
    for i in subcategories:
        path = os.path.join(current_path, local_path, i)
        print("subcategory --> ",i)
        print("files in subcategory-->",os.listdir(path))
        f = open(path+"/"+i.split("/")[-1]+".gsf")
        l = f.readlines()
        f.close()
        for j in l:
            if 'clipFileName' in j:
                clipname = j.split("=")[1].split("#")[0].strip().replace("\"","")
                print("clipname-->",clipname)
        f = open(path + '/path.txt')
        clip_path = f.readline().strip().split("=")[1].replace("\"","")
        f.close()
        print("path for clip",clip_path)
        whole_clip_path = os.path.join(clip_path,clipname)
        print("whole_clip_path",whole_clip_path)
        f1.write(whole_clip_path+"\n")

    f1.close()

    print("\noutput file*** "+output_file+" **present at ",os.getcwd())

def copy_files():
    destination = '/nfs/site/disks/xe3_clips_storage/Decoder/MFX/MPEG'
    f = open(output_file,'r')
    l = f.readlines()
    print(os.getcwd())
    for i in l[0:2]:
        clipname = i.strip().split("\\")[-1]
        print(clipname)
        dest_path = destination+"/"+clipname
        source = i.strip()
        print(source)
        print(dest_path)
        # shutil.copyfile(source,dest_path)



if 0:
    multiple_inputpath_path_file = []
    subcategory_contain_basic = []
    input_file = 'Decoder_HEVC'
    output_file = input_file + '_clip_paths.txt'
    excel_file = input_file + '.xls'
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    print("total sub categories",len(subcategories))
    subcategories = list(set(subcategories))
    basics = [x for x in subcategories if "basic" in x]
    subcategories = [x for x in subcategories if "basic" not in x]
    print(os.getcwd())
    os.chdir("../../../../../")
    current_path = os.getcwd()
    local_path = 'Perforce_folder\genGraphics\\validation\\tests\main\media'

    f1 = open(output_file, 'w')
    f2 = open("missed"+output_file,'w')
    counter = 0
    '''subcategories = ['UTP-Content/Decoder/HEVC/422/10bit/Allegro/Syntax_Main422_v5191',
    'UTP-Content/Decoder/HEVC/444/12bit/Stress/Stress_HEVC_Rext444_12bHT62_1920x1080_30fps_301_intra_stress_2.4.0',
    'UTP-Content/Decoder/HEVC/420/8bit/Allegro/Syntax/Allegro_HEVC_Main_HT50_INTER_06_192x200_a_60Hz_3.4',
    'UTP-Content/Decoder/HEVC/444/12bit/Stress/Syntax_HEVC_Rext444_12bHT62_1920x1080_30fps_104_inter_2.4.0',
    'UTP-Content/Decoder/HEVC/444/12bit/Stress/Syntax_HEVC_Rext444_12bHT62_1920x1080_30fps_009_intra_2.4.0',
    'UTP-Content/Decoder/HEVC/444/12bit/Stress/Syntax_HEVC_Rext444_12bHT62_1920x1080_30fps_116_inter_2.4.0',
    'UTP-Content/Decoder/HEVC/422/10bit/Stress',
    'UTP-Content/Decoder/HEVC/420/8bit/Allegro/Syntax/Allegro_HEVC_Main_HT50_SMALLRES_01_96x192_a_60Hz_2.0',
    'UTP-Content/Decoder/HEVC/420/8bit/Allegro/Syntax/Allegro_HEVC_Main_HT50_INTER_16_1920x1080_a_60Hz_3.0',
    'UTP-Content/Decoder/HEVC/420/8bit/Allegro/Syntax/Allegro_HEVC_Main_HT50_TILE_00_3840x2160_a_30Hz_3.0',
    'UTP-Content/Decoder/HEVC/420/10bit/Stress']'''
    for i in subcategories:
        counter += 1
        print("loop start")
        print("counter",counter)
        print(i)
        i = i.replace("/","\\")
        if i[-1] == "\\": i = i[0:len(i) - 1]
        path = os.path.join(current_path, local_path, i)

        f = open(path + '\\path.txt')
        total = f.read()
        f.close()
        print("total",total)

        if total.count("INPUTPATH") != 1:
            multiple_inputpath_path_file.append(i + "/path.txt")
            multiple_inputpath_path_file = list(set(multiple_inputpath_path_file))
            print("multiple paths", len(multiple_inputpath_path_file))
        else:
            all_lines = total.split("\n")
            all_lines = [x for x in all_lines if len(x) > 2]
            print("all lines",all_lines)

            clip_path = ''
            for line in all_lines:
                if "INPUTPATH" in line:
                    clip_path = line.strip().split("=")[1].replace("\"", "")
                    print("path for clip", clip_path)

                    all_files_in_path = os.listdir(path)
                    gsf_files = []
                    print("total files",len(all_files_in_path))
                    for item in all_files_in_path:
                        if "meta" in item or ".txt" in item or os.path.isdir(os.path.join(path,item)):
                            pass
                        else:
                            gsf_files.append(item)
                    print("total gsf files ",len(gsf_files))

                    for gsf_file in gsf_files:
                        gsf_path = os.path.join(path,gsf_file)
                        print("gsf path",gsf_path)
                        if os.path.exists(gsf_path):
                            try:
                                f = open(gsf_path, 'r')
                                l = f.readlines()
                                f.close()
                            except PermissionError:
                                # f2.write("path "+i+"\n")
                                # f2.write(str(gsf_files)+"\n")
                                # f2.write("gsf file "+gsf_file+"\n")
                                f2.write("not able to open "+gsf_path+"\n")
                                continue

                            for j in l:
                                if 'clipFileName' in j:
                                    clipname = j.split("=")[1].split("#")[0].strip().replace("\"", "")
                                    print("clipname-->", clipname)

                            whole_clip_path = os.path.join(clip_path, clipname)
                            print("path",path)
                            print("whole clip path",whole_clip_path)
                            # f1.write("gsf file "+gsf_file+"\n")
                            # f1.write("clips name " + clipname + "\n")
                            # f1.write("whole clip path "+whole_clip_path + "\n")
                            f1.write(whole_clip_path + "\n")

                        else:
                            # f2.write("file " + gsf_path + " not exists\n")
                            print("file " + gsf_path + " not exists")
                            f2.write(gsf_path+"\n")



    f1.close()
    f2.close()

    print("\noutput file*** " + output_file + " **present at ", os.getcwd())
    print("total basics",len(basics))

if 0:
    multiple_inputpath_path_file = []
    subcategory_contain_basic = []
    input_file = 'Decoder_HEVC'
    output_file = input_file + '_clip_paths.txt'
    excel_file = input_file + '.xls'
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])

    subcategories = list(set(subcategories))
    basics = [x for x in subcategories if "basic" in x]
    subcategories = [x for x in subcategories if "basic" not in x]
    # print(os.getcwd())
    os.chdir("C:\\Users\padavenx\\OneDrive - Intel Corporation\\Desktop\\Perforce_folder\\genGraphics\\validation\\tests\main\\media")
    current_path = os.getcwd()
    # print(current_path)

    # local_path = 'Perforce_folder\genGraphics\\validation\\tests\main\media'

    f1 = open(output_file, 'w')
    f2 = open("missed"+output_file,'w')
    counter = 0
    for i in subcategories:
        counter += 1
        # print("loop start")
        print("counter",counter)
        print("path",i)
        i = i.replace("/","\\")
        if i[-1] == "\\": i = i[0:len(i) - 1]
        path = os.path.join(current_path, i)

        f = open(path + '\\path.txt')
        total = f.read()
        f.close()
        # print("total",total)

        if total.count("INPUTPATH") != 1:
            multiple_inputpath_path_file.append(i + "/path.txt")
            multiple_inputpath_path_file = list(set(multiple_inputpath_path_file))
            # print("multiple paths", len(multiple_inputpath_path_file))
        else:
            all_lines = total.split("\n")
            all_lines = [x for x in all_lines if len(x) > 2]
            print("all lines",all_lines)

            clip_path = ''
            for line in all_lines:
                if "INPUTPATH" in line:
                    clip_path = line.strip().split("=")[1].replace("\"", "")
                    # print("path for clip", clip_path)

                    print("path",path)
                    all_files_in_path = os.listdir(path)
                    gsf_files = []
                    print("total files",len(all_files_in_path))
                    for item in all_files_in_path:
                        if "meta" in item or ".txt" in item or os.path.isdir(os.path.join(path,item)):
                            pass
                        else:
                            gsf_files.append(item)
                    print("total gsf files ",len(gsf_files))

                    for gsf_file in gsf_files:
                        gsf_path = os.path.join(path,gsf_file)
                        print("gsf path",gsf_path)
                        if os.path.exists(gsf_path):
                            try:
                                f = open(gsf_path, 'r')
                                l = f.readlines()
                                f.close()
                            except PermissionError:
                                # f2.write("path "+i+"\n")
                                # f2.write(str(gsf_files)+"\n")
                                # f2.write("gsf file "+gsf_file+"\n")
                                f2.write("not able to open "+gsf_path+"\n")
                                continue

                            for j in l:
                                if 'clipFileName' in j:
                                    clipname = j.split("=")[1].split("#")[0].strip().replace("\"", "")
                                    print("clipname-->", clipname)

                            whole_clip_path = os.path.join(clip_path, clipname)
                            print("path",path)
                            print("whole clip path",whole_clip_path)
                            # f1.write("gsf file "+gsf_file+"\n")
                            # f1.write("clips name " + clipname + "\n")
                            # f1.write("whole clip path "+whole_clip_path + "\n")
                            f1.write(whole_clip_path + "\n")

                        else:
                            # f2.write("file " + gsf_path + " not exists\n")

                            print("file " + gsf_path + " not exists")
                            f2.write("path "+path+"\n")
                            f2.write(gsf_path+"\n")
                            



    f1.close()
    f2.close()

    print("\noutput file*** " + output_file + " **present at ", os.getcwd())
    print("total basics",len(basics))
