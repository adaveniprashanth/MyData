'''
#!/usr/intel/bin/python
import os
import sys
import json
import requests
import subprocess
import xlsxwriter
from datetime import date
from datetime import timedelta
def create_xlsx(name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()
    return workbook, worksheet
def get_disks(filename):
    disks = []
    disklist = open(filename, 'r')
    for disk in disklist:
        disks.append(disk.strip())
    disklist.close()
    return disks
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def main():
    today = date.today()
    disks = get_disks("disks.txt")
    exe_group_list = []
    for i in range(len(sys.argv)-1):
        exe_group_list.append(sys.argv[i+1])
    print("Rolling up perf metadata for execution groups: ", exe_group_list)
    exe_group_name = ('_'.join(exe_group_list))
    workbook, worksheet = create_xlsx("axe_metadata_" + str(exe_group_name) + "_" + str(today) + ".xlsx")
    header = ["Job", "Test", "Func Status", "Metric Quantity", "Metric Unit",
              "Theoretical Target Rate", "Expected Clocks", "Axe Name", "Config",
              "ClockStart", "ClockEnd", "Clock difference", "Achieved Target Error Percent",
              "Actual Clocks", "Actual Perf", "Perf Bucket", "Test Category", "Actual Rate", "Rate Delta", "Rate Delta %",
              "Waveform", "Execution Group"]
    row = 0
    col = 0
    for i in range(len(header)):
        worksheet.write(row, col, header[i])
        col = col + 1
    for exe_group in exe_group_list:
        for disk in disks:
            jobs = []
            if os.path.isdir(disk+"/"+exe_group):
                for job_dir in (os.listdir(disk+"/"+exe_group)):
                    # DEBUG print(job_dir)
                    # DEBUG print(disk+"/"+exe_group+"/"+job_dir+"/Manifest.zip")
                    if os.path.isfile(disk+"/"+exe_group+"/"+job_dir+"/Manifest.zip") is False:
                        if os.path.isfile(disk+"/"+exe_group+"/"+job_dir+"/AxeExecutionClient.log.zip") is True:
                            jobs.append(disk+"/"+exe_group+"/"+job_dir+"/AxeExecutionClient.log.zip")
                print("Execution Group: " + exe_group + " Found Jobs: " + str(len(jobs)) + " Disk: " + disk)
            else:
                # DEBUG print("Execution Group: " + exe_group + " Found Jobs: " + str(len(jobs)) + " Disk: " + disk)
                continue
            # DEBUG print(jobs)
 
            for job in jobs:
                doc = {}
                log_file = job
                doc["Job"] = job
                os.system("unzip -o " + log_file + " > /dev/null")
                with open("./AxeExecutionClient.log", "r") as log_file_open:
                    data = log_file_open.readlines()
                    status = "Fail"
                    test = "NA"
                    rp = "NA"
                    category = "NA"
                    perf_found = False
                    count = 0
                    axe_name = "NA"
                    config = "NA"
                    for line in data:
                        if perf_found is False:
                            if ("Running Executable" in line) and ("web" in line):
                                # do something to find test
                                # DEBUG print(line)
                                # DEBUG print(line.split("/")[-1])
                                test = line.split("/")[-1]
                            elif ("Running:" in line) and ("-DaxeName") in line:
                                axe_name = line.split("/runtest")[0].split()[-1]
                                config = line.split("/runtest")[0].split()[-2]
                            elif "TimeStampPerf Analysis" in line:
                                # do something to find perf. result
                                # DEBUG print(line)
                                perf_found = True
                            elif "ClockStart" in line:
                                 perf_found = True
                            elif "CRC compared equal. FileName: gpuTick_0.tbx.dat LAR" in line:
                                count = 0
                                if count < 8:
                                    count = count + 1
                                    # DEBUG print(line)
                                    # DEBUG print(line.split("-- ")[-1])
                                     # DEBUG print(line.split("-- ")[-1].split(":"))
                                    perf = line.split("-- ")[-1].split(":")
                                    print(perf)
                                    # DEBUG print(perf[0], perf[1].strip())
                                    if(is_number(perf[1].strip())):
                                        # DEBUG print(perf[0], perf[1].strip())
                                        doc[perf[0]] = float(perf[1].strip())
                                    else:
                                        doc[perf[0]] = perf[1].strip()
                                else:
                                    perf_found = False
                                    # DEBUG exit()ClockStart
 
                            elif "Test ran to completion" in line or "Explicit failure triggered by test" in line:
                                # set status to pass
                                # DEBUG print(line)
                                status = "Pass"
                            elif "Platform Result Path:" in line:
                                rp = line.split("Platform Result Path: ")[1]
                        else:
                            if count < 5:
                                count = count + 1
                                # DEBUG print(line)
                                # DEBUG print(line.split("-- ")[-1])
                                # DEBUG print(line.split("-- ")[-1].split(":"))
                                perf = line.split("-- ")[-1].split(":")
                                # DEBUG print(perf[0], perf[1].strip())
                                if(is_number(perf[1].strip())):
                                    # DEBUG print(perf[0], perf[1].strip())
                                    doc[perf[0]] = float(perf[1].strip())
                                else:
                                    doc[perf[0]] = perf[1].strip()
                            else:
                                perf_found = False
                                # DEBUG exit()ClockStart
 
                doc["Test"] = test
                if "EUPerf" in test and "measure=lat" in test:
                    category = "PnP/Perf/uBM/EU/EU-Latency"
                elif "EUPerf" in test and "measure=lat" not in test:
                    category = "PnP/Perf/uBM/EU/EU-Throughput"
                elif "HdcLscSlmPerf" in test and "measure=lat" in test:
                    category = "PnP/Perf/uBM/GPGPU/Latency"
                elif "HdcLscSlmPerf" in test and "measure=lat" not in test:
                    if "l1" in test:
                        category = "PnP/Perf/uBM/GPGPU/L1-BW"
                    elif "slm" in test:
                        if "Atm" in test:
                            category = "PnP/Perf/uBM/GPGPU/SLM-Atomics"
                        else:
                            category = "PnP/Perf/uBM/GPGPU/SLM-BW"
                    elif "l3" in test:
                        if "Atm" in test:
                            category = "PnP/Perf/uBM/GPGPU/L3-Atomics"
                        else:
                            category = "PnP/Perf/uBM/GPGPU/L3-BW"
                elif "ComputeThreadDispatchPerf" in test:
                    category = "PnP/Perf/uBM/GPGPU/Thread-Dispatch"
                elif "localMemory" in test:
                    category = "PnP/Perf/uBM/SoC/MemoryController"
                doc["Test Category"] = category
                doc["Func Status"] = status
                doc["Waveform"] = rp
                doc["Axe Name"] = axe_name
                doc["Config"] = config
                doc["Execution Group"] = int(exe_group)
 
                row = row + 1
                col = 0
                for i in range(len(header)):
                    if header[i] in doc:
                        worksheet.write(row, col, doc[header[i]])
                    elif header[i] in "Actual Perf":
                       # =HEX2DEC(REPLACE([@[Achieved Target Clock Percent]],1,2,""))
                        formula = "=HEX2DEC(REPLACE(M" + str(row+1) + ',1,2,""))'
                        worksheet.write_formula(row, col, formula)
                    elif header[i] in "Actual Clocks":
                       # =HEX2DEC(REPLACE([@[Clock difference]],1,2,""))
                        formula = "=HEX2DEC(REPLACE(L" + str(row+1) + ',1,2,""))'
                        worksheet.write_formula(row, col, formula)
                    elif header[i] in "Perf Bucket":
                       # =IF([@Actual Perf]>100, "FAIL", "PASS")
                        formula = '=IF(O' + str(row+1) + '>105, "OVERPASS", IF(O' + str(row+1) + '>=95, "PASS", IF(O' + str(row+1) + '>=90, "5% to 10%", IF(O' + str(row+1) + '>=80, "10% to 20%", "20% +"))))'
                        worksheet.write_formula(row, col, formula)
                    elif header[i] in "Actual Rate":
                        # = [@[Metric Quantity]]/[@[Actual Clocks]]*1.7
                        if category is "PnP/Perf/uBM/GPGPU/Latency":
                            formula = "=N" + str(row+1) + "/D" + str(row+1) #N2/D2
                        else:
                            #formula = "=D" + str(row+1) + "/N" + str(row+1)
                            formula = "=PRODUCT(D" + str(row+1) + "/N" + str(row+1) + ",1.7)" # =PRODUCT(D1/N2,1.7)
                            print(formula)
                            worksheet.write_formula(row, col, formula)
                    elif header[i] in "Rate Delta":
                        # =[@[Theoretical Target Rate]]-[@[Actual Rate]]
                        formula = "=F" + str(row+1) + "-R" + str(row+1)
                        worksheet.write_formula(row, col, formula)
                    elif header[i] in "Rate Delta %":
                        # =[@[Rate Delta]]/[@[Theoretical Target Rate]]
                        formula = "=S" + str(row+1) + "/F" + str(row+1)
                        worksheet.write_formula(row, col, formula)
                    else:
                        worksheet.write(row, col, "NA")
                    col = col + 1
   
    workbook.close()
    os.system("echo 'Done' | mail -a axe_metadata_" + str(exe_group_name) + "_" + str(today) + ".xlsx -s 'AXE Perf Metadata Rollup' $USER@ecsmtp.fm.intel.com")
 
main()
'''



