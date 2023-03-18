
require 'json'




file = File.read('exitCodeSummary.json')
$data_hash = JSON.parse(file)
$data_hash.each do |entry|
   if entry["executionStageName"] =~ /Render/
      features = entry["features"]
      testListTestId = entry["testListTestId"]
      $data_hash.each do |entry|
         if entry["testListTestId"] == testListTestId
            entry["features"] = features
            break
         end
      end
   end
end


path = 'exitCodeSummary.mod.json'
File.open(path, 'w') do |file|
  JSON.dump($data_hash, file)
end


