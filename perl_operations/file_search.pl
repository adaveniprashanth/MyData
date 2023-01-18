#!/usr/intel/bin/perl
use strict ; 
use warnings ;
#print "hello\n";
use File::Basename;
use File::Path qw( make_path );
use List::Util 1.33 'any';
use File::Copy;
use autodie;
#use Text::Trim qw(trim);

use Cwd qw(cwd) ;
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


#finding the string from the sentence from the file and writing into new file with the new chnages
=my $output = 'output_file_for_command_generation.txt';
open(my $fh1, '>', $output) or die "Could not open file '$output' $!";

my $input = "input_file_for_command_generation.txt";
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
			my($model,$model_extra)= split('_',$val);
			print "model $model\n";
			print "model extra $model_extra\n";
			
			print "output result\n";
			my $total =  $start.$model."_".$model_extra."/".$model.$middle1." ".$rest.$end."\n";
			
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
			print "$total\n";
			print $fh1 "$total";
			
		}
	}
}
close $fh or die "Unable to close $input: $!";
close $fh1;
print "done\n";
=cut









#replacing the multiple white spaces with single space
=my $data = "What    is the STA++TUS of your mind right now?";

$data =~ s/ +/ /;		

print $data;
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
$ENV{'PATH'} = '/bin:/usr/bin:/home/fred/bin';
print $ENV{'PATH'};

my $val = 0;
print ~$val;