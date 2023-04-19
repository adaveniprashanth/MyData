#!/usr/intel/bin/perl
use strict; 
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
my $iteration = 1;
my $gfxbuild_run_sw = 1;
my $gk_gfxcmd_sw =0;
my $content_excel_sw = 1;

my $regress_run_path = "/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/elg/BMG_X2_1p0_pre/regress";

my $snapshot_model = "/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/elg/BMGX2_23WW14_SOC_RTL1p0_pre";

my $current_package_path = "/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/elg/BMG_X2_1p0_pre/IPX_upload/BMGX2_media_common_23ww15d-package";

my $SOC_drop_name = "BMG_X2_1p0_pre";

my $gk_input_tests = "/nfs/site/disks/lnl_soc_disk_001/ashish/soc_package/elg/BMG_X2_1p0_pre/gk_test.list";

eval { mkpath("$regress_run_path/gfxbuild_run"); 1 }   or die "Can't create gfxbuild_run directory: $@\n";

my $gfxbuild_run_path = "$regress_run_path/gfxbuild_run";


# GFX build run log
my $gfxbuild_run_log = "$gfxbuild_run_path/log_gfxbuild.txt";
open my $gfxrun_log, '>', $gfxbuild_run_log or die $!;

print "model path $snapshot_model\n";
print $gfxrun_log "model path $snapshot_model\n";

print "current_package_path path $current_package_path\n";
print $gfxrun_log "current_package_path path $current_package_path\n";

print "gfxbuild run dir  = $gfxbuild_run_path\n";
print $gfxrun_log "gfxbuild run dir  = $gfxbuild_run_path\n";

print "SOC_drop_name  = $SOC_drop_name\n";
print $gfxrun_log "SOC_drop_name  = $SOC_drop_name\n";


my @items = split('/', $snapshot_model);
my $snapshot_model_name = pop(@items); # snamshot model name
my $gt_model = '/nfs/site/disks/xe2_soc_disk_002/xe2_gt_23ww12p3_X2_2x2_GM_soc_0p7'
#code for target & context
my $directory = "$gt_model/bld/gt";
my $incomplete_folder = 'X2_SD';
opendir(my $vars2, $directory) || die "folder might not present $!";
my @vars3 = readdir($vars2);
 
my $media_path;
foreach my $vars4 (@vars3)
{
  my $match_found = "$vars4" =~ /^$incomplete_folder/;
  if ($match_found eq 1){$media_path = $vars4;}
}
 
my @items = split('\.', $media_path,2);
my $context = $items[0];
my $target = $items[-1];
 

