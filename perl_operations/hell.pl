#!/usr/intel/bin/perl
use strict ; 
use warnings ;
print "hello\n";
use File::Basename;
use File::Path qw( make_path );

#printing the current working directory
=use Cwd qw(cwd) ;
my $dir = cwd;
print "$dir\n";
print "$dir"."/abcd\n";
=cut

=use File::Basename ;
my $dirname = dirname(__FILE__);
print "$dirname\n";
=cut

#https://perldoc.perl.org/Cwd
#https://stackoverflow.com/questions/40506465/find-files-in-the-folder-and-subfolder
#pritnig the files and folders in the directory



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


#https://www.geeksforgeeks.org/perl-finding-files-and-directories/

#https://www.educba.com/perl-copy-file/

#https://stackoverflow.com/questions/206320/how-do-i-distinguish-a-file-from-a-directory-in-perl


=use File::Copy;
sub copyfile
{

	my $source = "$_[0]";
	my $destination = "$_[1]";
	print "copyfile source $source\n";
	print "copyfile destination $destination\n";

	opendir(my $vars2, $source) || die "folder might not present $!";
	my @vars3 = readdir($vars2);
	foreach my $vars4 (@vars3)
	{
		if($vars4 eq "." || $vars4 eq ".."){ next;}
		elsif(-f "$source/$vars4" ) 
		{
			print "name is $source/$vars4\n";	
			(my $name,my $dir,my $ext) = fileparse($vars4,'\..*');
			if ($ext eq ".rb.gz") 
			{
				if ( !-d $destination ) 
				{
					make_path $destination or die "Failed to create path: $destination";
				}
				copy "$source/$vars4", "$destination";
			}
		}
}
closedir($vars2);
}

use File::Copy;
sub findfile 
{
	my $source = "$_[0]";
	my $destination = "$_[1]";
	print "source $source\n";
	print "destination $destination\n";
	opendir(my $vars2, $source) || die "folder might not present $!";
	my @vars3 = readdir($vars2);
	foreach my $vars4 (@vars3)
	{
		print "file/folder $source/$vars4\n";
		if($vars4 eq "." || $vars4 eq ".."){ next;}#skips the current and parent directories while copying
		elsif (-d "$source/$vars4") 
		{
			print "folder $source/$vars4\n";
			copyfile(("$source/$vars4","$destination/$vars4"))
		}
	}
	closedir($vars2);
}

use Cwd qw(cwd) ;
my $dir = cwd;
findfile(("$dir/ashish_source","$dir/ashish_destination"));
=cut

=use Cwd qw(cwd) ;
my $dir = cwd;

print "current directory $dir\n";
my $destination ="$dir"."/abcd"; 
print "$destination\n";
#code to create the folder
=print "creating the abcd folder\n";
if ( !-d $destination ) 
				{
					make_path $destination or die "Failed to create path: $destination";
					print "created the folder $destination\n";
				}
print "goinig with next step\n";
=cut
#code to delete the folder and along its subfolders
=use File::Path;
if ( -d $destination ) 
				{
					#rmdir $destination or die "Failed to delete folder: $destination"; it will delete only leaf/last folder
					rmtree $destination or die "Failed to delete folder: $destination";#it will delete fodler and its subfolders/contents
					print "deleted the folder $destination\n";
				}
print "goinig with next step\n";
=cut
=cut

=print scalar localtime();
print "\n";
print "sleep started\n";  
# calling the sleep function
sleep(5);

print "sleep completed\n";
print scalar localtime();
=cut