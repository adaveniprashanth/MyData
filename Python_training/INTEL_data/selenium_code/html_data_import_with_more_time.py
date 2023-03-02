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
print(local_time)

print(os.listdir())
def removing_old_file():
	files = os.listdir()
	for i in files:
		path = os.path.join(os.getcwd(),i)

		if 'Axe' in path:print(path);os.remove(path)

	print(os.listdir())

removing_old_file()

def download_new_file():
	options = webdriver.ChromeOptions()
	prefs = {"download.default_directory": os.getcwd()}
	options.add_experimental_option('prefs', prefs)

	#set chromodriver.exe path
	# For chrome driver reference --> https://chromedriver.chromium.org/downloads
	s = Service("C:\chromedriver\chromedriver.exe")
	driver = webdriver.Chrome(service=s, options=options)
	# driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe",options=options)

	#launch URL to get data from axeweb page and kept idle for 5 seconds
	driver.get("https://axeweb.intel.com/axe/tests/testlists/306/latestresults/combined/executions")
	time.sleep(5)

	# opening the dropdown list at execution stage
	l = driver.find_element(By.XPATH,
							"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr[3]/th[1]/span")
	l.click()

	# selecting compare
	l = driver.find_element(By.XPATH, "//select/optgroup[@label='render Fulsim']/option[@label='Compare']")
	l.click()

	# selecting Lockup
	l = driver.find_element(By.XPATH, "//select/optgroup[@label='render']/option[@label='Lockup']")
	l.click()
	# making to sleep the driver for reloading with selected options
	time.sleep(5)

	# selecting the excel download option
	l = driver.find_element(By.XPATH,"//button[@class='btn btn-default buttons-collection']")
	l.click()
	time.sleep(20)
	# selecting the download option
	l = driver.find_element(By.XPATH,"//ul[@class='dropdown-menu']/li[@class='dt-button']")
	l.click()
	time.sleep(10)

	driver.quit()

download_new_file()

df = pd.read_csv(os.path.join(os.getcwd(),'Axe Datatable.csv'))
# print(df.columns)# printing column names
df.to_excel('abc.xlsx')

# separating the data based on execution stage types
execution_stage_groups = df.groupby('Execution Stage')

# selecting the compare and lockup groups from execution stage
compare_group = execution_stage_groups.get_group('Compare')
lockup_group = execution_stage_groups.get_group('Lockup')

# combining lockup and compare groups
combined_group =pd.concat([compare_group,lockup_group])
# separating only test area and result from combined group data
result_section = combined_group[['Test Area','Result']]

total_test_cases = result_section.shape[0]
total_pass = result_section.groupby('Result').get_group('Pass').shape[0]
total_fail = result_section.groupby('Result').get_group('Fail').shape[0]
remain_test_cases = total_test_cases - total_fail -total_pass

total_tests = [total_test_cases,total_pass,total_fail,remain_test_cases]
print(total_tests)


test_area_groups = result_section.groupby('Test Area')
total_groups = {}
for name,group in test_area_groups: #getting all grooups
	total = group.shape[0]
	data = group.groupby('Result')
	passed = 0; failed = 0
	for name1,group1 in data:
		final_results = list(group1['Result'])
		passed = final_results.count('Pass'); failed = final_results.count('Fail')
	remain = total - passed - failed
	# print(name,total,passed,failed,remain)
	total_groups[name] = [total,passed,failed,remain]

print(total_groups)

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

