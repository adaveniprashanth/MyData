
from datetime import datetime
import time
import webbrowser
import os
now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")
print("date", dt_string)

# get the current time in seconds since the epoch
seconds = time.time()
# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)
print(local_time)

# getting the data from the axeweb page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select



#set chromodriver.exe path
# driver = webdriver.Chrome(executable_path="chromedriver.exe")
# For chrome driver reference --> https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
# driver = webdriver.Chrome()
#launch URL and kept idle for 5 seconds
driver.get("https://axeweb.intel.com/axe/tests/testlists/306/latestresults/combined/executions")
time.sleep(5)

# opening the dropdown list at execution stage
l = driver.find_element(By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr[3]/th[1]/span")
l.click()

#selecting compare
l = driver.find_element(By.XPATH,"//select/optgroup[@label='render Fulsim']/option[@label='Compare']")
l.click()

#selecting Lockup
l = driver.find_element(By.XPATH,"//select/optgroup[@label='render']/option[@label='Lockup']")
l.click()
# making to sleep the driver for reloading with selected options
time.sleep(5)
# total count
total_count= driver.find_element(By.XPATH,'//div[@class="dataTables_info"]').text

#completed the execution stage selection

# selecting the result value from dropdown
l = driver.find_element(By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr[3]/th[6]/span/select")
print(l)
drop = Select(l)

#
# # working code for reference
# #selecting the warn option and getting the count
# drop.select_by_value("Warn")
# time.sleep(5)
# warn_count= driver.find_element(By.XPATH,'//div[@class="dataTables_info"]').text
# #removing all the options
# drop.deselect_all()

# filling the text box
# l = driver.find_element(By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr[3]/th[2]/input")


def get_actual_count(a):
	a = a.strip()
	if a == 'No records found':
		a = 0
	else:
		a = int(a.split(" ")[5])
	return a

overall_count = [get_actual_count(total_count)]
overall_list=['Error','Fail','NotRun','Pass','Warn']

for result in overall_list:
	drop.select_by_value(result)
	time.sleep(8)
	total = driver.find_element(By.XPATH,'//div[@class="dataTables_info"]').text
	overall_count.append(get_actual_count(total))
	drop.deselect_all()

overall_colors = []
colors = []
def find_overall_colors(a):
	percent =  int((a[4]/a[0])*100)
	if percent < 70:
		overall_colors.append('FF0000')#red color
	elif percent > 70 and percent < 80:
		overall_colors.append('FFFF00')#yellow
	elif percent > 80 and percent < 90:
		overall_colors.append('8AE62E')#light green
	elif percent > 90 and percent <= 100:
		overall_colors.append('008000')# heavy green
		# overall_colors.append('808080')#gray color

find_overall_colors(overall_count)

f = open('GFG.html', 'w')
html_template1 = (
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
			'''<p></p><h2>Overall</h2>'''
'''<table><tr><th>Overall Status</th>		<th>Total Test cases</th>								<th>Error</th>                                  <th>Fail</th>                                                                        <th>NotRun</th>                                                                          <th>Pass</th>                            <th>Warn</th>                                                            <th>Pass percentage</th></tr>'''
f'<td>Overall_Status</td><td id="row1Totaltestcases">{overall_count[0]}</td><td id="row1Error">{overall_count[1]}</td><td id="row1fail">{overall_count[2]}</td><td id="row1NotRun">{overall_count[3]}</td><td id="row1Pass">{overall_count[4]}</td><td id="row1Warn">{overall_count[5]}</td><td id="row1percentage" style="background-color:#{overall_colors[0]}">{str((overall_count[4]/overall_count[0])*100)[0:5]}%</td></tr>'
'''</table><p></p>'''
)
f.write(html_template1)
f.close()

filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
webbrowser.open_new_tab(filename)



test_area_names = ['GLOBALS/UnifiedMemory','HWFE/MemoryInterface','HWFE/Interrupt',
'HWFE/MicroController','GLOBALS/Flush','GLOBALS/Virtualization','GLOBALS/Caches',
'GLOBALS/HostGTAccesses','GLOBALS/Registers','HWFE/BatchBuffer','HWFE/Execlist','HWFE/RenderCompute',
'HWFE/RegisterAccess','HWFE/Semaphores','HWFE/Preemption','GLOBALS/PatMocs','Concurrency/AllEngine',
'Concurrency/ProducerConsumer']

result_values = ['Error','Fail','NotRun','Pass','Warn']

total_attributes = {}
# filling the test area text box
l = driver.find_element(By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr[3]/th[2]/input")

for test_area in test_area_names:
	print("test area ",test_area)
	result_count = []
	# sending the value to fill the text box
	l.send_keys(test_area)
	time.sleep(5)
	total = driver.find_element(By.XPATH, '//div[@class="dataTables_info"]').text
	result_count.append(get_actual_count(total))
	for result in result_values:
		drop.select_by_value(result)
		time.sleep(5)
		count = driver.find_element(By.XPATH, '//div[@class="dataTables_info"]').text
		result_count.append(get_actual_count(count))
		drop.deselect_all()
		time.sleep(5)
	# clear the text box
	l.clear()
	time.sleep(5)
	total_attributes[test_area]=result_count


driver.quit()
print(total_attributes)
print(overall_count)



# total_attributes = {'GLOBALS/UnifiedMemory': [399, 0, 0, 111, 288, 0], 'HWFE/MemoryInterface': [84, 0, 6, 12, 66, 0], 'HWFE/Interrupt': [23, 0, 2, 3, 18, 0], 'HWFE/MicroController': [74, 0, 25, 49, 0, 0], 'GLOBALS/Flush': [18, 0, 0, 16, 2, 0], 'GLOBALS/Virtualization': [19, 0, 4, 0, 15, 0], 'GLOBALS/Caches': [63, 0, 47, 0, 16, 0], 'GLOBALS/HostGTAccesses': [17, 0, 10, 3, 4, 0], 'GLOBALS/Registers': [4, 0, 1, 1, 2, 0], 'HWFE/BatchBuffer': [20, 0, 0, 10, 10, 0], 'HWFE/Execlist': [37, 0, 37, 2, 32, 0], 'HWFE/RenderCompute': [1, 0, 0, 0, 1, 0], 'HWFE/RegisterAccess': [2, 0, 0, 0, 2, 0], 'HWFE/Semaphores': [11, 0, 0, 1, 10, 0], 'HWFE/Preemption': [2, 0, 0, 0, 2, 0], 'GLOBALS/PatMocs': [2, 0, 0, 2, 0, 0], 'Concurrency/AllEngine': [100, 0, 0, 100, 0, 0], 'Concurrency/ProducerConsumer': [22, 0, 0, 22, 0, 0]}
# overall_count = [898, 0, 98, 332, 468, 0]

# print(total_attributes)
# print(overall_count)


tal = []#total area list
for i,j in total_attributes.items():
	tal.append([i,j])

# get the current time in seconds since the epoch
seconds = time.time()
# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)
# print(local_time)



total_cases = 0;total_errors = 0;total_fail = 0
total_notrun = 0;total_pass = 0;total_warn = 0


# finding the colors for the test area values
for i in range(len(tal)):
	value = (tal[i][1][4] / tal[i][1][0]) * 100
	# print(value)
	if value < 70:
		colors.append('FF0000')#red color
	elif value > 70 and value < 80:
		colors.append('FFFF00')#yellow
	elif value > 80 and value < 90:
		colors.append('8AE62E')#light green
	elif value > 90 and value <= 100:
		colors.append('008000')# heavy green

	total_cases += tal[i][1][0];total_errors += tal[i][1][1];total_fail += tal[i][1][2]
	total_notrun += tal[i][1][3];total_pass += tal[i][1][4];total_warn += tal[i][1][5]

summarized_values =[total_cases,total_errors,total_fail,total_notrun,total_pass,total_warn]



# creating and viewing the html files in python
# to open/create a new html file in the write mode
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template1 = (
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
			'''<p></p><h2>Overall</h2>'''
'''<table><tr><th>Overall Status</th>		<th>Total Test cases</th>								<th>Error</th>                                  <th>Fail</th>                                                                        <th>NotRun</th>                                                                          <th>Pass</th>                            <th>Warn</th>                                                            <th>Pass percentage</th></tr>'''
f'<td>Overall_Status</td>			n<td id="row1Totaltestcases">{overall_count[0]}</td><td id="row1Error">{overall_count[1]}</td><td id="row1fail">{overall_count[2]}</td><td id="row1NotRun">{overall_count[3]}</td><td id="row1Pass">{overall_count[4]}</td><td id="row1Warn">{overall_count[5]}</td><td id="row1percentage" style="background-color:#{overall_colors[0]}">{str((overall_count[4]/overall_count[0])*100)[0:5]}%</td></tr>'
'''</table><p></p>'''
'''<h2>Legacy</h2>'''
'''<table>'''
'''<tr><th>Test Area</th>                <th>Total</th>                       <th>Error</th>                       <th>Fail</th>                                                          <th>NotRun</th>                                                         <th>Pass</th>                                                         <th>Warn</th>                  <th>Pass percentage</th></tr>'''
f"<td>{tal[0][0]}</td><td id='row2Total'>{tal[0][1][0]}</td><td id='row2Error'>{tal[0][1][1]}</td><td id='row2Fail'>{tal[0][1][2]}</td><td id='row2NotRun'>{tal[0][1][3]}</td><td id='row2Pass'>{tal[0][1][4]}</td><td id='row2Warn'>{tal[0][1][5]}</td><td id='row2perecentage' style='background-color:#{colors[0]}'>{str((tal[0][1][4]/tal[0][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[1][0]}</td><td id='row3Total'>{tal[1][1][0]}</td><td id='row3Error'>{tal[1][1][1]}</td><td id='row3Fail'>{tal[1][1][2]}</td><td id='row3NotRun'>{tal[1][1][3]}</td><td id='row3Pass'>{tal[1][1][4]}</td><td id='row3Warn'>{tal[1][1][5]}</td><td id='row3perecentage' style='background-color:#{colors[1]}'>{str((tal[1][1][4]/tal[1][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[2][0]}</td><td id='row4Total'>{tal[2][1][0]}</td><td id='row4Error'>{tal[2][1][1]}</td><td id='row4Fail'>{tal[2][1][2]}</td><td id='row4NotRun'>{tal[2][1][3]}</td><td id='row4Pass'>{tal[2][1][4]}</td><td id='row4Warn'>{tal[2][1][5]}</td><td id='row4perecentage' style='background-color:#{colors[2]}'>{str((tal[2][1][4]/tal[2][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[3][0]}</td><td id='row5Total'>{tal[3][1][0]}</td><td id='row5Error'>{tal[3][1][1]}</td><td id='row5Fail'>{tal[3][1][2]}</td><td id='row5NotRun'>{tal[3][1][3]}</td><td id='row5Pass'>{tal[3][1][4]}</td><td id='row5Warn'>{tal[3][1][5]}</td><td id='row5perecentage' style='background-color:#{colors[3]}'>{str((tal[3][1][4]/tal[3][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[4][0]}</td><td id='row6Total'>{tal[4][1][0]}</td><td id='row6Error'>{tal[4][1][1]}</td><td id='row6Fail'>{tal[4][1][2]}</td><td id='row6NotRun'>{tal[4][1][3]}</td><td id='row6Pass'>{tal[4][1][4]}</td><td id='row6Warn'>{tal[4][1][5]}</td><td id='row6perecentage' style='background-color:#{colors[4]}'>{str((tal[4][1][4]/tal[4][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[5][0]}</td><td id='row7Total'>{tal[5][1][0]}</td><td id='row7Error'>{tal[5][1][1]}</td><td id='row7Fail'>{tal[5][1][2]}</td><td id='row7NotRun'>{tal[5][1][3]}</td><td id='row7Pass'>{tal[5][1][4]}</td><td id='row7Warn'>{tal[5][1][5]}</td><td id='row7perecentage' style='background-color:#{colors[5]}'>{str((tal[5][1][4]/tal[5][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[6][0]}</td><td id='row8Total'>{tal[6][1][0]}</td><td id='row8Error'>{tal[6][1][1]}</td><td id='row8Fail'>{tal[6][1][2]}</td><td id='row8NotRun'>{tal[6][1][3]}</td><td id='row8Pass'>{tal[6][1][4]}</td><td id='row8Warn'>{tal[6][1][5]}</td><td id='row8perecentage' style='background-color:#{colors[6]}'>{str((tal[6][1][4]/tal[6][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[7][0]}</td><td id='row9Total'>{tal[7][1][0]}</td><td id='row9Error'>{tal[7][1][1]}</td><td id='row9Fail'>{tal[7][1][2]}</td><td id='row9NotRun'>{tal[7][1][3]}</td><td id='row9Pass'>{tal[7][1][4]}</td><td id='row9Warn'>{tal[7][1][5]}</td><td id='row9perecentage' style='background-color:#{colors[7]}'>{str((tal[7][1][4]/tal[7][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[8][0]}</td><td id='row10Total'>{tal[8][1][0]}</td><td id='row10Error'>{tal[8][1][1]}</td><td id='row10Fail'>{tal[8][1][2]}</td><td id='row10NotRun'>{tal[8][1][3]}</td><td id='row10Pass'>{tal[8][1][4]}</td><td id='row10Warn'>{tal[8][1][5]}</td><td id='row10perecentage' style='background-color:#{colors[8]}'>{str((tal[8][1][4]/tal[8][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[9][0]}</td><td id='row11Total'>{tal[9][1][0]}</td><td id='row11Error'>{tal[9][1][1]}</td><td id='row11Fail'>{tal[9][1][2]}</td><td id='row11NotRun'>{tal[9][1][3]}</td><td id='row11Pass'>{tal[9][1][4]}</td><td id='row11Warn'>{tal[9][1][5]}</td><td id='row11perecentage' style='background-color:#{colors[9]}'>{str((tal[9][1][4]/tal[9][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[10][0]}</td><td id='row12Total'>{tal[10][1][0]}</td><td id='row12Error'>{tal[10][1][1]}</td><td id='row12Fail'>{tal[10][1][2]}</td><td id='row12NotRun'>{tal[10][1][3]}</td><td id='row12Pass'>{tal[10][1][4]}</td><td id='row12Warn'>{tal[10][1][5]}</td><td id='row12perecentage' style='background-color:#{colors[10]}'>{str((tal[10][1][4]/tal[10][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[11][0]}</td><td id='row13Total'>{tal[11][1][0]}</td><td id='row13Error'>{tal[11][1][1]}</td><td id='row13Fail'>{tal[11][1][2]}</td><td id='row13NotRun'>{tal[11][1][3]}</td><td id='row13Pass'>{tal[11][1][4]}</td><td id='row13Warn'>{tal[11][1][5]}</td><td id='row13perecentage' style='background-color:#{colors[11]}'>{str((tal[11][1][4]/tal[11][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[12][0]}</td><td id='row14Total'>{tal[12][1][0]}</td><td id='row14Error'>{tal[12][1][1]}</td><td id='row14Fail'>{tal[12][1][2]}</td><td id='row14NotRun'>{tal[12][1][3]}</td><td id='row14Pass'>{tal[12][1][4]}</td><td id='row14Warn'>{tal[12][1][5]}</td><td id='row14perecentage' style='background-color:#{colors[12]}'>{str((tal[12][1][4]/tal[12][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[13][0]}</td><td id='row15Total'>{tal[13][1][0]}</td><td id='row15Error'>{tal[13][1][1]}</td><td id='row15Fail'>{tal[13][1][2]}</td><td id='row15NotRun'>{tal[13][1][3]}</td><td id='row15Pass'>{tal[13][1][4]}</td><td id='row15Warn'>{tal[13][1][5]}</td><td id='row15perecentage' style='background-color:#{colors[13]}'>{str((tal[13][1][4]/tal[13][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[14][0]}</td><td id='row16Total'>{tal[14][1][0]}</td><td id='row16Error'>{tal[14][1][1]}</td><td id='row16Fail'>{tal[14][1][2]}</td><td id='row16NotRun'>{tal[14][1][3]}</td><td id='row16Pass'>{tal[14][1][4]}</td><td id='row16Warn'>{tal[14][1][5]}</td><td id='row16perecentage' style='background-color:#{colors[14]}'>{str((tal[14][1][4]/tal[14][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[15][0]}</td><td id='row17Total'>{tal[15][1][0]}</td><td id='row17Error'>{tal[15][1][1]}</td><td id='row17Fail'>{tal[15][1][2]}</td><td id='row17NotRun'>{tal[15][1][3]}</td><td id='row17Pass'>{tal[15][1][4]}</td><td id='row17Warn'>{tal[15][1][5]}</td><td id='row17perecentage' style='background-color:#{colors[15]}'>{str((tal[15][1][4]/tal[15][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[16][0]}</td><td id='row18Total'>{tal[16][1][0]}</td><td id='row18Error'>{tal[16][1][1]}</td><td id='row18Fail'>{tal[16][1][2]}</td><td id='row18NotRun'>{tal[16][1][3]}</td><td id='row18Pass'>{tal[16][1][4]}</td><td id='row18Warn'>{tal[16][1][5]}</td><td id='row18perecentage' style='background-color:#{colors[16]}'>{str((tal[16][1][4]/tal[16][1][0])*100)[0:5]}%</td></tr>"
f"<td>{tal[17][0]}</td><td id='row19Total'>{tal[17][1][0]}</td><td id='row19Error'>{tal[17][1][1]}</td><td id='row19Fail'>{tal[17][1][2]}</td><td id='row19NotRun'>{tal[17][1][3]}</td><td id='row19Pass'>{tal[17][1][4]}</td><td id='row19Warn'>{tal[17][1][5]}</td><td id='row19perecentage' style='background-color:#{colors[17]}'>{str((tal[17][1][4]/tal[17][1][0])*100)[0:5]}%</td></tr>"
f'<tr><td style="background-color:#B6B6A8">All</td><td id="all_total1" style="background-color:#B6B6A8">{summarized_values[0]}</td><td id="all_hw_pass1" style="background-color:#B6B6A8">{summarized_values[1]}</td><td id="all_hw_fail1" style="background-color:#B6B6A8">{summarized_values[2]}</td><td id="all_hw_hang1" style="background-color:#B6B6A8">{summarized_values[3]}</td><td id="all_hw_error1" style="background-color:#B6B6A8">{summarized_values[4]}</td><td id="all_rm_pass1" style="background-color:#B6B6A8">{summarized_values[5]}</td><td id="all_rm_fail1" style="background-color:#B6B6A8">{str((summarized_values[4]/summarized_values[0])*100)[0:5]}%</td></tr>'
'''</table><p></p></table></body></html>'''
)


# writing the code into the file
f.write(html_template1)

# close the file
f.close()

# 1st method how to open html files in chrome using
# filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
# webbrowser.open_new_tab(filename)




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
<td>Legacy.Decode.AVC</td><td id="row4Total">1458</td><td id="row4HWpass">0</td><td id="row4HWfail">0</td><td id="row4HWhang">0</td><td id="row4HWerror">0</td><td id="row4RMpass">1240</td><td id="row4RMfail">0</td><td id="row4RMerror">218</td><td id="row4New">0</td><td id="row4Gated">0</td><td id="row4GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#8AE62E">85.05%</td></tr>
<td>Legacy.Decode.JPEG</td><td id="row5Total">357</td><td id="row5HWpass">0</td><td id="row5HWfail">0</td><td id="row5HWhang">0</td><td id="row5HWerror">0</td><td id="row5RMpass">348</td><td id="row5RMfail">0</td><td id="row5RMerror">9</td><td id="row5New">0</td><td id="row5Gated">0</td><td id="row5GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">97.48%</td></tr>
<td>Legacy.Decode.MP2</td><td id="row6Total">50</td><td id="row6HWpass">0</td><td id="row6HWfail">0</td><td id="row6HWhang">0</td><td id="row6HWerror">0</td><td id="row6RMpass">44</td><td id="row6RMfail">0</td><td id="row6RMerror">6</td><td id="row6New">0</td><td id="row6Gated">0</td><td id="row6GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#8AE62E">88.00%</td></tr>
<td>Legacy.Decode.MVC</td><td id="row7Total">226</td><td id="row7HWpass">0</td><td id="row7HWfail">0</td><td id="row7HWhang">0</td><td id="row7HWerror">0</td><td id="row7RMpass">145</td><td id="row7RMfail">0</td><td id="row7RMerror">81</td><td id="row7New">0</td><td id="row7Gated">0</td><td id="row7GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">64.16%</td></tr>
<td>Legacy.Decode.VC1</td><td id="row8Total">0</td><td id="row8HWpass">0</td><td id="row8HWfail">0</td><td id="row8HWhang">0</td><td id="row8HWerror">0</td><td id="row8RMpass">0</td><td id="row8RMfail">0</td><td id="row8RMerror">0</td><td id="row8New">0</td><td id="row8Gated">0</td><td id="row8GatedHW">0</td><td>0</td><td style="background-color:#808080">0.00%</td><td style="background-color:#808080">0.00%</td><td style="background-color:#808080">0.00%</td></tr>
<td>Legacy.Decode.VP8</td><td id="row9Total">135</td><td id="row9HWpass">0</td><td id="row9HWfail">0</td><td id="row9HWhang">0</td><td id="row9HWerror">0</td><td id="row9RMpass">135</td><td id="row9RMfail">0</td><td id="row9RMerror">0</td><td id="row9New">0</td><td id="row9Gated">0</td><td id="row9GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">100.00%</td></tr>
<td>Legacy.Decode.VP9</td><td id="row10Total">28</td><td id="row10HWpass">0</td><td id="row10HWfail">0</td><td id="row10HWhang">0</td><td id="row10HWerror">0</td><td id="row10RMpass">28</td><td id="row10RMfail">0</td><td id="row10RMerror">0</td><td id="row10New">0</td><td id="row10Gated">0</td><td id="row10GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">100.00%</td></tr>
<td>Legacy.Decode.VVC</td><td id="row11Total">47</td><td id="row11HWpass">0</td><td id="row11HWfail">0</td><td id="row11HWhang">0</td><td id="row11HWerror">0</td><td id="row11RMpass">47</td><td id="row11RMfail">0</td><td id="row11RMerror">0</td><td id="row11New">0</td><td id="row11Gated">0</td><td id="row11GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">100.00%</td></tr>
<td>Legacy.PAK.AV1</td><td id="row12Total">117</td><td id="row12HWpass">0</td><td id="row12HWfail">0</td><td id="row12HWhang">0</td><td id="row12HWerror">0</td><td id="row12RMpass">11</td><td id="row12RMfail">0</td><td id="row12RMerror">28</td><td id="row12New">78</td><td id="row12Gated">0</td><td id="row12GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">9.40%</td></tr>
<td>Legacy.PAK.AVC</td><td id="row13Total">929</td><td id="row13HWpass">0</td><td id="row13HWfail">0</td><td id="row13HWhang">0</td><td id="row13HWerror">0</td><td id="row13RMpass">254</td><td id="row13RMfail">0</td><td id="row13RMerror">675</td><td id="row13New">0</td><td id="row13Gated">0</td><td id="row13GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">27.34%</td></tr>
<td>Legacy.PAK.HEVC</td><td id="row14Total">1448</td><td id="row14HWpass">0</td><td id="row14HWfail">0</td><td id="row14HWhang">0</td><td id="row14HWerror">0</td><td id="row14RMpass">396</td><td id="row14RMfail">0</td><td id="row14RMerror">1052</td><td id="row14New">0</td><td id="row14Gated">0</td><td id="row14GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">27.35%</td></tr>
<td>Legacy.PAK.JPEG</td><td id="row15Total">117</td><td id="row15HWpass">0</td><td id="row15HWfail">0</td><td id="row15HWhang">0</td><td id="row15HWerror">0</td><td id="row15RMpass">110</td><td id="row15RMfail">0</td><td id="row15RMerror">7</td><td id="row15New">0</td><td id="row15Gated">0</td><td id="row15GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">94.02%</td></tr>
<td>Legacy.PAK.MPEG</td><td id="row16Total">54</td><td id="row16HWpass">0</td><td id="row16HWfail">0</td><td id="row16HWhang">0</td><td id="row16HWerror">0</td><td id="row16RMpass">54</td><td id="row16RMfail">0</td><td id="row16RMerror">0</td><td id="row16New">0</td><td id="row16Gated">0</td><td id="row16GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">100.00%</td></tr>
<td>Legacy.PAK.VP9</td><td id="row17Total">16</td><td id="row17HWpass">0</td><td id="row17HWfail">0</td><td id="row17HWhang">0</td><td id="row17HWerror">0</td><td id="row17RMpass">16</td><td id="row17RMfail">0</td><td id="row17RMerror">0</td><td id="row17New">0</td><td id="row17Gated">0</td><td id="row17GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">100.00%</td></tr>
<td>Legacy.VDAQM</td><td id="row18Total">362</td><td id="row18HWpass">0</td><td id="row18HWfail">0</td><td id="row18HWhang">0</td><td id="row18HWerror">0</td><td id="row18RMpass">341</td><td id="row18RMfail">0</td><td id="row18RMerror">21</td><td id="row18New">0</td><td id="row18Gated">0</td><td id="row18GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">94.20%</td></tr>
<td>Legacy.VDEnc</td><td id="row19Total">31</td><td id="row19HWpass">24</td><td id="row19HWfail">2</td><td id="row19HWhang">2</td><td id="row19HWerror">2</td><td id="row19RMpass">0</td><td id="row19RMfail">0</td><td id="row19RMerror">1</td><td id="row19New">0</td><td id="row19Gated">0</td><td id="row19GatedHW">0</td><td>0</td><td style="background-color:#FFFF00">77.42%</td><td style="background-color:#FFFF00">80.00%</td><td style="background-color:#008000">96.77%</td></tr>
<td>Legacy.VE.SFC</td><td id="row20Total">514</td><td id="row20HWpass">0</td><td id="row20HWfail">0</td><td id="row20HWhang">0</td><td id="row20HWerror">0</td><td id="row20RMpass">509</td><td id="row20RMfail">0</td><td id="row20RMerror">5</td><td id="row20New">0</td><td id="row20Gated">0</td><td id="row20GatedHW">0</td><td>0</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#FF0000">0.00%</td><td style="background-color:#008000">99.03%</td></tr>
<td>Legacy.VEBOX</td><td id="row21Total">274</td><td id="row21HWpass">38</td><td id="row21HWfail">2</td><td id="row21HWhang">28</td><td id="row21HWerror">64</td><td id="row21RMpass">129</td><td id="row21RMfail">0</td><td id="row21RMerror">13</td><td id="row21New">0</td><td id="row21Gated">0</td><td id="row21GatedHW">0</td><td>0</td><td style="background-color:#FF0000">13.87%</td><td style="background-color:#FF0000">28.79%</td><td style="background-color:#008000">95.26%</td></tr>
<tr><td style="background-color:#B6B6A8">All</td><td id="all_total1" style="background-color:#B6B6A8">10963</td><td id="all_hw_pass1" style="background-color:#B6B6A8">62</td><td id="all_hw_fail1" style="background-color:#B6B6A8">4</td><td id="all_hw_hang1" style="background-color:#B6B6A8">30</td><td id="all_hw_error1" style="background-color:#B6B6A8">66</td><td id="all_rm_pass1" style="background-color:#B6B6A8">7749</td><td id="all_rm_fail1" style="background-color:#B6B6A8">0</td><td id="all_rm_error1" style="background-color:#B6B6A8">2965</td><td id="all_new1" style="background-color:#B6B6A8">87</td><td id="all_gated1" style="background-color:#B6B6A8">0</td><td id="all_gated_hw1" style="background-color:#B6B6A8">0</td><td id="all_tbd1" style="background-color:#B6B6A8">0</td><td style="background-color:#FF0000">0.57%</td><td style="background-color:#FF0000">38.27%</td><td style="background-color:#FF0000">72.16%</td></tr>
</table>

			<p>

			</p>
</table>


				</body>

				</html>
"""