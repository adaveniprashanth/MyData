import os,sys
import os,sys,getopt
import argparse
from shutil import copyfile
from datetime import date
import zipfile
import subprocess
import glob

last_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/WW51_SOC_LNL_A0_PROD/IPX_UPLOAD/xe2lpm_media_common-22ww53e-package'
current_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/LNL_B0_DROP/IPX_UPLOAD/xe3lpm_media_common-23ww13e-package'

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


log_file = 'log.txt'
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
	os.remove(os.path.join(os.getcwd(), log_file))

reference_include = os.path.join(last_drop, last_drop_smedia,'source/includes')
source_include = os.path.join(current_drop, current_drop_smedia,'source/includes')

print("checking the differenced files in includes folder")
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
	os.system("diff -r " + source_include + " " + reference_include + " >> log.txt")
else:
	os.system("diff -r " + source_include + " " + reference_include + " > log.txt")
reference_rtl = os.path.join(last_drop,last_drop_smedia, 'source/rtl/src')
source_rtl = os.path.join(current_drop, current_drop_smedia,'source/rtl/src')
print("checking the differenced files in rtl/src folder")
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
	os.system("diff -r " + source_rtl + " " + reference_rtl + " >> log.txt")
else:
	os.system("diff -r " + source_rtl + " " + reference_rtl + " > log.txt")

today = date.today()
d1 = today.strftime("%Y%m%d")


includes_folder ='smedia_top/source/includes'
if not os.path.isdir(os.path.join(os.getcwd(), includes_folder)):
	os.makedirs(includes_folder)
rtl_folder = 'smedia_top/source/rtl/src'
if not os.path.isdir(os.path.join(os.getcwd(), rtl_folder)):
	os.makedirs(rtl_folder)

new_file = open('updated_log.txt', 'w')
with open(log_file, 'r') as f1:
	content = f1.readlines()
for i in content:
	if i.startswith('diff -r'):
		if rtl_folder in i.split(" ")[2]:
			new_file.write("rtl folder "+i.split(" ")[2].split("/")[-1] + " present in both drops\n")
			copyfile(i.split(" ")[2], rtl_folder + "/" + i.split(" ")[2].split("/")[-1])
		if includes_folder in i.split(" ")[2]:
			new_file.write("includes folder "+i.split(" ")[2].split("/")[-1] + " present in both drops\n")
			copyfile(i.split(" ")[2], includes_folder + "/" + i.split(" ")[2].split("/")[-1])
	elif i.startswith('Only in'):
		if current_drop in i:
			if rtl_folder in i:
				new_file.write("rtl folder "+i.strip().replace(": ", "/").split("/")[-1] + " present in current drop\n")
				copyfile(i.strip().replace(": ", "/").split(" ")[2],rtl_folder + "/" + i.strip().replace(": ", "/").split("/")[-1])
			elif includes_folder in i:
				new_file.write("includes folder "+i.strip().replace(": ", "/").split("/")[-1] + " present in current drop\n")
				print(i)
				copyfile(i.strip().replace(": ", "/").split(" ")[2],includes_folder + "/" + i.strip().replace(": ", "/").split("/")[-1])
		elif last_drop in i:
			new_file.write(i.strip().replace(": ", "/").split("/")[-1] + " present in last drop\n")

new_file.close()

def zipdir(path, ziph):
	# ziph is zipfile handle
	for root, dirs, files in os.walk(path):
		for f in files:
			ziph.write(os.path.join(root, f),os.path.relpath(os.path.join(root, f),os.path.join(path, '..')))

print("creating the zip folder")
with zipfile.ZipFile('hotpatch_'+d1+'.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
	zipdir('smedia_top/', zipf)

