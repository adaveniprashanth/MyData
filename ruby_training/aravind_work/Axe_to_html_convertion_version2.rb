require 'json'
require 'open-uri'
require 'net/http'
require 'csv'
require 'date'

$hw_total_result = [0,0,0,0,0,0]
$rm_total_result = [0,0,0,0,0,0]
$total_results = [0,0,0,0,0,0]
$overall_table = ""
$axe_data = Hash.new { |hash, key| hash[key] = Hash.new { |k, v| k[v] = Hash.new {|data,value| data[value]= 0 } }}

#STEP1
#Downloading the AXE Page data
if not true
	def AxeDownload
	   uri = URI('https://axeweb.intel.com/axe/api/testlist/295/latest/combined')
	   puts uri
	   req = Net::HTTP::Get.new(uri)
	   req.basic_auth 'autoclient', 'gr@ph1c$'
	   download = true
	  
	   if download
		  print "#{Time.now.strftime("%l:%M:%S %p")} - Start download\n"
		  res = Net::HTTP.start(uri.hostname, uri.port, :use_ssl => true, :verify_mode => OpenSSL::SSL::VERIFY_NONE) {|http|
			http.request(req)
		  }
		  #puts res.body
		  
	   unless res.kind_of? Net::HTTPSuccess
		  puts "Error downloading results from Axe"
		  exit(9)
	   end
		  open('AXE_data2.json', 'wb') do |fileAXE|
			fileAXE << res.body
		  end
		  print "#{Time.now.strftime("%l:%M:%S %p")} - End download\n"
	   end
	end
	print "starting Downloading the AXE Page data\n"
	AxeDownload()
	print "completed Downloading the AXE Page data\n"
end


#STEP2
#json data to csv convertion
if not true
	print "starting json data to csv convertion\n"
	CSV.open("AXE_page2.csv", "w") do |csv| #open new file for write
	   #csv << ['executionID','Execution Stage','Result']	#adding column names in csv file
	  JSON.parse(File.open("AXE_data2.json").read).each do |hash| #open json to parse
		csv << hash.values #write value to file
	  end
	end
	print "completed json data to csv convertion\n"
end


#STEP3
#separating the required fields from csv file(Execution stage,Test Area, Result)
if true
	print "starting separating the required fields from csv file(Execution stage,Test Area, Result)\n"
	cols = [1,21,2]
	CSV.open("summarized2.csv", "w") do |csv| #open new file for write
		#csv << ['Execution Stage','Test Area','Result']#to add column names
		rendermill = 0
		emulation = 0
		CSV.foreach("AXE_page2.csv") do |row| 
			values = row.values_at(*cols)
			if values[0] == '2x4x8 Renderfulsim'
				values[0] = '2x4x8 Rendermill'
				rendermill+=1
			elsif values[0] == '2x4x8 Emulation Compare'
				values[0] = '2x4x8 Emulation Lockup'
				emulation+=1
			end
			if values[1].include?"Fulsim/Media_AVP_DEC/AVP_Dec_444"
				values[1] = "Fulsim/Media_AVP_DEC/AVP_Dec_444"
			elsif values[1].include?"Fulsim/Media_AVP_PAK"
				values[1] = "Fulsim/Media_AVP_PAK"
			elsif values[1].include?"Fulsim/Media_SFC"
				values[1] = "Fulsim/Media_SFC"
			elsif values[1].include?"Fulsim/Media_VVC_DEC"
				values[1] = "Fulsim/Media_VVC_DEC"
			end
			#Fulsim/Media_AVP_DEC/AVP_Dec_444
			#print values
			#print "\n"
			csv << values
		end
	end
	print "completed separating the required fields from csv file(Execution stage,Test Area, Result)\n"
end

