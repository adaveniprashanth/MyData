use strict; 
#use warnings;
use File::Find;
use File::Copy;
use File::Path;
use List::Util 1.33 'any';
use Cwd qw(cwd);
use File::Copy::Recursive qw(dircopy);
use Time::Piece;

##for reference --> https://metacpan.org/pod/Excel::Writer::XLSX::Examples#Example:-autofit.pl
##for reference --> https://metacpan.org/release/JMCNAMARA/Excel-Writer-XLSX-1.11/source/examples/autofilter.pl

my $content_excel_sw = 1;
if ($content_excel_sw eq 1)
{
  use List::Util 1.33 'any';
  use Cwd qw(cwd) ;
  use File::Copy::Recursive qw(dircopy);
  use Time::Piece;
  my @word = ();
  my $dir = cwd;
  use Excel::Writer::XLSX;
  
	my $input = "commands.txt";
	#my $input = "$gfxbuild_run_path/gfxbuild_cmd.list";
	open(my $fh, "<", $input) or die "Unable to open $!";
	#my $Excel_book1 = Excel::Writer::XLSX->new("$current_package_path/smedia_top/val/Media_BMG_x2_1p0_pre_test_content_delivery.xlsx");
	my $Excel_book1 = Excel::Writer::XLSX->new("content_delivery.xlsx");
	
	#creating the design for sheet1
	my $Excel_sheet1 = $Excel_book1->add_worksheet('Content_Opts_Status');
	my @sh1headings = ("Test ID","Test Name","Status on SM","Status on GM","Gfxbuild Command");
	
	#setting the design for rows and headings
	my $sh1headformat = $Excel_book1->add_format(border=>1,color=>'black',bg_color=>'#BDEEEE',bold=>1);
	my $sh1colAformat = $Excel_book1->add_format(border=>1,color=>'black',bold=>1,align=>'center');
	my $sh1colBformat = $Excel_book1->add_format(border=>1,color=>'black',bold=>1);
	my $sh1colCformat = $Excel_book1->add_format(border=>1,color=>'black',bold=>1,bg_color=>'#C9D08C',text_wrap=>1);
	my $sh1colDformat = $Excel_book1->add_format(border=>1,color=>'black',bold=>1,bg_color=>'#C9D08C');
	my $sh1colEformat = $Excel_book1->add_format(border=>1,color=>'black',bold=>1);
	
	$Excel_sheet1->write( "A1", \@sh1headings, $sh1headformat );
	
	#creating sheet2 and its headings
	my $Excel_sheet2 = $Excel_book1->add_worksheet('Content_Info');
	my @sheet2headings = ("Category","Sub feature","TestName","SM status","GM status","Fuse Override","Comments");
	my $sh2headformat = $Excel_book1->add_format(border=>1,color=>'black',bg_color=>'#BDEEEE',bold=>1);
	$Excel_sheet2->write( "A1", \@sheet2headings, $sh2headformat );
	my $sh2colCformat = $Excel_book1->add_format(border=>1,color=>'black',bold=>1);
	
	
	
	
	my @column_width = (5,10,15,15,30);
	sub column_widths {
		if (length($_[1]) > $column_width[1] ){
			$column_width[1] = length($_[1]);
		}
	}
	
	
	
	my $count = 1;
	while (<$fh>) {
		chomp $_;
		$count++;
		my @parts = split(/\//, $_);
		print "parts $parts[4]\n";
		
		my ($a,$b)=split('-testlib- ',$_,2);
		my @data_row = ($count-1,$parts[4],"","",$b);
		column_widths(@data_row);
		$Excel_sheet1->write( "A$count", $data_row[0],$sh1colAformat);
		$Excel_sheet1->write( "B$count", $data_row[1],$sh1colBformat);
		$Excel_sheet1->write( "C$count", $data_row[2],$sh1colCformat);
		$Excel_sheet1->write( "D$count", $data_row[3],$sh1colDformat);
		$Excel_sheet1->write( "E$count", $data_row[4],$sh1colEformat);
		$Excel_sheet2->write( "C$count", $data_row[1],$sh2colCformat);
		
	}
	#setting the columns width
	$Excel_sheet1->set_column('A:A',$column_width[0]);
	$Excel_sheet1->set_column('B:B',$column_width[1]);
	$Excel_sheet1->set_column('C:D',$column_width[2]);
	$Excel_sheet1->set_column('E:E',$column_width[4]);
	
	$Excel_sheet2->set_column('A:A',10);
	$Excel_sheet2->set_column('B:B',30);
	$Excel_sheet2->set_column('C:C',$column_width[1]);
	$Excel_sheet2->set_column('D:G',30);
	print "total tests are $count\n";
	
	
	
	
	$Excel_book1->close;
	close $fh or die "Unable to close $input: $!";
	print "Content Excel has created successfully \n";
	#print $gfxrun_log "Content Excel has created successfully \n";

}
