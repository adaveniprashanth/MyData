#!/usr/intel/bin/perl
use strict ; 
use warnings ;
#print "hello\n";
use File::Basename;
use File::Path qw( make_path );
use List::Util 1.33 'any';
use File::Copy;
use Excel::Writer::XLSX;
use autodie;
#use Text::Trim qw(trim);
use Time::Piece;
use Text::Wrap qw{ wrap };
use Spreadsheet::ParseExcel;

use Cwd qw(cwd);
my $dir = cwd;
#print "$dir\n";
=my $directory = "$dir"."/INTERACTIVE";
#print "$directory\n";
my $decpic = "$directory"."/Dec_PicParameterSet_0_CFG0";
#for unzipping the logic and decpic folder verification:
if ( -d $decpic ) 
{
	print "decpic folder present\n";
	opendir(my $vars2, $decpic) or die "Cannot open directory: $!";
	my @allfiles = readdir $vars2;
	print "@allfiles\n";
	my $logfile = 'runsim.log.gz';
	my $match_found = any { /$logfile/ } @allfiles;
	print "match $match_found\n";
	if($match_found eq 1) {
		print " do gunzip operation";
	}
	my $filename = "$decpic"."/runsim.log";
	print "filename $filename\n";

	#finding the path from log file
	#https://www.perltutorial.org/perl-read-file/
	open(FH, '<', $filename) or die "Sorry!! couldn't open";
	my @word = ();
	while(<FH>){
	   if($_ =~ /(RunScript)/)
			{
				if ($_ =~ /> /)
				{
					@word = split /> /, $_;
					print "$word[1]\n";
					@word = split /gen/,$word[1];
					print "$word[0]\n";
				
				}
				
			}
	}
	
	close(FH);
	
	print "path found from log file is $word[0]\n";
	#finding the dirname from the absolute path
	my $abspath = $word[0];
	use File::Basename;
	my $dirname  = dirname($abspath);
	print "$dirname\n";
	
	my $bin = "$dirname"."/bin";
	print "bin folder is $bin";
	my $lib =  "$dirname"."/lib/perl5";
	print "lib folder is $lib";
	
	my $destination = " smedia_top/val/gfxbuild/verif/validation/bin/";
	
}
else{
print "going to next step becaues decpic folder not present";
}
=cut
=use File::Copy::Recursive qw(dircopy);
dircopy($bin,"$val_dir/smedia_top/val/gfxbuild/verif/validation/bin/") or die("$!\n");
dircopy($lib,"$val_dir/smedia_top/val/gfxbuild/verif/validation/bin/") or die("$!\n");
=cut

#$val_dir/smedia_top/val/gfxbuild/verif/validation/bin/ <-- new files

#/nfs/site/disks/lnl_soc_regress_001/ashish/soc_package/LNL_IPX_UPLOAD/RTL1p0_pre/xe2lpm_media_common-22ww14.4e-package/smedia_top/val/gfxbuild/verif/validation/bin/ <--old files 
#for copying the missed files from older to new folder:
=my $old_files_path = "$dir"."/dummy";
opendir(my $vars, $old_files_path) or die "Cannot open directory: $!";
my @oldfiles = readdir $vars;
closedir $vars;
print "old files @oldfiles\n";

my $new_files_path = "$dir"."/ashish_destination";
opendir(my $vars2, $new_files_path) or die "Cannot open directory: $!";
my @newfiles = readdir $vars2;
closedir $vars2;
print "new files @newfiles\n";

use List::Util 1.33 'any';
foreach my $vars4 (@oldfiles)
{
	my $pattern = $vars4;
	my $match_found = any { /$pattern/ } @newfiles;
	if($match_found ne 1) {
		print "file not present in new files fodler is $vars4\n";
		copy "$old_files_path/$vars4", "$new_files_path/$vars4";
		print "copied the missed file $vars4 to new fodler\n";
	}
	else {
		print "file presented in both fodlers $vars4 $match_found\n";
	}
}
=cut

=use List::MoreUtils qw(firstidx);
my $idx = firstidx { $_ eq 'Python' } @newfiles;
print "$idx\n";
=cut

#use Array::Compare;
#my $lc = List::Compare->new(\@Llist, \@Rlist);

=my $lc = Array::Compare->new( {
    lists    => [\@newfiles, \@oldfiles],
    unsorted => 1,
} );
=cut
=use Array::Compare;
#my $comp1 = Array::Compare->new;


my $comp = Array::Compare->new;
 
