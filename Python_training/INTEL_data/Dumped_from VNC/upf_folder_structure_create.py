import os
import shutil

if not os.path.isdir(os.path.join(os.getcwd(),'upf')):
    os.mkdir("upf")

f= open("upf_files.txt")
lines = f.readlines()
f.close()
lines = [x.strip() for x in lines]
lines = [x for x in lines if len(x)>1]

for line in lines:
    path = line.split("/xl2upf/")[1]
    full_path = os.path.join(os.getcwd(),'upf',path)
    print(full_path)
    if not os.path.isdir(os.path.dirname(full_path)):
        os.makedirs(os.path.dirname(full_path))
    shutil.copyfile(line,full_path)