# total_attributes = {'GLOBALS/UnifiedMemory': [399, 0, 0, 111, 288, 0], 'HWFE/MemoryInterface': [84, 0, 6, 12, 66, 0], 'HWFE/Interrupt': [23, 0, 2, 3, 18, 0], 'HWFE/MicroController': [74, 0, 25, 49, 0, 0], 'GLOBALS/Flush': [18, 0, 0, 16, 2, 0], 'GLOBALS/Virtualization': [19, 0, 4, 0, 15, 0], 'GLOBALS/Caches': [63, 0, 47, 0, 16, 0], 'GLOBALS/HostGTAccesses': [17, 0, 10, 3, 4, 0], 'GLOBALS/Registers': [4, 0, 1, 1, 2, 0], 'HWFE/BatchBuffer': [20, 0, 0, 10, 10, 0], 'HWFE/Execlist': [37, 0, 37, 2, 32, 0], 'HWFE/RenderCompute': [1, 0, 0, 0, 1, 0], 'HWFE/RegisterAccess': [2, 0, 0, 0, 2, 0], 'HWFE/Semaphores': [11, 0, 0, 1, 10, 0], 'HWFE/Preemption': [2, 0, 0, 0, 2, 0], 'GLOBALS/PatMocs': [2, 0, 0, 2, 0, 0], 'Concurrency/AllEngine': [100, 0, 0, 100, 0, 0], 'Concurrency/ProducerConsumer': [22, 0, 0, 22, 0, 0]}
# overall_count = [898, 0, 98, 332, 468, 0]
# print(total_attributes)
# print(overall_count)

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


# creating and viewing the html files in python
# to open/create a new html file in the write mode
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
datepart1 = (
			'''<html><head>'''
			'''<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
			<script src="PTL_Media_jquery_functions_a0.js"></script>
			<style>
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
			</style>
			</head>'''
			'''<body>'''
			f'<h1>Last Updated: {local_time}</h1>'
)
overall_table = (
			'''<p></p><h2>Overall</h2>'''
'''<table><tr><th>Overall Status</th>		<th>Total Test cases</th>    <th>Pass</th>    <th>Fail</th>       <th>Remain</th><th>Pass percentage</th></tr>'''
f'<td>Overall_Status</td><td id="rowTotaltestcases">{total_tests[0]}</td><td id="rowPass">{total_tests[1]}</td><td id="rowfail">{total_tests[2]}</td><td id="rowremain">{total_tests[3]}</td><td id="rowpercentage" style="background-color:#{overall_colors[0]}">{str((total_tests[1]/total_tests[0])*100)[0:5]}%</td></tr>'
'''</table><p></p>'''
)

legcy_table_start = (
'''<h2>Legacy</h2>'''
'''<table>'''
'''<tr><th>Test Area</th>                <th>Total</th>               <th>Pass</th>          <th>Fail</th>                <th>Remain</th>                <th>Pass percentage</th></tr>'''
)

legcy_table_columns = (
f"<td>{group_names[0]}</td><td id='row2Total'>{total_groups[group_names[0]][0]}</td><td id='row2Pass'>{total_groups[group_names[0]][1]}</td><td id='row2Fail'>{total_groups[group_names[0]][2]}</td><td id='row2Remain'>{total_groups[group_names[0]][3]}</td><td id='row2perecentage' style='background-color:#{colors[group_names[0]]}'>{str((total_groups[group_names[0]][1]/total_groups[group_names[0]][0])*100)[0:5]}%</td></tr>"
f"<td>{group_names[1]}</td><td id='row2Total'>{total_groups[group_names[1]][0]}</td><td id='row2Pass'>{total_groups[group_names[1]][1]}</td><td id='row2Fail'>{total_groups[group_names[1]][2]}</td><td id='row2Remain'>{total_groups[group_names[1]][3]}</td><td id='row2perecentage' style='background-color:#{colors[group_names[1]]}'>{str((total_groups[group_names[1]][1]/total_groups[group_names[1]][0])*100)[0:5]}%</td></tr>"
)

