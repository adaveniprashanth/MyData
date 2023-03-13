#!/usr/intel/bin/perl
use strict ; 
use warnings ;

#code to find broken links in linux
#system( "ls -l");
#print "hello\n";
system("find . -xtype l");
1;