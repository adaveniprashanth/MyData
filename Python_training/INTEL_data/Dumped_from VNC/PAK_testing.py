import os,time
import pandas as pd
import shutil
from shutil import copyfile
from os import system

# PAK_JPEG clip paths extraction(Extraction)
if 0:
    input_file_name = 'PAK_JPEG'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("path file", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file", gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "yuvname =" not in data or "bitstreamname =" not in data:
                    print("gsf file having no clip")
                    gsf_file_with_no_clip.append(gsf_path)
                    print(gsf_files_in_subcategory)
                    continue
                l = data.split("\n")
                for j in l:
                    if 'yuvname =' in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("yuvname -> " + whole_clip_path + "\n")
                        print("whole path", whole_clip_path+"\n")
                    elif 'bitstreamname =' in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("bitstreamname -> " + whole_clip_path + "\n")
                        print("whole path", whole_clip_path + "\n")

    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()

# VDAQM clip paths extraction(Extraction)
if 0:
    input_file_name = 'VDAQM'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = [x for x in subcategories if "\ATS\\" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("path file", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file or ".ayuv" in file:
                    pass
                elif ".yu12" in file or ".csv" in file or ".pl" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file", gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "yuvname =" not in data:
                    print("gsf file having no clip")
                    gsf_file_with_no_clip.append(gsf_path)
                    print(gsf_files_in_subcategory)
                    continue
                l = data.split("\n")
                for j in l:
                    if 'yuvname =' in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("yuvname -> " + whole_clip_path + "\n")
                        print("whole path", whole_clip_path+"\n")
                    elif 'bitstreamname =' in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("bitstreamname -> " + whole_clip_path + "\n")
                        print("whole path", whole_clip_path + "\n")

    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()

# VDENC clip paths extraction(Extraction)
if 0:
    input_file_name = 'VDENC'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = [x for x in subcategories if "VDEnc\Media13.1\\" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("path file", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file or ".ayuv" in file:
                    pass
                elif ".yu12" in file or ".csv" in file or ".pl" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file", gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "yuvname =" not in data:
                    print("gsf file having no clip")
                    gsf_file_with_no_clip.append(gsf_path)
                    print(gsf_files_in_subcategory)
                    continue
                l = data.split("\n")
                for j in l:
                    if 'yuvname =' in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("yuvname -> " + whole_clip_path + "\n")
                        print("whole path", whole_clip_path+"\n")
                    elif 'bitstreamname =' in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("bitstreamname -> " + whole_clip_path + "\n")
                        print("whole path", whole_clip_path + "\n")

    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()

# PAK_AV1 clip paths extraction(REFERENCE)
if 0:
    input_file_name = 'PAK_AV1'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("path file", path_file)
        full_details.write("path.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file", gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")
                os.system("cat " + gsf_path + " > log.txt")
                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "encoder.source_file_name" not in data:
                    print("gsf file having no clip")
                    gsf_file_with_no_clip.append(gsf_path)
                    continue
                l = data.split("\n")
                for j in l:
                    if 'encoder.source_file_name' in j:# for others #if 'clipFileName =' in j: for decoder_VP9
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")
    print("path files not found-> ", path_file_not_found)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> " + str(gsf_file_with_no_clip).replace(", ", "\n") + "\n")
    full_details.close()

# PAK_AVC clip paths extraction(Extraction)
if 0:
    input_file_name = 'PAK_AVC'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("path file", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file", gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "encoder.source_file_name" not in data and 'encoder.source_names' not in data:
                    print("gsf file having no clip")
                    gsf_file_with_no_clip.append(gsf_path)
                    print(gsf_files_in_subcategory)
                    continue
                l = data.split("\n")
                for j in l:
                    if 'encoder.source_file_name' in j:# for others #if 'clipFileName =' in j: for decoder_VP9
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")
                    if ':encodedInputFile' in j and '"' in j:# for others #if 'clipFileName =' in j: for decoder_VP9
                        clipname = j.split("=>")[1].strip().replace("\"", "").replace(",","")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")
                    if "encoder.source_names" in j:
                        clipnames = j.split("=")[1].strip().replace("[","").replace("]","")
                        clipnames = clipnames.replace("\"","").split(", ")
                        print("clipnames",clipnames)
                        for clipname in clipnames:
                            print("clipname-->", clipname)
                            full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                            whole_clip_path = os.path.join(clip_path, clipname)
                            clips_file.write(whole_clip_path + "\n")
                            full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                            print("whole path", whole_clip_path + "\n")
    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()

# PAK_VP9 clip paths extraction(Extraction)
if 0:
    input_file_name = 'PAK_VP9'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [x.strip() for x in subcategories]
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("\npath file", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file",subcategory + "/" + gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "encoder.source_file_name" not in data:
                    if "encoder.source_names" not in data:
                        print("gsf file having no clip")
                        gsf_file_with_no_clip.append(gsf_path)
                        print(gsf_files_in_subcategory)
                        continue
                l = data.split("\n")
                for j in l:
                    if 'encoder.source_file_name' in j:# for others #if 'clipFileName =' in j: for decoder_VP9
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")
                    elif "encoder.source_names" in j:
                        clipnames = j.split("=")[1].strip().replace("[","").replace("]","")
                        clipnames = clipnames.replace("\"","").split(", ")
                        print("clipnames",clipnames)
                        for clipname in clipnames:
                            print("clipname-->", clipname)
                            full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                            whole_clip_path = os.path.join(clip_path, clipname)
                            clips_file.write(whole_clip_path + "\n")
                            full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                            print("whole path", whole_clip_path + "\n")

    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()

# SFC clip paths extraction not completed
if 0:
    input_file_name = 'SFC'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("path fille", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file", gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "SourceClip" not in data:
                    print("gsf file having no clip")
                    clips_file.write(clip_path+"\n")
                    gsf_file_with_no_clip.append(gsf_path)
                    print(gsf_files_in_subcategory)
                    continue
                l = data.split("\n")
                for j in l:
                    if 'SourceClip' in j:# for others #if 'clipFileName =' in j: for decoder_VP9
                        clipname = j.split("=>")[1].strip().replace("\"", "").replace(",","")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")
    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()

# VE clip paths extraction not completed
if 0:
    input_file_name = 'VE'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("path fille", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file", gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "SourceClip" not in data:
                    print("gsf file having no clip")
                    clips_file.write(clip_path+"\n")
                    gsf_file_with_no_clip.append(gsf_path)
                    print(gsf_files_in_subcategory)
                    continue
                l = data.split("\n")
                for j in l:
                    if 'SourceClip' in j:# for others #if 'clipFileName =' in j: for decoder_VP9
                        clipname = j.split("=>")[1].strip().replace("\"", "").replace(",","")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")
    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()

# HEVC_PAK_Reduced_list clip paths extraction(Extraction)
if 0:
    input_file_name = 'HEVC_PAK_Reduced_list'
    excel_file = input_file_name+'.xlsx'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("\npath file", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file",subcategory + "/" + gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "encoder.source_file_name" not in data:
                    if "encoder.source_names" not in data:
                        print("gsf file having no clip")
                        gsf_file_with_no_clip.append(gsf_path)
                        continue
                l = data.split("\n")
                for j in l:
                    if 'encoder.source_file_name' in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")
                    elif "encoder.source_names" in j:
                        clipnames = j.split("=")[1].strip().replace("[","").replace("]","")
                        clipnames = clipnames.replace("\"","").split(", ")
                        print("clipnames",clipnames)
                        for clipname in clipnames:
                            print("clipname-->", clipname)
                            full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                            whole_clip_path = os.path.join(clip_path, clipname)
                            clips_file.write(whole_clip_path + "\n")
                            full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                            print("whole path", whole_clip_path + "\n")
                    elif 'bitstreamname' in j and ":" not in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")

    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-7> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()

# VP9_PAK_Reduced_list clip paths extraction(Extraction)
if 0:
    #input_file_name = 'VP9_PAK_Reduced_list'
    input_file_name = 'VP9_PAK_Reduced_list_new'
    excel_file = input_file_name+'.xlsx'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    print(os.getcwd())
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [x.strip() for x in subcategories]
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    clips_file = open(gsf_clips_file, 'w')
    full_details = open(full_details_file, 'w')
    full_details.write("*** FOR SUMMARY GO TO END OF FILE ***\n")
    path_file_not_found = []
    pathfile_having_no_input=[]
    path_with_no_gsf_files =[]
    gsf_file_not_found = []
    gsf_file_with_no_clip = []
    for subcategory in subcategories:
        subcategory = subcategory.strip()
        path_file = subcategory + "/path.txt"
        try:
            f = open(path_file, 'r')
            text = f.read()
            f.close()
        except FileNotFoundError:
            path_file_not_found.append(path_file)
            continue
        print("\npath file", path_file)
        full_details.write("\npath.txt path-> " + path_file + "\n")
        paths = text.splitlines()

        paths = [x for x in paths if "Fulsim_include" not in x]
        paths = [x for x in paths if "fm5SVlab126" not in x]
        paths = [x for x in paths if "UTP - Content" not in x]
        paths = [x for x in paths if "UTP-Content" not in x]
        # \\fmsgfxauto5\test2$\Global_IP_Sync\Execution\Testfiles\media\content_include
        paths = [x for x in paths if len(x) > 2]
        paths = [x for x in paths if "./" not in x]

        if(len(paths)<=0):
            pathfile_having_no_input.append(path_file)
            continue
        for line in paths:
            clip_path = line.strip().split("=")[1].replace("\"", "")
            print("clip path", clip_path)
            full_details.write("clip path-> " + clip_path + "\n")
            all_files_in_subcategory = os.listdir(subcategory)
            gsf_files_in_subcategory = []
            for file in all_files_in_subcategory:
                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                    pass
                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
                    pass
                else:
                    gsf_files_in_subcategory.append(file)
            if len(gsf_files_in_subcategory) == 0:
                print("path "+subcategory+" contain no gsf files ")
                path_with_no_gsf_files.append(subcategory)
                continue
            for gsf_file in gsf_files_in_subcategory:
                print("gsf file",subcategory + "/" + gsf_file)
                gsf_path = subcategory + "/" + gsf_file
                # gsf_path = gsf_path.replace("/","\\")

                full_details.write("gsf file-> " + gsf_path + "\n")
                try:
                    os.system("cat " + gsf_path + " > log.txt")
                    f = open('log.txt', 'r')
                    data = f.read()
                    f.close()
                except FileNotFoundError:
                    gsf_file_not_found.append(gsf_path)
                    continue
                if "encoder.source_file_name" not in data:
                    if "encoder.source_names" not in data:
                        print("gsf file having no clip")
                        gsf_file_with_no_clip.append(gsf_path)
                        print(gsf_files_in_subcategory)
                        continue
                l = data.split("\n")
                for j in l:
                    if 'encoder.source_file_name' in j:# for others #if 'clipFileName =' in j: for decoder_VP9
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")
                    elif "encoder.source_names" in j:
                        clipnames = j.split("=")[1].strip().replace("[","").replace("]","")
                        clipnames = clipnames.replace("\"","").split(", ")
                        print("clipnames",clipnames)
                        for clipname in clipnames:
                            print("clipname-->", clipname)
                            full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                            whole_clip_path = os.path.join(clip_path, clipname)
                            clips_file.write(whole_clip_path + "\n")
                            full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                            print("whole path", whole_clip_path + "\n")
                    elif 'bitstreamname' in j and ":" not in j:
                        clipname = j.split("=")[1].strip().replace("\"", "")
                        print("clipname-->", clipname)
                        full_details.write("clipname from gsf file-> " + clipname + "\n\n")
                        whole_clip_path = os.path.join(clip_path, clipname)
                        clips_file.write(whole_clip_path + "\n")
                        full_details.write("whole clip path-> " + whole_clip_path + "\n\n")
                        print("whole path", whole_clip_path+"\n")

    print("path files not found-> ", path_file_not_found)
    print("pathfile having no input",pathfile_having_no_input)
    print("path with no gsf files", path_with_no_gsf_files)
    print("gsf files not found-> ", gsf_file_not_found)
    print("gsf files with no clip-> ", gsf_file_with_no_clip)

    clips_file.close()
    full_details.write("input_file_name-> "+input_file_name+".xls\n")
    full_details.write("total_sub_categories-> "+str(total_sub_categories)+"\n")
    full_details.write("summarized_subcategories-> "+str(summarized_subcategories)+"\n")
    full_details.write("path files not found-> " + str(path_file_not_found).replace(", ","\n") + "\n")
    full_details.write("pathfile having no input-> "+str(pathfile_having_no_input).replace(", ","\n") + "\n")
    full_details.write("path with no gsf files"+str(path_with_no_gsf_files).replace(", ","\n")+"\n")
    full_details.write("gsf files not found-> " + str(gsf_file_not_found).replace(", ","\n") + "\n")
    full_details.write("gsf files with no clip-> "+str(gsf_file_with_no_clip).replace(", ","\n") + "\n")
    full_details.close()




