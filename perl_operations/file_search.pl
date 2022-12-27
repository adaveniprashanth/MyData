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
my $directory = "$dir"."/INTERACTIVE";
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