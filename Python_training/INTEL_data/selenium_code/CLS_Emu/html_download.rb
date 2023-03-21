require 'json'
require 'open-uri'
require 'net/http'
#require 'builder'

$all_total = 0;
$all_hw_pass = 0;
$all_hw_fail = 0;
$all_hw_hang = 0;
$all_hw_error = 0;
$all_hw_pend = 0;
$all_rm_fail = 0;
$all_rm_warn = 0;
$all_rm_pass = 0;
$all_new = 0;
$all_doNotRun = 0;
$row_id = 0
$all_total_array = Array.new;
$all_hw_pass_array = Array.new;
$all_hw_fail_array = Array.new;
$all_hw_hang_array = Array.new;
$all_hw_error_array = Array.new;
$all_hw_pend_array = Array.new;
$all_rm_fail_array = Array.new;
$all_rm_warn_array = Array.new;
$all_rm_pass_array = Array.new;
$all_new_array = Array.new;
$all_doNotRun_array = Array.new;
$modelsHash = Hash.new
$modelsHashID = Hash.new
@skipV2V3 = false # no more skipping features, track all

def AxeDownload(download)
   uri = URI('https://axeweb.intel.com/axe/api/testlist/295/latest/combined')
   puts uri
   req = Net::HTTP::Get.new(uri)
   req.basic_auth 'autoclient', 'gr@ph1c$'
  
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
      open('result.json', 'wb') do |fileAXE|
        fileAXE << res.body
      end
      print "#{Time.now.strftime("%l:%M:%S %p")} - End download\n"
   end
end

download = ARGV[0]
download = true  if download.nil?
download = false if download =~ /false/

AxeDownload(download)