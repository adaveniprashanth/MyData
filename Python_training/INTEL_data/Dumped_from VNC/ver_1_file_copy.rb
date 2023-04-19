#include <ruby.h>

require 'fileutils'

puts "Hello, World! me";
#opening the file and reading the contents
file = File.open("clip_paths.txt")
array = file.readlines.map(&:chomp)
file.close


#printing current working directory
path = Dir.getwd
puts path

#creating the new directory in the current folder
Dir.mkdir("MPEG2")

#adding the MPEG2 folder to current path
path1 = path.concat("/MPEG2")
puts path1
dest_path = path1.concat("/")

#puts6 Dir.exist?"dir_name"

#array = ['one', 'two', 'three', 'four']
#copying the file from source to destination
for i in array
        if i.length > 2
            puts "clipname\n"
            clipname_split = i.split("\\")
            clipname = clipname_split[-1]
	    puts clipname
            puts "clip path\n"
            puts dest_path
            full_path =  dest_path+clipname
            puts full_path
            FileUtils.cp(i, full_path)
            
        end
end

puts "copy completed";