if ($comp->compare(\@newfiles, \@oldfiles)) {
  print "Arrays are the same\n";
} else {
  print "Arrays are different\n";
}
=cut

=use List::Util 1.33 'any';
my $var1 = "Python3";
my $match_found = any { /$var1/ } @newfiles;
print $match_found ne 0;
=cut

=my $fileName = "paths_file.txt";

if (-e $fileName) {
        open my $read, '<', $fileName;
        local $/; # slurp mode;
        my $data = <$read>;
        close $read;
        print "File exists and has been read\n";
        eval $data;
        unlink $fileName;
}
else {
        print "File does not yet exist\n";
}
=cut
#reading the file content ,ine by line
=my $file = 'paths_file.txt';
open my $info, $file or die "Could not open $file: $!";

while( my $line = <$info>)  {   
	print "evaluating the line\n";
	eval $line;
    #last if $. == 2;
}

close $info;
=cut

=my $file = "paths_file.txt";
open(my $fh, "<", $file) or die "Unable to open < sample.txt: $!";
my @lines;
while (<$fh>) {
chomp $_;
push (@lines, $_);
}
close $fh or die "Unable to open $file: $!";
#print @lines;
print $lines[0];
print $lines[1];
print $lines[2];
print $lines[3];
eval $lines[0];
eval $lines[1];
eval $lines[2];
eval $lines[3];
=cut

=my $file = "input_file.txt";
open(my $fh, "<", $file) or die "Unable to open < sample.txt: $!";
my @lines;
while (<$fh>) {
chomp $_;
my @spl = split('=',$_);
push (@lines, $spl[1]);
}
close $fh or die "Unable to open $file: $!";
print "@lines\n";
#print "$lines[0]";
=cut
#getting the variable values from other perl file
=require 'C:/Users/padavenx/OneDrive - Intel Corporation/Desktop/pandas_work/github_practice/MyData/perl_operations/dummy.pl';
my $val_dir_path = val_dir();
print "$val_dir_path\n";
my $snapshot_model = snapshot_model();
print "$snapshot_model\n";

my $previous_pkg_path = previous_pkg_path();
print "$previous_pkg_path\n";
my $fulsim_tool_path = fulsim_tool_path();
print "$fulsim_tool_path\n";
my $interactive_paths = interactive_paths();
print "$interactive_paths\n";
=cut

#finding the folder  with incomplete name
#print "$dir\n";
=my $directory = "$dir"."/INTERACTIVE";
#print "$directory\n";
my $decpic = "$directory"."/Dec_PicParameterSet_0_CFG0";
my $incomplete_folder = 'IronChef';
opendir(my $vars2, $decpic) || die "folder might not present $!";
my @vars3 = readdir($vars2);
my $total_path;
foreach my $vars4 (@vars3)
{
	my $match_found = "$vars4" =~ /$incomplete_folder/;
	if ($match_found eq 1)
	{
		print "file $vars4\n";
		$total_path = "$decpic"."/$vars4";
	}
}
print "total path is $total_path\n";
=cut


#finding the folder  with incomplete name and splitting the folder name
=print "$dir\n";
my $directory = "$dir"."/INTERACTIVE/bld/sm";
my $incomplete_folder = 'MEDIA';
opendir(my $vars2, $directory) || die "folder might not present $!";
my @vars3 = readdir($vars2);

my $media_path;
foreach my $vars4 (@vars3)
{
	my $match_found = "$vars4" =~ /^$incomplete_folder/;
	if ($match_found eq 1){$media_path = $vars4;}
}

print "media path is $media_path\n";
my @items = split('\.', $media_path,2);
my $context = $items[0];
my $target = $items[-1];

print "context $context target $target\n";
=cut


# Perl program to demonstrate the splitting on character
=my $snapshot_model="/nfs/site/disks/lnl_soc_regress_001/ashish/soc_package/snapshot_model/LNL/ww43p4_LNL_SOC_RTL1p0_post_rev1_snapshot";
my @items = split('/', $snapshot_model);
my $popped_element = pop(@items);
print "$popped_element\n";
=cut




