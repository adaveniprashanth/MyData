from shutil import copyfile
import shutil
import os
#shutil.copy2('sai_help.py','abcd/efh/sai_help.py')
#os.makedirs('abcd/efh/sai_help.py',exist_ok=True)
path = '/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/ptl/ptl_0p5_drop/snapshot_model/ptl_ww7p4_Media_SOC_0p5_snapshot_ankit/bld/sm/MEDIA_LPM_SD.o3c.vpi.sipdfx.gtsynth.goldenrpt.default64/export_ip/debug_u2c/ip_package/smedia_top/source/upf/sai_help.py'

rtl_folder = 'smedia_top/source'
print(path.index(rtl_folder))

full_path= 'abcd/'+path[217:]
print(full_path)
os.makedirs(os.path.dirname(full_path))
copyfile('sai_help.py',full_path)
