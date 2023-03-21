require 'set'


#For reference --> http://ruby-for-beginners.rubymonstas.org/index.html

=begin
#DICTIONARY/HASH
=end
#Hash/Dictionary
if not true
	dictionary = { "one" => "eins", "two" => "zwei", "three" => "drei" }
	puts dictionary.keys
	#converting dictionary keys to array for using for loop
	dictionary.keys.to_a.each do |k|
		puts dictionary[k]
	end
end

#nested dictionary
if not true
	h = Hash.new { |hash, key| hash[key] = Hash.new { |k, v| k[v] = Hash.new {|data,value| data[value]= 0 } }}
	h["monday"]["morning"]["early"] = h["monday"]["morning"]["early"] + 1
	h["monday"]["morning"]["early"] = h["monday"]["morning"]["early"] + 1
	#{"monday"=>{"morning"=>["Ben"]}} 
	puts h["monday"]["morning"]["early"]
elsif not true
	h = Hash.new { |hash, key| hash[key] = Hash.new { |k, v| k[v] = Array.new } }
	h["monday"]["morning"] << "Ben"
	#{"monday"=>{"morning"=>["Ben"]}} 
end

=begin
#ARRAY
=end
$hw_total_result = [0,0,0,0,0,0]
$rm_total_result = [0,0,0,0,0,0]
if true
	def update_array_value
		$hw_total_result = [$hw_total_result[0]+10,$hw_total_result[1]+15,$hw_total_result[2]+45,$hw_total_result[3]+33,$hw_total_result[4]+23,$hw_total_result[5]+78]
		$rm_total_result = [$rm_total_result[0]+56,$rm_total_result[1]+45,$rm_total_result[2]+45,$rm_total_result[3]+12,$rm_total_result[4]+89,$rm_total_result[5]+56]
		puts "updated"
	end
	update_array_value()
	puts $hw_total_result
	puts $rm_total_result
	update_array_value()
	puts $hw_total_result
	puts $rm_total_result
	
end
#array with for loop
if not true
	array = [1, 2, 3, 4, 5, 6]
	array.each { |x| puts x }

elsif not true
	array = [1, 2, 3, 4, 5, 6]
	array.each do |x| 
		puts x
	end
end
#array append
if not true
	array = [1, 2, 3, 4, 5, 6]
	array1 = [1, 2, 3, 4, 5, 6]
	array3 = array+array1
	puts array3
end

#set with append
if not true
	s1 = Set[]
	puts s1
	s1.add('abc')
	s1.add('def')
	s1.add('ghi')
	s1.add('abc')
	s1.add('def')
	s1.add('ghi')
	puts s1
	arr = s1.to_a
	puts arr
end

#sotred set creation
if not true
	sorted_set = SortedSet.new
	
	sorted_set << 'Lockup_Method'
	sorted_set << '2x4x8 Emulation Compare'
	sorted_set << 'Fulsim_Tests'
	sorted_set << '2x4x8 Rendermill'
	sorted_set << '2x4x8 Emulation Lockup'
	sorted_set << '2x4x8 Renderfulsim'
	

	puts sorted_set
	arr = sorted_set.to_a
	puts arr

end
