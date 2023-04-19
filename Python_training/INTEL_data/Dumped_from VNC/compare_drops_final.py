import os,sys
import os,sys,getopt
import argparse
from shutil import copyfile
from datetime import date
import zipfile
import subprocess
import glob

'''
if len(sys.argv) <3  or not sys.argv[1].startswith('/nfs/site') or not sys.argv[2].startswith('/nfs/site'):
    print("sample command is -->  python compare_drops.py <last_drop_path> <current_drop_path>")
    sys.exit("please try again with more details")
    sys.exit(2)
'''
#last_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/WW51_SOC_LNL_A0_PROD/IPX_UPLOAD/xe2lpm_media_common-22ww53e-package'
#current_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/LNL_B0_DROP/IPX_UPLOAD/xe3lpm_media_common-23ww13e-package'
last_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/elg/ELG_SOC_1p0_Prod/IPX_package/elg_media_common_23ww04e-package'
current_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/elg/BMG_X2_1p0_pre/IPX_upload/BMGX2_media_common_23ww15d-package'

'''
last_drop = sys.argv[1].strip()
current_drop = sys.argv[2].strip()
'''
last_drop_smedia = ''
temp = ''
for file in glob.glob(os.path.join(last_drop,'sm*')):
    temp = file
    print("last drop smedia folder name is ",temp)
last_drop_smedia = os.path.basename(temp)

current_drop_smedia = ''
temp = ''
for file in glob.glob(os.path.join(current_drop,'sm*')):
    temp = file
    print("current drop smedia folder name is ",temp)
current_drop_smedia = os.path.basename(temp)


#Finding the differnces in inlcludes folder data between current and last drops
log_file = 'diff_data_includes.txt'
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
	os.remove(os.path.join(os.getcwd(), log_file))
	print("deleted old "+log_file)

last_drop_include = os.path.join(last_drop, last_drop_smedia,'source/includes')
current_drop_include = os.path.join(current_drop, current_drop_smedia,'source/includes')
print("checking the differenced files in includes folder")
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
    os.system("diff -r " + current_drop_include + " " + last_drop_include + " >> "+log_file)
else:
    os.system("diff -r " + current_drop_include + " " + last_drop_include + " > "+log_file)

#Finding the differnces in inlcludes folder data between current and last drops
log_file = 'diff_data_rtl.txt'
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
	os.remove(os.path.join(os.getcwd(), log_file))
	print("deleted old "+log_file)

last_drop_rtl = os.path.join(last_drop,last_drop_smedia, 'source/rtl/src')
current_drop_rtl = os.path.join(current_drop, current_drop_smedia,'source/rtl/src')

print("checking the differenced files in rtl/src folder")
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
	os.system("diff -r " + current_drop_rtl + " " + last_drop_rtl + " >> "+log_file)
else:
	os.system("diff -r " + current_drop_rtl + " " + last_drop_rtl + " > "+log_file)

############ comparing drops completed #################

f = open('diff_data_includes.txt','r')
lines = f.readlines()
f.close()

f = open('diff_includes_full_paths.txt','w')
f1 = open('diff_includes.txt','w')
for line in lines:
    if line.startswith('diff -r'):
        line = line.strip().split(" ")
        f.write(line[2]+"\n")
        f1.write(line[2].strip().split("/")[-1]+"\n")

    elif line.startswith('Only in '):
        line = line.strip().split(" ")
        f.write(line[2][0:-1]+"/"+line[3].strip()+"\n")
        f1.write(line[3].strip()+"\n")

f.close()
f1.close()

f = open('diff_data_rtl.txt','r')
lines = f.readlines()
f.close()

f = open('diff_rtl_full_paths.txt','w')
f1 = open('diff_rtl.txt','w')
for line in lines:
    if line.startswith('diff -r'):
        line = line.strip().split(" ")
        f.write(line[2]+"\n")
        f1.write(line[2].strip().split("/")[-1]+"\n")

    elif line.startswith('Only in '):
        line = line.strip().split(" ")
        f.write(line[2][0:-1]+"/"+line[3].strip())
        f1.write(line[3].strip()+"\n")

f.close()
f1.close()

################################Completed the file names extraction #######################

f = open('diff_includes_full_paths.txt','r')
lines = f.readlines()
f.close()
lines = [x.strip() for x in lines]
res = open('diff_includes_rm_timedate.txt','w')
for line in lines:
    current_drop_file = line
    last_drop_file = line.replace(current_drop,last_drop)
    if os.path.isfile(last_drop_file):
        os.system("diff -r "+current_drop_file+" "+last_drop_file + "> abc.txt")
        f = open('abc.txt','r')
        l = f.readlines()
        f.close()
        data = "".join(l)
        if len(l) == 4 and '/// Copyright' not in data and 'Creation Date' not in data and '// MacroInsert begin: Bottom included from' not in data:
            line = line.strip().split("/")[-1]
            res.write(line+"\n")
            print("data",data)
            print("length",len(l))
            print("writing the file name "+line+"\n\n\n")
        elif len(l) > 4 and '/nfs/site' not in data and 'Creation Date' not in data:
            line = line.strip().split("/")[-1]
            res.write(line+"\n")
            print("data",data)
            print("length",len(l))
            print("writing the file name "+line+"\n\n\n")
        elif len(l) < 4:
            line = line.strip().split("/")[-1]
            res.write(line+"\n")


    else:
        line = line.strip().split("/")[-1]
        res.write(line+"\n")
        print("file not present in last drop ",last_drop_file)
res.close()


f = open('diff_rtl_full_paths.txt','r')
lines = f.readlines()
f.close()
lines = [x.strip() for x in lines]
res = open('diff_rtl_rm_timedate.txt','w')
for line in lines:
    current_drop_file = line
    last_drop_file = line.replace(current_drop,last_drop)
    if os.path.isfile(last_drop_file):
        os.system("diff -r "+current_drop_file+" "+last_drop_file + "> abc.txt")
        f = open('abc.txt','r')
        l = f.readlines()
        f.close()
        data = "".join(l)
        if len(l) == 4 and '/// Copyright' not in data and 'Creation Date' not in data and '// MacroInsert begin: Bottom included from' not in data:
            line = line.strip().split("/")[-1]
            res.write(line+"\n")
            print("data",data)
            print("length",len(l))
            print("writing the file name "+line+"\n\n\n")
        elif len(l) > 4 and '/nfs/site' not in data and 'Creation Date' not in data:
            line = line.strip().split("/")[-1]
            res.write(line+"\n")
            print("data",data)
            print("length",len(l))
            print("writing the file name "+line+"\n\n\n")
        elif len(l) < 4:
            line = line.strip().split("/")[-1]
            res.write(line+"\n")

    else:
        print("current drop file ",line)
        line = line.strip().split("/")[-1]
        res.write(line+"\n")
        print("file not present in last drop ",last_drop_file)
res.close()

#converting the result files into excel sheet
#os.system("perl "+"convert_to_excel.pl")








