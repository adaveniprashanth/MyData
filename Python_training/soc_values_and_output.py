f = open('soc_values.txt','r')
all_lines = f.readlines()
f.close()

soc_lines =[x.split('#')[0] for x in all_lines]
soc_lines =[x.strip() for x in soc_lines]
f = open('output.txt','r')
output_lines = f.readlines()
f.close()
lst = []
for soc_line in soc_lines:
    for output_line in output_lines:
        if soc_line in output_line:
            break
    else:
        print("not found "+soc_line)
        lst.append(soc_line)

print(lst)