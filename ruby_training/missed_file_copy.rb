#include <ruby.h>

require 'fileutils'

puts "Hello, World!\n";
#opening the file and reading the contents
file = File.open("SFC_missed_paths.txt")
array = file.readlines.map(&:chomp)
file.close


#printing current working directory
#path = Dir.getwd
#puts path



#puts6 Dir.exist?"dir_name"
dest_path="X:\\VPP\\"
#array = ['one', 'two', 'three', 'four']
#copying the file from source to destination
for i in array[0,2]
	puts i
	
	clipname = File.basename(i)
	a = dest_path+clipname
	puts a
	puts "\n"
	#FileUtils.cp(i, dest_path.concat(clipname))
end

=begin
\\DataGroveFMLC.fm.intel.com\GFXSV_Data\BASKL\MediaShare\Testfiles\Media\VPP\VEBOX\SVGfxTests\legacy\SRC\Source_clips\Space_Jam_Extras2.mpeg_720x480x736_i.yuy2
=end