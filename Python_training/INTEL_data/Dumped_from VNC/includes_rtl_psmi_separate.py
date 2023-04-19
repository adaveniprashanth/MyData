import os

f = open('log.txt')
total_lines = f.readlines()
f.close()

includes_folder ='smedia_top/source/includes'
rtl_folder = 'smedia_top/source/rtl/src'
current_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/LNL_B0_DROP/IPX_UPLOAD/xe3lpm_media_common-23ww13e-package'
last_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/WW51_SOC_LNL_A0_PROD/IPX_UPLOAD/xe2lpm_media_common-22ww53e-package'


diff_lines = [x for x in total_lines if 'diff -r' in x]
only_lines = [x for x in total_lines if 'Only in ' in x]

total_includes_lines = []
total_rtl_lines = []
for line in diff_lines:
    if includes_folder in line:
        total_includes_lines.append(line.split(" ")[2])
    elif rtl_folder in line:
        total_rtl_lines.append(line.split(" ")[2])

for line in only_lines:
    if includes_folder in line:
        line = line.split(" ")
        total_includes_lines.append(line[2][:-1]+"/"+line[3].strip())
    elif rtl_folder in line:
        line = line.split(" ")
        total_rtl_lines.append(line[2][:-1]+"/"+line[3].strip())

'''
f= open('dummy.txt','w')
for i in total_includes_lines:
    f.write(i+"\n")
f.close()
'''

f1= open('total_psmi_present_includes.txt','w')
f2= open('total_psmi_not_present_includes.txt','w')
for line in total_includes_lines:
    f = open(line.strip(),'r')
    data = f.read()
    f.close()

    if 'PSMI_REPLAY' in data:
        print('present in '+line)
        f1.write(line+"\n")
    elif 'PSMI_REPLAY' not in data:
        f2.write(line+"\n")
f1.close()
f2.close()

f1= open('total_psmi_present_rtl.txt','w')
f2= open('total_psmi_not_present_rtl.txt','w')
for line in total_rtl_lines:
    f = open(line,'r')
    data = f.read()
    f.close()

    if 'PSMI_REPLAY' in data:
        print('present in '+line)
        f1.write(line+"\n")
    elif 'PSMI_REPLAY' not in data:
        f2.write(line+"\n")
f1.close()
f2.close()






