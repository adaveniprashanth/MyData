#include <ruby.h>

require 'fileutils'

puts "Hello, World! me";
#opening the file and reading the contents
#file = File.open("clip_paths.txt")
#array = file.readlines.map(&:chomp)
#file.close


#printing current working directory
path = Dir.getwd
puts path

#creating the new directory in the current folder
#Dir.mkdir("MPEG2")

#adding the MPEG2 folder to current path
path1 = path.concat("/MPEG2")
puts path1
dest_path = path1.concat("/")

#puts6 Dir.exist?"dir_name"

array = ['one', 'two', 'three', 'four']
copying the file from source to destination
for i in array
	puts "filename"
	puts i
	clipname = File.basename(i) 
	FileUtils.cp(i, dest_path.concat(clipname))
end


#printing all files in directory
#filenames = Dir.entries(".")
#puts filenames



=begin
puts "current path"
path =  Dir.getwd
Dir.chdir(path.concat("/GFXMedia"))
puts "updated path"
path =  Dir.getwd
=end


=begin
#replacing the character
sentence = 'My name is \Robert \Robert  Robert Robert'
new = sentence.gsub(/[\\]/,'/')
puts "sentence is"
puts sentence
puts "new"
puts new
=end