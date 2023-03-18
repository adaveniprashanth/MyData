import sys,os,time
from datetime import datetime
import webbrowser
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")
print("date", dt_string)

seconds = time.time()# get the current time in seconds since the epoch
# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)
#print(local_time)

print(os.listdir())
def removing_old_file():
	files = os.listdir()
	for i in files:
		path = os.path.join(os.getcwd(),i)

		if 'Axe' in path:print(path);os.remove(path)

	print(os.listdir())


def download_new_file():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": os.getcwd()}
    options.add_experimental_option('prefs', prefs)

	#set chromodriver.exe path
	# For chrome driver reference --> https://chromedriver.chromium.org/downloads
    s = Service("C:\chromedriver\chromedriver.exe")
	#driver = webdriver.Chrome(service=s, options=options)
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe",options=options)

    #launch URL to get data from axeweb page and kept idle for 5 seconds
    driver.get("https://axeweb.intel.com/axe/tests/testlists/295/latestresults/combined/executions?executionStageId=3360,4363,4409")
    time.sleep(20)
    
    # selecting the download option
    l = driver.find_element(By.XPATH,"//button[@class='btn btn-default buttons-collection']")
    l.click()
    time.sleep(10)
    # clicking the download option
    l = driver.find_element(By.XPATH,"//ul[@class='dropdown-menu']/li[@class='dt-button']")
    l.click()
    time.sleep(20)
    driver.quit()


#removing_old_file()
#download_new_file()

path = os.path.join(os.getcwd(),'Axe Datatable.csv')
print(path)
df = pd.read_csv(path)
#df = pd.read_csv(os.path.join(os.getcwd(),'Axe_Datatable.csv'))
# print(df.columns)# printing column names
#df.to_excel('abc.xlsx')
df.head(5)
# separating the data based on execution stage types
execution_stage_groups = df.groupby('Execution Stage')

# selecting the Renderfulsim, Rendermill and Fulsim_Tests groups from execution stage
Renderfulsim_group = execution_stage_groups.get_group('2x4x8 Renderfulsim')
Rendermill_group = execution_stage_groups.get_group('2x4x8 Rendermill')
Fulsim_Tests_group = execution_stage_groups.get_group('Fulsim_Tests')

# combining lockup and compare groups
combined_group =pd.concat([Renderfulsim_group,Rendermill_group,Fulsim_Tests_group])

# separating only test area and result from combined group data
result_section = combined_group[['Test Area','Result']]

#total test cases from 3 execution areas
#print(result_section.shape)

total_test_cases = result_section.shape[0]
total_pass = result_section.groupby('Result').get_group('Pass').shape[0]
total_fail = result_section.groupby('Result').get_group('Fail').shape[0]
total_warn = result_section.groupby('Result').get_group('Warn').shape[0]
total_error = result_section.groupby('Result').get_group('Error').shape[0]
remain_test_cases = total_test_cases - total_fail -total_pass - total_warn - total_error

total_tests = [total_test_cases,total_pass,total_fail,total_warn,total_error,remain_test_cases]
print(total_tests)


Executions_stage_results = []
for group_name,group in execution_stage_groups:
    #print(group_name)
    group = group[['Test Area','Result']]
    #print(group)
    test_area_groups = group.groupby('Test Area')
    total_groups = {}
    for name,group in test_area_groups: #getting all grooups
        total = group.shape[0]
        data = group.groupby('Result')
        passed = 0; failed = 0;warnings = 0;errors = 0
        for name1,group1 in data:
            final_results = list(group1['Result'])
            passed = final_results.count('Pass'); failed = final_results.count('Fail')
            warnings = final_results.count('Warn');errors = final_results.count('Error')
        remain = total - passed - failed - warnings - errors
        #print(name,total,passed,failed,warnings,errors,remain)
        total_groups[name] = [total,passed,failed,warnings,errors,remain]
    Executions_stage_results.append([group_name,total_groups])





overall_colors = []
def find_overall_colors(total_tests1):
	percent =  (total_tests1[1]/total_tests1[0])*100
	if percent < 70:
		overall_colors.append('FF0000')#red color
	elif percent > 70 and percent < 80:
		overall_colors.append('FFFF00')#yellow
	elif percent > 80 and percent < 90:
		overall_colors.append('8AE62E')#light green
	elif percent > 90 and percent <= 100:
		overall_colors.append('008000')# heavy green
		# overall_colors.append('808080')#gray color
find_overall_colors(total_tests)



"""
# total_attributes = {'GLOBALS/UnifiedMemory': [399, 0, 0, 111, 288, 0], 'HWFE/MemoryInterface': [84, 0, 6, 12, 66, 0], 'HWFE/Interrupt': [23, 0, 2, 3, 18, 0], 'HWFE/MicroController': [74, 0, 25, 49, 0, 0], 'GLOBALS/Flush': [18, 0, 0, 16, 2, 0], 'GLOBALS/Virtualization': [19, 0, 4, 0, 15, 0], 'GLOBALS/Caches': [63, 0, 47, 0, 16, 0], 'GLOBALS/HostGTAccesses': [17, 0, 10, 3, 4, 0], 'GLOBALS/Registers': [4, 0, 1, 1, 2, 0], 'HWFE/BatchBuffer': [20, 0, 0, 10, 10, 0], 'HWFE/Execlist': [37, 0, 37, 2, 32, 0], 'HWFE/RenderCompute': [1, 0, 0, 0, 1, 0], 'HWFE/RegisterAccess': [2, 0, 0, 0, 2, 0], 'HWFE/Semaphores': [11, 0, 0, 1, 10, 0], 'HWFE/Preemption': [2, 0, 0, 0, 2, 0], 'GLOBALS/PatMocs': [2, 0, 0, 2, 0, 0], 'Concurrency/AllEngine': [100, 0, 0, 100, 0, 0], 'Concurrency/ProducerConsumer': [22, 0, 0, 22, 0, 0]}
# overall_count = [898, 0, 98, 332, 468, 0]
# print(total_attributes)
# print(overall_count)
"""