columns_data = ''
group_total_pass = 0
group_total_fail = 0
group_total_remain = 0
group_total = 0
for i in range(0,len(group_names)):
	# print("group name",group_names[i])
	s = "<td>"+group_names[i]+"</td><td id=row"+str(i)+"Total>"+str(total_groups[group_names[i]][0])+"</td><td id=row"+str(i)+"Pass>"+str(total_groups[group_names[i]][1])+"</td><td id=row"+str(i)+"Fail>"+str(total_groups[group_names[i]][2])+"</td><td id=row"+str(i)+"Remain>"+str(total_groups[group_names[i]][3])+"</td><td id=row"+str(i)+"perecentage style='background-color:#"+colors[group_names[i]]+"'>"+str((total_groups[group_names[i]][1]/total_groups[group_names[i]][0])*100)[0:5]+"%</td></tr>\n"
	columns_data = columns_data+s
	group_total += total_groups[group_names[i]][0]
	group_total_pass+=total_groups[group_names[i]][1]
	group_total_fail+=total_groups[group_names[i]][2]
	group_total_remain+=total_groups[group_names[i]][3]
# print("length",len(group_names))

legcy_table_end = (
f'<tr><td style="background-color:#B6B6A8">All</td><td id="all_total1" style="background-color:#B6B6A8">{total_tests[0]}</td><td id="all_hw_pass1" style="background-color:#B6B6A8">{total_tests[1]}</td><td id="all_hw_fail1" style="background-color:#B6B6A8">{total_tests[2]}</td><td id="all_remain" style="background-color:#B6B6A8">{total_tests[3]}</td><td id="all_rm_fail1" style="background-color:#B6B6A8">{str((total_tests[1]/total_tests[0])*100)[0:5]}%</td></tr>'
f'<tr><td style="background-color:#B6B6A8">All</td><td id="all_total1" style="background-color:#B6B6A8">{group_total}</td><td id="all_hw_pass1" style="background-color:#B6B6A8">{group_total_pass}</td><td id="all_hw_fail1" style="background-color:#B6B6A8">{group_total_fail}</td><td id="all_remain" style="background-color:#B6B6A8">{group_total_remain}</td><td id="all_rm_fail1" style="background-color:#B6B6A8">{str((group_total_pass/group_total)*100)[0:5]}%</td></tr>'
'''</table><p></p></table></body></html>'''
)

"""
f"<td>{tal[1][0]}</td><td id='row3Total'>{tal[1][1][0]}</td><td id='row3Error'>{tal[1][1][1]}</td><td id='row3Fail'>{tal[1][1][2]}</td><td id='row3NotRun'>{tal[1][1][3]}</td><td id='row3Pass'>{tal[1][1][4]}</td><td id='row3Warn'>{tal[1][1][5]}</td><td id='row3perecentage' style='background-color:#{colors[1]}'>{str((tal[1][1][4]/tal[1][1][0])*100)[0:5]}%</td></tr>"
"""

# writing the code into the file
f.write(datepart1+"\n")
f.write(overall_table+"\n")
f.write(legcy_table_start+"\n")
# f.write(legcy_table_columns+"\n")
f.write(columns_data+"\n")
f.write(legcy_table_end+"\n")

# close the file
f.close()

#  open html files in chrome
filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
webbrowser.open_new_tab(filename)




# getting the html code from webpage
'''
# import requests
#
# import urllib.request, urllib.error, urllib.parse
#
# url = 'https://axeweb.intel.com/axe/tests/testlists/306/latestresults/combined/executions?executionStageId=3528,3529'
#
# r = requests.get(url, allow_redirects=True)
# open('testing1.txt', 'wb').write(r.content)
#
#
# # url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
# #
# # response = urllib.request.urlopen(url)
# # webContent = response.read().decode('UTF-8')
# #
# # f = open('obo-t17800628-33.html', 'w')
# # f.write(webContent)
# # f.close
'''



