import os
print(os.getcwd())
new_path=os.path.join(os.getcwd(),'UTP-Content\Decoder\AVC')
print(new_path)

files = os.listdir(new_path)
gsf_folder=os.path.join(os.getcwd(),'gsf_folder')
clips_folder = os.path.join(os.getcwd(),'clips_folder')

if not os.path.exists(gsf_folder):
    os.mkdir(gsf_folder)
if not os.path.exists(clips_folder):
    os.mkdir(clips_folder)

print(gsf_folder)
for dirpath,dirnames,filenames in os.walk(new_path):
    lst = [dirpath,filenames]
    if len(filenames)>=1:
        #print(lst)
        #print()
        splits=dirpath.split("UTP-Content\\")
        created_path = os.path.join(gsf_folder,splits[1])
        print("created_path",created_path)
        if not os.path.exists(created_path):
            print("path not exists")
            print(gsf_folder)
            print(splits[1])
            os.makedirs(created_path)

