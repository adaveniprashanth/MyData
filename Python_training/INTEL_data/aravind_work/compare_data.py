if 0:#SD and media lines compare
    f = open('X2_SD_GM_SOC.list','r')
    sd_lines = f.readlines()
    f.close()
    sd_lines = [x.strip() for x in sd_lines]
    sd_lines = [x for x in sd_lines if len(x)>1]#removing empty lines
    sd_lines = [x for x in sd_lines if len(x)>50]#removing the unnecessary data
    sd_lines = [x for x in sd_lines if ")" not in x]#removing the unnecessary data which has length more than 50
    sd_lines = [x.replace(" ","",1) for x in sd_lines]#replacing the first occurance of " "(space)
    sd_lines = [x.split(" ")[0] for x in sd_lines]#splitting the string based on " " for getting testname only
    #sd_lines = [x.replace("-","") for x in sd_lines]#removing "-" in test name
    sd_lines = [x.split("#")[0] if "#" in x else x for x in sd_lines]#splitting to get only test name not iterations
    sd_lines = [x.split("_CFG")[0] if "_CFG" in x else x for x in sd_lines]#splitting to get only test name not iterations
    sd_lines = [x for x in sd_lines if len(x)>5]#to remove empty testnames

    f = open('X2_all_media_tests.list','r')
    media_lines = f.readlines()
    f.close()
    media_lines = [x.strip() for x in media_lines]
    media_lines = [x for x in media_lines if len(x)>1]
    media_lines = [x.replace(" ","",1) for x in media_lines]
    media_lines = [x.split(" ")[0] for x in media_lines]
    media_lines = [x.split("#")[0] if "#" in x else x for x in media_lines]
    media_lines = [x.split("_CFG")[0] if "_CFG" in x else x for x in media_lines]

    present_only_in_media = set(media_lines)-set(sd_lines)
    present_only_in_sd = set(sd_lines)-set(media_lines)
    res = open("SD_media_comparision_result.txt",'w')

    print("present_only_in_media".replace("_"," "))
    res.write("\npresent only in -->"+"X2_all_media_tests.list"+"\n\n")
    for c,i in enumerate(present_only_in_media,1):
        pass
        print(c,i)
        res.write(i+"\n")


    print("present_only_in_sd".replace("_"," "))
    res.write("\npresent only in -->"+"X2_SD_GM_SOC.list"+"\n\n")
    for c,i in enumerate(present_only_in_sd,1):
        pass
        print(c,i)
        res.write(i+"\n")

    res.close()

if 0:#SD and AXE page test names compare
    file1 = 'X2_SD_GM_SOC.list'
    f = open(file1,'r')
    sd_lines = f.readlines()
    f.close()
    sd_lines = [x.strip() for x in sd_lines]
    sd_lines = [x for x in sd_lines if len(x)>1]#removing empty lines
    sd_lines = [x for x in sd_lines if len(x)>50]#removing the unnecessary data
    sd_lines = [x for x in sd_lines if ")" not in x]#removing the unnecessary data which has length more than 50
    sd_lines = [x.replace(" ","",1) for x in sd_lines]#replacing the first occurance of " "(space)
    sd_lines = [x.split(" ")[0] for x in sd_lines]#splitting the string based on " " for getting testname only
    #sd_lines = [x.replace("-","") for x in sd_lines]#removing "-" in test name
    sd_lines = [x.split("#")[0] if "#" in x else x for x in sd_lines]#splitting to get only test name not iterations
    sd_lines = [x.split("_CFG")[0] if "_CFG" in x else x for x in sd_lines]#splitting to get only test name not iterations
    sd_lines = [x for x in sd_lines if len(x)>5]#to remove empty testnames

    file2 = 'axe_page_test_names.txt'
    f = open(file2,'r')
    axe_lines = f.readlines()
    f.close()
    axe_lines = [x.strip() for x in axe_lines]
    axe_lines = [x for x in axe_lines if len(x)>1]
    axe_lines = [x.replace(" ","",1) for x in axe_lines]
    axe_lines = [x.split(" ")[0] for x in axe_lines]
    #axe_lines = [x.split("#")[0] if "#" in x else x for x in axe_lines]
    axe_lines = [x.split("_CFG")[0] if "_CFG" in x else x for x in axe_lines]

    present_only_in_axe = set(axe_lines)-set(sd_lines)
    present_only_in_sd = set(sd_lines)-set(axe_lines)
    res = open("axe_SD_comparision_result.txt",'w')

    print("present_only_in_media".replace("_"," "))
    res.write("\npresent only in -->"+file2+" and not present in "+file1+"\n\n")
    for c,i in enumerate(present_only_in_axe,1):
        pass
        print(c,i)
        res.write(i+"\n")


    print("present_only_in_sd".replace("_"," "))
    res.write("\npresent only in -->"+file1+" and not present in "+file2+"\n\n")
    for c,i in enumerate(present_only_in_sd,1):
        pass
        print(c,i)
        res.write(i+"\n")

    res.close()

if 1:#median and AXE test names compare
    file1 = 'axe_page_test_names.txt'
    f = open(file1,'r')
    axe_lines = f.readlines()
    f.close()
    axe_lines = [x.strip() for x in axe_lines]
    '''axe_lines = [x for x in axe_lines if len(x)>1]#removing empty lines
    axe_lines = [x for x in axe_lines if len(x)>50]#removing the unnecessary data
    axe_lines = [x for x in axe_lines if ")" not in x]#removing the unnecessary data which has length more than 50
    axe_lines = [x.replace(" ","",1) for x in axe_lines]#replacing the first occurance of " "(space)
    axe_lines = [x.split(" ")[0] for x in axe_lines]#splitting the string based on " " for getting testname only
    #axe_lines = [x.replace("-","") for x in axe_lines]#removing "-" in test name
    axe_lines = [x.split("#")[0] if "#" in x else x for x in axe_lines]#splitting to get only test name not iterations
    axe_lines = [x.split("_CFG")[0] if "_CFG" in x else x for x in axe_lines]#splitting to get only test name not iterations
    axe_lines = [x for x in axe_lines if len(x)>5]#to remove empty testnames
    '''
    file2 = 'X2_all_media_tests.list'
    f = open(file2,'r')
    media_lines = f.readlines()
    f.close()
    media_lines = [x.strip() for x in media_lines]
    media_lines = [x for x in media_lines if len(x)>1]
    media_lines = [x.split(" ")[0] for x in media_lines]
    media_lines = [x.replace(" ","",1) for x in media_lines]
    #media_lines = [x.split("#")[0] if "#" in x else x for x in media_lines]
    media_lines = [x.split("_CFG")[0] if "_CFG" in x else x for x in media_lines]

    present_only_in_media = set(media_lines)-set(axe_lines)
    present_only_in_axe = set(axe_lines)-set(media_lines)
    res = open("axe_media_comparision_result.txt",'w')

    print("present_only_in_media".replace("_"," "))
    res.write("\npresent only in -->"+file2+" and not present in "+file1+"\n\n")
    for c,i in enumerate(present_only_in_media,1):
        pass
        print(c,i)
        res.write(i+"\n")


    print("present_only_in_axe".replace("_"," "))
    res.write("\npresent only in -->"+file1+" and not present in "+file2+"\n\n")
    for c,i in enumerate(present_only_in_axe,1):
        pass
        print(c,i)
        res.write(i+"\n")

    res.close()
