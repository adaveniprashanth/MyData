import os
f = open('psmi_present_in_current_drop.txt','r')
lines = f.readlines()
lines = [x.strip() for x in lines]
f.close()

last_drop = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/lnl/WW51_SOC_LNL_A0_PROD/IPX_UPLOAD/xe2lpm_media_common-22ww53e-package'
includes_folder ='smedia_top/source/includes'
log_file = 'psmi_diffrences_current_drop_includes.txt'

if os.path.isfile(os.path.join(os.getcwd(),log_file)):
    os.remove(os.path.join(os.getcwd(), log_file))

#os.system("diff -r "+file1+" "+file2 + "> abc.txt")

for line in lines:
    file_name = line.split(includes_folder)[1]
    current_file = line
    last_file = last_drop+"/"+includes_folder+file_name
    os.system("echo "+current_file+" >> "+log_file)
    os.system("diff -r "+current_file+" "+last_file + ">> "+log_file)