# html pagae received from aravind
html_template = """

			<html>

			<head>

			<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>

			<script src="PTL_Media_jquery_functions_a0.js"></script>
			<style>

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

			</style>

			</head>

			<body>

			<h1>Last Updated: Thu Jan  5 11:51:59 2023</h1>

			<h2>Selected Query:</h2>

			<span class="query">SELECT * FROM TestView WHERE(TestListID IN(</span>

			<span id="testListIDs" class="query"></span>
			<span class="query">))</span>

			<p></p><h2>Overall</h2>
<table>
<tr><th>Overall Status</th><th>Total</th><th>HW Pass</th><th>HW Miscompare</th><th>HW Hang</th><th>HW Error</th><th>RM Pass</th><th>RM Fail</th><th>RM Error</th><th>New</th><th>Gated</th><th>Gated HW</th><th>TBD</th><th>HW Pass Rate</th><th>Exec HW Pass Rate</th><th>RM Pass Rate</th></tr>
<td>Overall_Status</td><td id="row1Total">10963</td><td id="row1HWpass">62</td><td id="row1HWfail">4</td><td id="row1HWhang">30</td><td id="row1HWerror">66</td><td id="row1RMpass">7749</td><td id="row1RMfail">0</td><td id="row1RMerror">2965</td><td id="row1New">87</td><td id="row1Gated">0</td><td id="row1GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.57%</td><td style="background-color:#FF0000">38.27%</td><td style="background-color:#FF0000">72.16%</td></tr>
</table>

			<p>

			</p>
<h2>Legacy</h2>
<table>
<tr><th>Units</th><th>Total</th><th>HW Pass</th><th>HW Miscompare</th><th>HW Hang</th><th>HW Error</th><th>RM Pass</th><th>RM Fail</th><th>RM Error</th><th>New</th><th>Gated</th><th>Gated HW</th><th>TBD</th><th>HW Pass Rate</th><th>Exec HW Pass Rate</th><th>RM Pass Rate</th></tr>
<td>Legacy.Decode.AV1</td><td id="row2Total">2709</td><td id="row2HWpass">0</td><td id="row2HWfail">0</td><td id="row2HWhang">0</td><td id="row2HWerror">0</td><td id="row2RMpass">2590</td><td id="row2RMfail">0</td><td id="row2RMerror">110</td><td id="row2New">9</td><td id="row2Gated">0</td><td id="row2GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">95.61%</td></tr>
<td>Legacy.Decode.HEVC</td><td id="row3Total">2091</td><td id="row3HWpass">0</td><td id="row3HWfail">0</td><td id="row3HWhang">0</td><td id="row3HWerror">0</td><td id="row3RMpass">1352</td><td id="row3RMfail">0</td><td id="row3RMerror">739</td><td id="row3New">0</td><td id="row3Gated">0</td><td id="row3GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">64.66%</td></tr>
<td>Legacy.VEBOX</td><td id="row21Total">274</td><td id="row21HWpass">38</td><td id="row21HWfail">2</td><td id="row21HWhang">28</td><td id="row21HWerror">64</td><td id="row21RMpass">129</td><td id="row21RMfail">0</td><td id="row21RMerror">13</td><td id="row21New">0</td><td id="row21Gated">0</td><td id="row21GatedHW">0</td><td>0</td><td style="background-color:#FF0000">13.87%</td><td style="background-color:#FF0000">28.79%</td><td style="background-color:#008000">95.26%</td></tr>
<tr><td style="background-color:#B6B6A8">All</td><td id="all_total1" style="background-color:#B6B6A8">10963</td><td id="all_hw_pass1" style="background-color:#B6B6A8">62</td><td id="all_hw_fail1" style="background-color:#B6B6A8">4</td><td id="all_hw_hang1" style="background-color:#B6B6A8">30</td><td id="all_hw_error1" style="background-color:#B6B6A8">66</td><td id="all_rm_pass1" style="background-color:#B6B6A8">7749</td><td id="all_rm_fail1" style="background-color:#B6B6A8">0</td><td id="all_rm_error1" style="background-color:#B6B6A8">2965</td><td id="all_new1" style="background-color:#B6B6A8">87</td><td id="all_gated1" style="background-color:#B6B6A8">0</td><td id="all_gated_hw1" style="background-color:#B6B6A8">0</td><td id="all_tbd1" style="background-color:#B6B6A8">0</td><td style="background-color:#FF0000">0.57%</td><td style="background-color:#FF0000">38.27%</td><td style="background-color:#FF0000">72.16%</td></tr>
</table>
			<p>

			</p>
</table>


				</body>

				</html>
"""