##### GK test to gfxbuild cmd ###
if ($gk_gfxcmd_sw eq 1)
	{
		my $output = "$gfxbuild_run_path/gfxbuild_cmd.list";
		open(my $fh1, '>', $output) or die "Could not open file '$output' $!";
		 
		my $gk_input = "$gk_input_tests";   ####provide input gk testlist file 

		open(my $fh, "<", $gk_input) or die "Unable to open $!";
		 
		while (<$fh>) {
			chomp $_;
			if($_ =~ /(--)/){ next;}
			elsif ($_ eq ""){ next;}
			elsif($_ eq "backup_code") {
				my $old = $_;
				print "input string\n";
				print "$old\n";

				$old =~ s/\h+/ /g;
				$old =~ s/ +/ /;
				$old =~ s/\t+//;
				$old =~ s/ +/ /;
				$old =~ s/\t+//;

				$old =~ s/-repo_ver[ a-z _0-9a-z]* -/-/;
				$old =~ s/-repo_ver( [0-9]+)//eg; 
						
				my($first,$middle,$middle_a, $rest) = split(' ', $old, 4);
				my $val = $first;

				$rest =~ s/-fulsim_opt "/-fulsim_opt -qq /;
				$rest =~ s/-grits_opt "/-grits_opt -qq /;
				$rest =~ s/-testlib_opt "/-testlib_opt -qq /;
				$rest =~ s/(?<!%)\"/ qq-/g;

				my $start = '$GT_ROOT/verif/scripts/gfxbuild_sm $GT_ROOT/source/rtl/cfg_env/dut/sm/gk_tests/';
				my $middle1 = '.gsf -dut sm -soc_model soc -context MEDIA_LPM_SD -T o3c.vpi.sipdfx.gtsynth.goldenrpt.default64 -testlib';
				my $end = ' -testlib- -noclean -seed 0x1 | tee log.txt';
		 

				if($val =~ /(CFG)/){
					my($model,$model_extra)= split('_CFG',$val);
					print "model $model\n";
					print "model extra $model_extra\n";

					print "output result\n";
          ##my $total =  $start.$model."_".$model_extra."/".$model.$middle1." ".$rest.$end."\n";
          my $total =  $start.$val."/".$model.$middle1." ".$rest.$end."\n";
          
					$total =~ s/ +/ /;
					$total =~ s/\t+//;
					$total =~ s/\h+/ /g;

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
					$total =~ s/\h+/ /g;

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
					$total =~ s/\h+/ /g;

					print $fh1 "$total";

				}
			}
			else {
				my $start = '$GT_ROOT/verif/scripts/gfxbuild_gt $SM_ROOT/';
        my $middle1 = '.gsf -soc_model gt_standalone -context '.$context.' -target '.$target.' -testlib -grits_opt -qq -wa l3GlobalInvalidationBeforeSaveToFile -wa l3GlobalInvalidationBeforeMemoryPoll qq- -testlib_opt -qq -nojitval -trkset=soc -chkpass -enable_dop_clkgt -enable_unit_clkgt -disable_gt_moat -disable_jem qq- -testlib- -testlib';
        my $end = ' -testlib- -seed 0x1 | tee log.txt';
		my $pavp_end = ' -testlib- -enable_pavp -seed 0x1 | tee log.txt';
		
        my $old = $_;
        #print "input string\n";
        #print "$old\n";

        $old =~ s/ +/ /;
        $old =~ s/\t+//;
        $old =~ s/ +/ /;
        $old =~ s/\t+//;
		$old =~ s/\h+/ /g;

        $old =~ s/-repo_ver[ a-z _0-9a-z]* -/-/;
        $old =~ s/-repo_ver( [0-9]+)//eg; 
		   		
        my($first,$middle,$middle_a, $rest) = split(' ', $old, 4);
        my $val = $first;

        $rest =~ s/-fulsim_opt "/-fulsim_opt -qq /;
        $rest =~ s/-grits_opt "/-grits_opt -qq /;
        $rest =~ s/-testlib_opt "/-testlib_opt -qq /;
        $rest =~ s/(?<!%)\"/ qq-/g;

        
 
		my $total = '';
        if($val =~ /(CFG)/){
            my($model,$model_extra)= split('_CFG',$val);
            print "val $val\n";
			print "start $start\n";
			print "model $model\n";
            print "model extra $model_extra\n";
			print "rest $rest\n";

            print "output result\n";
			if ($rest =~/(-enable_pavp)/){
				my ($new_rest,$remain) = split(' -enable_pavp',$rest);
				$total =  $start.$val."/".$model.$middle1." ".$new_rest.$pavp_end."\n";
			}
			else{
				$total =  $start.$val."/".$model.$middle1." ".$rest.$end."\n";
			}
            $total =~ s/ +/ /;
            $total =~ s/\t+//;
            print "$total\n";
            print $fh1 "$total";

        }elsif($val =~ /(#)/){
            my($model,$model_extra)= split('#',$val);
            print "model $model\n";
            print "model extra $model_extra\n";

            print "output result\n";
			
			if ($rest =~/(-enable_pavp)/){
				my ($new_rest,$remain) = split(' -enable_pavp',$rest);
				$total = $start.$model."_CFG".$model_extra."/".$model.$middle1." ".$new_rest.$pavp_end."\n";
			}
			else{
				$total = $start.$model."_CFG".$model_extra."/".$model.$middle1." ".$rest.$end."\n";
			}
			
            #my $total = $start.$model."_CFG".$model_extra."/".$model.$middle1." ".$rest.$end."\n";
            $total =~ s/\t+//;
            $total =~ s/ +/ /;
            $total =~ s/\t+//;
            print "$total\n";
            print $fh1 "$total";

        }else{
            my $model = $val;
            my $model_extra = "0";
            print "model $model\n";
            print "model extra $model_extra\n";

            print "output result\n";
			if ($rest =~/(-enable_pavp)/){
				my ($new_rest,$remain) = split(' -enable_pavp',$rest);
				$total = $start.$model."/".$model.$middle1." ".$new_rest.$pavp_end."\n";
			}
			else{
				$total = $start.$model."/".$model.$middle1." ".$rest.$end."\n";
			}
            #my $total = $start.$model."/".$model.$middle1." ".$rest.$end."\n";
            $total =~ s/ +/ /;
            $total =~ s/\t+//;
            print "$total\n";
            print $fh1 "$total";
        }
			
			}
		}

		close $fh or die "Unable to close $gk_input: $!";
		close $fh1;
		print "GK to Gfxbuild cmd is done\n";
		print  $gfxrun_log "GK to Gfxbuild_cmd.list has creatred successfully\n";
	}

 #### GFXBUILD RUN  ###

mkdir ("$gfxbuild_run_path/PRECOMP_TESTS");
mkdir ("$gfxbuild_run_path/PRECOMP_RUN");


if ($gfxbuild_run_sw eq 1)
  {
        my $testlist_filename = "$gfxbuild_run_path/testlist.list";
    open(my $fh, '>', $testlist_filename) or die "Could not open file '$testlist_filename' $!";

    #opendir (DIR, "$gfxbuild_run_path/PRECOMP_TESTS") or die "Could not open directory "."$gfxbuild_run_path/PRECOMP_TESTS";
    open FILE_IN, "$gfxbuild_run_path/gfxbuild_cmd.list" or die "Could not open file "."$gfxbuild_run_path/gfxbuild_cmd.list";

		print  $gfxrun_log "gfxbuild run START\n";
    print "gfxbuild run START\n";

    while (<FILE_IN>)
    {
      my $result = -1;
      my $line = $_;
      chomp ($line);
      my $working_dir = system ("pwd");
      print "Creating a new test directory\n";
      #system ("mkdir test_$iteration");
      mkdir ("$gfxbuild_run_path/PRECOMP_TESTS/test_$iteration");
      #system ("cd test_$iteration");
      chdir ("$gfxbuild_run_path/PRECOMP_TESTS/test_$iteration");
      $working_dir = system ("pwd");
      print "Running script on test_$iteration\n";
      $result = system ($line);

      my $gfxtests_log = "$gfxbuild_run_path/PRECOMP_TESTS/test_$iteration/log.txt";
      open FILE_IN1, $gfxtests_log or die "Could not open file $gfxbuild_run_path/PRECOMP_TESTS/test_$iteration/log.txt ";
      while (<FILE_IN1>)
      {
	      chomp;  
	      if ($_ =~ m/GFXBUILD - SUCCESS/) 
	        {
	            print  $gfxrun_log "gfxbuild run for test_$iteration completed\n";
              print  "gfxbuild run for test_$iteration completed\n";
          }
      }
      #code to get testlib opt in testlist file.
      my @word = split /-testlib_opt -qq/, $line;
      #print "$word[1]\n";
      @word = split /qq- /,$word[1];
      #print "$word[0]\n";
      my $final_output = $word[0];
      print "test_$iteration -testlib_opt\"$final_output\" \n";

      print $fh "test_$iteration -testlib opt \"$final_output\" \n";

      #sleep(60);
      #system ("cd ..");
      chdir ("$gfxbuild_run_path/PRECOMP_TESTS");
      $iteration = $iteration + 1;
      
    }
    print "gfxbuild run is Done with all the tests\n";
    print $gfxrun_log "gfxbuild run is Done with all the tests\n";
    close $fh;
    
  }
    else {
      print "gfxbuild run skipped\n";
      print $gfxrun_log "gfxbuild run skipped\n";
    }


   ##### Content EXcel ####
if ($content_excel_sw eq "dummy")
{
  use List::Util 1.33 'any';
  use Cwd qw(cwd) ;
  use File::Copy::Recursive qw(dircopy);
  use Time::Piece;
  my @word = ();
  my $dir = cwd;
  use Excel::Writer::XLSX;
  
	my $input = "$gfxbuild_run_path/gfxbuild_cmd.list";
	open(my $fh, "<", $input) or die "Unable to open $!";
	my $Excel_book1 = Excel::Writer::XLSX->new("$current_package_path/smedia_top/val/Media_BMG_x2_1p0_pre_test_content_delivery.xlsx");
	my $Excel_sheet1 = $Excel_book1->add_worksheet();
	my $count = 1;
	my $format = $Excel_book1->add_format(); # Add a format
	$format->set_bold();
	$format->set_color('Black');
	$format->set_align('center');
	$format->set_bg_color('green');

	while (<$fh>) {
		chomp $_;
		$count++;
		my @parts = split(/\//, $_);
		my @data_row = (($count-1),$parts[10],$_);
		#print "$data_row[1]\n";
		$Excel_sheet1->write( "A1", "Test ID", $format );
		$Excel_sheet1->write( "B1", "Test Name", $format ); 
		$Excel_sheet1->write( "C1", "Gfxbuild Command", $format );     
		$Excel_sheet1->write( "A$count", \@data_row );
	}
	print "total tests are $count\n";
	$Excel_book1->close;
	close $fh or die "Unable to close $input: $!";
	print "Content Excel has created successfully \n";
	print $gfxrun_log "Content Excel has created successfully \n";

}
if ($content_excel_sw eq 1)
{
  use List::Util 1.33 'any';
  use Cwd qw(cwd) ;
  use File::Copy::Recursive qw(dircopy);
  use Time::Piece;
  my @word = ();
  my $dir = cwd;
  use Excel::Writer::XLSX;
  
  	#my $input = "commands.txt";
	my $input = "$gfxbuild_run_path/gfxbuild_cmd.list";
	open(my $fh, "<", $input) or die "Unable to open $!";
	my $Excel_book1 = Excel::Writer::XLSX->new("$current_package_path/smedia_top/val/Media_BMG_x2_1p0_pre_test_content_delivery.xlsx");
	#my $Excel_book1 = Excel::Writer::XLSX->new("content_delivery.xlsx");
	my $Excel_sheet1 = $Excel_book1->add_worksheet('Content_Opts_Status');
	my $Excel_sheet2 = $Excel_book1->add_worksheet('Content_Info');
	my @headings = ("Test ID","Test Name","Status on SM","Status on GM","Gfxbuild Command");
	my @sheet2headings = ("Category","Sub feature","TestName","SM status","GM status","Fuse Override","Comments");
	my $format = $Excel_book1->add_format(border=>1); # Add a format
	my $borderformat = $Excel_book1->add_format(border=>1);
	$format->set_bg_color('#C9D08C');
	#setting the columns format
	$Excel_sheet1->set_column('A:A',10,$borderformat);
	$Excel_sheet1->set_column('B:B',30,$borderformat);
	$Excel_sheet1->set_column('C:D',15,$format);
	$Excel_sheet1->set_column('E:E',30,$borderformat);
	#$Excel_sheet1->set_border('A:A',60);
	
	my $headformat = $Excel_book1->add_format(border=>1);
	$headformat->set_bold();
	$headformat->set_color('Black');
	#$format->set_align('center');
	$headformat->set_bg_color('#BDEEEE');
	$Excel_sheet1->write( "A1", \@headings, $headformat );
	$Excel_sheet2->set_column('A:A',10,$borderformat);
	$Excel_sheet2->set_column('B:B',30,$borderformat);
	$Excel_sheet2->set_column('C:D',15,$borderformat);
	$Excel_sheet2->set_column('E:G',30,$borderformat);
	$Excel_sheet2->write( "A1", \@sheet2headings, $headformat );
	
	my $count = 1;

	while (<$fh>) {
		chomp $_;
		$count++;
		my @parts = split(/\//, $_);
		print "parts $parts[4]\n";
		my ($a,$b)=split('-testlib- ',$_,2);
		my @data_row = ($count-1,$parts[4],"","",$b);
		
     
		$Excel_sheet1->write( "A$count", \@data_row);
		$Excel_sheet2->write( "C$count", $data_row[1]);
	}
	print "total tests are $count\n";
	$Excel_book1->close;
	close $fh or die "Unable to close $input: $!";
	print "Content Excel has created successfully \n";
	#print $gfxrun_log "Content Excel has created successfully \n";

}
 close  $gfxrun_log;
