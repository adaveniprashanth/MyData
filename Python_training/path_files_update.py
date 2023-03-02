import os
import pandas as pd
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
path_value = '/nfs/site/disks/xe3_clips_storage/VPP'
for i in subcategories:
    path_file = os.path.join(i,'path.txt')
    if os.path.exists(path_file):
        print(path_file)
        f= open(path_file,'w')
        f.write('INPUTPATH="/nfs/site/disks/xe3_clips_storage/VPP"'+"\n")
        f.close()