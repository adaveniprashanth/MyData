require 'csv'

cols = [1,21,2]
CSV.open("summarized.csv", "w") do |csv| #open new file for write
	#csv << ['Execution Stage','Test Area','Result']#to add column names
	CSV.foreach("AXE_page.csv") do |row| 
		puts row.values_at(*cols)
		csv << row.values_at(*cols)
	end
end