#STEP4
#calcuate the data about Execution stage and test area results
if true
	print "starting calcuate the data about Execution stage and test area results\n"
	CSV.foreach("summarized2.csv") do |row|
		if row[2].nil?
			row[2] ="NotRun"
		end
		#puts row
		
		#puts h[row[0]][row[1]].keys
		if $axe_data[row[0]][row[1]][row[2]].nil?
			$axe_data[row[0]][row[1]][row[2]] = 1
		else
			$axe_data[row[0]][row[1]][row[2]] += 1
		end
		
		if not($axe_data[row[0]][row[1]].keys.include?"Pass")
			$axe_data[row[0]][row[1]]["Pass"] = 0
		elsif not($axe_data[row[0]][row[1]].keys.include?"Fail")
			$axe_data[row[0]][row[1]]["Fail"] = 0
		elsif not($axe_data[row[0]][row[1]].keys.include?"Warn")
			$axe_data[row[0]][row[1]]["Warn"] = 0
		elsif not($axe_data[row[0]][row[1]].keys.include?"Error")
			$axe_data[row[0]][row[1]]["Error"] = 0
		elsif not($axe_data[row[0]][row[1]].keys.include?"NotRun")
			$axe_data[row[0]][row[1]]["NotRun"] = 0
		end
		$axe_data[row[0]][row[1]]["Total"] = $axe_data[row[0]][row[1]]["Pass"] +$axe_data[row[0]][row[1]]["Fail"] +$axe_data[row[0]][row[1]]["Warn"]+$axe_data[row[0]][row[1]]["Error"]+$axe_data[row[0]][row[1]]["NotRun"]	
	end
	print "completed calcuate the data about Execution stage and test area results\n"
end

#STEP5 
#creation of html page

