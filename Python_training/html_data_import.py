# creating nd viewing the html files in python

# import webbrowser
# import os
#
# # to open/create a new html file in the write mode
# f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
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
# # writing the code into the file
# f.write(html_template)
#
# # close the file
# f.close()
#
# # 1st method how to open html files in chrome using
# filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
# webbrowser.open_new_tab(filename)
#
#



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
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
url="https://axeweb.intel.com/axe/tests/testlists/306/latestresults/combined/executions?executionStageId=3528,3529"
driver.get("{}".format(url))
# driver.maximize_window()
story_points = str(driver.find_element(By.ID, "DataTables_Table_3_info").text)
print(story_points)
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

#set chromodriver.exe path
driver = webdriver.Chrome(executable_path="chromedriver.exe")


#launch URL
driver.get("https://axeweb.intel.com/axe/tests/testlists/306/latestresults/combined/executions")
time.sleep(3)


'''
#dont delete
l= driver.find_element(By.XPATH,'//div[@class="dataTables_info"]').text
print(l)

l=driver.find_element(By.CLASS_NAME, "multiselect-native-select")
print(l)
print("text",l.text)
wait = WebDriverWait(driver, 30)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\multiselect-native-select:nth-child(1) .\/btn btn-default btn-sm multiselect dropdown-toggle ng-scope"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\multiselect-native-select:nth-child(1)"))).click()

# #browser quit
driver.quit()
'''

# multiselect-native-select
'''l = driver.find_element(By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr/th/span[@class='multiselect-native-select']")
print(l)
l.click()
'''


# l = driver.find_element(By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead")
# print(l.text)



l = driver.find_element(By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr[3]/th[1]/span/select/optgroup[@label='render Fulsim']/option")
# print(l)
drop = Select(l)
drop.select_by_value("object:30")

print("hello")
l = driver.find_element(By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr[3]/th[6]/span/select")
print(l)
drop = Select(l)
drop.select_by_value("Pass")

# wait = WebDriverWait(driver, 30)
# wait.until(EC.presence_of_element_located((By.XPATH,"//table[@class='axe-data-table pageResize table table-striped table-bordered table-hover table-condensed axe-table-word-break-all ng-isolate-scope dataTable no-footer']/thead/tr[3]/th[6]"))).click()
time.sleep(5)


# pass count
m= driver.find_element(By.XPATH,'//div[@class="dataTables_info"]').text
print(m)

driver.quit()

