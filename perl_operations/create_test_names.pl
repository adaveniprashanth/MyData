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

#finding the string from the sentence from the file and writing into new file with the new chnages
my $output = "commands.txt";
open(my $fh1, '>', $output) or die "Could not open file '$output' $!";
 
my $input = "gk_test.list";
open(my $fh, "<", $input) or die "Unable to open $!";
my $context = 'X2_SD';
my $target = 'goldenrpt.red2slc.red2ssm.gm.default64';
while (<$fh>) {
    chomp $_;
    if($_ =~ /(--)/){ next;}
    elsif ($_ eq ""){ next;}
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
close $fh or die "Unable to close $input: $!";
close $fh1;
print "done\n";

=elsif($val =~ /(#)/){
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
=end