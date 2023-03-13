print("hello")

f = open("test_names.txt",'r')
test_names_lines = f.readlines()
f.close()

f = open("test_lists.txt",'r')
test_list_lines = f.readlines()
f.close()


f = open("sheet1_data.txt",'r')
sheet1_data = f.readlines()
f.close()

f = open("sheet2_data.txt",'r')
sheet2_data = f.readlines()
f.close()



test_names_lines = [x.strip() for x in test_names_lines]
test_names_lines = [x.split("_CFG")[0] for x in test_names_lines if "_CFG" in x]

#for i in test_names_lines:
#    print(i)


test_list_lines = [x.strip() for x in test_list_lines]
test_list_lines = [x.split("  ")[0] for x in test_list_lines]
test_list_lines = [x.split("#")[0] for x in test_list_lines if "#" in x]
#for i in test_list_lines:
#    print(i)

sheet1_data = [x.strip() for x in sheet1_data]
sheet1_data = [x.split("_CFG")[0] for x in sheet1_data if "_CFG" in x]
sheet1_data = [x.split("#")[0] for x in sheet1_data if "#" in x]

sheet2_data = [x.strip() for x in sheet2_data]
sheet2_data = [x.split("_CFG")[0] for x in sheet2_data if "_CFG" in x]
sheet2_data = [x.split("#")[0] for x in sheet2_data if "#" in x]

f1 = open("test_result.txt",'w')
'''
for i in test_list_lines:
    if i in sheet1_data or i in sheet1_data:
        continue
    else:
        print(i)
        f1.write(i+"\n")

for i in test_names_lines:
    if i in sheet1_data or i in sheet1_data:
        continue
    else:
        print(i)
        f1.write(i+"\n")
'''

total_tests=test_list_lines+test_names_lines
total_tests = list(set(total_tests))
for i in total_tests:
    if i in sheet1_data or i in sheet2_data:
        continue
    else:
        print(i)
        f1.write(i+"\n")

f1.close()
