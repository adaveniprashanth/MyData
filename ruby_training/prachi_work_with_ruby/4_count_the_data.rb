require 'csv'

=begin
pass = fail = warn = error = notrun = total = 0;
Emulation_Compare_2x4x8 = [pass,fail,warn,error,notrun,total]
Emulation_Lockup_2x4x8 = [pass,fail,warn,error,notrun,total]
Renderfulsim_2x4x8 = [pass,fail,warn,error,notrun,total]
Rendermill_2x4x8 = [pass,fail,warn,error,notrun,total]
Fulsim_Tests = [pass,fail,warn,error,notrun,total]
Lockup_Method = [pass,fail,warn,error,notrun,total]
total_result = [pass,fail,warn,error,notrun,total]

CSV.foreach("summarized.csv") do |row| 
	#puts row
	total_result[5]+=1
	if row[2] == 'Pass'
		total_result[0]+=1
	elsif row[2] == 'Fail'
		total_result[1]+=1
	elsif row[2] == 'Warn'
		total_result[2]+=1
	elsif row[2] == 'Error'
		total_result[3]+=1
	elsif row[2].nil?
		total_result[4]+=1
	end
	
	if row[0] == '2x4x8 Emulation Compare'
		Emulation_Compare_2x4x8[5] +=1
		if row[2] == 'Pass'
			Emulation_Compare_2x4x8[0] +=1
		elsif row[2] == 'Fail'
			Emulation_Compare_2x4x8[1] += 1
		elsif row[2] == 'Warn'
			Emulation_Compare_2x4x8[2] += 1
		elsif row[2] == 'Error'
			Emulation_Compare_2x4x8[3] += 1
		elsif row[2].nil?
			Emulation_Compare_2x4x8[4] += 1
		end
	elsif row[0] == '2x4x8 Emulation Lockup'
		Emulation_Lockup_2x4x8[5] +=1
		if row[2] == 'Pass'
			Emulation_Lockup_2x4x8[0] +=1
		elsif row[2] == 'Fail'
			Emulation_Lockup_2x4x8[1] += 1
		elsif row[2] == 'Warn'
			Emulation_Lockup_2x4x8[2] += 1
		elsif row[2] == 'Error'
			Emulation_Lockup_2x4x8[3] += 1
		elsif row[2].nil?
			Emulation_Lockup_2x4x8[4] += 1
		end
	elsif row[0] == '2x4x8 Renderfulsim'
		Renderfulsim_2x4x8[5] +=1
		if row[2] == 'Pass'
			Renderfulsim_2x4x8[0] +=1
		elsif row[2] == 'Fail'
			Renderfulsim_2x4x8[1] += 1
		elsif row[2] == 'Warn'
			Renderfulsim_2x4x8[2] += 1
		elsif row[2] == 'Error'
			Renderfulsim_2x4x8[3] += 1
		elsif row[2].nil?
			Renderfulsim_2x4x8[4] += 1
		end
	elsif row[0] == '2x4x8 Rendermill'
		Rendermill_2x4x8[5] +=1
		if row[2] == 'Pass'
			Rendermill_2x4x8[0] +=1
		elsif row[2] == 'Fail'
			Rendermill_2x4x8[1] += 1
		elsif row[2] == 'Warn'
			Rendermill_2x4x8[2] += 1
		elsif row[2] == 'Error'
			Rendermill_2x4x8[3] += 1
		elsif row[2].nil?
			Rendermill_2x4x8[4] += 1
		end
	elsif row[0] == 'Fulsim_Tests'
		Fulsim_Tests[5] +=1
		if row[2] == 'Pass'
			Fulsim_Tests[0] +=1
		elsif row[2] == 'Fail'
			Fulsim_Tests[1] += 1
		elsif row[2] == 'Warn'
			Fulsim_Tests[2] += 1
		elsif row[2] == 'Error'
			Fulsim_Tests[3] += 1
		elsif row[2].nil?
			Fulsim_Tests[4] += 1
		end
	elsif row[0] == 'Lockup_Method'
		Lockup_Method[5] +=1
		if row[2] == 'Pass'
			Lockup_Method[0] +=1
		elsif row[2] == 'Fail'
			Lockup_Method[1] += 1
		elsif row[2] == 'Warn'
			Lockup_Method[2] += 1
		elsif row[2] == 'Error'
			Lockup_Method[3] += 1
		elsif row[2].nil?
			Lockup_Method[4] += 1
		end
	end
	
end

