
f = open('killed','r')
killed = f.readlines()
f.close()

f = open('pass','r')
passed = f.readlines()
f.close()
missed_killed = []
count = 0
search_killed = []
for i in killed:
    count+=1
    j = i.split("maxfail=1 -t ")
    if len(j) < 2:
        missed_killed.append(j)
    else:
        # print(j[1].split(" ")[0])
        search_killed.append(j[1].split(" ")[0])
d = {}
for i in passed:
    for j in search_killed:
        if j in i:
            mtl = i.split("Cobalt/")[1].split(" ")[0]
            # print(i.split("Cobalt/")[1].split(" ")[0])
            repo_version =i.split("repo_ver ")[1].split(" ")[0]
            print(i.split("repo_ver ")[1].split(" ")[0])
            d[j] = [mtl,repo_version]
print(d)
f = open('result_killed.txt','w')
for i in killed:
    for key,v in d.items():
        if key in i:
            print(key)
            before_repo = i.split("repo_ver ")[0]
            after_repo = i.split("repo_ver ")[1].split(" ",1)[1]
            repo_value = "repo_ver "+v[1]+" "
            j = before_repo+repo_value+after_repo
            print(j)
            before_mtl = j.split("Cobalt/")[0]
            mtl_value = "Cobalt/"+v[0]+" "
            after_mtl = j.split("Cobalt/")[1].split(" ",1)[1]
            k = before_mtl+mtl_value+after_mtl
            # f.write(key+"\n")
            f.write(k)
            break
f.close()

