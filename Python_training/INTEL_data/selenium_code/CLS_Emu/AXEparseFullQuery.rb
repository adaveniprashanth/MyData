require 'json'
require 'open-uri'
require 'net/http'
require 'builder'

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
   uri = URI('https://axeweb.intel.com/axe/api/testlist/290/latest/combined')
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
   $data_hash.each do |entry|
      if entry["executionStageName"] =~ /Render/
         features = entry["features"]
         testListTestId = entry["testListTestId"]
         $data_hash.each do |entry|
            if entry["testListTestId"] == testListTestId && entry["executionStageName"] =~ /Emulation/
               entry["features"] = features
               break
            end
         end
      end
      if entry["fileName"] =~ /sampleMissingAlpha/
         entry["testAreaPath"] = "sampler"
      end
   end
   print "#{Time.now.strftime("%l:%M:%S %p")} - End conversion\n"

   #print "#{Time.now.strftime("%l:%M:%S %p")} - Start read\n"
   #file = File.read('exitCodeSummary.mod.json')
   #$data_hash = JSON.parse(file)
   #print "#{Time.now.strftime("%l:%M:%S %p")} - End read\n"

end
$htmlFile = "CLS_AXE_A0_indicators.html"
$tmpHTMLFile = $htmlFile + ".gen"
$queryFile = "CLS_AXE_A0_indicators.jqueryfile.js"
$tmpQueryFile = $queryFile + ".gen"
$queryFileRM = "CLS_AXE_A0_indicators.jqueryfile.RM.js"
$tmpQueryFileRM = $queryFileRM + ".gen"

$f = open($tmpHTMLFile, 'w')
$jf = open($tmpQueryFile, 'w')


def openFiles()

=begin
$f.puts "<style text/css>
table.inlineTable{
display:inline;
}
</style>"
=end
   $time = Time.now.strftime("%b %e %l:%M %p")
   #my $tmpFile = "$main::htmlfile.gen";

   $f.puts "<!DOCTYPE html>\n
			<html>\n
			<head>\n
         <title>CLS_AXE</title>
         <link rel=\"shortcut icon\" href=\"file://///datagroveFMLC.fm.intel.com/Gfxsv_debug\$/xfer/kheiney/indicator/favicon.ico\" /> 
			<script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js\"></script>\n
			<script src=\"#{$queryFile}\"></script>
			<script src=\"#{$queryFileRM}\"></script>
