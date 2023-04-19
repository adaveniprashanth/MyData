if 1:
    import os
    f = open('missed_clips_paths.txt','r')
    #f2 = open("missed_output.txt",'w')
    f2 = open("missed_output_for_prachi_mail.txt",'w')
    lines = f.readlines()
    f.close()
    lines = [x.strip() for x in lines]
    lines = [x for x in lines if len(x)!=0]

    for i in lines:
        path = os.path.join(os.getcwd(),i)
        files = os.listdir(path)
        print(files)
        for file in files:
            if '.gsf' in file and 'metadata' not in file:
                f= open(os.path.join(path,file),'r')
                data_lines = f.readlines()
                f.close()
                for data_line in data_lines:
                    if 'SourceClip' in data_line:
                        clip_name = data_line.split('SourceClip=>')[1].replace('"','').replace(",","")
                        print(clip_name)
                        f2.write(i+"\n\n"+clip_name)
    f2.close()


