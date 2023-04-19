use strict; 
#use warnings;
use File::Find;
use File::Copy;
use File::Path;
use List::Util 1.33 'any';
use Cwd qw(cwd);
use File::Copy::Recursive qw(dircopy);
use Time::Piece;
use Excel::Writer::XLSX;


#creating the excel sheet
my $Excel_book1 = Excel::Writer::XLSX->new("final_result.xlsx");

#creating the design for sheet1
my $diff_includes_sheet = $Excel_book1->add_worksheet('diff_includes');
my $diff_includes_sheet_rm_timedate = $Excel_book1->add_worksheet('diff_includes_rm_timedate');
my $diff_rtl_sheet = $Excel_book1->add_worksheet('diff_rtl');
my $diff_rtl_sheet_rm_timedate = $Excel_book1->add_worksheet('diff_rtl_rm_timedate');



#adding data into diff_includes_sheet
my $input = "diff_includes.txt";
if (-e $input){
	open(my $fh, "<", $input) or die "Unable to open $!\n";

	my $count = 0;
	while (<$fh>) {
		chomp $_;
		$count++;
		my @data_row = ($_,"","",'Netlist Impact=',"","",'comment=');
		$diff_includes_sheet->write("A$count",\@data_row);
	}
	
	close $fh or die "Unable to close $input: $!\n";
}
else {
	print "file not exists--> $input\n";
}

#adding data into diff_includes_rm_timedate
my $input = "diff_includes_rm_timedate.txt";
if (-e $input){
	open(my $fh, "<", $input) or die "Unable to open $!\n";

	my $count = 0;
	while (<$fh>) {
		chomp $_;
		$count++;
		my @data_row = ($_,"","",'Netlist Impact=',"","",'comment=');
		$diff_includes_sheet_rm_timedate->write("A$count",\@data_row);
	}
	
	close $fh or die "Unable to close $input: $!\n";
}
else {
	print "file not exists--> $input\n";
}

#adding data into diff_rtl
my $input = "diff_rtl.txt";
if (-e $input){
	open(my $fh, "<", $input) or die "Unable to open $!\n";

	my $count = 0;
	while (<$fh>) {
		chomp $_;
		$count++;
		my @data_row = ($_,"","",'Netlist Impact=',"","",'comment=');
		$diff_rtl_sheet->write("A$count",\@data_row);
	}
	
	close $fh or die "Unable to close $input: $!\n";
}
else {
	print "file not exists--> $input\n";
}

#adding data into diff_rtl_rm_timedate
my $input = "diff_rtl_rm_timedate.txt";
if (-e $input){
	open(my $fh, "<", $input) or die "Unable to open $!\n";

	my $count = 0;
	while (<$fh>) {
		chomp $_;
		$count++;
		my @data_row = ($_,"","",'Netlist Impact=',"","",'comment=');
		$diff_rtl_sheet_rm_timedate->write("A$count",\@data_row);
	}
	
	close $fh or die "Unable to close $input: $!\n";
}
else {
	print "file not exists--> $input\n";
}


#adding data into diff_libs_sheet
my $input = "diff_libs.txt";
if (-e $input){
	my $diff_libs_sheet = $Excel_book1->add_worksheet('diff_libs');	
	open(my $fh, "<", $input) or die "Unable to open $!\n";

	my $count = 0;
	while (<$fh>) {
		chomp $_;
		$count++;
		my @data_row = ($_,"","",'Netlist Impact=',"","",'comment=');
		$diff_libs_sheet->write("A$count",\@data_row);
	}
	
	close $fh or die "Unable to close $input: $!\n";
}
else {
	print "file not exists--> $input\n";
}

#adding data into diff_libs_rm_timedate
my $input = "diff_libs_rm_timedate.txt";
if (-e $input){
	my $diff_libs_sheet_rm_timedate = $Excel_book1->add_worksheet('diff_libs_rm_timedate');	
	open(my $fh, "<", $input) or die "Unable to open $!\n";

	my $count = 0;
	while (<$fh>) {
		chomp $_;
		$count++;
		my @data_row = ($_,"","",'Netlist Impact=',"","",'comment=');
		$diff_libs_sheet_rm_timedate->write("A$count",\@data_row);
	}
	
	close $fh or die "Unable to close $input: $!\n";
}
else {
	print "file not exists--> $input\n";
}


$Excel_book1->close;

