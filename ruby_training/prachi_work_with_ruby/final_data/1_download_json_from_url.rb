require 'json'
require 'open-uri'
require 'net/http'


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
      open('AXE_data.json', 'wb') do |fileAXE|
        fileAXE << res.body
      end
      print "#{Time.now.strftime("%l:%M:%S %p")} - End download\n"
   end
end

AxeDownload()