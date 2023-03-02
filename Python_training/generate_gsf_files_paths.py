import os
import pandas as pd
print("hello")

#print(os.getcwd())
## \UTP-Content\SFC\Legacy\Bug_coverage
#full_path =os.path.join(os.getcwd(),'UTP-Content\SFC')
#print("full_path",full_path)
#print()
#all_paths =os.listdir(full_path)
#f= open("full_details.txt",'w')
#
#'''
#all_files_in_subcategory = os.listdir(subcategory)
#            gsf_files_in_subcategory = []
#            for file in all_files_in_subcategory:
#                if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
#                    pass
#                elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
#                    pass
#                else:
#                    gsf_files_in_subcategory.append(file)
#
#'''
#
#
#
#for dirpath,dirnames,filenames in os.walk(full_path):
#    print("dirpath",dirpath)
#    # print(dirnames)
#    print("filenames",filenames)
#    print()
#    if len(filenames) == 0:
#        continue
#    gsf_files_in_subcategory = []
#    for file in filenames:
#        if "meta" in file or ".txt" in file or os.path.isdir(
#                os.path.join(dirpath, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
#            pass
#        elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
#            pass
#        elif ".exe" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file:
#            pass
#        else:
#            gsf_files_in_subcategory.append(file)
#    # f.write("dirpath "+dirpath+"\n")
#    # f.write("filenames "+str(filenames)+"\n")
#    # f.write("filenames " + str(gsf_files_in_subcategory) + "\n")
#    for i in gsf_files_in_subcategory:
#        f.write(os.path.join(dirpath,i)+"\n")
#    # f.write("\n")
#
#f.close()
#

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
f= open(excel_file+"_full_details.txt",'w')
for subcategory in subcategories:
    subcategory = subcategory.strip()
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
        continue
    for gsf_file in gsf_files_in_subcategory:
        print("gsf file",subcategory + "/" + gsf_file)
        #gsf_path = subcategory + "/" + gsf_file
        gsf_path = os.path.join(cwd,subcategory,gsf_file)
        gsf_path = gsf_path.replace("/","\\")
        f.write(gsf_path + "\n")


f.close()