puts "total_result"
puts total_result
puts "Emulation_Compare_2x4x8"
puts Emulation_Compare_2x4x8
puts "Emulation_Lockup_2x4x8"
puts Emulation_Lockup_2x4x8
puts "Renderfulsim_2x4x8"
puts Renderfulsim_2x4x8
puts "Rendermill_2x4x8"
puts Rendermill_2x4x8
puts "Fulsim_Tests"
puts Fulsim_Tests
puts "Lockup_Method"
puts Lockup_Method
=end

h = Hash.new { |hash, key| hash[key] = Hash.new { |k, v| k[v] = Hash.new {|data,value| data[value]= 0 } }}
CSV.foreach("summarized.csv") do |row|
	if row[2].nil?
		row[2] ="NotRun"
	end
	puts row
	
	puts h[row[0]][row[1]].keys
	if h[row[0]][row[1]][row[2]].nil?
		h[row[0]][row[1]][row[2]] = 1
	else
		h[row[0]][row[1]][row[2]] += 1
	end
	
	if not(h[row[0]][row[1]].keys.include?"Pass")
		h[row[0]][row[1]]["Pass"] = 0
	elsif not(h[row[0]][row[1]].keys.include?"Fail")
		h[row[0]][row[1]]["Fail"] = 0
	elsif not(h[row[0]][row[1]].keys.include?"Warn")
		h[row[0]][row[1]]["Warn"] = 0
	elsif not(h[row[0]][row[1]].keys.include?"Error")
		h[row[0]][row[1]]["Error"] = 0
	elsif not(h[row[0]][row[1]].keys.include?"NotRun")
		h[row[0]][row[1]]["NotRun"] = 0
	end
	h[row[0]][row[1]]["Total"] = h[row[0]][row[1]]["Pass"] +h[row[0]][row[1]]["Fail"] +h[row[0]][row[1]]["Warn"]+h[row[0]][row[1]]["Error"]+h[row[0]][row[1]]["NotRun"]
	
end
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

def create_table(hw,rm,hash_data)
	test_area_values = hash_data[hw].keys
	arr= test_area_values.sort.to_a
	puts "\n"
	puts rm+" and "+hw
	hw_result = []
	rm_result = []
	table_start = "<table>"
	puts table_start
	head = "<tr><th>Units</th><th>HW Total</th><th>HW Pass</th><th>HW Fail</th><th>HW Warn</th><th>HW Error</th><th>HW Remain</th><th>RM Total</th><th>RM Pass</th><th>RM Fail</th><th>RM Warn</th><th>RM Error</th><th>RM Remain</th><th>HW Pass %</th><th>RM Pass %</th></tr>"
	puts head
	arr.each do |x| 
		hw_result =[hash_data[hw][x]["Total"],hash_data[hw][x]["Pass"],hash_data[hw][x]["Fail"],hash_data[hw][x]["Warn"],hash_data[hw][x]["Error"],hash_data[hw][x]["NotRun"]]
		rm_result =[hash_data[rm][x]["Total"],hash_data[rm][x]["Pass"],hash_data[rm][x]["Fail"],hash_data[rm][x]["Warn"],hash_data[rm][x]["Error"],hash_data[rm][x]["NotRun"]]
		total_result =[x]+hw_result+rm_result
		hw_string = "<tr><td>#{total_result[0]}</td><td>#{total_result[1]}</td><td>#{total_result[2]}</td><td>#{total_result[3]}</td><td>#{total_result[4]}</td><td>#{total_result[5]}</td><td>#{total_result[6]}</td>"
		rm_string = "<td>#{total_result[7]}</td><td>#{total_result[8]}</td><td>#{total_result[9]}</td><td>#{total_result[10]}</td><td>#{total_result[11]}</td><td>#{total_result[12]}</td>"
		percentage_string = "<td style='background-color:#{create_color_value([total_result[1],total_result[2]])}'>#{((total_result[2]/total_result[1].to_f)*100).to_s[0..4]}%</td><td id=row2perecentage style='background-color:#{create_color_value([total_result[7],total_result[8]])}'>#{((total_result[8]/total_result[7].to_f)*100).to_s[0..4]}%</td></tr>"
		#puts total_result
		puts hw_string + rm_string+percentage_string
	end
	table_close = "</table>"
	puts table_close
end

create_table('2x4x8 Emulation Compare','2x4x8 Renderfulsim',h)
create_table('2x4x8 Emulation Lockup','2x4x8 Rendermill',h)
create_table('Lockup_Method','Fulsim_Tests',h)