#
#my $iteration = 1;
#
#open FILE_IN, "/nfs/site/disks/mtl_pipesm_aravind_av_regress/ashish_reg/SoC_package/LNL_RTL_1p0_refresh/gfxbuild/gfxbuild_cmd.list" or die "Could not open file /nfs/site/disks/mtl_pipesm_aravind_av_regress/ashish_reg/SoC_package/LNL_RTL_1p0_refresh/gfxbuild/gfxbuild_cmd.list";
#
#open(FH, '>', "/nfs/site/disks/mtl_pipesm_aravind_av_regress/ashish_reg/SoC_package/LNL_RTL_1p0_refresh/gfxbuild/testlist.list")
#while (<FILE_IN>)
#  {
#  my $result = -1;
#  my $line = $_;
#  chomp ($line);
#  my $working_dir = system ("pwd");
#  print "Creating a new test directory\n";
#  #system ("mkdir test_$iteration");
#  mkdir ("/nfs/site/disks/mtl_pipesm_aravind_av_regress/ashish_reg/SoC_package/LNL_RTL_1p0_refresh/gfxbuild/LNL_SOC_1p0_refresh_PRECOMP_TESTS_newfulsim/test_$iteration");
#  #system ("cd test_$iteration");
#  chdir ("/nfs/site/disks/mtl_pipesm_aravind_av_regress/ashish_reg/SoC_package/LNL_RTL_1p0_refresh/gfxbuild/LNL_SOC_1p0_refresh_PRECOMP_TESTS_newfulsim/test_$iteration");
#  $working_dir = system ("pwd");
#  print "Running script on test_$iteration\n";
#  $result = system ($line);
#  #sleep(60);
#  #system ("cd ..");
#  chdir ("/nfs/site/disks/mtl_pipesm_aravind_av_regress/ashish_reg/SoC_package/LNL_RTL_1p0_refresh/gfxbuild/LNL_SOC_1p0_refresh_PRECOMP_TESTS_newfulsim");
#  $iteration = $iteration + 1;
#  }
  
  


#writing the data into file.
=my $filename = '/nfs/site/disks/mtl_pipesm_aravind_av_regress/ashish_reg/SoC_package/LNL_RTL_1p0_refresh/gfxbuild/testlist.list';
open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";

print $fh "test_$iteration\n";


close $fh;
print "done\n";
=cut



=my $filename = "input_file_for_command_generation.txt";
open(FH, '<', $filename) or die "Sorry!! couldn't open";
	my @word = ();
	while(<FH>){
	   if($_ =~ /(RunScript)/)
			{
				if ($_ =~ /> /)
				{
					@word = split /> /, $_;
					print "$word[1]\n";
					@word = split /gen/,$word[1];
					print "$word[0]\n";
				
				}
				
			}
	}
	
	close(FH);
=cut

#++++need to wrok on
#finding the string from the sentence from the file and writing into new file with the new chnages
=my $output = 'output_file_for_command_generation1.txt';
open(my $fh1, '>', $output) or die "Could not open file '$output' $!";

my $input = "input_file_for_command_generation1.txt";
open(my $fh, "<", $input) or die "Unable to open $!";


