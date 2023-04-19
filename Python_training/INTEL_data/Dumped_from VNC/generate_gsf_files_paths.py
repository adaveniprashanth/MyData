import os
import pandas as pd
print("hello")


input_file_name = 'VDENC'
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
f= open(input_file_name+"_full_details.txt",'w')
f1= open(input_file_name+"_paths_not_in_perforce.txt",'w')
for subcategory in subcategories:
    if not os.path.exists(subcategory):
        f1.write(subcategory+"\n")
    else:
        subcategory = subcategory.strip()
        all_files_in_subcategory = os.listdir(subcategory)
        gsf_files_in_subcategory = []
        for file in all_files_in_subcategory:
            if "meta" in file or ".txt" in file or os.path.isdir(os.path.join(subcategory, file)) or ".bsf" in file or ".par" in file or '.nv12' in file:
                pass
            elif ".json" in file or ".av1" in file or ".pl" in file or ".p010" in file or ".bin" in file or ".jpg" in file or ".py" in file:
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
            #print(gsf_path.split("\\"))
            f.write(gsf_path + "\n")
f.close()
f1.close()