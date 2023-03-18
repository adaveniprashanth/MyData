require 'json'
require 'open-uri'
require 'net/http'
#require 'builder'

def AxeDownload(download)
   #uri = URI('https://axeweb.intel.com/axe/api/testlist/290/latest/combined')
   uri = URI('https://axeweb.intel.com/axe/tests/testlists/295/latestresults/combined/summary/executionStageTestArea')
   puts uri
   req = Net::HTTP::Get.new(uri)
   req.basic_auth 'autoclient', 'gr@ph1c$'
  
   if true
      print "#{Time.now.strftime("%l:%M:%S %p")} - Start download\n"
      res = Net::HTTP.start(uri.hostname, uri.port, :use_ssl => true, :verify_mode => OpenSSL::SSL::VERIFY_NONE) {|http|
        http.request(req)
      }
      #puts res.body
      
   unless res.kind_of? Net::HTTPSuccess
      puts "Error downloading results from Axe"
      exit(9)
   end
      open('exitCodeSummary.json', 'wb') do |fileAXE|
        fileAXE << res.body
      end
      print "#{Time.now.strftime("%l:%M:%S %p")} - End download\n"
   end

   fileSize = File.size("exitCodeSummary.json")
   puts "#{fileSize}"
   exit if fileSize < 1000

   print "#{Time.now.strftime("%l:%M:%S %p")} - Start conversion\n"
   #system("ruby copyFeatures.rb")
   file = File.read('exitCodeSummary.json')
   $data_hash = JSON.parse(file)
   print "#{Time.now.strftime("%l:%M:%S %p")} - End conversion\n"
end
download = true
AxeDownload(download)