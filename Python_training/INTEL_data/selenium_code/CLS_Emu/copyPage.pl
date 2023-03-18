
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
$year += 1900;
$mon += 1;

#backupDG2
my $filename = "CLS_A0_indicators_" . $mon . "_" . $mday . "_" . $year;
print "$filename\n";

print("copy /y CLS_AXE_A0_indicators.html .\\backup\\$filename.html\n");
system("copy /y CLS_AXE_A0_indicators.html .\\backup\\$filename.html\n");
