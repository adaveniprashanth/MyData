
#1st method
if false
	# File Handling Program
	# Creating a file
	fileobject = File.new("sample.txt", "w+");

	# Writing to the file
	fileobject.syswrite("File Handling");	

	# Closing a file
	fileobject.close();
end

#2nd method
if false
	open('myfile.out', 'w') { |f|
	  f << "Four score\n"
	  f << "and seven\n"
	  f << "years ago\n"
	}
end