"""
colors = {}
group_names = []
# finding the colors for the test area values
for group_name,value in total_groups.items():
	percent = (value[1]/value[0]) * 100
	# print(percent)
	group_names.append(group_name)
	if percent < 70:
		colors[group_name]='FF0000'#red color
	elif percent > 70 and percent < 80:
		colors[group_name]='FFFF00'#yellow
	elif percent > 80 and percent < 90:
		colors[group_name]='8AE62E'#light green
	elif percent > 90 and percent <= 100:
		colors[group_name]='008000'# heavy green

"""
def create_color_value(data):
    pass
    percent = (data[1]/data[0]) * 100
	# print(percent)
    if percent < 25:
        return 'FF0000'#red color
    elif percent >= 25 and percent < 50:
        return 'FFFF00'#yellow
    elif percent >= 50 and percent < 75:
        return '8AE62E'#light green
    elif percent >= 75 and percent <= 100:
        return '008000'# heavy green

# the html code which will go in the file GFG.html
page_start = ('''<html>\n''')
head_start = ('''<head>\n''')
style_code = ('''<style>
			table, th, td {border: 1px solid black;
						   border-collapse:collapse;
						   font-family: "Arial";}
			th, td {padding: 5px;}
			th {text-align: center;
				color: white;
				background-color: #3E5A93;}
			td {background-color: #FFB84D;}
			h2 {font-family: "Arial";
				font-size: 20px;}
			h1 {font-family: "Arial";
				font-size: 12px;}
			span {font-family: "Arial";
				font-size: 10px;}
			</style>\n''')

head_close=('''</head>\n''')
body_start = ('''<body>\n''')
date_details = (f'<h1>Last Updated: {local_time}</h1>')
overall_heading = ('''<h2>Overall</h2>\n''')
table_start = ('''<table>\n''')
table_close = ('''</table>\n''')
body_close = ('''</body>\n''')
page_close = ('''</html>\n''')


# creating and viewing the html files in python
# to open/create a new html file in the write mode
f = open('practice_with_separate_tables.html', 'w')
f.writelines([page_start,head_start,style_code,head_close,body_start,date_details])

#writing the overall table data
overall_table = (
			'''<p></p><h2>Overall</h2>'''
'''<table><tr><th>Overall Status</th><th>Total Test cases</th><th>Pass</th><th>Fail</th><th>Warn</th><th>Error</th><th>Remain</th><th>Pass percentage</th></tr>'''
f'<td>Overall_Status</td><td>{total_tests[0]}</td><td>{total_tests[1]}</td><td>{total_tests[2]}</td><td>{total_tests[3]}</td><td>{total_tests[4]}</td><td>{total_tests[5]}</td><td style="background-color:#{create_color_value(total_tests)}">{str((total_tests[1]/total_tests[0])*100)[0:5]}%</td></tr>'
'''</table><p></p>'''
)

f.write(overall_table+"\n")

def table_heading_creation(data):
    pass
    f.write(f"<p></p><h2>{data}</h2>")
    
def table_data_creation(data):
    total = passed = failed = warned = error = remained = 0
    for k,v in data.items():
        f.write(f"<tr><td>{k}</td><td>{v[0]}</td><td>{v[1]}</td><td>{v[2]}</td><td>{v[3]}</td><td>{v[4]}</td><td>{v[5]}</td><td id=row2perecentage style='background-color:#{create_color_value(v)}'>{str((v[1]/v[0])*100)[:5]}%</td></tr>")
        total+=v[0]
        passed+=v[1]
        failed+=v[2]
        warned+=v[3]
        error+=v[4]
        remained+=v[5]
    return total,passed,failed,warned,error,remained

#print(Executions_stage_results)

#test area tables creation
for i in Executions_stage_results:
    print(i)
    table_heading_creation(i[0])
    f.write(table_start)
    f.write('''<tr><th>Test Area</th><th>Total</th><th>Pass</th><th>Fail</th><th>Warn</th><th>Error</th><th>Remain</th><th>Pass %    </th></tr>''')
    returned = table_data_creation(i[1])
    f.write(f"<tr><td style='background-color:#B6B6A8'>All</td><td style='background-color:#B6B6A8'>{returned[0]}</td><td style='background-color:#B6B6A8'>{returned[1]}</td><td style='background-color:#B6B6A8'>{returned[2]}</td><td style='background-color:#B6B6A8'>{returned[3]}</td><td style='background-color:#B6B6A8'>{returned[4]}</td><td style='background-color:#B6B6A8'>{returned[5]}</td><td id=row2perecentage style='background-color:#{create_color_value(returned)}'>{str((returned[1]/returned[0])*100)[:5]}%</td></tr>")
    #print(returned)
    f.write(table_close)



f.writelines(['<p></p><p></p>',body_close,page_close])

# close the file
f.close()

#  open html files in chrome
#filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'