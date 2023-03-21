require 'date'



def create_color_value(data)
    percent = (data[1]/data[0]) * 100
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

total_result = [13893,1800,40,196,16459,32389]
puts total_result[0]/total_result[5].to_f
Emulation_Compare_2x4x8 = [53,23,0,5,688,769,"2x4x8 Emulation Compare"]
Emulation_Lockup_2x4x8 = [6186,353,0,72,8085,14696,'2x4x8 Emulation Lockup']
Renderfulsim_2x4x8 = [350,415,0,0,4,769,'2x4x8 Renderfulsim']
Rendermill_2x4x8 = [6876,820,40,6,6954,14696,'2x4x8 Rendermill']
Fulsim_Tests = [428,21,0,0,280,729,'Fulsim_Tests']
Lockup_Method = [0,168,0,113,448,729,'Lockup_Method']
puts Fulsim_Tests + Lockup_Method

$combined_result = []
def combined_HW_and_RM_data(a,b)
	test_names_combined = a[6]+" and "+b[6]
	data = a+" and "+b
	fileobject.write("<p></p><h2>#{data}</h2>")
	
end


# File Handling Program
# Creating a file
fileobject = File.new("output.html", "w");

current_time = DateTime.now
local_time = current_time.strftime "%d/%m/%Y %H:%M"
puts "Current Date and Time: "+local_time

# the html code which will go in the file html page
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


head_close="</head>\n"
body_start = "<body>\n"
date_details = "<h1>Last Updated: #{local_time}</h1>\n"

table_start = "<table>\n"
table_close = "</table>\n"
body_close = "</body>\n"
page_close = "</html>\n"


#writing the overall table data
overall_table = "<p></p><h2>Overall</h2>\n
<table>
<tr>
<th>Overall Status</th><th>Total Test cases</th><th>Pass</th><th>Fail</th><th>Warn</th><th>Error</th><th>Remain</th><th>Pass percentage</th>
</tr>
<tr>
<td>Overall_Status</td><td>#{total_result[5]}</td><td>#{total_result[0]}</td><td>#{total_result[1]}</td><td>#{total_result[2]}</td><td>#{total_result[3]}</td><td>#{total_result[4]}</td><td style=\"background-color:\##{create_color_value(total_result)}\">#{((total_result[0]/total_result[5].to_f)*100).to_s[0..4]}%</td>
</tr>
</table><p></p>"


# Writing to the file
fileobject.write(page_start);
fileobject.write(head_start);
fileobject.write(style_code);
fileobject.write(head_close);
fileobject.write(body_start);
fileobject.write(date_details);
fileobject.write(overall_table);



fileobject.write(body_close);
fileobject.write(page_close);

# Closing a file
fileobject.close();
