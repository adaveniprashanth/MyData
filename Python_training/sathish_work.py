import os
path = "/nfs/site/disks/xe3_ptl_model_bld_002/sanbalax/PTL_WW05p2_PSS_jem23_NEW/bld/gt/LPG_2X6.emu_nodfx.noupf.default64/emubuild.2.8.11/zse3"
os.system("cd "+path)
f = open("testbench.inputs",'r')
output = open("testbench.outputs",'w')
counter = 0
lines = f.readlines()
for line in lines:
	
	if '-D' in line and counter ==0:
		output.write(i)
		output.write("-DEMU_PERF"+"\n")
		counter+=1
	output.write(i)

f.close()
output.close()

os.system("mv testbench.outputs testbench.inputs")
os.system("cd ../log")
file_name = 'emubuild.ZSE_ZS3_common_testbench.log'
if os.path.exists(file_name):
	
	f = open("emubuild.ZSE_ZS3_common_testbench.log")
	lines = f.readlines()
	for line in lines:
		if 'g++' in line:
			start = line.split("&&")[2]
			end = start.split(")")[0]
			if "lib"in end:
				break
	f.close()

print(end)
os.system("cd "+path)
os.system("mkdir lib_perf")
end = end.replace("lib","lib_perf")
print(end)
#os.system(end)


