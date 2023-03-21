require 'csv'    

result = {}
file = File.read('input.csv')
csv = CSV.parse(file, headers: true)
csv.each do |row|
  if result[row[1]]
    result[row[1]].push row[0]
  else
    result[row[1]] = [row[0]]
  end
end

puts result