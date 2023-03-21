require 'csv'
require 'json'
require 'csv'




=begin
CSV.open("your_csv.csv", "w") do |csv| #open new file for write
   csv << ['executionID','Execution Stage','Result']	
  JSON.parse(File.open("result.json").read).each do |hash| #open json to parse
    csv << hash.values #write value to file
  end
end
=end

=begin
CSV.foreach(("your_csv.csv"), headers: true, col_sep: ",") do |row|
    puts row 
end 
=end

=begin
col_data = []
CSV.foreach(FILENAME) {|row| col_data << row[COL_INDEX]}
=end

=begin
col_data = []
CSV.foreach("your_csv.csv") {|row| col_data << row[1,2]}

puts col_data
=end

=begin
CSV.open("abcd.csv", "w") do |csv| #open new file for write
	csv << ['executionID','Execution Stage','Result']
	CSV.foreach("your_csv.csv") do |row| 
		puts row[1,2]
		csv << row[1,2]
	end
end
=end