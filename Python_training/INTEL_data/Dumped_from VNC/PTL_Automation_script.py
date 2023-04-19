import os,sys,getopt
import argparse
from shutil import copyfile
from datetime import date
import zipfile
import subprocess
import glob

folder_name = "not given"
reference_path = "not given"
pull_path = "not given"

def myfunc(argv):
	global folder_name
	global reference_path
	global pull_path

        #arg_help = "{0} -f <repo_folder_name> -n <project_name> -p <path_where_to_execute>".format(argv[0])
	arg_help = """{0} -f <repo_folder_name> -p <model_path_to_pull> -r <reference_package_path>\nsample command
        python  test.py -f 'ww52_prashanth_practice' -p '/nfs/data/...' -r '/nfs/data'""".format(argv[0])
        
	try:
		opts, args = getopt.getopt(argv[1:], "h:f:p:r:", ["help", "foldername=",
		"pathtopull=", "referencepackagepath="])
	except:
        	print(arg_help)
        	sys.exit(2)
        
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print(arg_help)
			print("sample command")
			print("python test.py -f 'ww52_prashanth_practice' -p '/path/to/pull/model' -r '/reference/package/path'")
			sys.exit(2)
		elif opt in ("-f", "--foldername"):
			folder_name = arg
		elif opt in ("-p", "--pathtopull"):
			pull_path = arg
		elif opt in ("-r", "--referencepackagepath"):
			reference_path = arg
          
        #print("opts,args",opts)
myfunc(sys.argv)
print('repo folder name:', folder_name)
print('path to pull model:', pull_path)
print('reference package path:', reference_path)


input_command = 'python '
for i in sys.argv:
    input_command+= i+" "
print("input command is \n",input_command)

if folder_name =='not given' or reference_path == 'not given':
	sys.exit("repo folder name/ refrence package path not provided")
	sys.exit(2)

print("current path")
os.system("pwd")



folder = folder_name
print("cwd",os.getcwd())


if not os.path.isdir(os.path.join(os.getcwd(),folder)):
    print("cloning is starting")
    cmd = "git clone $GK_XE3MEDIA_HEAD "+ folder
    os.system(cmd)
    print("cloning is completed")
else:
    print("cloned done already!")



print("going to inside repo folder")
try:
	os.chdir(os.path.join(os.getcwd(),folder))
except FileNotFoundError:
	sys.exit('Need to run the source command!')
os.system("pwd")
print("pulling changes from the given pull paths")
pull_paths = pull_path.split(";")
#user_path = pull_path#input("provide the path for pulling\n")
if pull_path != 'not given':
	for i in pull_paths:
		pull_command = "git pull "+i
		print("pull command is ",pull_command)
		os.system(pull_command)
	print("pull is completed")



print("running elab command")
#elab_command = "gnr elab -d sm --context MEDIA_LPM_1VD1VE_SD --target o3c.vpi.sipdfx.goldenrpt.default64 --autorpt --no-grip -- --optimus"
#elab_command = "gnr gen_rtl --autorpt --no-grip --context MEDIA_HPG_2VD2VE_SD -T o3c.vpi.gtsynth.goldenrpt.default64 -d sm -- --optimus && gnr elab --no-genrtl -F debug_u2c --context MEDIA_HPG_2VD2VE_SD -T o3c.vpi.gtsynth.goldenrpt.default64 -d sm -- --partcomp"
elab_command = "gnr gen_rtl --autorpt --no-grip --context MEDIA_LPM_SD -T o3c.vpi.sipdfx.gtsynth.goldenrpt.default64 -j 4 --use-tmp  -d sm -- --clean --pinspector --optimus && gnr elab --no-genrtl -F debug_u2c --context MEDIA_LPM_SD -T o3c.vpi.sipdfx.gtsynth.goldenrpt.default64 -j 4 --use-tmp -d sm -- --clean --partcomp"
print(elab_command)
os.system(elab_command)
print("elab is completed")
print("running export command")
#export_command = 'gnr export_ip --context MEDIA_HPG_2VD2VE_SD -T o3c.vpi.gtsynth.goldenrpt.default64 --no-elab --gen-struct --collaterals-yaml cfg/export_ip/sm/collaterals.yaml --collaterals-copy -d sm'
export_command = "gnr export_ip --context MEDIA_LPM_SD -T o3c.vpi.sipdfx.gtsynth.goldenrpt.default64 --no-elab --gen-struct --collaterals-yaml cfg/export_ip/sm/collaterals.yaml --collaterals-copy -d sm -- --disable-test val rtl_questa"
print("export command is ",export_command)
os.system(export_command)
print("Export IP command completed")
export_command_break = export_command.split(" ")
export_folder = 'bld/sm/'+export_command_break[3]+'.'+export_command_break[5]
model_folder = 'export_ip/debug_u2c/ip_package'
print('current drop')
current_drop = os.path.join(os.getcwd(),export_folder,model_folder)
print(current_drop)
if not os.path.isdir(current_drop):
	sys.exit("export not done properly")

last_drop = reference_path#input("enter the reference path\n")
print("last drop is",last_drop)
#os.chdir(reference_path)
#os.system("pwd")

#last_drop = '/nfs/site/disks/lnl_soc_regress_001/ashish/soc_package/LNL_IPX_UPLOAD/RTL1p0_refresh/xe2lpm_media_common-22ww44e-package'
#current_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/WW51_SOC_LNL_A0_PROD/IPX_UPLOAD/xe2lpm_media_common-22ww53e-package'

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

reference_upf = os.path.join(last_drop,last_drop_smedia,'source/upf')
source_upf = os.path.join(current_drop,current_drop_smedia,'source/upf')

print("checking the differenced files in includes folder")
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
	os.system("diff -r " + source_upf + " " + reference_upf + " >> log.txt")
else:
	os.system("diff -r " + source_upf + " " + reference_upf + " > log.txt")

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
		new_file.write(i.split(" ")[2].split("/")[-1] + " present in both drops\n")
		if rtl_folder in i.split(" ")[2]:
			copyfile(i.split(" ")[2], rtl_folder + "/" + i.split(" ")[2].split("/")[-1])
		if includes_folder in i.split(" ")[2]:
			copyfile(i.split(" ")[2], includes_folder + "/" + i.split(" ")[2].split("/")[-1])
	elif i.startswith('Only in'):
		if current_drop in i:
			new_file.write(i.strip().replace(": ", "/").split("/")[-1] + " present in current drop\n")
			if rtl_folder in i:
				copyfile(i.strip().replace(": ", "/").split(" ")[2],rtl_folder + "/" + i.strip().replace(": ", "/").split("/")[-1])
			elif includes_folder in i:
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