import os
import sys
import json
import requests
import subprocess
import xlsxwriter
from datetime import date
from datetime import timedelta
def create_xlsx(name):
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()
    return workbook, worksheet
def get_disks(filename):
    disks = []
    disklist = open(filename, 'r')
    for disk in disklist:
        disks.append(disk.strip())
    disklist.close()
    return disks
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    today = date.today()
    disks = get_disks("disks.txt")
    exe_group_list = []
    for i in range(len(sys.argv)-1):
        exe_group_list.append(sys.argv[i+1])
    print("Rolling up perf metadata for execution groups: ", exe_group_list)
    exe_group_name = ('_'.join(exe_group_list))
    workbook, worksheet = create_xlsx("axe_metadata_" + str(exe_group_name) + "_" + str(today) + ".xlsx")
    header = ["Job", "Test", "Func Status", "Metric Quantity", "Metric Unit",
              "Theoretical Target Rate", "Expected Clocks", "Axe Name", "Config",
              "ClockStart", "ClockEnd", "Clock difference", "Achieved Target Error Percent",
              "Actual Clocks", "Actual Perf", "Perf Bucket", "Test Category", "Actual Rate", "Rate Delta", "Rate Delta %",
              "Waveform", "Execution Group"]
    row = 0
    col = 0
    for i in range(len(header)):
        worksheet.write(row, col, header[i])
        col = col + 1
    for exe_group in exe_group_list:
        for disk in disks:
            jobs = []
            if os.path.isdir(disk+"/"+exe_group):
                for job_dir in (os.listdir(disk+"/"+exe_group)):
                    # DEBUG print(job_dir)
                    # DEBUG print(disk+"/"+exe_group+"/"+job_dir+"/Manifest.zip")
                    if os.path.isfile(disk+"/"+exe_group+"/"+job_dir+"/Manifest.zip") is False:
                        if os.path.isfile(disk+"/"+exe_group+"/"+job_dir+"/AxeExecutionClient.log.zip") is True:
                            jobs.append(disk+"/"+exe_group+"/"+job_dir+"/AxeExecutionClient.log.zip")
                print("Execution Group: " + exe_group + " Found Jobs: " + str(len(jobs)) + " Disk: " + disk)
            else:
                # DEBUG print("Execution Group: " + exe_group + " Found Jobs: " + str(len(jobs)) + " Disk: " + disk)
                continue
            # DEBUG print(jobs)
 
            for job in jobs:
                doc = {}
                log_file = job
                doc["Job"] = job
                os.system("unzip -o " + log_file + " > /dev/null")
                with open("./AxeExecutionClient.log", "r") as log_file_open:
                    data = log_file_open.readlines()
                    status = "Fail"
                    test = "NA"
                    rp = "NA"
                    category = "NA"
                    perf_found = False
                    count = 0
                    axe_name = "NA"
                    config = "NA"
                    for line in data:
                        if perf_found is False:
                            if ("Running Executable" in line) and ("web" in line):
                                # do something to find test
                                # DEBUG print(line)
                                # DEBUG print(line.split("/")[-1])
                                test = line.split("/")[-1]
                            elif ("Running:" in line) and ("-DaxeName") in line:
                                axe_name = line.split("/runtest")[0].split()[-1]
                                config = line.split("/runtest")[0].split()[-2]
                            elif "TimeStampPerf Analysis" in line:
                                # do something to find perf. result
                                # DEBUG print(line)
                                perf_found = True
                            elif "ClockStart" in line:
                                 perf_found = True
                            elif "CRC compared equal. FileName: gpuTick_0.tbx.dat LAR" in line:
                                count = 0
                                if count < 8:
                                    count = count + 1
                                    # DEBUG print(line)
                                    # DEBUG print(line.split("-- ")[-1])
                                     # DEBUG print(line.split("-- ")[-1].split(":"))
                                    perf = line.split("-- ")[-1].split(":")
                                    print(perf)
                                    # DEBUG print(perf[0], perf[1].strip())
                                    if(is_number(perf[1].strip())):
                                        # DEBUG print(perf[0], perf[1].strip())
                                        doc[perf[0]] = float(perf[1].strip())
                                    else:
                                        doc[perf[0]] = perf[1].strip()
                                else:
                                    perf_found = False
                                    # DEBUG exit()ClockStart
 
                            elif "Test ran to completion" in line or "Explicit failure triggered by test" in line:
                                # set status to pass
                                # DEBUG print(line)
                                status = "Pass"
                            elif "Platform Result Path:" in line:
                                rp = line.split("Platform Result Path: ")[1]
                        else:
                            if count < 5:
                                count = count + 1
                                # DEBUG print(line)
                                # DEBUG print(line.split("-- ")[-1])
                                # DEBUG print(line.split("-- ")[-1].split(":"))
                                perf = line.split("-- ")[-1].split(":")
                                # DEBUG print(perf[0], perf[1].strip())
                                if(is_number(perf[1].strip())):
                                    # DEBUG print(perf[0], perf[1].strip())
                                    doc[perf[0]] = float(perf[1].strip())
                                else:
                                    doc[perf[0]] = perf[1].strip()
                            else:
                                perf_found = False
                                # DEBUG exit()ClockStart
 
                doc["Test"] = test
                if "EUPerf" in test and "measure=lat" in test:
                    category = "PnP/Perf/uBM/EU/EU-Latency"
                elif "EUPerf" in test and "measure=lat" not in test:
                    category = "PnP/Perf/uBM/EU/EU-Throughput"
                elif "HdcLscSlmPerf" in test and "measure=lat" in test:
                    category = "PnP/Perf/uBM/GPGPU/Latency"
                elif "HdcLscSlmPerf" in test and "measure=lat" not in test:
                    if "l1" in test:
                        category = "PnP/Perf/uBM/GPGPU/L1-BW"
                    elif "slm" in test:
                        if "Atm" in test:
                            category = "PnP/Perf/uBM/GPGPU/SLM-Atomics"
                        else:
                            category = "PnP/Perf/uBM/GPGPU/SLM-BW"
                    elif "l3" in test:
                        if "Atm" in test:
                            category = "PnP/Perf/uBM/GPGPU/L3-Atomics"
                        else:
                            category = "PnP/Perf/uBM/GPGPU/L3-BW"
                elif "ComputeThreadDispatchPerf" in test:
                    category = "PnP/Perf/uBM/GPGPU/Thread-Dispatch"
                elif "localMemory" in test:
                    category = "PnP/Perf/uBM/SoC/MemoryController"
                doc["Test Category"] = category
                doc["Func Status"] = status
                doc["Waveform"] = rp
                doc["Axe Name"] = axe_name
                doc["Config"] = config
                doc["Execution Group"] = int(exe_group)
 
                row = row + 1
                col = 0
                for i in range(len(header)):
                    if header[i] in doc:
                        worksheet.write(row, col, doc[header[i]])
                    elif header[i] in "Actual Perf":
                       # =HEX2DEC(REPLACE([@[Achieved Target Clock Percent]],1,2,""))
                        formula = "=HEX2DEC(REPLACE(M" + str(row+1) + ',1,2,""))'
                        worksheet.write_formula(row, col, formula)
                    elif header[i] in "Actual Clocks":
                       # =HEX2DEC(REPLACE([@[Clock difference]],1,2,""))
                        formula = "=HEX2DEC(REPLACE(L" + str(row+1) + ',1,2,""))'
                        worksheet.write_formula(row, col, formula)
                    elif header[i] in "Perf Bucket":
                       # =IF([@Actual Perf]>100, "FAIL", "PASS")
                        formula = '=IF(O' + str(row+1) + '>105, "OVERPASS", IF(O' + str(row+1) + '>=95, "PASS", IF(O' + str(row+1) + '>=90, "5% to 10%", IF(O' + str(row+1) + '>=80, "10% to 20%", "20% +"))))'
                        worksheet.write_formula(row, col, formula)
                    elif header[i] in "Actual Rate":
                        # = [@[Metric Quantity]]/[@[Actual Clocks]]*1.7
                        if category == "PnP/Perf/uBM/GPGPU/Latency":
                            formula = "=N" + str(row+1) + "/D" + str(row+1) #N2/D2
                        else:
                            #formula = "=D" + str(row+1) + "/N" + str(row+1)
                            formula = "=PRODUCT(D" + str(row+1) + "/N" + str(row+1) + ",1.7)" # =PRODUCT(D1/N2,1.7)
                            print(formula)
                            worksheet.write_formula(row, col, formula)
                    elif header[i] in "Rate Delta":
                        # =[@[Theoretical Target Rate]]-[@[Actual Rate]]
                        formula = "=F" + str(row+1) + "-R" + str(row+1)
                        worksheet.write_formula(row, col, formula)
                    elif header[i] in "Rate Delta %":
                        # =[@[Rate Delta]]/[@[Theoretical Target Rate]]
                        formula = "=S" + str(row+1) + "/F" + str(row+1)
                        worksheet.write_formula(row, col, formula)
                    else:
                        worksheet.write(row, col, "NA")
                    col = col + 1
   
    workbook.close()
    os.system("echo 'Done' | mail -a axe_metadata_" + str(exe_group_name) + "_" + str(today) + ".xlsx -s 'AXE Perf Metadata Rollup' $USER@ecsmtp.fm.intel.com")
 
#main()
'''
print(os.getcwd())
#creating the folder structure
with open('folder_structure.txt','r') as folder:
    folder_name = folder.readlines()
    print(folder_name)
'''