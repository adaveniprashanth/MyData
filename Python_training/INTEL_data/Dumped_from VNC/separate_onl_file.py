f = open('log.txt','r')
lines = f.readlines()
f.close()

f = open('only_lines.txt','w')
lines = [x.strip() for x in lines if 'Only in' in x ]
for i in lines:
    line = i.split(" ")
    print(line[2][:-1]+'/'+line[3])
    f.write(line[2][0:-1]+'/'+line[3]+"\n")

f.close()
