import os
import pandas as pd
if 0:#VE
    input_file_name = 'VE'
    excel_file = input_file_name+'.xls'
    gsf_clips_file = input_file_name+'_clip_paths.txt'
    full_details_file = input_file_name+'_clip_paths_full_details.txt'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)

    print("summarized_subcategories", summarized_subcategories)
    #INPUTPATH="/nfs/site/disks/xe3_clips_storage/VPP"
    for i in subcategories:
        path_file = os.path.join(i,'path.txt')
        if os.path.exists(path_file):
            print(path_file)
            f= open(path_file,'w')
            f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/VPP"'+"\n")
            f.close()


if 0:#Decoder_AV1
    input_file_name = 'Decoder_AV1'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    #INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/AV1"
    for i in subcategories:
        path_file = os.path.join(i,'path.txt')
        if os.path.exists(path_file):
            print(path_file)
            f= open(path_file,'w')
            f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/AV1"'+"\n")
            f.close()
if 0:#PAK_AVC
    input_file_name = 'PAK_AVC'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    #INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/AV1"
    for i in subcategories:
        path_file = os.path.join(i,'path.txt')
        if os.path.exists(path_file):
            print(path_file)
            f= open(path_file,'w')
            f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/PAK/AVC"'+"\n")
            f.close()

if 0:#PAK_JPEG
    input_file_name = 'PAK_JPEG'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    #INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/AV1"
    for i in subcategories:
        path_file = os.path.join(i,'path.txt')
        if os.path.exists(path_file):
            print(path_file)
            f= open(path_file,'w')
            f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/PAK/JPEG"'+"\n")
            f.close()

if 0:#PAK_AV1
    input_file_name = 'PAK_AV1'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/PAK/AV1"'+"\n")
                f.close()
    f1.close()

if 0:#Decoder_JPEG
    input_file_name = 'Decoder_JPEG'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/MFX/JPEG"'+"\n")
                f.close()
    f1.close()

if 0:#Decoder_VP8
    input_file_name = 'Decoder_VP8'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/MFX/VP8"'+"\n")
                f.close()
    f1.close()

if 0:# Decoder_HEVC
    input_file_name = 'Decoder_HEVC'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    f2=open(input_file_name+"_path_text_file_not_present_previously.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/HCP/HEVC"'+"\n")
                f.close()
            else:
                f2.write(path_file+"\n")
    f1.close()


if 0:#Decoder_AVC
    input_file_name = 'Decoder_AVC'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/MFX/AVC"'+"\n")
                f.close()
    f1.close()

if 0:#Decoder_MVC
    input_file_name = 'Decoder_MVC'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/MFX/MVC"'+"\n")
                f.close()
    f1.close()


if 0:#Decoder_MP2
    input_file_name = 'Decoder_MP2'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/MFX/MPEG/'+i.split("/",3)[-1]+'"'+"\n")
                f.close()
                print('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/MFX/MPEG/'+i.split("/",3)[-1]+'"'+"\n")
    f1.close()

#

if 0:#Decoder_VP9
    input_file_name = 'Decoder_VP9'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
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
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/DEC/HCP/VP9"'+"\n")
                f.close()
    f1.close()

if 0:# PAK_VP9_Reduced_list
    input_file_name = 'PAK_VP9_Reduced_list'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file)
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "basic" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    f2=open(input_file_name+"_path_text_file_not_present_previously.txt",'w')
    f3=open(input_file_name+"_path_files.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f3.write(path_file+"\n")
                f= open(path_file,'w')
                f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/PAK/VP9"'+"\n")
                f.close()
            else:
                f2.write(path_file+"\n")
    f1.close()
    f2.close()
    f3.close()


if 0:# updated_VDENC
    input_file_name = 'updated_VDENC'
    excel_file = input_file_name+'.xls'
    cwd=os.getcwd()
    df = pd.read_excel(excel_file,sheet_name='TestList')
    subcategories = list(df['SubCategory'])
    subcategories = [i[0:len(i) - 1] if i[-1] == "/" or i[-1] == "\\" else i for i in subcategories]
    total_sub_categories = len(subcategories)
    print("total_sub_categories", total_sub_categories)
    subcategories = [x for x in subcategories if "Media13.1" not in x]
    subcategories = list(set(subcategories))
    summarized_subcategories = len(subcategories)
    print("summarized_subcategories", summarized_subcategories)
    f1= open(input_file_name+"_paths_not_updated.txt",'w')
    f2=open(input_file_name+"_path_text_file_not_present_previously.txt",'w')
    f3=open(input_file_name+"_path_files.txt",'w')
    for i in subcategories:
        if not os.path.exists(i):
            f1.write(i+"\n")
        else:
            path_file = os.path.join(i,'path.txt')
            if os.path.exists(path_file):
                print(path_file)
                f3.write(path_file+"\n")
                f = open(path_file,'r')
                data = f.read()
                f.close()
                data = data.split("\n")[0].split("VDENC/")[1].replace('"',"")
                data = 'INPUTPATH="/nfs/site/disks/xe3_clips_storage/VDENC'+'/'+data+'"'+"\n"
                f= open(path_file,'w')
                f.write(data)
                f.close()
            else:
                f2.write(path_file+"\n")
    f1.close()
    f2.close()
    f3.close()

#************************NOT NEEDED ***********************
if 0:#VDENC1
    input_file_name = 'VDENC1'
    excel_file = input_file_name+'.xls'
    file_names = ['TestList1','TestList2']
    for file_name in file_names:
        df = pd.read_excel(excel_file,sheet_name=file_name)
        print(len(list(df.index)))
        total_rows = len(list(df.index))
        for i in range(total_rows):
            print(".".join([str(x) for x in list(df.iloc[i])]))




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


##############################NOT NEEDED #################################

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
