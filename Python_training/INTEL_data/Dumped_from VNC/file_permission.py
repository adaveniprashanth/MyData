import os

f = open('full_details.txt','r')
l = f.readlines()
l = [x.strip() for x in l]

for gsf_file in l:
    # print(gsf_file)
    directory=os.path.dirname(gsf_file)
    files_in_directory = os.listdir(directory)
    metadata_files = []
    for file in files_in_directory:
        if "metadata" in file:
            metadata_files.append(os.path.join(directory,file))
    if len(metadata_files)>1:
        print(directory)
        print(metadata_files)
        print()



# os.system("chmod 644 "+filename)