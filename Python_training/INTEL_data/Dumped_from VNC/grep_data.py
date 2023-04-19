import os
path = '/nfs/site/disks/dg2_pipemedia_emu_regress3/cramasw1/XE3/models/xe3_scal_val_repo/src'

log = open('log_data.txt','w')

for dirpath,dirnames,filenames in os.walk(path):
    #print("path",dirpath)
    #print("folders in path",dirnames)
    #print("files in path",filenames)
    if len(filenames) != 0:
        for j in filenames:
            filename = os.path.join(dirpath,j)
            #print(filename)
            data = ''
            f = open(filename,'r')
            try:
                data = f.readlines()
            except Exception as e:
                pass
                log.writelines(["data cannot be read from ",filename,'\n'])
                log.writelines(["error is --> ",str(e),'\n'])
            finally:
                f.close()
                if len(data)>0:
                    for line in data:
                        line = line.strip()
                        if 'pm_mode_sfcen' in line and '//' not in line:
                            log.writelines(["line--> ",line,'\n'])
                            log.writelines(['pm_mode_sfcen ',filename,'\n'])
                        if 'fuse_gt_vebox_enable_gcp' in line and '3:0]' in line and 'logic' in line and '//' not in line:
                            log.writelines(["line--> ",line,'\n'])
                            log.writelines(['fuse_gt_vebox_enable_gcp ',filename,'\n'])
                        if 'fuse_gt_vebox_enable' in line and '3:0]' in line and 'logic' in line and '//' not in line:
                            log.writelines(["line--> ",line,'\n'])
                            log.writelines(['fuse_gt_vebox_enable ',filename,'\n'])
                        if 'gtfs_mgsr_vebox_enable' in line and '3:0]' in line and 'logic' in line and '//' not in line:
                            log.writelines(["line--> ",line,'\n'])
                            log.writelines(['gtfs_mgsr_vebox_enable ',filename,'\n'])
                        if 'pm_mode_veboxen' in line and '3:0]' in line and 'logic' in line and '//' not in line:
                            log.writelines(["line--> ",line,'\n'])
                            log.writelines(['pm_mode_veboxen ',filename,'\n'])
log.close()
f = open('log_data.txt','r')
lines = f.readlines()
f.close()
lines = [x for x in lines if "line-->" not in x]
lines = [x for x in lines if "error is -->" not in x]
lines = list(set(lines))
lines.sort()
f = open('final_log.txt','w')
f.writelines(lines)
f.close()
