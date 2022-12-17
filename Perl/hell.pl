#!/usr/intel/bin/perl
use strict ; 
use warnings ;
print "hello";


#printing the current working directory
use Cwd qw(cwd) ;
my $dir = cwd;
print "$dir\n";
print "$dir"."/abcd\n";


=use File::Basename ;
my $dirname = dirname(__FILE__);
print "$dirname\n";
=cut

#https://perldoc.perl.org/Cwd
#https://stackoverflow.com/questions/40506465/find-files-in-the-folder-and-subfolder
#pritnig the files and folders in the directory

=use File::Spec ;

my $rel_path = 'sample1.txt';
my $abs_path = File::Spec->rel2abs( $rel_path ) ;
print "$abs_path\n";
=cut

=use File::Find ;
sub process_file {
    next if (($_ eq '.') || ($_ eq '..'));
    if (-d && $_ eq 'fp'){
        $File::Find::prune = 1;
        return;
    }
    print "Directory: $_\n" if -d;
    print "File: $_\n" if -f;
    #Do search replace operations on file below
}
find(\&process_file, $dir);
=cut


=print "===========";

sub routine
{
#print "$_\n";
print "@_\n";
}

my $html = "hello";
routine($html);

print "===========";
=cut


=use File::Spec;
my $rel_path = 'sample4.txt';
my $abs_path = File::Spec->rel2abs( $rel_path );

print "$abs_path\n"
=cut


#https://www.geeksforgeeks.org/perl-finding-files-and-directories/

#use File::Find;
=find(
{
	wanted => \&findfiles,
},
'dummy'
);
=cut

=sub findfiles
{

	#To search only the directory
	#print "$File::Find::dir\n";
	#To search the files inside the directories
	if (-f) {
		
		print "$File::Find::name\n";
	
	}
}
use Cwd qw(cwd) ;
my $dir = cwd;
find(\&findfiles, $dir);
=cut

#https://www.educba.com/perl-copy-file/

use File::Copy;
sub findfile
{
print "print all params passed to routine @_\n";
my $source = "$_[0]";
my $destination = "$_[1]";
opendir(my $vars2, $source) || die "folder might not present $!";
my @vars3 = readdir($vars2);
foreach my $vars4 (@vars3)
{
if(-f "$source/$vars4" ) {
	copy "$source/$vars4", "$destination";
}elsif($vars4 eq "." || $vars4 eq ".."){ next;}
elsif (-d "$source/$vars4" ) {
	findfile("$source/$vars4","$destination")
}
}
closedir($vars2);
}

#findfile(("$dir/dummy",$dir));


my $source = $dir;
opendir(my $vars2, $source) || die "User not able to open $!";
my @vars3 = readdir($vars2);
foreach my $vars4 (@vars3)
{
if (-f "$vars4") {
	print "file $vars4\n";
	}
elsif($vars4 eq "." || $vars4 eq ".."){ next;}#skips the current and parent directories while copying
elsif (-d "$vars4") {
	print "folder $vars4\n";
	findfile(("$vars4",$dir))
}
}
closedir($vars2);



#https://stackoverflow.com/questions/206320/how-do-i-distinguish-a-file-from-a-directory-in-perl
=sub wanted {
     if (-d) { 
         print $File::Find::name." is a directory\n";
     }
}

find(\&wanted, $dirname);
=cut


=use File::Copy;
my @files = glob("$PATH1/*.txt");

for my $file (@files) {
    copy($file, $ENV{DIRWORK}) or die "Copy failed: $!";
}
=cut
