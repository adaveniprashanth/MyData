import os
import shutil
from shutil import copyfile

print("hello remote")
print(os.getcwd())
# remote_path = "Z:\clip_paths"+"/"
#
# all_files = os.listdir(os.getcwd())
# clip_paths = [x for x in all_files if "clip_paths.txt" in x]
# full_details = [x for x in all_files if "full_details.txt" in x]
# print(all_files)
# print("clip paths",clip_paths)
# print("full details", full_details)

# if not os.path.exists(os.getcwd()+"/"+"clip_paths"):
#     os.mkdir("clip_paths")

# for x in all_files:
#     copyfile(x,"clip_paths/"+x)
# os.chdir('clip_paths')
# print(os.getcwd())
# all_clip_paths = os.listdir(os.getcwd())
# all_clip_paths = [x for x in all_clip_paths if "full_details.txt" in x]
# # Z:\clip_paths

# for x in all_clip_paths:
#     copyfile(x,remote_path+x)

# # copying clip_paths
# for x in clip_paths:
#     print("copying ",x)
#     copyfile(x,remote_path+x)
#
# # copying full details
# for x in full_details:
#     print("copying ", x)
#     copyfile(x,remote_path+x)

# all_files = os.listdir(os.getcwd())
# reduced_list = [x for x in all_files if "Reduced_list" in x]
# reduced_list = [x for x in reduced_list if ".xlsx" not in x]
# for x in reduced_list:
#     print("copying ", x)
#     copyfile(x,remote_path+x)

if 0:
    pass
    # /nfs/site/disks/arl_gt_disk2/WW05P4
    # remote_path = "Y:\\"
    # print(os.listdir(remote_path))
    #
    # path = "/nfs/site/disks/sc6_hbudidhx/WW54P1_RS/val0/HWFE/ARLP_WW54P1/gt/ARL_2X4X16_SD.o3c.vpi.goldenrpt.default64/REGRESS_OUTPUT/executeIndirectLoop_CFG41"
    # new_path =path.replace("REGRESS_OUTPUT","LOGFILES")
    # filename =new_path.replace("/nfs","Y:")
    # f = open(filename,'r')
    # a = f.read()
    # f.close()
    # a = a.split("\n")
    #
    # for i in a:
    #     if "CPU time" in i:
    #         print(i)
    #
    # # print(a)