<script>
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName(\"tabcontent\");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = \"none\";
    }
    tablinks = document.getElementsByClassName(\"tablinks\");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(\" active\", \"\");
    }
    document.getElementById(cityName).style.display = \"block\";
    evt.currentTarget.className += \" active\";
}
</script>
         
			<style>\n
			table, th, td {border: 1px solid black;\n
						   border-collapse:collapse;
						   font-family: \"Arial\";}\n
			th, td {padding: 5px;}\n
			th {text-align: center;\n
				color: white;\n
				background-color: #3E5A93;}\n
			td {background-color: #FFB84D;}\n
			h2 {font-family: \"Arial\";\n
				font-size: 20px;}\n
			h1 {font-family: \"Arial\";\n
				font-size: 12px;}\n
			span {font-family: \"Arial\";\n
				font-size: 10px;}\n
			</style>\n
			</head>\n
			<body>\n
			<h1>Last Updated: #{$time}</h1>\n
			
         <h1>Selected Query HW:</h1>\n
			<span class=\"query\">
            https://axeweb.intel.com/axe/tests/testlists/290/latestresults/combined/executions?id=
         </span>
			<span id=\"testListIDs\"class=\"query\">
         </span>
			<span class=\"query\">&executionStageId=3586,3587,3588,3589,3590,3591
         </span>

			<h1>Selected Query RM:</h1>\n
			<span class=\"query\">
            https://axeweb.intel.com/axe/tests/testlists/290/latestresults/combined/executions?id=
         </span>
			<span id=\"testListIDsRM\"class=\"query\">
         </span>
			<span class=\"query\">&executionStageId=3161,3162,3211,3238,3239,3240,3563,3564,3565
         </span>

			<p></p>

         <p><a href=\"file://///datagroveFMLC.fm.intel.com/Gfxsv_debug\$/xfer/kheiney/indicator/IndicatorLinks.html\">Indicators Page</a></p>
         <p><a href=\"https://axeweb.intel.com/axe/tests/testlists/290/latestresults/combined/executions?executionStageId=3589,3590,3591\">AXE Link 2x6</a>
            <a href=\"https://axeweb.intel.com/axe/tests/testlists/290/latestresults/combined/executions?executionStageId=3586,3587,3588\">AXE Link 10x6</a></p>
	"
         $jf.puts "\$(document).ready(function(){\n";
         $jf.puts "	\$(\".query\").hide();\n";
end


def printCellQuery (cell_id, tlid_array)
	#cell_id = shift;
	#tlid_array_ref = shift;
	#my @tlid_array = @{$tlid_array_ref};
	tlid_string = "";
	
	if (tlid_array[0]) 
      tlid_array.each do |value|
         tlid_string = tlid_string.to_s + "%7C" + value.to_s
      end
		
      $jf.print"	\$(\"#"+cell_id.to_s+"\").dblclick(function(){\n";
      $jf.print "		\$(\"#testListIDs\").text(\"#{tlid_string}\")\n";
      $jf.print "		\$(\".query\").show();\n";
      $jf.print "	});\n";
	else 
      $jf.print "	\$(\"#"+cell_id.to_s+"\").dblclick(function(){\n";
      $jf.print "		\$(\".query\").hide();\n";
      $jf.print "	});\n";
   end
end

def closeFiles 
	#print $fh "</table>\n\n
#				</body>\n
#				</html>";
   $jf.print "});\n";
				
   $f.close;
   $jf.close;

   `copy /Y #{$tmpHTMLFile} #{$htmlFile}`;
   `copy /Y #{$tmpQueryFile} #{$queryFile}`;

   #Open RM file and search and replace testListIDs with testListIDsRM
   tmpQ = open($tmpQueryFileRM, 'w')
   File.open($tmpQueryFile, "r") do |lines|
      while line = lines.gets
         if line =~ /testListIDs/
            tmpQ.print line.gsub("testListIDs","testListIDsRM")
         else
            tmpQ.print line
         end
      end
   end
   tmpQ.close
   `copy /Y #{$tmpQueryFileRM} #{$queryFileRM}`;

end

def getColor(number)
   color = "#FFD683";
   
   if (number < 40) 
      color = "#FF0000";
   elsif (number < 70) 
      color = "#FFFF00";
   elsif (number < 90) 
      color = "#8AE62E";
   elsif (number >= 90) 
      color = "#008000";
   end   
   return color;
end

def getColorWarn(number, default)
   color = default
   #color = "#B6B6A8";
   
   if (number > 100) 
      color = "#FF0000";
   end  
   return color;
end

def endTable() 
   $f.print "</table>\n\
			<p>\n
			</p>\n";
end

def startTable()
   $f.print "<table>\n";
end

def printTitle(input)
	title = input;
   $f.print"<h2>#{title}</h2>\n";
end

def printTableHeaderModels()
   $f.print"<tr><th>SKU</th><th>Model</th><th>Model</th><th>Model</th><th>Stale Tests</th></tr>\n"
end
def printTableHeader(input)
	item_name = input;
   $f.print"<tr><th>#{item_name}</th><th>Total</th><th>HW Pass</th><th>HW Miscompare</th><th>HW Hang</th><th>HW Error</th><th>HW Pend</th><th>Gated</th><th>RM Pass</th><th>RM Warn</th><th>RM Fail</th><th>RM New</th><th>HW Pass Rate</th><th>Exec HW Pass Rate</th><th>RM Pass Rate</th></tr>\n"
end

def printTabHeader()
   $f.print "<div class=\"tab\">
   <button class=\"tablinks\" onclick=\"openCity(event, 'Overall')\">Overall</button>
   <button class=\"tablinks\" onclick=\"openCity(event, '2x6')\">2x6</button>
   <button class=\"tablinks\" onclick=\"openCity(event, '7x4x8')\">7x4x8</button>
   <button class=\"tablinks\" onclick=\"openCity(event, 'Val 0')\">Val 0</button>
   <button class=\"tablinks\" onclick=\"openCity(event, 'Val .25')\">Val .25</button>
   <button class=\"tablinks\" onclick=\"openCity(event, 'Val .5')\">Val .5</button>
   <button class=\"tablinks\" onclick=\"openCity(event, 'Val .85')\">Val .85</button>
   <button class=\"tablinks\" onclick=\"openCity(event, 'Val 1.0')\">Val 1.0</button>
   <button class=\"tablinks\" onclick=\"openCity(event, 'DCN')\">DCN</button>
   <button class=\"tablinks\" onclick=\"openCity(event, 'Misc')\">Misc</button>
   </div>\n";
end

def startDivision (name)
   puts "Starting #{name} Division"
   $f.print "<div id=\"#{name}\" class=\"tabcontent\">\n";
end

def endDivision()
   $f.print "</div>\n";
end

def printAll()
   all_hw_pass_rate = 0;
	all_exec_hw_pass_rate = 0;
	all_rm_pass_rate = 0;

   all_hw_pass_rate = (($all_hw_pass.to_f/$all_total.to_f)*100).round(2)
   all_rm_pass_rate = ((($all_rm_pass.to_f+$all_rm_warn)/$all_total.to_f)*100).round(2)
   all_exec_hw_pass_rate = (($all_hw_pass.to_f/($all_hw_pass.to_f+$all_hw_fail.to_f+$all_hw_error.to_f+$all_hw_hang.to_f))*100).round(2)

   all_hw_pass_rate_color = getColor(all_hw_pass_rate);
	all_exec_hw_pass_rate_color = getColor(all_exec_hw_pass_rate);
	all_rm_pass_rate_color = getColor(all_rm_pass_rate);
	all_rm_warn_rate_color = getColorWarn($all_rm_warn,"#B6B6A8");

   # Create row lables for double click info
	$row_id += 1
   row_total_id = "row"+$row_id.to_s+ "Total"
	row_hw_pass_id = "row"+$row_id.to_s+"HWpass"
   row_hw_fail_id = "row"+$row_id.to_s+"HWfail"
	row_hw_hang_id = "row"+$row_id.to_s+"HWhang"
	row_hw_error_id = "row"+$row_id.to_s+"HWerror"
	row_hw_pend_id = "row"+$row_id.to_s+"HWpend"
	row_rm_pass_id = "row"+$row_id.to_s+"RMpass"
	row_rm_warn_id = "row"+$row_id.to_s+"RMwarn"
	row_rm_fail_id = "row"+$row_id.to_s+"RMfail"
   row_new_id = "row"+$row_id.to_s+"New"
   row_doNotRun_id = "row"+$row_id.to_s+"Gated"
   $f.print "<tr>";
	$f.print "<td style=\"background-color:#B6B6A8\">All</td>";
	$f.print "<td id=\"#{row_total_id}\" style=\"background-color:#B6B6A8\">#{$all_total}</td>";
	$f.print "<td id=\"#{row_hw_pass_id}\" style=\"background-color:#B6B6A8\">#{$all_hw_pass}</td>";
	$f.print "<td id=\"#{row_hw_fail_id}\" style=\"background-color:#B6B6A8\">#{$all_hw_fail}</td>";
	$f.print "<td id=\"#{row_hw_hang_id}\" style=\"background-color:#B6B6A8\">#{$all_hw_hang}</td>";
	$f.print "<td id=\"#{row_hw_error_id}\" style=\"background-color:#B6B6A8\">#{$all_hw_error}</td>";
	$f.print "<td id=\"#{row_hw_pend_id}\" style=\"background-color:#B6B6A8\">#{$all_hw_pend}</td>";
	$f.print "<td id=\"#{row_doNotRun_id}\" style=\"background-color:#B6B6A8\">#{$all_doNotRun}</td>";
	$f.print "<td id=\"#{row_rm_pass_id}\" style=\"background-color:#B6B6A8\">#{$all_rm_pass}</td>";
	$f.print "<td id=\"#{row_rm_warn_id}\" style=\"background-color:#{all_rm_warn_rate_color}\">#{$all_rm_warn}</td>";
	$f.print "<td id=\"#{row_rm_fail_id}\" style=\"background-color:#B6B6A8\">#{$all_rm_fail}</td>";
	$f.print "<td id=\"#{row_new_id}\" style=\"background-color:#B6B6A8\">#{$all_rm_new}</td>";

	$f.print "<td style=\"background-color:#{all_hw_pass_rate_color}\">#{all_hw_pass_rate}\%</td>";
	$f.print "<td style=\"background-color:#{all_exec_hw_pass_rate_color}\">#{all_exec_hw_pass_rate}\%</td>";
	$f.print "<td style=\"background-color:#{all_rm_pass_rate_color}\">#{all_rm_pass_rate}\%</td>";
	$f.print "</tr>\n";
   printCellQuery(row_total_id,$all_total_array);
	printCellQuery(row_hw_pass_id,$all_hw_pass_array);
	printCellQuery(row_hw_fail_id,$all_hw_fail_array);
	printCellQuery(row_hw_hang_id,$all_hw_hang_array);
	printCellQuery(row_hw_error_id,$all_hw_error_array);
	printCellQuery(row_hw_pend_id,$all_hw_pend_array);
	printCellQuery(row_doNotRun_id,$all_doNotRun_array);
	printCellQuery(row_rm_pass_id,$all_rm_pass_array);
	printCellQuery(row_rm_warn_id,$all_rm_warn_array);
	printCellQuery(row_rm_fail_id,$all_rm_fail_array);
	printCellQuery(row_new_id,$all_new_array);

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
end

def printModels(input, name)
   filterHash = input
   row_name = name
   rmFail = Array.new
   hwNotPass = Array.new
   staleRender = Array.new
   #file = File.read('exitCodeSummary.json')
   #$data_hash = JSON.parse(file)
   $data_hash.each do |entry|
      found = 0
      filterHash.each do |key, value|
         #print"key:#{key} value:#{value}  "
         unless(entry.has_key?(value))
            print("\nCould not find Key:#{value} in data hash\n")
            exit
         end
         if key =~ /^!(.*)/   # if search is for negative case, strip out ! marker and do !~ search
            if entry[value] !~ /#{$1}/i
               #Found Match
               found += 1
            else
               #No match
            end
         else                 # normal positive search
            if entry[value] =~ /#{key}/i
               #Found Match
               found += 1
            else
               #No match
            end            
         end
      end
      if found == filterHash.length
         if entry["latestTestListTestStatus"] =~ /Waived/
            #print "Waived test #{entry["fileName"]}\n"
            next
         end
         #print " - #{found}\n"
         #next if(entry["executionStageName"] =~ /Emulation Compare 2 /)
         #next unless(entry["executionStageName"] =~ /Branch/)
         next if entry["executionStatus"] =~ /Pass/
         next if entry["executionStatus"].nil?
         next if entry["testAreaPath"] =~ /AUBCAPS/
         #puts entry["executionStatus"]
         if entry["executionStageName"] =~ /Render/
            if entry["executionStatus"] !~ /Pass/
               if entry["executionStatus"] !~ /Warn/
                  rmFail << entry["testListTestId"]
               end
            end
         end
         if entry["executionStageName"] =~ /Emulation/
            if $modelsHash[entry["platformVersionLabel"]].nil?
               $modelsHash[entry["platformVersionLabel"]] = 1
               $modelsHashID[entry["platformVersionLabel"]] = [entry["testListTestId"]]
            else
               $modelsHash[entry["platformVersionLabel"]] += 1
               $modelsHashID[entry["platformVersionLabel"]] << entry["testListTestId"]
            end            
            if (entry["executionStatus"] !~ /Pass/)
               hwNotPass << entry["testListTestId"]
            end
         end
      end
   end
   staleRender = hwNotPass & rmFail
   #puts filterHash
   #puts staleRender
   #puts $modelsHash
   #puts $modelsHashID
   # Top 3 models used
   modelArray = $modelsHash.sort_by(&:last).reverse.slice(0,3)   
   modelArrayID = $modelsHashID.sort_by(&:last).reverse.slice(0,3) 
   #puts modelArray[0]
   #puts $modelsHashID[modelArray[0][0]]
   # Create row lables for double click info
	$row_id += 1
   row_total1_id = "row"+$row_id.to_s+ "Total1" 
   row_total2_id = "row"+$row_id.to_s+ "Total2" 
   row_total3_id = "row"+$row_id.to_s+ "Total3" 
   row_total4_id = "row"+$row_id.to_s+ "Total4" 
## $f.puts "<td id=\"#{row_total_id}\">#{total}</td>";
   # Print Row
   $f.puts "<td>#{row_name}</td>";
   unless modelArray[0].nil?
      $f.puts "<td id=\"#{row_total1_id}\">#{modelArray[0]}</td>" 
   else
      $f.puts "<td id=\"#{row_total1_id}\">-</td>" 
   end
   unless modelArray[1].nil?
      $f.puts "<td id=\"#{row_total2_id}\">#{modelArray[1]}</td>" 
   else
      $f.puts "<td id=\"#{row_total2_id}\">-</td>" 
   end
   unless modelArray[2].nil?
      $f.puts "<td id=\"#{row_total3_id}\">#{modelArray[2]}</td>" 
   else
      $f.puts "<td id=\"#{row_total3_id}\">-</td>" 
   end
   $f.puts "<td id=\"#{row_total4_id}\">#{staleRender.length}</td>" unless staleRender.nil?
   $f.puts "</tr>\n";
   printCellQuery(row_total1_id,$modelsHashID[modelArray[0][0]]) unless modelArray[0].nil?
   printCellQuery(row_total2_id,$modelsHashID[modelArray[1][0]]) unless modelArray[1].nil?
   printCellQuery(row_total3_id,$modelsHashID[modelArray[2][0]]) unless modelArray[2].nil?
   printCellQuery(row_total4_id,staleRender) unless staleRender.nil?
   $modelsHash = Hash.new
   $modelsHashID = Hash.new
end

def printFeatureRow(input, name)
   filterHash = input
   #filterHash = {"2x6|2x4|2x4x16" => "executionStageName", "0.0" => "milestone"}
   row_name = name


   #puts $data_hash
   #puts $data_hash.length
   #puts $data_hash[0]["features"]

   hw_hang = 0
   hw_fail = 0
   hw_pass = 0
   hw_error = 0
   total = 0
   total_RP = 0
   rm_pass = 0
   rm_fail = 0
   rm_warn = 0
   rm_new = 0
   doNotRun = 0
   hw_pass_rate = 0
   exec_hw_pass_rate = 0
   rm_pass_rate = 0
   hw_pending = Array.new
   hw_pending_cnt = 0

   total_array = Array.new
	hw_pass_array = Array.new
	hw_fail_array = Array.new
	hw_error_array = Array.new;
	hw_hang_array = Array.new
	rm_pass_array = Array.new
	rm_warn_array = Array.new
	rm_fail_array = Array.new;
	new_array = Array.new
   doNotRun_array = Array.new

   rm_pass_array = Array.new
   hw_notrun_array = Array.new
         
   skipFeatures = ["22011229030","22010943846 ","14014577164","14013478381","14014411987","22010751633","22010751635","14013109946","22011787452","16012330530","16013692951","22012991463","16012396654","1409780112","14014577164","14014181222","22012521285","14014069143","14014313782","22011223560","22012919778","14013043186","22012782909","22012939252","14015171903","14015181142","16014614053"]

   $data_hash.each do |entry|
      found = 0
      filterHash.each do |key, value|
         #print"key:#{key} value:#{value}  "
         unless(entry.has_key?(value))
            print("\nCould not find Key:#{value} in data hash\n")
            exit
         end
         if key =~ /^!(.*)/   # if search is for negative case, strip out ! marker and do !~ search
            if entry[value] !~ /#{$1}/i
               #Found Match
               found += 1
            else
               #No match
            end
         else                 # normal positive search
            if entry[value] =~ /#{key}/i
               #Found Match
               found += 1
            else
               #No match
            end            
         end
      end
      if found == filterHash.length
         #Skip V2/V3/WMTP
         if @skipV2V3
            skip = false
            skipFeatures.each do |item|
               if entry["features"] =~ /#{item}/
                  skip = true
                  break
               end
            end
            next if skip
         end


         # Skip AUBCAPTURES FOR now
         #next if entry["testAreaPath"] =~ /AUBCAPS/
         #next unless(entry["executionStageName"] =~ /Branch/)
         if entry["latestTestListTestStatus"] =~ /Waived/
            #print "Waived test #{entry["fileName"]}\n"
            next
         end
         #print " - #{found}\n"
         if entry["executionStageName"] =~ /Emulation/
            total_array << entry["testListTestId"]
            if entry["latestTestListTestStatus"] =~ /DoNotRun/
               doNotRun += 1
               doNotRun_array << entry["testListTestId"]
            elsif entry["executionStatus"] =~ /Pass/
               hw_pass += 1
               hw_pass_array << entry["testListTestId"]
            elsif entry["executionStatus"] =~ /Fail/
               if entry["exitCodeMessage"]  =~ /AUBLOAD_CRC_MISCOMPARE/
                  hw_fail += 1
                  hw_fail_array << entry["testListTestId"]
               elsif entry["exitCodeMessage"]  =~ /AUBLOAD_POLL_TIMEOUT/
                  hw_hang += 1
                  hw_hang_array << entry["testListTestId"]
               elsif entry["exitCodeMessage"]  =~ /AUBLOAD_GENERAL_ERROR/ && entry["failureSignatureMessage"]  =~ /TEST ERROR: Explicit failure triggered by test/
                  hw_fail += 1
                  hw_fail_array << entry["testListTestId"]
               #elsif entry["exitCodeMessage"]  =~ /AUBLOAD_GENERAL_ERROR/
               else
                  hw_error += 1
                  hw_error_array << entry["testListTestId"]
               #else
               #   print("Should not be here HW, Fail exit code message #{entry["exitCodeMessage"]}\n")
               end
            elsif entry["executionStatus"] =~ /Error/
               hw_error += 1
               hw_error_array << entry["testListTestId"]
            elsif entry["executionStatus"].nil?
               hw_notrun_array << entry["testListTestId"]
            else
               print("Should not be here Emulation, executionStatus #{entry["executionStatus"]}\n")
            end
         elsif entry["executionStageName"] =~ /Render/
=begin
            if entry["classification"].nil?
               entry["classification"] = row_name 
            else
               entry["classification"] += row_name
               print"--------------------Multiple classification #{entry["classification"]}\n"
            end
=end
            if entry["executionStatus"] =~ /Pass/
               rm_pass += 1
               rm_pass_array << entry["testListTestId"]
            elsif entry["executionStatus"] =~ /Fail/
               rm_fail += 1
               rm_fail_array << entry["testListTestId"]
            elsif entry["executionStatus"] =~ /Error/
               rm_fail += 1
               rm_fail_array << entry["testListTestId"]
            elsif entry["executionStatus"] =~ /Warn/
               rm_warn += 1
               rm_warn_array << entry["testListTestId"]
            elsif entry["executionStatus"].nil?
               rm_new += 1
               new_array << entry["testListTestId"]
            else
               print("Should not be here #{entry["executionStatus"]}\n")
            end
         end
      end
   end

   hw_pending = hw_notrun_array & (rm_pass_array + rm_warn_array)
   hw_pending_cnt = hw_pending.length
   total = rm_fail + rm_pass + rm_new + rm_warn
   print("Total:#{total} HW Pass:#{hw_pass} HW Hangs:#{hw_hang} HW Miscompare:#{hw_fail} HW Pend:#{hw_pending_cnt} RM Pass:#{rm_pass} RM Fail:#{rm_fail} RM New:#{rm_new}\n")
   rm_pass_rate = (((rm_pass.to_f+rm_warn.to_f)/total.to_f)*100).round(2)
   hw_pass_rate = ((hw_pass.to_f/total.to_f)*100).round(2)
   exec_hw_pass_rate = ((hw_pass.to_f/(hw_pass.to_f+hw_fail.to_f+hw_error.to_f+hw_hang.to_f))*100).round(2)
   
   hw_pass_rate_color = getColor(hw_pass_rate);
   exec_hw_pass_rate_color = getColor(exec_hw_pass_rate);
   rm_pass_rate_color = getColor(rm_pass_rate);
   rm_warn_color = getColorWarn(rm_warn,"#FFB84D")

   # Create row lables for double click info
	$row_id += 1
   row_total_id = "row"+$row_id.to_s+ "Total"
	row_hw_pass_id = "row"+$row_id.to_s+"HWpass"
   row_hw_fail_id = "row"+$row_id.to_s+"HWfail"
	row_hw_hang_id = "row"+$row_id.to_s+"HWhang"
	row_hw_error_id = "row"+$row_id.to_s+"HWerror"
	row_hw_pend_id = "row"+$row_id.to_s+"HWpend"
	row_rm_pass_id = "row"+$row_id.to_s+"RMpass"
	row_rm_warn_id = "row"+$row_id.to_s+"RMwarn"
	row_rm_fail_id = "row"+$row_id.to_s+"RMfail"
   row_new_id = "row"+$row_id.to_s+"New"
   row_doNotRun_id = "row"+$row_id.to_s+"Gated"


     # Print Feature Row
   $f.puts "<td>#{row_name}</td>";
   $f.puts "<td id=\"#{row_total_id}\">#{total}</td>";
   $f.puts "<td id=\"#{row_hw_pass_id}\">#{hw_pass}</td>";
   $f.puts "<td id=\"#{row_hw_fail_id}\">#{hw_fail}</td>";
   $f.puts "<td id=\"#{row_hw_hang_id}\">#{hw_hang}</td>";
   $f.puts "<td id=\"#{row_hw_error_id}\">#{hw_error}</td>";
   $f.puts "<td id=\"#{row_hw_pend_id}\">#{hw_pending_cnt}</td>";
   $f.puts "<td id=\"#{row_doNotRun_id}\">#{doNotRun}</td>";
   $f.puts "<td id=\"#{row_rm_pass_id}\">#{rm_pass}</td>";
   $f.puts "<td id=\"#{row_rm_warn_id}\" style=\"background-color:#{rm_warn_color}\">#{rm_warn}</td>";
   $f.puts "<td id=\"#{row_rm_fail_id}\">#{rm_fail}</td>";
   $f.puts "<td id=\"#{row_new_id}\">#{rm_new}</td>";
   $f.puts "<td style=\"background-color:#{hw_pass_rate_color}\">#{hw_pass_rate}\%</td>";
   $f.puts "<td style=\"background-color:#{exec_hw_pass_rate_color}\">#{exec_hw_pass_rate}\%</td>";
   $f.puts "<td style=\"background-color:#{rm_pass_rate_color}\">#{rm_pass_rate}\%</td>";
   $f.puts "</tr>\n";

   printCellQuery(row_total_id,total_array);
	printCellQuery(row_hw_pass_id,hw_pass_array);
	printCellQuery(row_hw_fail_id,hw_fail_array);
	printCellQuery(row_hw_hang_id,hw_hang_array);
	printCellQuery(row_hw_error_id,hw_error_array);
	printCellQuery(row_hw_pend_id,hw_pending);
	printCellQuery(row_doNotRun_id,doNotRun_array);
	printCellQuery(row_rm_pass_id,rm_pass_array);
	printCellQuery(row_rm_warn_id,rm_warn_array);
	printCellQuery(row_rm_fail_id,rm_fail_array);
	printCellQuery(row_new_id,new_array);

   $all_total += total;
   $all_hw_pass += hw_pass;
   $all_hw_fail += hw_fail;
   $all_hw_hang += hw_hang;
   $all_hw_error += hw_error;
   $all_hw_pend += hw_pending_cnt;
   $all_rm_fail += rm_fail;
   $all_rm_warn += rm_warn;
   $all_rm_pass += rm_pass;
   $all_new += rm_new;
   $all_doNotRun += doNotRun;
   $all_total_array += total_array;
   $all_hw_pass_array += hw_pass_array;
   $all_hw_fail_array += hw_fail_array;
   $all_hw_hang_array += hw_hang_array;
   $all_hw_error_array += hw_error_array;
   $all_hw_pend_array += hw_pending;
   $all_rm_fail_array += rm_fail_array;
   $all_rm_warn_array += rm_warn_array;
   $all_rm_pass_array += rm_pass_array;
   $all_new_array += new_array;
   $all_doNotRun_array += doNotRun_array;
end


openFiles

download = ARGV[0]
download = true  if download.nil?
download = false if download =~ /false/

AxeDownload(download)
printTabHeader()

startDivision("Overall")
printTitle("CLS 3D all SKU")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "2x6")
filterHash = {"4x6" => "executionStageName", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "4x6")
filterHash = {"10x6" => "executionStageName", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "10x6")
printAll()
endTable()

print("Creating Models Table\n")
printTitle("Models Table - non passing tests")
startTable()
printTableHeaderModels()
filterHash = {"2x6" => "executionStageName", "!AUBCAPS" => "testAreaPath"}
printModels(filterHash, "2x6")
filterHash = {"4x6" => "executionStageName", "!AUBCAPS" => "testAreaPath"}
printModels(filterHash, "4x6")
filterHash = {"10x6" => "executionStageName", "!AUBCAPS" => "testAreaPath"}
printModels(filterHash, "10x6")
endTable()



endDivision()


startDivision("2x6")


@skipV2V3 = false
printTitle("CLS 3D 2x6 Features")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS|Concurrency|Global|Sampler" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312|22011229030" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"2x6" => "executionStageName", "Sampler" => "testAreaPath",  "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Sampler")
filterHash = {"2x6" => "executionStageName", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"2x6" => "executionStageName", "Concurrency" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Concurrency")
filterHash = {"2x6" => "executionStageName", "Global" => "testAreaPath", "!Virtualization" => "tags", "!1209977693|1409033976|1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Global")
filterHash = {"2x6" => "executionStageName", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"2x6" => "executionStageName", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"2x6" => "executionStageName", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"2x6" => "executionStageName", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"2x6" => "executionStageName", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "!PowerManagement" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"2x6" => "executionStageName", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"2x6" => "executionStageName", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"2x6" => "executionStageName", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"2x6" => "executionStageName", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"2x6" => "executionStageName", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"2x6" => "executionStageName", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"2x6" => "executionStageName", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM Focused")
filterHash = {"2x6" => "executionStageName", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()

#@skipV2V3 = true


endDivision()




startDivision("4x6")


@skipV2V3 = false
printTitle("CLS 3D 4x6 Features")
startTable()
printTableHeader("SKU")
filterHash = {"4x6" => "executionStageName", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS|Concurrency|Global|Sampler" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312|22011229030" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"4x6" => "executionStageName", "Sampler" => "testAreaPath",  "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Sampler")
filterHash = {"4x6" => "executionStageName", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"4x6" => "executionStageName", "Concurrency" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Concurrency")
filterHash = {"4x6" => "executionStageName", "Global" => "testAreaPath", "!Virtualization" => "tags", "!1209977693|1409033976|1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Global")
filterHash = {"4x6" => "executionStageName", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"4x6" => "executionStageName", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"4x6" => "executionStageName", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"4x6" => "executionStageName", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"4x6" => "executionStageName", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "!PowerManagement" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"4x6" => "executionStageName", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"4x6" => "executionStageName", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"4x6" => "executionStageName", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"4x6" => "executionStageName", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"4x6" => "executionStageName", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"4x6" => "executionStageName", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"4x6" => "executionStageName", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM Focused")
filterHash = {"4x6" => "executionStageName", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()

#@skipV2V3 = true


endDivision()








startDivision("10x6")
printTitle("CLS 3D 10x6 Features")
startTable()
printTableHeader("SKU")
filterHash = {"10x6" => "executionStageName", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"10x6" => "executionStageName", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"10x6" => "executionStageName", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"10x6" => "executionStageName", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"10x6" => "executionStageName", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"10x6" => "executionStageName", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"10x6" => "executionStageName", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"10x6" => "executionStageName", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"10x6" => "executionStageName", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"10x6" => "executionStageName", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"10x6" => "executionStageName", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"10x6" => "executionStageName", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"10x6" => "executionStageName", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"10x6" => "executionStageName", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM")
filterHash = {"10x6" => "executionStageName", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()



endDivision()


startDivision("Val 0")
printTitle("CLS 3D all SKU Val 0")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "2x6")
filterHash = {"10x6" => "executionStageName", "0.0" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "10x6")
printAll()
endTable()

printTitle("CLS 3D 2x6 Val 0 Features")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM")
filterHash = {"2x6" => "executionStageName", "0.0" => "milestone", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()

endDivision()



startDivision("Val .25")
printTitle("CLS 3D all SKU Val .15-.25")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "0.15|0.25" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "2x6")
filterHash = {"10x6" => "executionStageName", "0.15|0.25" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "10x6")
printAll()
endTable()

printTitle("CLS 3D 2x6 Val .25 Features")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM")
filterHash = {"2x6" => "executionStageName", "0.25" => "milestone", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()

endDivision()

startDivision("Val .5")
printTitle("CLS 3D all SKU Val .5")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "2x6")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "10x6")
printAll()
endTable()

printTitle("CLS 3D 2x6 Val .5 Features")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM")
filterHash = {"2x6" => "executionStageName", "0.5" => "milestone", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()



printTitle("CLS 3D 10x6 Val .5 Features")
startTable()
printTableHeader("SKU")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM")
filterHash = {"10x6" => "executionStageName", "0.5" => "milestone", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()

endDivision()

startDivision("Val .85")
printTitle("CLS 3D all SKU Val .85")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "2x6")
filterHash = {"10x6" => "executionStageName", "0.85" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "10x6")
printAll()
endTable()

printTitle("CLS 3D 2x6 Val .85 Features")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM")
filterHash = {"2x6" => "executionStageName", "0.85" => "milestone", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()


endDivision()




startDivision("Val 1.0")
printTitle("CLS 3D all SKU Val 1.0")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "2x6")
filterHash = {"10x6" => "executionStageName", "1.0" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "10x6")
printAll()
endTable()

printTitle("CLS 3D 2x6 Val 1.0 Features")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "!GPGPU|Blitter|Virtualization|ObservationArchitecture|MicroController|Power|AUBCAPS" => "testAreaPath", "!1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|220159686|1406907150|1209977693|1409033976|14010627246|1407986807|14010049556|1209977859|1209978161|1209977746|1408727231|14011185056|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "3D")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "GPGPU" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|1209978161|220159686" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compute")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "1209977746" => "features", "!1209977859" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Tessellation")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "220159686" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Ray Tracing")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Mesh")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "Blitter" => "testAreaPath", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Blitter")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "1209977693|1409033976" => "features", "Virtualization" => "testAreaPath", "Virtualization" => "tags", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "SRIOV")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Compression")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "1209977859" => "features", "!14010627246|1407986807|14010049556" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "TBIMR")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "\!1209977693|1409033976" => "features", "MicroController" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "GuC")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "1209978161" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976|14010627246|1407986807|14010049556|220159686|2207540312" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "Multi CTX")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "ObservationArchitecture" => "testAreaPath", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "OA")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "1809192879|1809135480|1809194531|14010517341|2209866075|1809091730|14010795215|1408727231|14011185056" => "features", "!Virtualization" => "testAreaPath", "!1209977693|1409033976" => "features", "!PM" => "executionStageName"}
printFeatureRow(filterHash, "UMA/SVM")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "Power" => "testAreaPath"}
printFeatureRow(filterHash, "PM")
filterHash = {"2x6" => "executionStageName", "1.0" => "milestone", "PM" => "executionStageName"}
printFeatureRow(filterHash, "PM Flex")
printAll()
endTable()


endDivision()






startDivision("Misc")
printTitle("CLS 3D all SKU Val Unassigned")
startTable()
printTableHeader("SKU")
filterHash = {"2x6" => "executionStageName", "!0.0|0.15|0.25|0.5|0.85|1.0" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "2x6")
filterHash = {"10x6" => "executionStageName", "!0.0|0.15|0.25|0.5|0.85|1.0" => "milestone", "!AUBCAPS" => "testAreaPath"}
printFeatureRow(filterHash, "10x6")
printAll()
endTable()

endDivision()



startDivision("DCN")
=begin


printTitle("Xe2 Compute DCN Table")
startTable()
printTableHeader("DCN")
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011229030"  => "features"};
#printFeatureRow(filterHash,"22011229030 : [WMTP][PARENT] Compute Walker Mid-Thread Preemption");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012140225"  => "features"};
printFeatureRow(filterHash,"14012140225 : Barrier Support Lite(staged)");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011602589"  => "features"};
printFeatureRow(filterHash,"22011602589 : New descriptor bit to distinguish between Typed(TGM) SIMT16 and SIMT32 messages");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011751538"  => "features"};
printFeatureRow(filterHash,"22011751538 : Add Append Counter operations to Typed Buffers in LSC");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011223560"  => "features"};
#printFeatureRow(filterHash,"22011223560 : Dynamic LSC/Sampler Routing");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010516253"  => "features"};
printFeatureRow(filterHash,"14010516253 : Replace legacy Media block messages with Typed 2D block message");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1409930426"  => "features"};
printFeatureRow(filterHash,"1409930426 : Larger SLM Allocation (>128KB) in LSC");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "18012155753"  => "features"};
#printFeatureRow(filterHash,"18012155753 : Extend timestamp to 64 bits");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010526392"  => "features"};
#printFeatureRow(filterHash,"22010526392 : Enable State Prefetch for Compute Threads");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012177321"  => "features"};
#printFeatureRow(filterHash,"22012177321 : Delta feature for Large SLM allocation");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010405166"  => "features"};
printFeatureRow(filterHash,"14010405166 : [PARENT] Subslice Bussing Reorganization and LSC support of Typed Messages");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011241409"  => "features"};
printFeatureRow(filterHash,"14011241409 : [Gen12.9]Scalable 2D Untyped block needed in converged LSC");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012468106"  => "features"};
printFeatureRow(filterHash,"14012468106 : [DCN] Allow non-zero value for Immediate Global Base offset in Dataport messages");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010579047"  => "features"};
printFeatureRow(filterHash,"22010579047 : Support simd32/16 encoding for URB messages and converge with LSC ld/st");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010706571"  => "features"};
printFeatureRow(filterHash,"22010706571 : Add new atomic opcodes for Typed surfaces to support DX SM6.6");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010951686"  => "features"};
printFeatureRow(filterHash,"22010951686 : New Micro-architecture for LSC");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011353442"  => "features"};
printFeatureRow(filterHash,"22011353442 : Subslice Bussing Reorganization for Better DSS Utilization");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012521445"  => "features"};
printFeatureRow(filterHash,"22012521445 : [Bugfix]Update EU sideband to support global offset feature");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012602903"  => "features"};
printFeatureRow(filterHash,"22012602903 : [Bugfix][PERF][DCN] TDL -> GW Barrier Flush");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010298712"  => "features"};
printFeatureRow(filterHash,"14010298712 : Deliver TDR directly from TDL to EU");
printAll()
endTable()

printTitle("Xe2 AMFS DCN Table")
startTable()
printTableHeader("DCN")
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010983067"  => "features"};
#printFeatureRow(filterHash,"14010983067 : AMFS: (1.0 spec compliance) Sampler to request additional feedback map surface state");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16013261006"  => "features"};
#printFeatureRow(filterHash,"16013261006 : [AMFS DCN] AMFS security fix to support per-slice contexts executing simultaneously in different address spaces");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011445621"  => "features"};
printFeatureRow(filterHash,"22011445621 : [AMFS] AMFS Standard Mip Region Layout Support");
printAll()
endTable()

printTitle("Xe2 Compression DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010049556"  => "features"};
printFeatureRow(filterHash,"14010049556 : [UUC] [PARENT] 256B compression block for 3D/GPGPU with unified CCS codes");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1406519725"  => "features"};
printFeatureRow(filterHash,"1406519725 : [UUC] [CHILD] Compression support in L3 including 256B and sectoring");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010514922"  => "features"};
printFeatureRow(filterHash,"14010514922 : [UUC] [STANDALONE] Z Plane compression");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010786296"  => "features"};
#printFeatureRow(filterHash,"14010786296 : [UUC][CHILD] Z fast clear");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011195676"  => "features"};
printFeatureRow(filterHash,"14011195676 : [UUC][STANDALONE] 2x Fast Clear Fabric TPT");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011946253"  => "features"};
#printFeatureRow(filterHash,"14011946253 : [UUC] 256B Render Fast Clear");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010198509"  => "features"};
#printFeatureRow(filterHash,"22010198509 : [UUC] [CHILD] Copy Engine Fast Clear");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010313133"  => "features"};
printFeatureRow(filterHash,"22010313133 : [UUC][STANDALONE]L3 Super Q updates");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012235606"  => "features"};
printFeatureRow(filterHash,"22012235606 : [DCN] L3 handling of 512B and 1K fast clear");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012655533"  => "features"};
printFeatureRow(filterHash,"22012655533 : [Xe2] [Delta] [UUC] Add XeTLB stateless compression control register");
printAll()
endTable()

printTitle("Xe2 Config DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010229513"  => "features"};
printFeatureRow(filterHash,"14010229513 : [PARENT] 3D Pipeline Changes for SIMD16 EU");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011217695"  => "features"};
printFeatureRow(filterHash,"14011217695 : [PARENT] Scalability requirements");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1408582291"  => "features"};
#printFeatureRow(filterHash,"1408582291 : [CHILD] Make Sampler Compatible with Monolithic SIMD16 EU");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1409267114"  => "features"};
printFeatureRow(filterHash,"1409267114 : [CHILD] GEOMFF Changes for Monolithic SIMD16 EU Dispatch");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1409877587"  => "features"};
printFeatureRow(filterHash,"1409877587 : [CHILD] PS thread payload change for SIMD16 EU");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010182034"  => "features"};
printFeatureRow(filterHash,"14010182034 : [Child] Connecting RCC to Physical L3");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011143571"  => "features"};
printFeatureRow(filterHash,"14011143571 : [CHILD] Scalability of Raster X-Bar");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011184919"  => "features"};
printFeatureRow(filterHash,"14011184919 : Add 3D connections to Fabric");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011184997"  => "features"};
printFeatureRow(filterHash,"14011184997 : L3 Bank configuration");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011200519"  => "features"};
printFeatureRow(filterHash,"14011200519 : [Child][Scalability] L3 Node/Fabric configuration");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011455836"  => "features"};
#printFeatureRow(filterHash,"14011455836 : [Xe2 Configuration definition -  Configurations - IP Concept");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012166647"  => "features"};
printFeatureRow(filterHash,"14012166647 : [CHILD] Thread dispatch scalability changes for Xe2");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012433807"  => "features"};
#printFeatureRow(filterHash,"14012433807 : Xe2_HPG Client Product Configurations");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010473645"  => "features"};
printFeatureRow(filterHash,"22010473645 : Gen12.9 TSL add 3D thread dispatches");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010888375"  => "features"};
#printFeatureRow(filterHash,"22010888375 : Fuse/Recovery Capabilities");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012532957"  => "features"};
#printFeatureRow(filterHash,"22012532957 : Xe2 Product DownBin Configurations");
printAll()
endTable()

printTitle("Xe2 Copy Engine DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16010969967"  => "features"};
printFeatureRow(filterHash,"16010969967 : [Xe2] Copy Engine Configuration for Xe2");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16010970208"  => "features"};
printFeatureRow(filterHash,"16010970208 : [Gen12.9] [CHILD] Data Security: Add a flow in Copy Engine to securely evict encrypted surfaces from L3");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16011738287"  => "features"};
printFeatureRow(filterHash,"16011738287 : Xe2: Link and Paging Copy Memory interface consolidation");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16012977047"  => "features"};
printFeatureRow(filterHash,"16012977047 : [Bugfix][Xe2]Add a flow in Copy Engine to evict non-encrypted surfaces from L3 - Delta Feature");
printAll()
endTable()

#printTitle("Xe2 Dataport DCN Table")
#startTable()
#printTableHeader("DCN")

#printAll()
#endTable()

#printTitle("Xe2 EU DCN Table")
#startTable()
#printTableHeader("DCN")
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011608542"  => "features"};
#printFeatureRow(filterHash,"22011608542 : Xe2 systolic array must run 8 logical deep DPAS instructions");
#printAll()
#endTable()

printTitle("Xe2 Geo/Raster DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010990208"  => "features"};
printFeatureRow(filterHash,"14010990208 : Out of order raster and pixel pipe");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16014085103"  => "features"};
#printFeatureRow(filterHash,"16014085103 : [DCN] OOO Raster enhancment -Rxbar Vertex Repacking");
printAll()
endTable()

printTitle("Xe2 HW Frontend DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "220160875"  => "features"};
printFeatureRow(filterHash,"220160875 : Auto Tail Update");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1406612157"  => "features"};
printFeatureRow(filterHash,"1406612157 : PPGTT support for Ring Buffers");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011271903"  => "features"};
printFeatureRow(filterHash,"14011271903 : [CHILD] Scalability requirements - HWFE");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012140225"  => "features"};
printFeatureRow(filterHash,"14012140225 : Barrier Support Lite(staged)");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012959004"  => "features"};
printFeatureRow(filterHash,"14012959004 : [DCN XE2]: OA_MMIO_TRIG must be added to the Allowed Register List of RCS and CCS*");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014532611"  => "features"};
#printFeatureRow(filterHash,"14014532611 : [Delta Feature]: Missing CFEG scope in Changes to LSC L1 cache invalidation/flush");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16011452494"  => "features"};
#printFeatureRow(filterHash,"16011452494 : RDOP and FFDOP support from HWFE");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16013328753"  => "features"};
#printFeatureRow(filterHash,"16013328753 : [BugFix] Copy Engine/GuC  changes to support MOCS modification for L3/L4 cacheability - delta feature");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010492970"  => "features"};
printFeatureRow(filterHash,"22010492970 : Remove flush between Render and Compute Workloads – Reduced Version");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011313376"  => "features"};
printFeatureRow(filterHash,"22011313376 : [DCN] Remove Support for two address space workloads in a SS");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011785677"  => "features"};
printFeatureRow(filterHash,"22011785677 : Timespy G-Buffer Phase Performance Improvements");
printAll()
endTable()

printTitle("Xe2 Mem Pipe DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010253015"  => "features"};
printFeatureRow(filterHash,"14010253015 : Extend 57b VA for Mem Pipe");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010515700"  => "features"};
printFeatureRow(filterHash,"14010515700 : Page Walker and TLB separation");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011041967"  => "features"};
printFeatureRow(filterHash,"14011041967 : Support for Device-scoped Atomics in System Memory in PCIE mode");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011184940"  => "features"};
printFeatureRow(filterHash,"14011184940 : [Parent] Latency Reduction & improving latency coverage");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011184965"  => "features"};
printFeatureRow(filterHash,"14011184965 : [Child] Latency reduction in SQIDI");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011185027"  => "features"};
printFeatureRow(filterHash,"14011185027 : Scalable Memory Interface (to connect to L4 & flavors of local memory)");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011185056"  => "features"};
printFeatureRow(filterHash,"14011185056 : MOCS");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012963620"  => "features"};
printFeatureRow(filterHash,"14012963620 : [Bugfix DCN] Propagating request priority for diamond lane requests to Memory interface");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14013093611"  => "features"};
printFeatureRow(filterHash,"14013093611 : Replicate WOPCM and GSM range due to GAM split");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14013598335"  => "features"};
printFeatureRow(filterHash,"14013598335 : [DCN] Move LMEM Config register to page walker");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014662613"  => "features"};
printFeatureRow(filterHash,"14014662613 : [Bug Fix DCN]  Invalid access flow updates");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010492566"  => "features"};
printFeatureRow(filterHash,"22010492566 : Transient Data Flush for Display");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010650444"  => "features"};
printFeatureRow(filterHash,"22010650444 : [Child] L3 changes to support SQIDI latency reduction changes");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011510814"  => "features"};
printFeatureRow(filterHash,"22011510814 : Add support for 48b Virtual Address");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011664923"  => "features"};
printFeatureRow(filterHash,"22011664923 : [DCN] Improve L3 bank sequential Atomic performance");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011854147"  => "features"};
printFeatureRow(filterHash,"22011854147 : Xe2:  MERT to LNEP  connectivity optmization");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012780896"  => "features"};
printFeatureRow(filterHash,"22012780896 : [Bugfix]ATS Invalidation Handling with shared page walker");



filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1406519725"  => "features"};
printFeatureRow(filterHash,"1406519725 : Compression support in L3 including 256B and sectoring ");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010045801"  => "features"};
printFeatureRow(filterHash,"14010045801 : [Child] Data Security Implications to L3");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1607634291"  => "features"};
printFeatureRow(filterHash,"1607634291 : [PARENT] XEFI Specification");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010182034"  => "features"};
printFeatureRow(filterHash,"14010182034 : Connecting RCC to Physical L3");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011184919"  => "features"};
printFeatureRow(filterHash,"14011184919 : Add 3D connections to Fabric");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011184997"  => "features"};
printFeatureRow(filterHash,"14011184997 : L3 Bank configuration");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011200519"  => "features"};
printFeatureRow(filterHash,"14011200519 : [UUC][STANDALONE] 2x Fast Clear Fabric TPT(compression)");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16013377015"  => "features"};
printFeatureRow(filterHash,"16013377015 : [BugFix] Copy Engine Verbatim Copy Fix for XeFI compatibility (compression)");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014483489"  => "features"};
printFeatureRow(filterHash,"14014483489 : [Delta feature]Instruction based caching to override PAT/MOCS");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012780896"  => "features"};
printFeatureRow(filterHash,"22012780896 : [Bugfix]ATS Invalidation Handling with shared page walker");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011092630"  => "features"};
printFeatureRow(filterHash,"22011092630 : [Child]XEFI_UUC: Pre-TLB Client side changes for XEFI");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011092845"  => "features"};
printFeatureRow(filterHash,"22011092845 : Security -  Flushing Physical RCC");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011092661"  => "features"};
printFeatureRow(filterHash,"22011092661 : [Child] XEFI_UUC: Post-TLB changes for XEFI (Fabric, external interfaces)");

filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012235606"  => "features"};
printFeatureRow(filterHash,"22012235606 : [DCN] L3 handling of 512B and 1K fast clear (compression)");

printAll()
endTable()

printTitle("Xe2 Mesh DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011124973"  => "features"};
printFeatureRow(filterHash,"14011124973 : Mesh Shader Performance Fixes (ZBBed from DG2)");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010672845"  => "features"};
printFeatureRow(filterHash,"22010672845 : Mesh shader autostrip optimization");
printAll()
endTable()

printTitle("Xe2 Multi CTX DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010473604"  => "features"};
printFeatureRow(filterHash,"22010473604 : Gen12.9 Multi-Context");
printAll()
endTable()



printTitle("Xe2 Pixel Pipe DCN Table")
startTable()
printTableHeader("DCN")
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010048738"  => "features"};
#printFeatureRow(filterHash,"14010048738 : [CHILD] Remove HDC and map typed UAV accesses to pixel path (read/write/atomics)");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010214975"  => "features"};
printFeatureRow(filterHash,"14010214975 : Tile64 change for MSAA layout - due to Physical L3 and therefore physical RCC:");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010848132"  => "features"};
printFeatureRow(filterHash,"14010848132 : Demote early depth testing to lateZ for overlapping cachelines");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011334914"  => "features"};
printFeatureRow(filterHash,"14011334914 : [CHILD] Extend Render Target Send message to SIMD32");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012020990"  => "features"};
printFeatureRow(filterHash,"14012020990 : Render target prefetching");
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011952162"  => "features"};
#printFeatureRow(filterHash,"22011952162 : Removal of MRS+radial mode CPS (sw defeature)");
printAll()
endTable()

printTitle("Xe2 PM DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1409855589"  => "features"};
printFeatureRow(filterHash,"1409855589 : Drop DFR From Sampler");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010274564"  => "features"};
printFeatureRow(filterHash,"14010274564 : Removal of the Tessellation DOP");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011356278"  => "features"};
printFeatureRow(filterHash,"14011356278 : [Wave 2.5] 3D DOP clock removal Parent HSD");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011372198"  => "features"};
printFeatureRow(filterHash,"14011372198 : [Xe2] Media Clock handling");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011412784"  => "features"};
printFeatureRow(filterHash,"14011412784 : [DCN] Add support for DFPD for 3D and Media units");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012135356"  => "features"};
printFeatureRow(filterHash,"14012135356 : [Xe2] Psys Capping Feature for GT on  Xe2  (cloned from PVC-XL)");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012177480"  => "features"};
printFeatureRow(filterHash,"14012177480 : MsgCh Wave2.5:  MsgCh updates for Gen12.9/Wave2.5/Media13.1");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012312261"  => "features"};
printFeatureRow(filterHash,"14012312261 : ACM for Xe2");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012538169"  => "features"};
printFeatureRow(filterHash,"14012538169 : Xe2");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14013112356"  => "features"};
printFeatureRow(filterHash,"14013112356 : Paging Copy Engine PM and Reset support");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014985014"  => "features"};
printFeatureRow(filterHash,"14014985014 : [Bugfix] Make Master XeTLB MsgCh GrpID 0");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16012331520"  => "features"};
printFeatureRow(filterHash,"16012331520 : Xe2 X3 GT SD: RRunit connectivity: update needed for GTSCSIDE & GTSCMID");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010513025"  => "features"};
printFeatureRow(filterHash,"22010513025 : GT and Media PM handling");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011404884"  => "features"};
printFeatureRow(filterHash,"22011404884 : Xe2 - Power Management validation test modes for instant boot and power flows optimizations");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011455870"  => "features"};
printFeatureRow(filterHash,"22011455870 : [Xe2] Clock Division Throttling for Psys Power Capping Feature");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011461444"  => "features"};
printFeatureRow(filterHash,"22011461444 : Gen12.9 CMI ADM path FDI control");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012318005"  => "features"};
printFeatureRow(filterHash,"22012318005 : Xe2 3D IP HVM Warm Reset Simplification");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012519640"  => "features"};
printFeatureRow(filterHash,"22012519640 : [Xe2] DCN to Force n=8 value to CPunit when PsysCapping Feature is Disabled  & Detection of when new n value is written before previous n value is consumed by CPunit");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012718228"  => "features"};
printFeatureRow(filterHash,"22012718228 : Updates to Xe2 GT CMI D2D pinlist");
printAll()
endTable()

printTitle("Xe2 Ray Tracing DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010540651"  => "features"};
printFeatureRow(filterHash,"14010540651 : Increase RTT and RTQ thru'put - RT Performance");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011192593"  => "features"};
printFeatureRow(filterHash,"14011192593 : Wide EU related optimization for TraceRay message");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14013390450"  => "features"};
printFeatureRow(filterHash,"14013390450 : RTT restructuring for scalability");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012111137"  => "features"};
printFeatureRow(filterHash,"22012111137 : [DCN] Move the num of stack ids from RayTracingControl Register to CFE_STATE");
printAll()
endTable()

printTitle("Xe2 Security DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14010045801"  => "features"};
printFeatureRow(filterHash,"14010045801 : [Child] Data Security Implications to L3");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011092845"  => "features"};
printFeatureRow(filterHash,"22011092845 : Security -  Flushing Physical RCC");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011730232"  => "features"};
printFeatureRow(filterHash,"22011730232 : Converged SAI for SG Unit/MGSR default values");
printAll()
endTable()

printTitle("Xe2 System WG DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012364796"  => "features"};
printFeatureRow(filterHash,"14012364796 : Reflect GFX PCI Device ID");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14012558700"  => "features"};
printFeatureRow(filterHash,"14012558700 : [Wave2.5][Elasti] Add support for CSC");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014387340"  => "features"};
printFeatureRow(filterHash,"14014387340 : Discrete I+I opportunity - add doorbell write support");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010459594"  => "features"};
printFeatureRow(filterHash,"22010459594 : [Wave2.5] Combined PVC and SAMedia device logic support");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010459668"  => "features"};
printFeatureRow(filterHash,"22010459668 : [CLS]  Connectivity (SAMedia");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011317668"  => "features"};
printFeatureRow(filterHash,"22011317668 : [Wave2.5][Discrete] SGunit 16 bit portID IOSF SB endpoint");
printAll()
endTable()

#printTitle("Xe2 TED DCN Table")
#startTable()
#printTableHeader("DCN")
#filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011534764"  => "features"};
#printFeatureRow(filterHash,"14011534764 : TE-TED Interface Enhancement for Control packets");
#printAll()
#endTable()

printTitle("Xe2 XeFi DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1607634291"  => "features"};
printFeatureRow(filterHash,"1607634291 : [PARENT] XEFI Specification");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011092630"  => "features"};
printFeatureRow(filterHash,"22011092630 : [Child]XEFI_UUC: Pre-TLB Client side changes for XEFI");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011092661"  => "features"};
printFeatureRow(filterHash,"22011092661 : [Child] XEFI_UUC: Post-TLB changes for XEFI (Fabric");
printAll()
endTable()



@skipV2V3 = false

printTitle("Xe2 V2 DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014181222"  => "features"};
printFeatureRow(filterHash,"14014181222 : [DCN] Add active-thread"" only barrier in Xe2");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012521285"  => "features"};
printFeatureRow(filterHash,"22012521285 : [Bugfix][PERF][DCN] Changes to LSC L1 cache invalidation/flush");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014069143"  => "features"};
printFeatureRow(filterHash,"14014069143 : [DCN] Adding HW support for FP64 IEEE DIV/SQRT Macro");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014313782"  => "features"};
printFeatureRow(filterHash,"14014313782 : Caching system memory requests in the GPU");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22011223560"  => "features"};
printFeatureRow(filterHash,"22011223560 : Dynamic LSC/Sampler Routing");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012919778"  => "features"};
printFeatureRow(filterHash,"22012919778 : Cut index on list topology performance improvement");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14013043186"  => "features"};
printFeatureRow(filterHash,"14013043186 : DCN: Add gather4_l support to Sampler");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012782909"  => "features"};
printFeatureRow(filterHash,"22012782909 : Fix messages for sparse textures for Vulkan and OGL compliance");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22012939252"  => "features"};
printFeatureRow(filterHash,"22012939252 : [Xe2][Delta] Add support to gather4_l_c and gather4_i_c");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14015171903"  => "features"};
printFeatureRow(filterHash,"14015171903 : Fixed Function Execute Indirect Loop Unroll");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14015181142"  => "features"};
printFeatureRow(filterHash,"14015181142 : [XE2 BUG FIX]: CB2 on Ctx Switch Out Always for GW State Clear");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16014614053"  => "features"};
printFeatureRow(filterHash,"16014614053 : [Xe2][BUG FIX DCN]Remove CHICKEN_PWR_CTX_CSBE_3/4 from allowed list");
printAll()
endTable()

printTitle("Xe2 V3 DCN Table")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14013109946"  => "features"};
printFeatureRow(filterHash,"14013109946 : Timespy Vertex ordering performance improvement");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22010943846"  => "features"};
printFeatureRow(filterHash,"22010943846 : Region-Based Tessellation Redistribution");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "220866013"  => "features"};
printFeatureRow(filterHash,"220866013 : Pipeline Drawing Rectangle State");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14015087272"  => "features"};
printFeatureRow(filterHash,"14015087272 : conservative test @HiZ for overlapping pixels");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14011781153"  => "features"};
printFeatureRow(filterHash,"14011781153 : DFD GT Wave2.5: OA decoupling from NOA2VISA");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "22014018980"  => "features"};
printFeatureRow(filterHash,"22014018980 : Dynamic ray management for Synchronous Ray Tracing");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14015119174"  => "features"};
printFeatureRow(filterHash,"14015119174 : HLSL_6_7 Add per pixel offset support to Sampler");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16012330530"  => "features"};
printFeatureRow(filterHash,"16012330530 : XE2: Diamond Lane Support for GuC and CS memory requests");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16013692951"  => "features"};
printFeatureRow(filterHash,"16013692951 : [Delta Feature]: Diamond Lane");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "16012396654"  => "features"};
printFeatureRow(filterHash,"16012396654 : XE2 [BASE] - OA Disaggregation Support on Key Perf Cluster Events");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "1409780112"  => "features"};
printFeatureRow(filterHash,"1409780112 : Support DX, Vulkan and Metal API for Barycentrics");
filterHash = {"2x6|2x4|7x4x8"  => "executionStageName", "14014577164"  => "features"};
printFeatureRow(filterHash,"14014577164 : [DELTA FEATURE] BSpec Correction for Support DX");

printAll()
endTable()
=end

printTitle("Xe2 WMTP DCN")
startTable()
printTableHeader("DCN")
filterHash = {"2x6|2x4|10x6"  => "executionStageName", "22011229030"  => "features"};
printFeatureRow(filterHash,"22011229030 : [WMTP][PARENT] Compute Walker Mid-Thread Preemption");
printAll()
endTable()

endDivision()
closeFiles
exit