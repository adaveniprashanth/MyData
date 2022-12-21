#!/usr/intel/bin/perl
use strict ; 
use warnings ;
print "hello\n";


use Cwd qw(cwd) ;
my $dir = cwd;
print "$dir\n";
=my $directory = "$dir"."/INTERACTIVE";
#print "$directory\n";
my $decpic = "$directory"."/Dec_PicParameterSet_0_CFG0";
my $filename = "$decpic"."/runsim.log.gz";

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
use File::Copy::Recursive qw(dircopy);
dircopy($bin,"$val_dir/smedia_top/val/gfxbuild/verif/validation/bin/") or die("$!\n");
dircopy($lib,"$val_dir/smedia_top/val/gfxbuild/verif/validation/bin/") or die("$!\n");
=cut

#$val_dir/smedia_top/val/gfxbuild/verif/validation/bin/ <-- new files

#/nfs/site/disks/lnl_soc_regress_001/ashish/soc_package/LNL_IPX_UPLOAD/RTL1p0_pre/xe2lpm_media_common-22ww14.4e-package/smedia_top/val/gfxbuild/verif/validation/bin/ <--old files 

my $old_files_path = $dir;
opendir(my $vars, $old_files_path) or die "Cannot open directory: $!";
my @oldfiles = readdir $vars;
closedir $vars;
print "@oldfiles\n";

my $new_files_path = $dir;
opendir(my $vars2, $new_files_path) or die "Cannot open directory: $!";
my @newfiles = readdir $vars2;
closedir $vars2;
print "@newfiles\n";

my @misseditems = ();

use List::Util 1.33 'any';
foreach my $vars4 (@oldfiles)
{
	my $match_found = any { /$vars4/ } @newfiles;
	if($match_found ne 1) {
		push(@misseditems, $vars4);
	}
	print "$vars4 $match_found\n";
}

print "missed from old files are @misseditems\n";

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