# the html code which will go in the html page file
page_start = "<html>\n"
head_start = "<head>\n"
style_code = "<style>
			table, th, td {border: 1px solid black;
						   border-collapse:collapse;
						   font-family: \"Arial\";}
			th, td {padding: 5px;}
			th {text-align: center;
				color: white;
				background-color: #3E5A93;}
			td {background-color: #FFB84D;}
			h2 {font-family: \"Arial\";
				font-size: 20px;}
			h1 {font-family: \"Arial\";
				font-size: 12px;}
			span {font-family: \"Arial\";
				font-size: 10px;}
			</style>\n"


#getting the current date and time
current_time = DateTime.now
local_time = current_time.strftime "%d/%m/%Y %H:%M"
puts "Current Date and Time: "+local_time 

head_close="</head>\n"
body_start = "<body>\n"
date_details = "<h1>Last Updated: #{local_time}</h1>\n"

table_start = "<table>\n"
table_close = "</table>\n"
body_close = "</body>\n"
page_close = "</html>\n"



def calculate_overall_data(hw,rm,hash_data)
	test_area_values = hash_data[hw].keys
	arr= test_area_values.sort.to_a
	hw_result = []
	rm_result = []
	arr.each do |x| 
		hw_result =[hash_data[hw][x]["Total"],hash_data[hw][x]["Pass"],hash_data[hw][x]["Fail"],hash_data[hw][x]["Warn"],hash_data[hw][x]["Error"],hash_data[hw][x]["NotRun"]]
		rm_result =[hash_data[rm][x]["Total"],hash_data[rm][x]["Pass"],hash_data[rm][x]["Fail"],hash_data[rm][x]["Warn"],hash_data[rm][x]["Error"],hash_data[rm][x]["NotRun"]]
		
		$hw_total_result = [$hw_total_result[0]+hw_result[0],$hw_total_result[1]+hw_result[1],$hw_total_result[2]+hw_result[2],$hw_total_result[3]+hw_result[3],$hw_total_result[4]+hw_result[4],$hw_total_result[5]+hw_result[5]]
		$rm_total_result = [$rm_total_result[0]+rm_result[0],$rm_total_result[1]+rm_result[1],$rm_total_result[2]+rm_result[2],$rm_total_result[3]+rm_result[3],$rm_total_result[4]+rm_result[4],$rm_total_result[5]+rm_result[5]]
		$total_results = [$total_results[0]+hw_result[0]+rm_result[0],$total_results[1]+hw_result[1]+rm_result[1],$total_results[2]+hw_result[2]+rm_result[2],$total_results[3]+hw_result[3]+rm_result[3],$total_results[4]+hw_result[4]+rm_result[4],$total_results[5]+hw_result[5]+rm_result[5]]
	end
end
def calculate_data(data_hash)
	#calculate_overall_data('2x4x8 Emulation Compare','2x4x8 Renderfulsim',data_hash)
	calculate_overall_data('2x4x8 Emulation Lockup','2x4x8 Rendermill',data_hash)
	calculate_overall_data('Lockup_Method','Fulsim_Tests',data_hash)
end


def create_color_value(data)
    percent = (data[1]/data[0].to_f) * 100
	# print(percent)
    if percent < 25
        return 'FF0000'#red color
    elsif percent >= 25 and percent < 50
        return 'FFFF00'#yellow
    elsif percent >= 50 and percent < 75
        return '8AE62E'#light green
    elsif percent >= 75 and percent <= 100
        return '008000'# heavy green
	end
end
def create_overall_table
	calculate_data($axe_data)
	#writing the overall table data
	$overall_table = "<p></p><h2>Overall</h2>\n
	<table>
	<tr>
	<th>Overall Status</th><th>Total Test cases</th><th>HW Pass</th><th>HW Fail</th><th>HW Warn</th><th>HW Error</th><th>HW NotRun</th>
	<th>RM Pass</th><th>RM Fail</th><th>RM Warn</th><th>RM Error</th><th>RM NotRun</th><th>HW Pass percentage</th><th>RM Pass percentage</th>
	</tr>
	<tr>
	<td>Overall_Status</td><td>#{$hw_total_result[0]}</td><td>#{$hw_total_result[1]}</td><td>#{$hw_total_result[2]}</td><td>#{$hw_total_result[3]}</td><td>#{$hw_total_result[4]}</td><td>#{$hw_total_result[5]}</td>
	<td>#{$rm_total_result[1]}</td><td>#{$rm_total_result[2]}</td><td>#{$rm_total_result[3]}</td><td>#{$rm_total_result[4]}</td><td>#{$rm_total_result[5]}</td>
	<td style=\"background-color:\##{create_color_value($hw_total_result)}\">#{(($hw_total_result[1]/$hw_total_result[0].to_f)*100).to_s[0..4]}%</td>
	<td style=\"background-color:\##{create_color_value($rm_total_result)}\">#{(($rm_total_result[1]/$rm_total_result[0].to_f)*100).to_s[0..4]}%</td>
	</tr>
	</table><p></p>"
	$fileobject.write($overall_table);
end

def create_table(hw,rm,hash_data)
	test_area_values = hash_data[hw].keys
	arr= test_area_values.sort.to_a
	if rm.include?"Rendermill"
		table_name = "<h2>"+"2x4x8 Emulation"+"</h2>\n"
		$fileobject.write(table_name)
	elsif rm.include?"Fulsim_Tests"
		table_name = "<h2>"+"Fulsim_Tests"+"</h2>\n"
		$fileobject.write(table_name)
	end
	hw_result = []
	rm_result = []
	table_start = "\n<table>\n"
	$fileobject.write(table_start)
	head = "\n<tr><th>Units</th><th>HW Total</th><th>HW Pass</th><th>HW Fail</th><th>HW Warn</th><th>HW Error</th><th>HW NotRun</th><th>RM Pass</th><th>RM Fail</th><th>RM Warn</th><th>RM Error</th><th>RM NotRun</th><th>HW Pass %</th><th>RM Pass %</th></tr>\n"
	$fileobject.write(head)
	hw_total = [0,0,0,0,0,0]#total,pass,fail,warn,error,notrun
	rm_total = [0,0,0,0,0]#pass,fail,warn,error,notrun 
	arr.each do |x| 
		hw_result =[hash_data[hw][x]["Total"],hash_data[hw][x]["Pass"],hash_data[hw][x]["Fail"],hash_data[hw][x]["Warn"],hash_data[hw][x]["Error"],hash_data[hw][x]["NotRun"]]
		rm_result =[hash_data[rm][x]["Pass"],hash_data[rm][x]["Fail"],hash_data[rm][x]["Warn"],hash_data[rm][x]["Error"],hash_data[rm][x]["NotRun"]]
		
		hw_string = "<tr><td>#{x}</td><td>#{hw_result[0]}</td><td>#{hw_result[1]}</td><td>#{hw_result[2]}</td><td>#{hw_result[3]}</td><td>#{hw_result[4]}</td><td>#{hw_result[5]}</td>"
		rm_string = "<td>#{rm_result[0]}</td><td>#{rm_result[1]}</td><td>#{rm_result[2]}</td><td>#{rm_result[3]}</td><td>#{rm_result[4]}</td>"
		hw_percentage_string = "<td style='background-color:#{create_color_value([hw_result[0],hw_result[1]])}'>#{((hw_result[1]/hw_result[0].to_f)*100).to_s[0..4]}%</td>"
		rm_percentage_string = "<td style='background-color:#{create_color_value([hw_result[0],rm_result[0]])}'>#{((rm_result[0]/hw_result[0].to_f)*100).to_s[0..4]}%</td></tr>\n"
		#puts hw_string + rm_string+hw_percentage_string+rm_percentage_string
		hw_total[0]+=hw_result[0];hw_total[1]+=hw_result[1];hw_total[2]+=hw_result[2];hw_total[3]+=hw_result[3];hw_total[4]+=hw_result[4];hw_total[5]+=hw_result[5];
		rm_total[0]+=rm_result[0];rm_total[1]+=rm_result[1];rm_total[2]+=rm_result[2];rm_total[3]+=rm_result[3];rm_total[4]+=rm_result[4]
		$fileobject.write(hw_string + rm_string+hw_percentage_string+rm_percentage_string)
	end
	hw_total_string = "\n<tr><td style='background-color:#B6B6A8'>All</td><td style='background-color:#B6B6A8'>#{hw_total[0]}</td><td style='background-color:#B6B6A8'>#{hw_total[1]}</td><td style='background-color:#B6B6A8'>#{hw_total[2]}</td><td style='background-color:#B6B6A8'>#{hw_total[3]}</td><td style='background-color:#B6B6A8'>#{hw_total[4]}</td><td style='background-color:#B6B6A8'>#{hw_total[5]}</td>"
	rm_total_string = "<td style='background-color:#B6B6A8'>#{rm_total[0]}</td><td style='background-color:#B6B6A8'>#{rm_total[1]}</td><td style='background-color:#B6B6A8'>#{rm_total[2]}</td><td style='background-color:#B6B6A8'>#{rm_total[3]}</td><td style='background-color:#B6B6A8'>#{rm_total[4]}</td>"
	hw_percentage_string = "<td style='background-color:#{create_color_value([hw_total[0],hw_total[1]])}'>#{((hw_total[1]/hw_total[0].to_f)*100).to_s[0..4]}%</td>"
	rm_percentage_string = "<td style='background-color:#{create_color_value([hw_total[0],rm_total[0]])}'>#{((rm_total[0]/hw_total[0].to_f)*100).to_s[0..4]}%</td></tr>"
	puts hw
	puts hw_total[1]/hw_total[0].to_f
	puts rm
	puts rm_total[0]/hw_total[0].to_f
	$fileobject.write(hw_total_string+rm_total_string+hw_percentage_string+rm_percentage_string)
	table_close = "\n</table>\n"
	$fileobject.write(table_close);
end

def create_execution_tables
	#create_table('2x4x8 Emulation Compare','2x4x8 Renderfulsim',$axe_data)
	create_table('2x4x8 Emulation Lockup','2x4x8 Rendermill',$axe_data)
	create_table('Lockup_Method','Fulsim_Tests',$axe_data)
end
print "starting creation of html page\n"
$fileobject = File.new("Axe_to_html2.html", "w");#opening the html page
$fileobject.write(page_start);
$fileobject.write(head_start);
$fileobject.write(style_code);
$fileobject.write(head_close);
$fileobject.write(body_start);
$fileobject.write(date_details);
create_overall_table()
create_execution_tables()
$fileobject.write(body_close);
$fileobject.write(page_close);
# Closing a file
$fileobject.close();
print "completed creation of html page\n"
print "html file created in folder ",Dir.pwd();