while (<$fh>) {
	chomp $_;
	if($_ =~ /(--)/){ next;}
	elsif ($_ eq ""){ next;}
	else {
		my $old = $_;
		print "input string\n";
		print "$old\n";
		
		$old =~ s/ +/ /;
		$old =~ s/\t+//;
		$old =~ s/ +/ /;
		$old =~ s/\t+//;
		
		print "$old\n";
		$old =~ s/-repo_ver[ a-z _0-9a-z]* -/-/;
		my($first,$middle,$middle_a, $rest) = split(' ', $old, 4);
		my $val = $first;

		$rest =~ s/-fulsim_opt "/-fulsim_opt -qq /;
		$rest =~ s/-grits_opt "/-grits_opt -qq /;
		$rest =~ s/-testlib_opt "/-testlib_opt -qq /;
		$rest =~ s/(?<!%)\"/ qq-/g;
		
		my $start = '$GT_ROOT/verif/scripts/gfxbuild_sm $GT_ROOT/source/rtl/cfg_env/dut/sm/gk_tests/';
		my $middle1 = '.gsf -dut sm -soc_model soc --context MEDIA_LPM_SD -T o3c.vpi.sipdfx.gtsynth.default64 -testlib';
		my $end = ' -testlib- -noclean -seed 0x1 | tee log.txt';


		if($val =~ /(CFG)/){
			my($model,$model_extra)= split('_CFG',$val);
			print $fh1 "\n";
			print $fh1 "$val\n";
			print $fh1 "model $model\n";
			print $fh1 "model extra $model_extra\n";
			
			print "output result\n";
			#my $total =  $start.$model."_".$model_extra."/".$model.$middle1." ".$rest.$end."\n";
			my $total =  $start.$val."/".$model.$middle1." ".$rest.$end."\n";
			
			print "$total\n";
			print $fh1 "$_\n";
			print $fh1 "$total";
			
		}
		elsif($val =~ /(#)/){
			print "\n";
			#my($model,$model_extra)= split('#',$val);
			#print "model $model\n";
			#print "model extra $model_extra\n";
			#
			#print "output result\n";
			#my $total = $start.$model."_CFG".$model_extra."/".$model.$middle1." ".$rest.$end."\n";
			#$total =~ s/\t+//;
			#
			#print "$total\n";
			#print $fh1 "$total";
			
		}
		else{
			print "\n";
			#my $model = $val;
			#my $model_extra = "0";
			#print "model $model\n";
			#print "model extra $model_extra\n";
			#
			#print "output result\n";
			#my $total = $start.$model."/".$model.$middle1." ".$rest.$end."\n";
			#print "$total\n";
			#print $fh1 "$total";
			
		}
	}
}
close $fh or die "Unable to close $input: $!";
close $fh1;
print "done\n";
=cut




#replacing the multiple white spaces with single space
=my $data ='    media_gk_pm_flr      -repo_ver 253041		-fid Media_PM_GK/basic/media_gk_pm_flr  -fulsim_opt "-pavpcPavpEnable false -enableFeature :xefiSupport"   -grits_opt "-DpavpEnable=false"  -testlib_opt " -disable_unit_clkgt -flr_memwipe -gsc_fuseoff"				';
print "old data $data\n";
#$data =~ s/ +//;
$data =~ s/\h+/ /g;#this will also work.

#$data =~ s/\t+/ /;
print "new data $data\n";

=Canonicalize horizontal whitespace:

s/\h+/ /g;
Canonicalize vertical whitespace:

s/\v+/\n/g;
Canonicalize all whitespace:

s/[\h\v]+/ /g;
=cut


=cut


=my $res = "GT_ROOT/source/rtl/cfg_env/dut/sm/gk_tests/Dec_PicParameterSet_0_CFG0/Dec_PicParameterSet_0.gsf -dut sm -soc_model soc -context MEDIA_LPM_1VD1VE_SD -target o3c.vpi.sipdfx.gtsynth.goldenrpt.default64/ -testlib -fulsim_opt -qq -pavpcPavpEnable false -enableFeature :xefiSupport qq- -grits_opt -qq -DpavpEnable=false -DvalidationMode=gold qq- -testlib_opt -qq -chkpass -disable_unit_clkgt qq- -testlib- -noclean -seed 0x1 | tee log.txt";
print "required res\n";
print "$res\n";
print "\n";
=cut

#reaplcing the input string with the required changes
=my $old = 'MocsPat_CFG41 -cid GLOBALS/Caches -repo_ver 254606 -grits_opt "-DpavpEnable=false" -fulsim_opt "-pavpcPavpEnable false -enableFeature :xefiSupport" -testlib_opt "-enable_dop_clkgt -enable_unit_clkgt -gsc_disable -gsc_fuseoff" -seed 2215237305';
#my $old = 'gam_single_walker#10     -repo_ver head      -cid GLOBALS/UnifiedMemory    -fulsim_opt "-pavpcPavpEnable false -enableFeature :xefiSupport" -grits_opt "-DpavpEnable=false -DsriovEnable=true"    -testlib_opt "-enable_unit_clkgt -gsc_disable -gsc_fuseoff"';
#my $old = 'gsc_boot_fw_load  -repo_ver head  -fid GSC  -fulsim_opt "-PAVPFuseCsmeModeEnable false  -PAVPFuseKcrSlaveDisable false -PAVPFuseBusValue 7" -grits_opt "-DpavpEnable=true -DgscEnable=true -DgscFwPagingEnable=true"  -testlib_opt "-gsc_enable -enable_pavp_production_mode -fuse_gtdis_en" -enable_pavp';
print "input string\n";
print "$old\n";
$old =~ s/ +/ /;
$old =~ s/-repo_ver[ _0-9]+ -/-/;

my($first,$middle,$middle_a, $rest) = split(' ', $old, 4);
my $val = $first;

$rest =~ s/-fulsim_opt "/-fulsim_opt -qq /;
$rest =~ s/-grits_opt "/-grits_opt -qq /;
$rest =~ s/-testlib_opt "/-testlib_opt -qq /;
$rest =~ s/(?<!%)\"/ qq-/g;
my $start = 'GT_ROOT/source/rtl/cfg_env/dut/sm/gk_tests/';
my $middle1 = '.gsf -dut sm -soc_model soc --context MEDIA_LPM_SD -T o3c.vpi.sipdfx.gtsynth.default64 -testlib';
my $end = ' -testlib- -noclean -seed 0x1 | tee log.txt';


print "val $val\n";
if($val =~ /(CFG)/){
	my($model,$model_extra)= split('_',$val);
	print "***************\n";
	print "model $model\n";
	print "model extra $model_extra\n";


	#print "$old\n";
	print "\n";
	print "output result\n";
	print $start.$model."_".$model_extra."/".$model.$middle1." ".$rest.$end;
}
elsif($val =~ /(#)/){
	my($model,$model_extra)= split('#',$val);
	print "#################";
	print "model $model\n";
	print "model extra $model_extra\n";
	
	print "\n";
	print "output result\n";
	print $start.$model."_CFG".$model_extra."/".$model.$middle1." ".$rest.$end;
}
else{
	#my($model,$model_extra)= split('#',$val);
	my $model = $val;
	my $model_extra = "0";
	print "model $model\n";
	print "model extra $model_extra\n";


	
	print "\n";
	print "output result\n";
	my $total = $start.$model."_CFG".$model_extra."/".$model.$middle1." ".$rest.$end;
	print "$total\n";
}
=cut

#replacing the all occurances of character
=my $s = 'bla""bla';
$s =~ s/(?<!%)\"/./g;
print $s;
=cut

#splitting the string to particular count
=my $old = 'Dec_PicParameterSet_0#0              -grits_opt "-DpavpEnable=false -DvalidationMode=gold"  -testlib_opt "-chkpass  -disable_unit_clkgt"';
my($first,$middle,$middle_a, $rest) = split(' ', $old, 4);
=cut

#replacing the particular string 
=my $x = 'Time to -repo_ver 254606 -cat!';
$x =~ s/-repo_ver[ _0-9]+ -/-/; 
print "$x\n";
=cut

#if -else logic
=my $value_From_input_file = 2;
my $value = $value_From_input_file;
if($value eq 1){ print "the given value is 1";}
elsif ($value eq 2){ print "the given value is 2";}
=cut

#setting the environmental variable
#$ENV{'PATH'} = '/bin:/usr/bin:/home/fred/bin';
#print $ENV{'PATH'};

#writing the outputfile commands in excel sheet
=use Text::Wrap qw{ wrap };
$Text::Wrap::columns=60;
#$Text::Wrap::separator="|";
#print wrap("","","This is a bit of text that forms a normal book-style paragraph");
my $input = "output_file_for_command_generation.txt";
open(my $fh, "<", $input) or die "Unable to open $!";
my $Excel_book1 = Excel::Writer::XLSX->new('new_excel.xlsx' );
my $Excel_sheet1 = $Excel_book1->add_worksheet();
my $count = 0;
while (<$fh>) {
	chomp $_;
	$count++;
	my @parts = split(/\//, $_);
	
	my @data_row = ($parts[7],wrap("","",$_));
	#my @data_row = ($parts[7],$_);
	
	#print "$data_row[1]\n";
	$Excel_sheet1->write( "A$count", \@data_row );
}
print "counted is $count\n";
$Excel_book1->close;
close $fh or die "Unable to close $input: $!";
=cut


#excel data handling
my $Excel_book1 = Excel::Writer::XLSX->new('new_excel.xlsx');
my $Excel_sheet1 = $Excel_book1->add_worksheet();
my @data_row = (1, 2, 3, 4);
my @table_data = (
	["l", "m"],
	["n", "o"],
	["p", "q"],
);
my @data_column = (1, 2, 3, 4, 5, 6, 7);

# Using write() to write values in sheet
$Excel_sheet1->write( "A1", "Geeks For Geeks" );
$Excel_sheet1->write( "A2", "Perl|Reading Files in Excel" );
$Excel_sheet1->write( "A3", \@data_row );
$Excel_sheet1->write( 4, 0, \@table_data );
$Excel_sheet1->write( 1, 4, [ \@data_column ] );
$Excel_book1->close;


#reading the data from xls sheet
=my $parser   = Spreadsheet::ParseExcel->new();
my $workbook = $parser->parse('Copy of node_signals_for_assertions.xls');
 
if ( !defined $workbook ) {
    die $parser->error(), ".\n";
}

my $output = 'excel_output.txt';
open(my $fh1, '>', $output) or die "Could not open file '$output' $!";


for my $worksheet ( $workbook->worksheets() ) {
 
    my ( $row_min, $row_max ) = $worksheet->row_range();
    my ( $col_min, $col_max ) = $worksheet->col_range();
 
    for my $row ( $row_min .. $row_max ) {
        for my $col ( $col_min .. $col_max ) {
 
            my $cell = $worksheet->get_cell( $row, $col );
            next unless $cell;
 
            print "Row, Col    = ($row, $col)\n";
            print "Value       = ", $cell->value(),       "\n";
            print "Unformatted = ", $cell->unformatted(), "\n";
            print "\n";
			print $fh1 $cell->value(),"\n";
        }
    }
}

close $fh1;
=cut

#below code is not working
#reading the data from xls sheet
#use Spreadsheet::Read qw(ReadData);
#my $workbook = ReadData ('new_excel1.xlsx');
=use Spreadsheet::ParseExcel;
use Spreadsheet::Read;
my $workbook = Spreadsheet::Read->new ("new_excel1.xlsx");

#use Spreadsheet::XLSX;
#my $parser   = Spreadsheet::XLSX->new();
#my $workbook = $parser->parse('new_excel1.xlsx');
 
if ( !defined $workbook ) {
    die $parser->error(), ".\n";
}

my $output = 'excel_output.txt';
open(my $fh1, '>', $output) or die "Could not open file '$output' $!";


for my $worksheet ( $workbook->worksheets() ) {
 
    my ( $row_min, $row_max ) = $worksheet->row_range();
    my ( $col_min, $col_max ) = $worksheet->col_range();
 
    for my $row ( $row_min .. $row_max ) {
        for my $col ( $col_min .. $col_max ) {
 
            my $cell = $worksheet->get_cell( $row, $col );
            next unless $cell;
 
            print "Row, Col    = ($row, $col)\n";
            print "Value       = ", $cell->value(),       "\n";
            print "Unformatted = ", $cell->unformatted(), "\n";
            print "\n";
			print $fh1 $cell->value(),"\n";
        }
    }
}

close $fh1;
=cut



#wrapping the text 
=use Text::Wrap;
Text::Wrap::columns = 60;
my $longdna_string = ''adfsfargrhgt at jh  ER TJH  YT REFaestgarhat jjjjjjjjjjjjjjjjjjjjtesfdagfwe g r eh   aejh tar  jh  ywtk  r eagawrewgreg;

my $str_60 =Text::Wrap::fill( '', '', join '', uc($longdna_string) );
print $str_60;


my $longdna_string = <<END;
ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA
END

$longdna_string =~ s/(.{60})/$1\n/gs;

print $longdna_string;




# $Text::Wrap::break   = qr/\s/;
$Text::Wrap::columns = 80;
my $firstline = q();
my $wrapped = wrap(undef, undef, $firstline . $buff);
$wrapped =~ s/\n(.*)$/\n/;
my $lastline = $1;
print $wrapped;
$firstline = $lastline;



$Text::Wrap::columns=20;
#$Text::Wrap::separator="|";
print wrap("","","This is a bit of text that forms a normal book-style paragraph");
=cut



#finding the creation time of a file
=my $input = "output_file_for_command_generation.txt";
open(my $fh, "<", $input) or die "Unable to open $!";

my $epoch_timestamp = (stat($fh))[9];
my $timestamp       = localtime($epoch_timestamp);
print "$timestamp\n";
=cut

#another logic
=use File::stat;
use Time::localtime;
my $timestamp1 = ctime(stat($fh)->mtime);


my $epoch_timestamp = (stat($fh))[9];
my $timestamp1       = localtime($epoch_timestamp);
print "$timestamp1\n";
=cut

#converting the date to epoch value


=my $date = Time::Piece->strptime($timestamp,
  "%a %b %e %H:%M:%S %Y");
my $epoch_date = $date->epoch;

print "$epoch_date\n";
=cut

#finding the latest modified file from the directory
=use Time::Piece;
opendir(my $vars2, $dir) or die "Cannot open directory: $!";
my @allfiles = readdir $vars2;
my $length = @allfiles;
#print "@allfiles\n";
closedir($vars2);

my $latest_epoch = scalar 0;
my $latest_file;
my $modifiedtime;

foreach my $vars4 (@allfiles)
{
	if($vars4 eq "." || $vars4 eq ".." || -d $vars4){ next;}
	if($vars4 =~ /(collage)/){
		my $input = $vars4;
		open(my $fh, "<", $input) or die "Unable to open $!";
		my $epoch_timestamp = (stat($fh))[9];
		my $timestamp = localtime($epoch_timestamp);
		my $date = Time::Piece->strptime($timestamp,"%a %b %e %H:%M:%S %Y");
		my $epoch_date = $date->epoch;
		if ($epoch_date > $latest_epoch) {
			$latest_epoch = $epoch_date;
			$latest_file = $vars4;
			$modifiedtime = $timestamp;
			}
	}
}

print "latest file is $latest_file\n";
print "modified time is $modifiedtime\n";
=cut

#reading the file
=my $input = "input_file_for_command_generation.txt";
open(my $fh, "<", $input) or die "Unable to open $!";

my @alllines = <$fh>;
print $alllines[-1];

if ($alllines[-1] eq 'compared striing') {
	print "both strings are same";
}
else {
	print "\nnot same";
}
=cut

#VDEBOX SV Content sync to AXE and setup of execution



=use strict; 
#use warnings;
use File::Find;
use File::Copy;
use File::Path;
use List::Util 1.33 'any';
use Cwd qw(cwd) ;
use File::Copy::Recursive qw(dircopy);
use Time::Piece;

my @word = ();
my $dir = cwd;

#finding the string from the sentence from the file and writing into new file with the new chnages
my $output = "gfxbuild_cmd.list";
open(my $fh1, '>', $output) or die "Could not open file '$output' $!";
 
my $input = "level0_sd_soc.list";
open(my $fh, "<", $input) or die "Unable to open $!";
 

while (<$fh>) {
    chomp $_;
    if($_ =~ /(--)/){ next;}
    elsif ($_ eq ""){ next;}
    else {
        my $old = $_;
        print "input string\n";
        print "$old\n";

        $old =~ s/ +/ /;
        $old =~ s/\t+//;
        $old =~ s/ +/ /;
        $old =~ s/\t+//;
		$old =~ s/\h+/ /g;

        $old =~ s/-repo_ver[ a-z _0-9a-z]* -/-/;
        $old =~ s/-repo_ver( [0-9]+)//eg; 
		   		
        my($first,$middle,$middle_a, $rest) = split(' ', $old, 4);
        my $val = $first;

        $rest =~ s/-fulsim_opt "/-fulsim_opt -qq/;
        $rest =~ s/-grits_opt "/-grits_opt -qq/;
        $rest =~ s/-testlib_opt "/-testlib_opt -qq/;
        $rest =~ s/(?<!%)\"/ qq-/g;

        my $start = '$GT_ROOT/verif/scripts/gfxbuild_sm $GT_ROOT/source/rtl/cfg_env/dut/sm/gk_tests/';
        my $middle1 = '.gsf -dut sm -soc_model soc -context MEDIA_LPM_SD -T o3c.vpi.sipdfx.gtsynth.default64 -testlib';
        my $end = ' -testlib- -noclean -seed 0x1 | tee log.txt';
 

        if($val =~ /(CFG)/){
            my($model,$model_extra)= split('_',$val);
            print "model $model\n";
            print "model extra $model_extra\n";

            print "output result\n";
            my $total =  $start.$model."_".$model_extra."/".$model.$middle1." ".$rest.$end."\n";
            $total =~ s/ +/ /;
            $total =~ s/\t+//;
            print "$total\n";
            print $fh1 "$total";

        }
        elsif($val =~ /(#)/){
            my($model,$model_extra)= split('#',$val);
            print "model $model\n";
            print "model extra $model_extra\n";

            print "output result\n";
            my $total = $start.$model."_CFG".$model_extra."/".$model.$middle1." ".$rest.$end."\n";
            $total =~ s/\t+//;
            $total =~ s/ +/ /;
            $total =~ s/\t+//;
            print "$total\n";
            print $fh1 "$total";

        }
        else{
            my $model = $val;
            my $model_extra = "0";
            print "model $model\n";
            print "model extra $model_extra\n";

            print "output result\n";
            my $total = $start.$model."/".$model.$middle1." ".$rest.$end."\n";
            $total =~ s/ +/ /;
            $total =~ s/\t+//;
            print "$total\n";
            print $fh1 "$total";

        }
    }
}
close $fh or die "Unable to close $input: $!";
close $fh1;
print "done\n";
=cut

#finding the version number from xml file 31-01-2023
=my $filename = "data.xml";
print "filename $filename\n";
open(FH, '<', $filename) or die "Sorry!! couldn't open";
my @word = ();
my $lines = 0;
my $version = 0;
while(<FH>){   
	$lines = $lines+1;
	last if ($lines >= 10);
	
	if ($_ =~ /<version>/)
	{
		print "line number $lines\n";
		@word = split />/, $_;
		@word = split /</,$word[1];
		$version = $word[0];
	
	}
}

close(FH);
print "version is $version\n";
=cut

#extracting the testlib option values from input data
=my $line = '$GT_ROOT/verif/scripts/gfxbuild_sm $GT_ROOT/source/rtl/cfg_env/dut/sm/gk_tests/Dec_PicParameterSet_0_CFG0/Dec_PicParameterSet_0.gsf -dut sm -soc_model soc -context MEDIA_LPM_SD -T o3c.vpi.sipdfx.gtsynth.default64 -testlib -fulsim_opt -qq -pavpcPavpEnable false -enableFeature :xefiSupport qq- -grits_opt -qq -DpavpEnable=false qq- -testlib_opt -qq -chkpass -disable_unit_clkgt qq- -testlib- -noclean -seed 0x1 qq- | tee log.txt';

my @word = split /-testlib_opt /, $line;
print "$word[1]\n";
@word = split /qq- /, $word[1];
print "$word[0]\n";
=cut
#$word[0] =~ s/-qq //;
#my $final_output = "-testlib_opt ".$word[0]."\"";
#print "$final_output\n";


#reading all files in current directory
#my $dir = cwd;
=opendir(DIR, $dir) or die "can't open $dir: $!";
my @allfiles = readdir DIR;
closedir DIR;
print @allfiles;

#deleting the files with .rb extension inside fodlers
foreach my $vars (@allfiles)
{
	if($vars eq "." || $vars eq ".." || -f $vars){ next;}
	unlink glob "$vars/*.rb";
}
=cut

#copying the required data from eon file to other file
=my $filename1 = "abc.txt";
my $filename2 = 'xyz.txt';
print "input filename $filename1\n";
print "output filename $filename2\n";

open(FH, '<', $filename1) or die "Sorry!! couldn't open";
open(my $fh, '>', $filename2) or die "Could not open file '$filename2' $!";

while(<FH>){   
	if ($_ =~ /gt_tb.v/)
	{
	print $_;
	}
	elsif ($_ =~ /media_tile_wrapper.v/){
		print $_;
	}
	else {
	print $fh "$_";
	}
}

close(FH);
close $fh;
=cut

#dictionary in perl
=my %data = ('John Paul' => 45, 'Lisa' => 30, 'Kumar' => "abcd");

print "$data{'John Paul'}\n";
print "$data{'Lisa'}\n";
print "$data{'Kumar'}\n";
=cut
#counting the particular character in line
=my $str = "a:b:c:d:e#f:g";
my $count = ($str =~ tr/#//);
print $count, "\n";
=cut
#copying the lines which having # in the lines.
=my $filename1 = "X:\\site\\disks\\mtl_pipesm_aravind_av_regress\\aravind\\vfcat_with_fix\\mtl_cf_fix\\sm\\MTL_2VD1VE_SD.o3c.vpi.nodfx.gtsynth.default64\\INTERACTIVE\\GuCVFCatFaults_CFG0\\GuCVFCatFaults.gsf";
my $dir_name = dirname($filename1);
print "dir_name $dir_name";

my $file_name = basename($filename1);
print "basname $file_name";

#my $filename2 = $dir_name."\\"."comments_for_".$file_name;
my $filename2 = "xyz.txt";
print "input filename $filename1\n";
print "output filename $filename2\n";

open(FH, '<', $filename1) or die "Sorry!! couldn't open";
open(my $fh, '>', $filename2) or die "Could not open file '$filename2' $!";

while(<FH>){
	if ($_ =~ /#/){
		my $count = ($_ =~ tr/#//);
		if ($count eq 1){
			my @word = split /#/, $_;
			print $fh "#"."$word[1]\n";
		}
		else {
			#if ($_ =~ /^#/){
				print $fh "$_";
			#}
		}
	}
}
close(FH);
close $fh;
=cut

=if ($_ =~ /00e038a618/ and $_ =~ /10009000/){	
$_ =~ s/-qq //;
=cut


#code to find broken links in linux
=system( "ls -l");
system("find . -xtype l");
1;
#code to find broken links and delete them.
#system("find . -xtype l -delete);
=cut

#file size in perl script
=my $filename = $ARGV[0];
if(@ARGV == 0)
{
print "Please pass the name of file as an argument to check its size\n";
exit;
}
my $filesize = -s $filename;
if ($filesize == 0)
{
print "File Size Is Zero";
}
else
{
print "Size of the file $ARGV[0] is ".$filesize/1024 ." Bytes\n";
print "Size of the file $ARGV[0] is ".$filesize/1024 ." KB\n";
}
=cut



use 5.010; 
use File::Find; 
my $total; 
#my $dir = cwd;
find(sub { $total += -s if -f;}, $dir); 
$total = $total/1024;
$total = $total/1024;
say $total;