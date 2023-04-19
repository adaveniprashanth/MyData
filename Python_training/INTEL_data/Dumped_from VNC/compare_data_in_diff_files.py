import os

f = open('log.txt')
lines = f.readlines()
f.close()

includes_folder ='smedia_top/source/includes'

lines = [x for x in lines if 'diff -r' in x]
lines = [x for x in lines if includes_folder in x]

print("total changed files are ",len(lines))

log_file = 'differences_in_files.txt'
if os.path.isfile(os.path.join(os.getcwd(), log_file)):
	os.remove(os.path.join(os.getcwd(), log_file))
f3 = open('more_changes_in_current_drop.txt','w')
for i in lines[:]:
    data = i.split(" ")
    file1 = data[2]
    file2 = data[3].strip()
    print(file1)
    print(file2)
    os.system("diff -r "+file1+" "+file2 + "> abc.txt")
    os.system("diff -r "+file1+" "+file2 + ">> differences_in_files.txt")    
    #os.system("diff -U 0 "+file1+" "+file2+" | grep -v ^@ | wc -l") #to get count of changes in 2 files
    f = open('abc.txt','r')
    l = f.readlines()
    f.close()
    print("changes ",len(l))
    if len(l) > 4:
        f3.write(file1+"\n")
        print(l)
f3.close()


f = open('more_changes_in_current_drop.txt','r')
lines = f.readlines()
f.close()
lines = [x.strip() for x in lines]

psmi_present = open('psmi_present_in_current_drop.txt','w')
psmi_not_present = open('psmi_not_present_in_current_drop.txt','w')

for line in lines:
    f = open(line,'r')
    data = f.read()
    f.close()

    if 'PSMI_REPLAY' in data:
        print('present in '+line)
        psmi_present.write(line+"\n")
    elif 'PSMI_REPLAY' not in data:
        psmi_not_present.write(line+"\n")

psmi_present.close()
psmi_not_present.close()


'''
current_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/LNL_B0_DROP/IPX_UPLOAD/xe3lpm_media_common-23ww13e-package'
last_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/WW51_SOC_LNL_A0_PROD/IPX_UPLOAD/xe2lpm_media_common-22ww53e-package'

rtl_folder = 'smedia_top/source/rtl/src'

more_changes = open('current_drop_more_changes.txt','w')

for line in lines:
    current_file_name = current_drop+"/"+includes_folder+"/"+line
    last_file_name = last_drop+"/"+includes_folder+"/"+line
    f = open(current_file_name,'r')
    current_file_lines = f.readlines()
    f.close()
    f = open(last_file_name,'r')
    last_file_lines = f.readlines()
    f.close()
    counter = 0
    l=[]
    for current_line,last_line in zip(current_file_lines,last_file_lines):
        if current_line != last_line:
            counter +=1
            l.append(current_line.strip()+" <<< "+last_line.strip()+"\n")
    if counter >=2:
        print(current_file_name)
        more_changes.write(current_file_name+"\n")
        more_changes.writelines(l)
    if 'PSMI_REPLAY' not in data:
        print('present in '+file_name)
        res.write(file_name+"\n")

more_changes.close()
'''
