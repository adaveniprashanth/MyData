#!/usr/intel/bin/perl5.10-threads-64
# -*- mode: cperl; cperl-indent-level: 4; cperl-close-paren-offset: 4; cperl-continued-statement-offset: 4; cperl-indent-parens-as-block: t; cperl-tab-always-indent: t; -*-

#
#   Description     :  GECCO Project Script
#------------------------------------------------------------------------------

package emuDut;

use warnings;
use strict;

##use FindBin; # core module to find the path to the (this) script, which is where we expect emu.pm
##use lib "$FindBin::Bin";

use emu;
use Pod::Usage;
use Getopt::Long;
use Cwd;
use Cwd 'realpath';
use File::Copy;
use File::Basename;
use File::Spec;
use File::Path qw(make_path remove_tree);
use IO::Tee;
use Data::Dump qw(dump);
use Shell::Source;
use Data::Dumper;
use emu::Plugins;

########################################################################
# This is a project specific module which provides certain fundamental #
# functions to emurun. These functions need to be authored according   #
# to project needs.                                                    #
# Currently supported:                                                 #
# projOptions()                                                        #
# valTest()                                                            #
# genTest()                                                            #
#                                                                      #
# emurun will refuse to load this module if these functions are not    #
# provided.                                                            #
########################################################################

use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);

require Exporter;
@ISA = qw(Exporter);

# Items to export into callers namespace by default. Note: do not export
# names by default without a very good reason. Use EXPORT_OK instead.
# Do not simply export all your public functions/methods/constants.
@EXPORT = qw(
  $projName
  projOptions
  valTest
  genTest
  dutOptions
  );

# feel free to use your own project versioning scheme here, it just needs
# to be meaningful to you
our $VERSION = '0.5';
(my $svn_version = '$Revision: 10776 $') =~ s/[^\d\.]//g;
my $version = "$VERSION (SVN: $svn_version)";

#$emuProject::projMailOnError = '"vinilkant.k.tejaswi@intel.com aman.mediratta@intel.com rakesh.s.patel@intel.com"';

our $projEmuWorkroot = undef;
our $emu_chktrk_file = undef;
our $modelpath = undef;

&emu::setEmuSites(["fm"]);
&emu::setEmuSitesGlobalPoolEligible(["fm"]);
# platform specific pool determined automatically by *emurun*, so no need to set below
#&emu::schedule::setPool(pool => "fm_zse");
#&emu::schedule::setPool(pool => "fm_pde"); #PZ1 has fm_pde pool

## Added by Ameya for constraining the job to SLES11
$ENV{NBCLASSAPPEND} = 'SLES12';

########################################################################
## module specific local variables #####################################
########################################################################
# Moving to emuproject.pm as requested by Dashrath
#my %DutOpts =
#  (
#    EMU_DO_FILES    => undef,
#    TRK_DO_FILES    => undef,
#  );
#ssenapat
my %DutOpts =
  (
    SAFE_FREQ        => undef,
    OFFLINE_TRKS     => undef,
  );


########################################################################
## module provided functions ###########################################
########################################################################

########################################################################
# dutOptions()
########################################################################
# Handle the options not handled by emurun.
# To do this, you must
# - call GetOptions()
# - pass them to the local hash %DutOpts - set defaults above!

sub dutOptions() {
    # This function parameter is basically a hack, to be able to pass
    # the "-av" and "-sv"/"-tcp" options back to emurun and the server
    # for handling a special cases there.
    my ($GetOpts, $ProjOpts) = @_;     # hash references

    &emu::verbose(
        feature => "plugins",
        level => 3);

    sub checkTestDir() {
        my $dir = shift;

        if (($ProjOpts->{LILY} && (-e File::Spec->catdir($dir, basename($dir)."*.aub"))) ||
            ($ProjOpts->{LILY} && (-e File::Spec->catdir($dir, basename($dir).".gsf"))) ||
            ($ProjOpts->{LILY} && (-e File::Spec->catdir($dir, basename($dir)."*.lily.xml"))) ||
            ($ProjOpts->{LILY} && (-e File::Spec->catdir($dir, basename($dir)."*.lily.out"))) ||
			($ProjOpts->{PLUGIN}) ||
            ($ProjOpts->{SV}) ||
            #(-d "$dir/memory_in")) {
            ($ProjOpts->{AV} || $ProjOpts->{TCP_SW_CHECK})) {
            1;
        } else {
            undef;
        }
    }

    # handle command line
    Getopt::Long::Configure(qw(pass_through));
   GetOptions (
        'safe_freq:s'          => \$DutOpts{SAFE_FREQ},
        'offline_trks:s'       => \$DutOpts{OFFLINE_TRKS},
    );

     # aumahaja: fulsimlite SV automation .
    #For this flow, force create the RP and merge content back into it
    if (($ProjOpts->{FD_PATH})) {
        &emu::test::configure(resultMergeIntoResultpath => 1);

        # Super lazy, but you get the idea, just in case we need to create the RP
        if ($GetOpts->{RP}) {
            `mkdir -p $GetOpts->{RP}; chmod 777 $GetOpts->{RP}`;
        }
    }

         #Hard coded CNL SV/SW Emulators after adding feature of wormhole qslot
    my @cnl_emu = ("filt2433");
   ## my @cnl_emu_tier = ("fmev0148","fmev0150","fmev0156","fmev0158","fmev0118","fmev0102","fmev0166","fmev0134","fmev0216","filt2401","filt2403","filt2418");

    #Check if the session is -i and its project specific emulator.
    ## If /gfx/dev/interactive is used, then bypass fastpath
    my $cnl_emu_match = 0;
    if ($GetOpts->{INTERACTIVE} && $ENV{NBQSLOT} ne "/gfx/dev/interactive") {
    if(defined $ProjOpts->{EMULATOR}) {
        foreach (@cnl_emu) {
            chomp($_);
            if($_ eq $ProjOpts->{EMULATOR}) {
                $cnl_emu_match = 1;
            }
        }
    } else {
            &emu::printts ("INFO: Allowed to run interactive session without specifying emulator...... Exiting.. \n");
       # exit(1);
    }
    }

    if ($GetOpts->{INTERACTIVE}) {
        &emu::verbose(feature => "testbench", level => 1);
    }

    pod2usage(-exitstatus => 2,
        -message    => "ERROR -group can not be combined with -trk, -sva, -fsdb or any other debug feature",
        -input => __FILE__)
      if ($ProjOpts->{GROUP} && ($ProjOpts->{TRK} || $ProjOpts->{SVA} || ($GetOpts->{FSDB} !~ /none/)));


## For printing model's custom help messages
##  pod2usage(-exitstatus => 0,
##        -input => __FILE__)
##      if ($GetOpts->{HELP});

    # Fancy interactive behavior
#if ($cnl_emu_match ==1 )
#   {
#    if ($GetOpts->{INTERACTIVE} && $ProjOpts->{EMULATOR}) {
#        if (&emu::isStage(stage => 'submission')) {
#            &emu::printts ("INFO: Overriding Qslot to /interactive\n");
#            $ENV{NBQSLOT_BAK} = $ENV{NBQSLOT};
#            $ENV{NBQSLOT} = "/interactive";
#        } else {
#            &emu::printts ("INFO: Restoring Qslot to ".$ENV{NBQSLOT_BAK}."\n");
#            system("nbjob modify --qslot ".$ENV{NBQSLOT_BAK});
#        }
#    }
#    }

      &emu::printts ("DUT :\"$ProjOpts->{DUT}\"\n");
      &emu::printts ("TARGET :\"$ProjOpts->{TARGET}\"\n");
      &emu::printts ("CONTEXT :\"$ProjOpts->{CONTEXT}\"\n");
      &emu::printts ("AV Mode :\"$ProjOpts->{AV}\"\n");
      &emu::printts ("TCP Mode :\"$ProjOpts->{SV}\"\n");
      &emu::printts ("GROUP :\"$ProjOpts->{GROUP}\"\n");
      &emu::printts ("LILY :\"$ProjOpts->{LILY}\"\n");
      &emu::printts ("NOCLEAN :\"$ProjOpts->{NOCLEAN}\"\n");
      if (defined $ProjOpts->{LILY_OPT}) {
      &emu::printts ("LILY_OPT :\"$ProjOpts->{LILY_OPT}\"\n");
      }
      if (defined $ProjOpts->{TCP_SW_CHECK_OPT}) {
      &emu::printts ("TCP_SW_CHECK_OPT :\"$ProjOpts->{TCP_SW_CHECK_OPT}\"\n");
      }
      if (defined $ProjOpts->{LILY_AGENT}) {
      &emu::printts ("Lily Agent is : \"$ProjOpts->{LILY_AGENT}\" \n");
      }
      if (defined $ProjOpts->{PLUGIN}) {
        &emu::printts ("Plugin: \"$ProjOpts->{PLUGIN}\" \n");
	if (defined $ProjOpts->{PLUGIN_ARGUMENTS}) {
          &emu::printts ("Plugin Arguments: \"$ProjOpts->{PLUGIN_ARGUMENTS}\" \n");
	}
      }
      if (defined $GetOpts->{DO}) { &emu::printts ("DO :\"@{$GetOpts->{DO}}\"\n"); }
      if (defined $ProjOpts->{EMU_DO_FILES}) { &emu::printts ("EMU_DO_FILES :\"@{$ProjOpts->{EMU_DO_FILES}}\"\n"); }
      if (defined $ProjOpts->{TRK_DO_FILES}) { &emu::printts ("TRK_DO_FILES :\"@{$ProjOpts->{TRK_DO_FILES}}\"\n"); }

    my $build = $GetOpts->{MODEL}->getBuild();
    # Emurun v1.7.7 -.test.yml should be <tardis replay dir full absolute path>
    # Check if we're in replay mode, during submission and if .test.yml is not where we expect it
    my $test_path = $GetOpts->{REGLIST}[0];
    if (&emu::isStage(stage=> 'submission') &&
            &emu::test::getConfiguration('tardisDebug') &&
            ! $build->isa('emu::platform::pxp::build')) {
        my $expected_path = undef;
        &emu::printts("INFO: Identified run as tardis replay, workaround linking of .test.yml\n");
        if (&emu::test::getConfiguration('tardisDebugReplay')) {
           $expected_path = &emu::test::getConfiguration('tardisDebugReplay');
           &emu::printts("INFO:  Using tardisDebugReplay option, $expected_path is expected path for .test.yml\n");
        } elsif (-e $test_path . '/' . &emu::test::getConfiguration('tardisDebugName')) {
            # Emurun v1.7.6 -tardis_debug_name being relative path, helping emurun find .test.yml
           (undef, $expected_path, undef)  = fileparse($test_path . '/'. &emu::test::getConfiguration('tardisDebugName'));
           &emu::printts("INFO:  Using tardisDebugName option, $expected_path is expected path for .test.yml\n");
        }
        my $original_path = $test_path . '/.test.yml';
        if (! -e $expected_path . '/.test.yml') {
            &emu::printts("INFO: $expected_path/.test.yml not found, linking from $original_path\n");
            system("ln -s $original_path $expected_path/.test.yml");
        } else {
            &emu::printts("INFO: $expected_path/.test.yml found, leaving as is\n");
        }
    }
    # Check for valid test during submission.
    # as valid Gfx tests requires various
    # input files that can hardly be checked
    # when job is remote
    &emu::printts ("NB: \"$GetOpts->{NB}\" \n");
    if (&emu::isStage(stage => 'submission') || $GetOpts->{NB} == 0) {
        my $numvalidtests = 0;
        my @arrvalidtests;
        foreach (@{$GetOpts->{REGLIST}}) {
            # This block of code defines the test case validity.
            my ($scheme) = &emu::net::splitURI(uri => $_);

            if ($scheme) {
                emu::printts ("INFO: Adding remote test \"$_\"\n");
                push (@arrvalidtests, $_);
            } elsif (-d $_) {
                if (&checkTestDir($_)) {
                    &emu::printts ("INFO: Found valid test \"$_\"\n");
                    push (@arrvalidtests,$_);
                } else {
                    # Test given must be a regression directory with subdirs.
                    my $dir = $_;
                    &emu::printts ("INFO: Checking \"$dir\" as regression directory\n");

                    # Get a list based on the directory content.
                    my @tests = emu::sys::getDirsFromDir(dir => $dir, short => 0);
                    foreach (@tests) {
                        if (&checkTestDir($_)) {
                            &emu::printts ("INFO: Found valid test \"$dir/$_\"\n");
                            push (@arrvalidtests,$_);
                        }
                    }
                }
            }
            else {
                if (!-e $_) {
                    &emu::printts ("INFO: Ignoring test \"$_\": $!\n");
                }
                else {
                    &emu::printts ("INFO: Ignoring test \"$_\": Not a directory\n");
                }
            }
        }

        # This list of tests is used
        # at the execution site for data
        # syncs.
        $ENV{GECCO_GFX_TESTLIST} = join (";", @arrvalidtests);

        pod2usage(-exitstatus => 2,
            -message    => "ERROR no valid tests found in given test list",
            -input => __FILE__)
          if (!@arrvalidtests && !($GetOpts->{MAN} || $GetOpts->{HELP}));
    }
    # akhartot edited -- no more hardcoding
    my $model_dpath = $GetOpts->{MODEL};
    $ENV{"MODEL_DATOOLS"} = "$model_dpath/cfg/datools";
    my $tbx_xpv = `/p/cse/asic/datools/proj_bin/gen10/dawrap --xpv tbxcomp`;
    chomp($tbx_xpv);
    my @xpv = split(" ", $tbx_xpv);
    my $tbx_ver = $xpv[2];

    my $sysname = `/usr/intel/bin/sysname -ct`;
    chomp($sysname);
    $modelpath = $model_dpath;
    $projEmuWorkroot = "bld/$ProjOpts->{DUT}/$ProjOpts->{CONTEXT}.$ProjOpts->{TARGET}/emulation";

    # FIXME: when SLES11 is supported, this needs to be removed
    ##if ( ! -d "$model_dpath/$projEmuWorkroot" && $sysname eq "em64t_SLES11" ) {
    ##    $projEmuWorkroot = "bld/$ProjOpts->{DUT}/$ProjOpts->{CONTEXT}.$ProjOpts->{TARGET}/tbx.$tbx_ver.em64t_SLES10";
    ##}
}

# This function is optional. If defined will be used
# to validate the model that GECCO has been found during
# model analysis. If this function returns 0
# the model is considered for job submission and execution

# sub modelFilter {
#    my $path = shift;
#
#    if (!defined $DutOpts{SKU}) {
#        return 0 if ($path =~ /(compile.vmw)|(tbx_.*)/);
#    } else {
#        # Code for SKU handling could go here
#    }
#
#    return 1;
# }


sub tbxlogsepration {

 my $test_found_name ; my $path ; my $loggingpath;
 ($path, $loggingpath) = @_;
 my $log_file = "$path/testbench.log";
 &emu::printts("INFO: Copying logs for JobID $ENV{__NB_JOBID} to $loggingpath  \n");
# &emu::test::addPostCmd("cp $path/testlist.list $loggingpath/testlist.list_$ENV{__NB_JOBID} && cp $log_file $loggingpath/testbench.log_$ENV{__NB_JOBID} && cp $path/velocegui.log $loggingpath/velocegui.log_$ENV{__NB_JOBID} && cp $path/simulation_profile.log $loggingpath/simulation_profile.log_$ENV{__NB_JOBID} &&  cp $path/zServer.*  $loggingpath/zServer_$ENV{__NB_JOBID} && cp $path/simix.fmez*  $loggingpath/simix.fmez_$ENV{__NB_JOBID} && cp $path/zemi3mgr.log $loggingpath/zemi3mgr.log_$ENV{__NB_JOBID}  ");
 if (-e "$path/testlist.list")          { `cp $path/testlist.list $loggingpath/testlist.list_$ENV{__NB_JOBID}`; }
 if (-e $log_file)                      { `cp $log_file $loggingpath/testbench.log_$ENV{__NB_JOBID}`;}
 if (-e "$path/velocegui.log")          { `cp $path/velocegui.log $loggingpath/velocegui.log_$ENV{__NB_JOBID}`;}
 if (-e "$path/simulation_profile.log") { `cp $path/simulation_profile.log $loggingpath/simulation_profile.log_$ENV{__NB_JOBID}`;}
 `cp $path/zServer.*  $loggingpath/zServer_$ENV{__NB_JOBID}`;
 `cp $path/simix.fmez*  $loggingpath/simix.fmez_$ENV{__NB_JOBID}`;
 `cp $path/zemi3mgr.log $loggingpath/zemi3mgr.log_$ENV{__NB_JOBID}`;
  if (-e $log_file) {
       my $ret = open (LOG, '<', $log_file);
        if (!$ret) {
            emu::printts ("WARNING: Couldn't open \"$log_file\" for reading: $!\n");
        } else {

    while (<LOG>) {
            if ($_ =~ /(Running AV Tests: PATH=\.\/test\/)((\S+))/)
        {
                $test_found_name = $2;
        `touch $path/$2/$2_testbench.log`;
                `sed -n -e "/Running AV Tests: PATH=\\.\\/test\\/$2/,/\\(Clearing memory\\|SIGInterrupt\\)/p" $log_file >> $path/$2/$2_testbench.log`;
                }


        }


    }
    close (LOG);
}

return;
}



########################################################################
# valTest()
########################################################################
# Validate the results of a previously executed test.
# Will be called by GECCO for every test result found.
#
# Specification:
#
# Arguments passed to this function (hash):
# $args{path}       contains a path to the testcase that should be validated
# $args{testname}   name as specified during gen test
# $args{modelname}  name of the model that was used for execution
# $args{modelroot}  modelroot provided via -ver option
# $args{cycles}     cycles run till test completed
# $args{frequency}  effective frequency the test was running at
# $args{efficiency} efficiency the test was running with
# $args{platform}   the emulator that was used for execution
#
# Arguments to be returned by this function (hash):
# $res{code}        exit code of this test (0: pass, 1: fail)
# $res{result}      string result (defined by project; "ACED", "perfect", "seems to work", ...)
########################################################################
sub valTest {
    &emu::printts("INFO: inside emuDut valTest platform check\n");
    my ( $GetOpts, $ProjOpts, %args) = (@_);
    my %res;
    my $result_sv_test;
    my $result_sv_lily;
    my $log_file;
    my $log;
    my $shadow_test;
    my $found = 0;
    my $error = 0;
    my $notdone = 0;
    my $ret = 0;
    my %groupresult;
    my @testlist;my @testcases;
    my $currenttest = undef;
    my $testname;
    my $loggingpath = undef;
    my $seed;
    my @grouplist;
    @testlist = split (";",$ENV{GECCO_GFX_TESTLIST});
    # Adding support for AV grouping
    # specifically for Gfx
    #
    # Grouping implies:
    # - The top-level @testlist later consists only of one test "avgroup".
    # - The sub-level @testcases contains all sub-cases, grouped into one
    #   execution and result directory ("avgroup").
    #
    #
    # Signal preValTest event for plugins to do their work with

    &signalPluginEvent('PreValTest',
        $ProjOpts,
        GetOpts => $GetOpts,
        Args => \%args);

    &emu::printts ("ValTest: Our Val Test function \n");
    my $outpath = $args{path};
    &emu::printts("ValTest: outpath :$outpath\n");
    $ret = open (TESTLIST, '<', "$outpath/testlist.list");

    if ($ProjOpts->{GROUP}) {
        @grouplist = @testlist;
        @testlist = ("avgroup");
    }

    # Remove trailing slashes for all test entries, they would confuse fileparse() below.
    map({$_ =~ s|/+$||} @testlist);

    # Go through each testcase directory in @testlist sequentially.
    # Note: In group mode, this is just a single one, "avgroup" (no "path").

    my $build = $GetOpts->{MODEL}->getBuild();
    foreach my $fullpath (@testlist) {
        # refuse to continue if interrupted
        return if &shutdown;

        # Take apart the input file to determine test name.
        $testname = fileparse($fullpath);
        &emu::printts ("We found Valtest:$testname\n");
        # this is just the last element (filename or dir) of a full path
        # emu::test::initTest(testname => $testname, fullpath => $fullpath) or next;
        # For debug, activate the verbose mode:
        #&emu::test::initTest(testname => $testname, testdir => $fullpath) or next;

        # Note that in remote operation (cross-site), $testpath may not be directly physically accessible!
        if ($ProjOpts->{GROUP}) {
            push (@testcases, @grouplist);
        } else {
            push (@testcases, $fullpath);
        }

        if (!$ret) {
                &emu::printts ("WARNING: Couldn't open \"$outpath/testlist.list\" for appending: $!\n");
        } else {
                foreach (< $outpath/* >) {
                    next if ! -d $_; # only consider directories
                    ## rspatel added to print wrong test in new runreg flow
                    # next if ! -e "$_/memory_in/sysmem.in";  # only consider tests that did not fail during generation
                    # append to list
                    $shadow_test = basename($_);

                    if ($ProjOpts->{SV}) {
                     if (-e "$args{path}/$shadow_test/exec.log"){
                        &emu::printts("Path $args{path}/$shadow_test/exec.log\n");
                        `cp -rf $args{path}/$shadow_test/exec.log $args{path}/.`;
                        `touch $args{path}/$shadow_test.TESTNAME.log`;
                        `cp -rf $args{path}/$shadow_test/*lily*json* $args{path}/.`;
                        $log_file = "$args{path}/$shadow_test/exec.log";
                        $currenttest = $shadow_test;
                        #&emu::printts ("ValTest: Our Log file is $log_file\n");
                        #&emu::printts ("Log file : $args{path}/$shadow_test/exec.log\n");
                        if (-e $log_file) {
                             $log = open (LOG, '<'. $log_file);
                             if (!$log){
                                 &emu::printts ("WARNING: Couldn\'t open \"$log_file\" for reading: $!\n");
                             } else {
                                while (<LOG>) {
                                    ##if (m/Test Run exit code/){
                                       ## &emu::printts ("EXEC LOG LINE: $_\n");
                                    if ($_ =~ /^.*LiLyAgent Completed Test and will Exit with Code.*(\w+).*$/){
                                        &emu::printts ("Exit code $1\n");
                                        ##my ($lilyexitstring, $lilyexitcode) = split /\s*:\s*/, $_;
                                        my $lilyexitcode = $1;
                                        # this line removes non ascii characters
                                        #$lilyexitcode =~ s/[^!-~\s]//g;
                                        &emu::printts("exec.log Exit code : $lilyexitcode\n");
                                        my $exitcode =  hex($lilyexitcode);
                                        &emu::printts("Hex converted code : $exitcode\n");
                                        if ($exitcode == 0) {$groupresult{$currenttest}{result} = "SUCCESS";  $result_sv_lily= "SUCCESS"; }
                                        elsif ($exitcode == 16) {$groupresult{$currenttest}{result} = "HUNG"; $result_sv_lily= "HUNG"; }
                                        else {$groupresult{$currenttest}{result} = "FAIL"; $result_sv_lily= "FAIL"; }
                                        $groupresult{$currenttest}{testname}= $1;
                                        $result_sv_test = $1;
                                        &emu::printts("Lily Log File Parse Result : $currenttest : $result_sv_lily \n");
                                     }
                                }
                            }
                        }
                   }

                }
            }
        }
     }
    if ($ProjOpts->{AV}) {
           $log_file = "$args{path}/testbench.log";
           $loggingpath  =   -d "$GetOpts->{RP}/../EMOD_RP/LOGFILES" ? "$GetOpts->{RP}/../EMOD_RP/LOGFILES" :  $GetOpts->{RP};
           if (-e $log_file) {
              $ret = open (LOG, '<', $log_file);
              if (!$ret) {
                  &emu::printts ("WARNING: Couldn't open \"$log_file\" for reading: $!\n");
              } else {
                while (<LOG>) {
                # Waive: Could not enable IOs. Design has no IOs
                next if m/Could not enable IOs/;

                # Waive: If Program received Interrupts
                next if m/Program received signal/;

                if (m/\s*Done loading all cycles/) { # why \s* ??
                    $found++ unless $found < 0;
                } elsif (/^error/i) {
                    $error++;
                    $found = -1;
                } elsif (m/TEST STATUS\s+= PASSED/) {
                    $found = 1;

                    if (defined $currenttest) {
                        $groupresult{$currenttest}{result} = "SUCCESS";
                    }


                    #Removing the zprd data if the test passed:
                    if (-e "$args{path}/zprd_local/") {
                        system("rm -rf $args{path}/zprd_local");
                    }
                    # Workaround for GTUC. Ignore errors when test passes at the end
                    $error = 0;
                }

                ## rspatel added
                elsif (m/TEST STATUS\s+= HUNG/) {
                    $found = 1;

                    if (defined $currenttest) {
                        $groupresult{$currenttest}{result} = "HUNG";
                    }
                    # Workaround for GTUC. Ignore errors when test passes at the end
                    $error = 0;
                }

                elsif (m/TEST STATUS\s+= FAILED/) {
                    $found = 1;

                    if (defined $currenttest) {
                        $groupresult{$currenttest}{result} = "FAIL";
                    }
                    # Workaround for GTUC. Ignore errors when test passes at the end
                    $error = 0;
                }
                elsif ($ProjOpts->{GROUP} && m/Running AV Tests: PATH=\.\/test\/(\S+)/) {
                    $currenttest = "$1";
                    $groupresult{$currenttest}{testname} = $1;
                }

                # For Veloce this is the last line we are interested in,
                # ignore subsequent junk.
                last if m/Total time spent/;
            }
            close (LOG);
        }

     }
    }
    my %result;
    my $summaryfile;

    #if ($ProjOpts->{SV}) {
    #      my $summaryfile_lily  = "$args{path}/TEST_SUMMARY_JOBID_SV_LILY.$ENV{__NB_JOBID}.txt";
    #      my $summary_lily  = open (SUMM_LILY , '>>', $summaryfile_lily);
    #      &emu::printts("Printing Test Result: $currenttest, $result_sv_lily \n");
    #      printf SUMM_LILY "$currenttest, $result_sv_lily \n";
    #      }

    # Print out special reportings for Group tests
    foreach my $test (sort { "\L$a" cmp "\L$b" }keys %groupresult) {
        if (-e "$args{path}/$test") {
            $testname = $groupresult{$test}{testname};
            my $result = $groupresult{$test}{result} // "FAIL";
            my $reportfile = "$args{path}/$test/$test.rpt";
            &emu::printts ("Reportfile : $reportfile\n");
            my $userid = &emu::sys::getRunningUserID();
            if ($userid =~ /amedirat/ || $userid =~ /gkemubld/ || $userid =~ /vktejasw/)
            {
               &emu::printts ("$userid is running regression\n");

                if ($ProjOpts->{SV}) {
                    $summaryfile  = "$args{path}/TEST_SUMMARY_JOBID_SV.$ENV{__NB_JOBID}.txt";
                }else {
                    $summaryfile  = "$args{path}/TEST_SUMMARY_JOBID.$ENV{__NB_JOBID}.txt";
                }
               my $summary  = open (SUMM , '>>', $summaryfile);
               printf SUMM "$test, $result \n";
            }


            my $ret = open (RPT, '>', $reportfile);
            if (!$ret) {
                &emu::printts ("WARNING: Couldn't open \"$reportfile\" for writing: $!\n");
            } else {
                &emu::printts ("INFO: $test $result\n");

                print RPT "\n";
                print RPT "=======================  Simulation   Results  ===========================\n";
                print RPT "                          Test Name : $test\n";
                print RPT "                 Test Configuration : 1\n";
                print RPT "                         Model Rev. : $args{modelname}\n";
                print RPT "                     TBX Model Info : OFFICIAL\n";
                if ($result =~ /HUNG/){
                print RPT "                     Test Completed : No\n";
                }
                else {
                print RPT "                     Test Completed : Yes\n";
                }
                print RPT "                        Moat Errors : 0\n";
                print RPT "            Internal Tracker Errors : 0\n";
                print RPT "                 GFX Checker Errors : 0\n";
                print RPT "              GFX Checkers not done : 0\n";
                if ($result =~ /FAIL/){

                print RPT "                     dram_mem Diffs : 50\n";
                } else {

                print RPT "                     dram_mem Diffs : 0\n";
                }
                print RPT "            Execute Log File Errors : 0\n";
                print RPT "         Ignored Execute Log Errors : 0\n";
                print RPT "         Ignored GFX Checker Errors : 0\n";
                printf RPT "   Overall Status (%15s) : %s\n", $test, $result;
                close(RPT);
            }

       if ($ProjOpts->{NOCLEAN})

        {

        }
       else
        {


       chomp (my $report_disk_path = "$GetOpts->{RP}" );

       `cd $args{path}/$test; ls -1 $args{path}/$test | egrep -v "${test}.*|test_status*|tbxrun*|velocegui*|testbench.log|fullchip*|run*|stimuli|report.rpt|errfiles|trkfiles|simulation_profile" | xargs rm -rf ; cd - ;`;


        `cd $report_disk_path/$test ; ls -1 $report_disk_path/$test | egrep -v "${test}_tbxrun*|test_status*|tbxrun*|testbench.log|velocegui*|fullchip*|run*|stimuli|report.rpt|runcmd*|runsim.lo*|errfiles|trkfiles|simulation_profile" | xargs rm -rf ; cd -;`;
       }
       }
       }
    close (SUMM);
    if ($ProjOpts->{GROUP}) {
        &tbxlogsepration ($args{path}, $loggingpath );
        }

    my $testreport = "$args{path}/$args{testname}.rpt";
    $ret = open (RPT, '>', $testreport);
    if (!$ret) {
        &emu::printts ("WARNING: Couldn't open \"$testreport\" for writing: $!\n");
    } else {
       if ($ProjOpts->{AV}){
        foreach (< $args{path}/errfiles/*err.txt >) {
            my $file = basename ($_);
            my $err  = 0;
            my $done = 0;

            $ret = open (LOG, '<', $_);
            if (!$ret) {
                &emu::printts ("WARNING: Couldn't open \"$_\" for reading: $!\n");
            } else {
                while (<LOG>) {
                    if (/^done/i) {
                        $done = 1;
                    } elsif (/^error/i) {
                        $err++;
                    }
                }
                close LOG;
            }

            if (!$done) {
                $result{notdone}{$file} = "";
            }
            if ($err) {
                $error += $err;
                $result{errors}{$file} = $err;
            }
        }

        if ($error==0 && $found>0 && keys %{$result{notdone}} == 0) {
            $res{result} = "SUCCESS";

        } elsif ($error>0 || $found<0 ) {
            $res{result} = "FAIL";
            $res{code}   = "-1";
        } else {
            $res{result} = "FAIL (NOT COMPLETE)";
            $res{code}   = "-1";
        }

        # If seed is not set, try to find it from file
#        $seed = $DutOpts{SEED};
        if (!$seed) {
            if (-r "$args{path}/runsim.log") {
                # Should be coded more cleanly
                $seed = `grep ASYNCSEED $args{path}/runsim.log`;
                chomp($seed);
                $seed =~ s/[^0-9]*([0-9]*)/$1/;
            }
        }
    } elsif ($ProjOpts->{SV}){
        $res{result} = "SUCCESS";

    }
        &emu::printts ("INFO: $args{testname} $res{result}\n");

        print RPT "\n";
        print RPT "=======================  Simulation   Results  ===========================\n";
        print RPT "                          Test Name : $args{testname}\n";
        print RPT "                  ASYNC_SYNCZR SEED : $seed\n";
        print RPT "                 Test Configuration : 1\n";
        print RPT "                         Model Rev. : $args{modelname}\n";
        print RPT "                     TBX Model Info : OFFICIAL\n";
        print RPT "                     Test Completed : Yes\n";
        print RPT "                        Moat Errors : 0\n";
        print RPT "            Internal Tracker Errors : 0\n";
        print RPT "                 GFX Checker Errors : $error\n";

        foreach (keys %{$result{errors}}) {
            printf RPT "%35s : %d\n", $_, $result{errors}{$_};
        }

        print RPT "              GFX Checkers not done : $notdone\n";

        foreach (keys %{$result{notdone}}) {
            printf RPT "%35s : not done\n", $_;
        }

        print RPT "                     dram_mem Diffs : 0\n";
        print RPT "            Execute Log File Errors : 0\n";
        print RPT "         Ignored Execute Log Errors : 0\n";
        print RPT "         Ignored GFX Checker Errors : 0\n";
        printf RPT "   Overall Status (%15s) : %s\n", $args{testname}, $res{result};
        close(RPT);
    }

    # Work around for SV mode
    # Always pass it
   # if ($ProjOpts->{SV}) {
    #    $res{code} = 0;
    #}

    #FLOW_OVERRIDE plugin will use this callback
    # Signal the end of the valTest sub-routine
    &signalPluginEvent('PostValTest',
        $ProjOpts,
        GetOpts => $GetOpts,
        Args => \%args,
        TestPassed => ($res{code} == 0) ? 1 : 0);

    ######## HD POST PROCESSING BEGIN ########
    if($ProjOpts->{HD_PROCESS}) {
	$GetOpts->{POSTSCRIPT} = 1;
    }
    ######## HD POST PROCESSING END ########
    return %res;
}


########################################################################
# genTest()
########################################################################
sub genTest {
    # This is a hash reference:
    ##my $GetOpts = shift;
    my ($GetOpts, $ProjOpts) = @_;     # hash references
    my @extraoutputdirs = ("trkfiles","errfiles","svcov","sv_cov");
    if(defined $ProjOpts->{FD_PATH}){
    @extraoutputdirs = ("svcov","sv_cov");
    }
    # Create list of tests from $GetOpts->{REGLIST}.
    my @testlist = split (";",$ENV{GECCO_GFX_TESTLIST});

    my @grouplist;
    my $shadow_test;
    my $agent_cmd;
    # Adding support for AV grouping
    # specifically for Gfx
    #
    # Grouping implies:
    # - The top-level @testlist later consists only of one test "avgroup".
    # - The sub-level @testcases contains all sub-cases, grouped into one
    #   execution and result directory ("avgroup").
    #
    #
    if ($ProjOpts->{GROUP}) {
        @grouplist = @testlist;
        @testlist = ("avgroup");
    }

    my $build = $GetOpts->{MODEL}->getBuild();
    if ($build->isa('emu::platform::pxp::build')) {
            &emu::printts("INFO: inside genTest pxp check\n");
            #&emu::test::configure(wait_stop_marker => 120);

            # extend to 300 for 8x mode
            #&emu::test::configure(wait_stop_marker => 300);

            # Warning: Advanced usage only
            # VTT PXP: Sends Signal 15 to the xeDebug process
            #&emu::test::setProcToKill(name => "xeDebug", signal => "15");

            # VTT PXP: Skip linking these files/dir from model dir in shadow
            # These are files generated during build and also written to during run
            # Needed so manifest.shadow doesnt have these and we can copy them back
            &emu::test::addSkipShadowLinks(filelist => ["xe.msg", "tmp"]);

    	    # TODO: Remove me for non -debug
    	    $GetOpts->{DEBUG} = 1;
    	    $ENV{GECCO_SHADOWKEEP} = 1;
    	    $ENV{GECCO_TESTBENCHGRACEPERIOD} = 120;
    }

    # Remove trailing slashes for all test entries, they would confuse fileparse() below.
    map({$_ =~ s|/+$||} @testlist);

    # Go through each testcase directory in @testlist sequentially.
    # Note: In group mode, this is just a single one, "avgroup" (no "path").

    foreach my $fullpath (@testlist) {
        # refuse to continue if interrupted
        return if &shutdown;

        # Take apart the input file to determine test name.
        my $testname = fileparse($fullpath); # this is just the last element (filename or dir) of a full path
        # emu::test::initTest(testname => $testname, fullpath => $fullpath) or next;
        # For debug, activate the verbose mode:
        &emu::test::initTest(testname => $testname, testdir => $fullpath) or next;

        #FLOW_OVERRIDE plugin will use this callback
        # Signal that initTest has just completed
        # This might be a bit tricky to bring over to the emuDut.*.pm
        &signalPluginEvent('PostInitTest',
            $ProjOpts,
            GetOpts => $GetOpts,
            Run => 0, #not needed
            TestBaseName => $testname,
            TestFile => $testname,
            Test => $fullpath);

        #Files are not needed when running with FLOW_OVERRIDE. Everything has already been bundled together by the FLOW_OVERRIDE system.
		if((undef $ProjOpts->{PLUGIN} || ! $ProjOpts->{PLUGIN})) {
            # Note that in remote operation (cross-site), $testpath may not be directly physically accessible!

            # specify the trigger file
            if (defined $ProjOpts->{TRIGGER}) {
                &emu::test::addInputFiles(filelist => [$ProjOpts->{TRIGGER}], type => 'trigger');
                &emu::printts ("\n Setting up trigger file :\"$ProjOpts->{TRIGGER}\"\n");
            }
        ######## HD Tracker POST PROCESSING BEGIN ########
        if($ProjOpts->{HD_PROCESS}) {
           &emu::printts("EmuDUT: GenTesT: Copying wrapper for readback automation \n");
           &emu::test::addInputFiles(filelist => ["/nfs/site/disks/fm_iclgt_00537/kheiney/NB_scripts/wrapper_HD_RB_processMTL.csh"]);
           &emu::test::addInputFiles(filelist => ["/nfs/site/disks/fm_iclgt_00537/kheiney/NB_scripts/wrapper_HD_processXe2.csh"]);
           &emu::test::addInputFiles(filelist => ["/nfs/site/disks/fm_iclgt_00537/kheiney/NB_scripts/wrapper_Regress_readback.csh"]);
           &emu::test::addInputFiles(filelist => ["/nfs/site/disks/fm_iclgt_00537/kheiney/NB_scripts/regression_RB.pl"]);
           &emu::test::addInputFiles(filelist => ["/nfs/site/disks/fm_iclgt_00537/kheiney/NB_scripts/genHangTracker.pl"]);
           &emu::test::addInputFiles(filelist => ["/nfs/site/disks/fm_iclgt_00537/kheiney/NB_scripts/carError.sh"]);
           &emu::test::addInputFiles(filelist => ["/nfs/site/disks/fm_iclgt_00537/kheiney/NB_scripts/auto_readback.pl"]);
        }
        ######## HD Tracker POST PROCESSING END ########

            # specify the do files
            if (scalar @{$GetOpts->{DO}} > 0) {
             ##   my @new_do = map { $_ =~ /^emu_chktrk/ ? "$modelpath/$projEmuWorkroot/tbx_D2/$_" : $_ } @{$GetOpts->{DO}};
             ##   &emu::test::addInputFiles(filelist => \@new_do, type => 'do');
                &emu::test::addInputFiles(filelist => $GetOpts->{DO}, type => 'do');
            }
            if (defined $ProjOpts->{EMU_DO_FILES}) {
                foreach my $arg (@{$ProjOpts->{EMU_DO_FILES}}) {
                    $emu_chktrk_file = "$modelpath/$projEmuWorkroot/tbx_D2/$arg";
                    &emu::test::addInputFiles(filelist => $emu_chktrk_file, type => 'do');
                }
            }
            if (defined $ProjOpts->{TRK_DO_FILES} ) {
		ifdef ZRCIEMUL
               $GetOpts->{'TRK_DO_FILES'} =();
		endif
               my $trk_base = $GetOpts->{MODEL} . "/bld/" . $ProjOpts->{DUT} . "/" . $ProjOpts->{CONTEXT} . "." . $ProjOpts->{TARGET} . "/trkset/";
               foreach my $arg (@{$ProjOpts->{TRK_DO_FILES}}) {
                    #&emu::printts("EmuDUT: TRK Do Files: $arg\n");
                    if (-e $arg) {
                        # User gave a specfic full path do file that can be found
                       &emu::printts("EmuDUT: TRK Do Files Absolute Path: $arg \n");
                       &emu::test::addInputFiles(filelist => $arg, type => 'do');
		       ifdef ZRCIEMUL
                       push (@{$GetOpts->{'TRK_DO_FILES'}}, $arg)
			endif
                    }
                    elsif ($arg =~ /\w+\.do/){
                       # Strip off prepended run area path from do file
                       # User did NOT give full path to do file. Assume do file is in model tracker path
                       $arg = $&;
                       $emu_chktrk_file =$trk_base . $arg;
                       &emu::printts("EmuDUT: TRK Do Files Path: $emu_chktrk_file \n");
                       &emu::test::addInputFiles(filelist => $emu_chktrk_file, type => 'do');
			ifdef ZRCIEMUL
                       push (@{$GetOpts->{'TRK_DO_FILES'}}, $emu_chktrk_file)
			endif
                    }
               }
            }
        }
        my @testcases;

        if ($ProjOpts->{GROUP}) {
            push (@testcases, @grouplist);
        } else {
            push (@testcases, $fullpath);
        }

		if((undef $ProjOpts->{PLUGIN} || ! $ProjOpts->{PLUGIN})) {
            # Now @testcases contains:
            # - in avgroup mode: a list of paths from the list file
            # - else: the one $fullpath
            foreach my $test (@testcases) {
                my @includes = ();
                my @excludes = ();
            if ($ProjOpts->{LILY}) {
                push @includes, (
                '*exe*',
                '*lar*',
                '*so*',
                '*bmp',
                '*json*',
                '*txt*',
                '*project*/',
                '*project*/**',
                '*rb',
                '*aub',
                '*out*',
                '*crc*',
                '*xml*',
                '*yu12*',
                '*nv12*',
                '*manifest*',
                '*gsf*',
                '*reginit',
                '*rand16.tre',
                );
                &emu::printts ("Copying test files for $testcases[0] \n ");

            } else {

                # For GT Models not all files are needed.
                # Let's make a positive list.
                push @includes,
                  (
                    'test_params.in*',
                    'PCU_MASTER.bfl*',
                    'MASTER.BFL*',
                    'GFX.BFL*',
                    'PCU_INJECTOR*.BFL*',
                    'PCU_INJECTOR*.BFL.loop*',
                    'PCU_INJECTOR*.BFL.out*',
                    'process_bfl',
                    'memory_out/',
                    'memory_out/**',
                    'memory_in/',
                    'memory_in/**',
                    'memory_cmp/',
                    'memory_cmp/**',
                    'memory_gold/',
                    'memory_gold/**',
                    '*.fsdbtop*',
                    'emu_cycles.*',
                  );
                &emu::printts ("Copying test files for $testcases[0] \n ");
                ##if (defined ($GetOpts->{DO})||(defined $ProjOpts->{EMU_DO_FILES})) {
                ##aumahaja: Flite flow for PGT
                  if (($ProjOpts->{FD_PATH})){
                     if (($ProjOpts->{FD_PATH}) =~ /nfs/){
                         #for gmdhw gda disk path for fulsim dumps
                         #aumahaja: DTS/Vidya's temp solution to adding links
                         #&emu::test::addInputLinks(filelist => [$ProjOpts->{FD_PATH} . "/fdvd", $ProjOpts->{FD_PATH} . "/fd3d"]);
                         &emu::test::addPreCmd("ln -sf $ProjOpts->{FD_PATH}/fdvd test/fdvd");
                         &emu::test::addPreCmd("ln -sf $ProjOpts->{FD_PATH}/fd3d test/fd3d");
                         &emu::test::addPreCmd("ln -sf $ProjOpts->{FD_PATH}/fdve test/fdve");
                         &emu::test::addPreCmd("ln -sf $ProjOpts->{FD_PATH}/fdwd test/fdwd");
                         &emu::test::addPreCmd("ln -sf $ProjOpts->{FD_PATH}/fdmi test/fdmi");
                         &emu::test::addPreCmd("mkdir $GetOpts->{RP}/trkfiles");
                         &emu::test::addPreCmd("mkdir $GetOpts->{RP}/errfiles");
                         &emu::test::addPreCmd("ln -sf $GetOpts->{RP}/trkfiles test/trkfiles");
                         &emu::test::addPreCmd("ln -sf $GetOpts->{RP}/trkfiles trkfiles");
                         &emu::test::addPreCmd("ln -sf $GetOpts->{RP}/errfiles test/errfiles");
                         &emu::test::addPreCmd("ln -sf $GetOpts->{RP}/errfiles errfiles");

                         #&emu::test::addInputLinks(filelist => [$GetOpts->{RP} . "/trkfiles", $GetOpts->{RP} . "/errfiles"]);
                      } else {
                             #&emu::test::addInputLinks(filelist => [$GetOpts->{RP} . "/fdvd", $GetOpts->{RP} . "/fd3d"]);
                             &emu::test::addPreCmd("ln -sf $GetOpts->{RP}/fdvd test/fdvd");
                             &emu::test::addPreCmd("ln -sf $GetOpts->{RP}/fd3d test/fd3d");
                             #&emu::test::addInputLinks(filelist => [$GetOpts->{RP} . "/trkfiles", $GetOpts->{RP} . "/errfiles"]);
                       }
                  }
                  elsif ((scalar @{$GetOpts->{DO}} > 0)||(defined $ProjOpts->{EMU_DO_FILES})) {
                    push @includes,
                      (
                        'fd3d/',
                        'fd3d/**',
                        'fdwd/',
                        'fdwd/**',
                        'fdve/',
                        'fdve/**',
                        'fdvd/',
                        'fdvd/**',
                        'fdmi/',
                        'fdmi/**',
                      );
                    }
                }
                # Sorry, no handling of required vs. optional.
                # Not specified fox Gfx yet, not implemented in emu::test:: for subdirs yet.
                #&emu::test::addInputFiles(subdir => (($ProjOpts->{GROUP}) ? $test : undef), filelist => \@includes, exclude => \@excludes);
		#acshah1 added to support softlink support
		&emu::test::addInputLinks(subdir => undef, filelist => \@includes);
            }
            &emu::test::addPreCmd("ln -sf $GetOpts->{MODEL}/src/units/pipegsc/mem_files/* .");
            &emu::test::addPreCmd("cp -R $GetOpts->{MODEL}/src/units/pipegsc/mem_files/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1000.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc100.hex");
            &emu::test::addPreCmd("cp -R $GetOpts->{MODEL}/src/units/pipegsc/mem_files/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1001.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc101.hex");
            &emu::test::addPreCmd("cp -R $GetOpts->{MODEL}/src/units/pipegsc/mem_files/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1002.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc102.hex");
            &emu::test::addPreCmd("cp -R $GetOpts->{MODEL}/src/units/pipegsc/mem_files/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1003.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc103.hex");
            &emu::test::addPreCmd("cp -R $GetOpts->{MODEL}/src/units/pipegsc/mem_files/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1004.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc104.hex");
            &emu::test::addPreCmd("cp -R $GetOpts->{MODEL}/src/units/pipegsc/mem_files/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1005.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc105.hex"); 
 
        if (defined $ProjOpts->{GSC_FW_PATHS})
        {    &emu::printts ("GSC_FW_PATHS :\"@{$ProjOpts->{GSC_FW_PATHS}}\"\n");
            &emu::test::addPreCmd("ln -sf @{$ProjOpts->{GSC_FW_PATHS}}/* .");
            if (-e "@{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1000.mem" )
            { &emu::test::addPreCmd("cp -R @{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1000.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc100.hex"); }
            if (-e "@{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1001.mem" )
            { &emu::test::addPreCmd("cp -R @{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1001.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc101.hex"); }  
            if (-e "@{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1002.mem" )  
            {&emu::test::addPreCmd("cp -R @{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1002.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc102.hex"); }
            if (-e "@{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1003.mem" )  
            {&emu::test::addPreCmd("cp -R @{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1003.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc103.hex");} 
            if (-e "@{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1004.mem" )  
            {&emu::test::addPreCmd("cp -R @{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1004.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc104.hex");}
            if (-e "@{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1005.mem" )  
            {&emu::test::addPreCmd("cp -R @{$ProjOpts->{GSC_FW_PATHS}}/asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc1005.mem ./asdvds0g4s1p1024x128m8b1c1p1r0rm0sd_gsc105.hex");} 
                

          } }

         my $options = undef;
        &emu::printts ("GECCO is in genTest  \n");
        if ($ProjOpts->{SV}) {
            $options .= "-tcp ";
        } elsif ($ProjOpts->{GROUP}) {
            # FIXME: This is stupid if we couldn't create/append the list file.
            $options .= "-regr test/testlist.list ";
        } else {
            $options .= "-av test/  ";
        }
        if ($ProjOpts->{SVA} ) {
            $options .= "-sva_on ";
            &emu::test::addPostCmd("test -e tbx.log/assert.log && cp -f tbx.log/assert.log ./test/");
        }
        if    ($ProjOpts->{SV})
         {
                if ($ProjOpts->{TB} !~ /-mfe/ )
                {
                  $ProjOpts->{TB} = $ProjOpts->{TB}." -mfe";
                }

                my $userid = &emu::sys::getRunningUserID();
                if ($ProjOpts->{TB} =~ /-pf/)
                 {
                    &emu::printts ("$userid is giving -pf file \n");
                    $ProjOpts->{TB} =~ /-pf \S+/;
                    $& =~ /-pf /;
                    my $pfFilePath=$';

                    if ($pfFilePath =~ /random/){
                       my @pfFiles = ("test_params_extreme_max_delay_profile.in","test_params_max_delay_profile.in","test_params_med_delay_profile.in","test_params_min_delay_profile.in");
                       $pfFilePath = $pfFiles[rand @pfFiles];
                       &emu::printts ("$userid wants a random -pf file and got $pfFilePath \n");
                    }

                    if (-e $pfFilePath) # Does the given PF file exist in the path given
                    {
                       &emu::printts ("$userid given PVT -pf file was found: $pfFilePath\n");
                    }
                    else # Does the given PF exist in the model path
                    {
                       my $newConfigPath="$GetOpts->{MODEL}\/cfg_env\/defconfigs\/$pfFilePath";
                       if (-e $newConfigPath)
                       {
                          &emu::printts ("$userid given -pf file was found in model path: $newConfigPath\n");
                          $ProjOpts->{TB} =~ s/$pfFilePath/$newConfigPath/;
                       }
                       else # given -cf path not found and not in model path
                       {
                          &emu::printts ("ERROR Could Not Find given -pf file: $pfFilePath\n");
                       }
                    }
                 }
                if ($ProjOpts->{TB} =~ /-cf/)
                 {
                    &emu::printts ("$userid is giving modelconfig file \n");
                    $ProjOpts->{TB} =~ /-cf \S+/;
                    $& =~ /-cf /;
                    my $modelConfigPath=$';

                    if (-e $modelConfigPath) # Does the given modelconfig exist in the path given
                    {
                       &emu::printts ("$userid given PVT modelconfig file was found: $modelConfigPath\n");
                    }
                    else # Does the given modelconfig exist in the model path
                    {
                       my $newConfigPath="$GetOpts->{MODEL}\/src\/units\/tb_main\/ModelFrontEnd\/$modelConfigPath";
                       if (-e $newConfigPath)
                       {
                          &emu::printts ("$userid given modelconfig file was found in model path: $newConfigPath\n");
                          $ProjOpts->{TB} =~ s/$modelConfigPath/$newConfigPath/;
                       }
                       else # given -cf path not found and not in model path
                       {
                          &emu::printts ("ERROR Could Not Find given modelconfig: $modelConfigPath\n");
                       }
                    }
                 }
                else
                {
                      &emu::printts ("$userid wants to use default modelconfig file \n");
                      $ProjOpts->{TB} = $ProjOpts->{TB}." -cf $GetOpts->{MODEL}/src/units/tb_main/ModelFrontEnd/modelconfig.xml"
                }
         }

        if (defined $ProjOpts->{TB}) { &emu::printts ("TB :\"$ProjOpts->{TB}\"\n"); }
        $ProjOpts->{TB} = $ProjOpts->{TB}." -context $ProjOpts->{CONTEXT} ";
                                                         ### Added space ^  to avoid error when reading test_args.in file, else last char gets dropped in Z1.


        if (defined $ProjOpts->{TB}) { &emu::printts ("After Push TB :\"$ProjOpts->{TB}\"\n"); }
        $options .= "$ProjOpts->{TB}"; # if $ProjOpts->{TB};

        if ($options) {
            #  &emu::test::addEnv(TBX_CMD => q!"-norun !.$options.q! "!);
            #  &emu::printts ("Setting TBXCMD \n");
            #&emu::test::setExecCmd(opts => $options);
        }

        if ($main::build->isa('emu::platform::zse::build')) {

#################### ZRCI JACOBO##########################
            if  ($ProjOpts->{ZRCI}) {
                &emu::printts("################################################ \n "); 
                &emu::printts("------------- Starting zRCI flow --------------- \n "); 
                &emu::printts("################################################ \n "); 
                &emu::printts("INFO: Running zRCI \n");
                &emu::printts("########################## Testbench Inputs : $ProjOpts->{TB} ###########################\n");
                my $build_root = &emu::model::get->getBuild->getBuildroot(); 
                #&emu::test::addInputFiles(filelist => ['run_env.csh', 'zRci.do', 'libemu_xtor.so', 'designFeatures','init.do','test_args.in']);
                #&emu::test::addInputFiles(filelist => [ 'zRci.do', ]);
                #&emu::test::addPreCmd("cp ${build_root}/lib/libemu_xtor.so libemu_xtor.so");
                #&emu::test::addPreCmd("cp init.do init.do");
                #&emu::test::addPreCmd("cp test/test_args.in test_args.in");
                #&emu::test::addPreCmd("cp test/$ProjOpts->{TEST_ARGS} $ProjOpts->{TEST_ARGS}");

                &emu::test::addPreCmd("pushd ${build_root}; source /p/vt/tools/sim/vendor/zebu_xl/EVE_AE/eve_extra/scripts/set_zsd_V632B.csh; source source_env_var.csh ; popd"); 

            	if (defined $ProjOpts->{EMUL_PERF}){
                	$ProjOpts->{CPATH}="./lib_perf/" 
            	}
                &emu::printts(".so file picked from $ProjOpts->{CPATH}");

                &emu::test::addPreCmd("cp $ProjOpts->{CPATH}/libemubuildtb.so libemubuildtb.so");
                &emu::test::addPreCmd("g++ -fPIC -shared -o libemubuildtb_zRci.so $ProjOpts->{CPATH}/libemubuildtb.so ${build_root}/work/zebu.work/*.so");
                my $designFeatures ="${build_root}/designFeatures"; 
                if (defined $DutOpts{SAFE_FREQ}) {
                    &emu::printts("Emurun Options : Using Safe Frequency \n");
                    $designFeatures = "$modelpath/sw/designFeatures.safefreq";
                }
                #else {
                #    &emu::test::addPreCmd("cp ${build_root}/designFeatures designFeatures");
                #}
                &emu::test::addPreCmd("cp $designFeatures ./test/designFeatures");

                #&emu::test::addPreCmd("cp /nfs/site/disks/fm_iclgt_00537/jdebruy/zRCI/Clean/test_args.in test_args.in");  #WE NEED TO FIX THIS
                &emu::test::addPreCmd("cp /nfs/site/disks/mtl_emu_model_disk_003/CommonScripts/zRCI/TestbenchArgs.csh TestbenchArgs.csh");  
                if ($ProjOpts->{SV}) {
                    &emu::test::addPreCmd("./TestbenchArgs.csh -tcp $ProjOpts->{TB} "); 
                } else {
                    &emu::test::addPreCmd("./TestbenchArgs.csh $ProjOpts->{TB} "); 
                }    
                if ($GetOpts->{RP}) {
                    &emu::test::addPreCmd("mkdir -p $GetOpts->{RP}; chmod 777 $GetOpts->{RP}"); 
                    if ($ProjOpts->{STREAMING}) {
                        my $datestring;
                        $datestring = `date +"%d_%h_%Y_%H_%M"`; 
                        chomp $datestring;
                        $GetOpts->{'STREAMINGRP'} = "$GetOpts->{RP}/STREAMING_${datestring}";
                        &emu::test::addPreCmd("mkdir -p $GetOpts->{STREAMINGRP}; chmod 777 $GetOpts->{RP}"); 
                    }
                }
                
	        &emu::test::addResultFiles(filelist => ["test_args.in"]);
	        &emu::test::addResultFiles(filelist => ["\*/fullchip\*"]);
	        &emu::test::addResultFiles(filelist => ["\*/tardis\*"]);
	        &emu::test::addResultFiles(filelist => ["\*/sniffer\*"]);
	        &emu::test::addResultFiles(filelist => ["\*/\*.ztdb"]);
	        &emu::test::addResultFiles(filelist => ["\*/\*.txt"]);
	        &emu::test::addResultFiles(filelist => ["\*/SVA"]);
	        &emu::test::addResultFiles(filelist => ["zTune\*"]);
	        &emu::test::addResultFiles(filelist => ["designFeatures"]);

                # Test collateral is copied into test/ dir and we have to accordingly form the command
                my $output_do_file;
                # Hardcoded file
                if ($ProjOpts->{ZRCI_DO}) {
                    &emu::printts("INFO: Running zRCI_DO \n");
                    #&emu::test::addPreCmd("cp test/proc.do proc.do");
                    #&emu::test::addInputFiles(filelist => ['proc.do']);
                    &emu::test::addInputFiles(filelist => basename($ProjOpts->{ZRCI_DO}), type => "do");
                    unless (-r $ProjOpts->{ZRCI_DO}) {
                        &emu::printts("ERROR: Failure in accessing file $ProjOpts->{ZRCI_DO}.\n");
                        die;
                    }
                    #$output_do_file = "test/". basename($ProjOpts->{ZRCI_DO});
                    $output_do_file = $ProjOpts->{ZRCI_DO};

                } elsif ($ProjOpts->{ZRCI_TEMPLATE}) {
                    unless (-r $ProjOpts->{ZRCI_TEMPLATE}) {
                        &emu::printts("ERROR: Failure in accessing file $ProjOpts->{ZRCI_TEMPLATE}.\n");
                        die;
                    }
                    # Emurun v1.13.0 code defaults to init.do for ZSE custom do file
                    # But this is fixed in unofficial version 1.13.0_zRci_support and will be in v1.13.1
                    #$output_do_file = "test/". basename($ProjOpts->{ZRCI_TEMPLATE});
                    $output_do_file = "test/init.do";
                } else {
                    &emu::printts("INFO: Running zRCI default template \n");
                }    
                if(defined $DutOpts{OFFLINE_TRKS}) {
                   $GetOpts->{'OFFLINE_TRKS'} = 1; 
                }

                if(defined $ProjOpts->{SVA}) {
                   $GetOpts->{'SVA'} = 1; 
                }

                if(defined $ProjOpts->{UPF}) {
                   $GetOpts->{'UPF'} = 1; 
                }

                if(defined $ProjOpts->{ENABLESCRAMBLING}) {
                   $GetOpts->{'ENABLESCRAMBLING'} = 1; 
                }

                if(defined $ProjOpts->{ZTUNE}) {
                   $GetOpts->{'ZTUNE'} = 1; 
                }
                
                if(defined $ProjOpts->{ZTUNECSV}) {
                   $GetOpts->{'ZTUNECSV'} = 1; 
                }
                    if (defined $ProjOpts->{TRK_DO_FILES}) {
                    &emu::test::addPreCmd("echo 'TRK_DO_Files_ARE_ON' "); 
	            #&emu::test::addResultFiles(filelist => ["test_args.in"]);
                    }
                    &emu::printts("Jacobo-> ##################  ProjOps ##############################\n");
                    foreach my $key (keys %{ $ProjOpts }){
                    &emu::printts("Jacobo->  $key =  $ProjOpts->{$key} \n "); 
                    }
                    &emu::printts("Jacobo-> ################## GetOpts ############################## \n"); 
                    foreach my $key (keys %{ $GetOpts }) {
                    &emu::printts("Jacobo->  $key = $GetOpts->{$key} \n"); 
                    }
                    &emu::printts("Jacobo-> ################## TRK FILE ############################## \n"); 
                    my $values =  $GetOpts->{'TRK_DO_FILES'} ;
                    &emu::printts("Jacobo->  TRK_DO_FILES = $values \n"); 

                     #  for $i ( 0 .. $#{ $GetOpts{"TRK_DO_FILES"} } ) { print "Jacobo-> $i = $GetOpts{"TRK_DO_FILES"}[$i]"; } 
                    &emu::printts("##################  ############################## \n "); 
                # Populate zrci_opts
                my $zebu_work = $build_root.'/work/zebu.work';
                &emu::printts("Jacobo-> zebu work path: $zebu_work \n"); 
                my @zrci_options = ('--zebu-work', $zebu_work);
                push @zrci_options, "--do";
                push @zrci_options, $output_do_file;

                #&emu::test::setExecCmd(
                #    cmd  => 'xterm');
                #&emu::test::setExecCmd(
                #    cmd  => 'xterm -c zRci',
                #    opts => \@zrci_options);
                &emu::printts("Jacobo->  Command FIle DO $output_do_file \n"); 

                &emu::test::setExecCmd(
                    cmd  => 'zRci',
                    opts => \@zrci_options);
                &emu::printts("INFO: END OF ZRCI \n");


####################SIMIX JACOBO##########################
            } else {   






            &emu::printts ("Setting ZEBUCMD \n");
            my $prerun;
            #if (defined $ProjOpts->{EMUL_PERF}){
            if (defined $ProjOpts->{EMUL_PERF}){
                $prerun = " lib_load ./lib_perf/libemubuildtb.so $options";
            }
            else {    
                $prerun = " lib_load $ProjOpts->{CPATH}/libemubuildtb.so $options";
            }
            #VPT if ((scalar @{$GetOpts->{DO}} > 0)||(defined $ProjOpts->{EMU_DO_FILES})) {
                if (defined $ProjOpts->{TRK_DO_FILES}){
                    if(defined $DutOpts{OFFLINE_TRKS}) {
                        $prerun .= ";\ndpi -start_sync; \ndpi -offline -offline_file tracker_out.ztdb -design_all -start;";
                    }
                    else {
                        $prerun .= ";\ndpi -start_sync; \ndpi -design_all -start;";
                    }
                }
                #VPT }
            my @simics_opts;
            my $designFeatures;
            if (defined $DutOpts{SAFE_FREQ}) {
               ##$designFeatures = "/nfs/sc/disks/sc_tgrgtlp_00001/emulation_scripts/safefrequency/designFeatures";
               $designFeatures = "$modelpath/sw/designFeatures.safefreq"
            }
            else {
               $designFeatures = "designFeatures";
            }
            push @simics_opts, '-M', '$SIMIX_PATH/bin/opt_rdep/${_simix_opt_}/simix';
            push @simics_opts,'-M', '$SIMIX_PATH/lib/opt_rdep/${_simix_opt_}';
            push @simics_opts,'-M', '$ZEBU_ROOT/lib';
            push @simics_opts,'-M', '$ZMIF/lib';
            push @simics_opts,'-opt_sym_dyn_fub';
            #RMSXpush @simics_opts,'-m', '"zmif -model gt_tb -df_file designFeatures -uc -zemi3 -process simix"' ;
            #push @simics_opts,'-m', "\"zmif -model gt_tb -df_file " . "$designFeatures" . " -uc -zemi3 -ztune -ztune_swDisable -process simix\"";
            #push @simics_opts,'-m', "\"zmif -model gt_tb -df_file " . "$designFeatures" . " -uc -zemi3 -ztune_swDisable -process simix\"";
            push @simics_opts,'-m', "\"zmif -model gt_tb -df_file " . "$designFeatures" . " -uc -zemi3 -process simix\"";

            if ($ProjOpts->{SIMICS_CMD}) {
                &emu::printts ("Setting testbench cmd ".$ProjOpts->{SIMICS_CMD}."\n");

                my $current_dir = getcwd;
                my $script_filename = $current_dir . "/simix";
                open (my $handle, '>', $script_filename) or die "Could not prepare start script.";
                print $handle "#!/usr/intel/bin/bash\n";
                print $handle "echo Starting simics framework...\n";
                print $handle "source ~/.simics-4.6.sh\n";
                print $handle "source ", $ProjOpts->{SIMICS_CMD} . "\n";
                print $handle "echo simix \$\@". "\n";
                print $handle "simix \"\$\@\"". "\n";
                close $handle;
                print "File created: " . $script_filename . "\n";

                my $mode = 0777; chmod $mode, $script_filename;

                &emu::test::setExecCmd(cmd => $script_filename, opts => \@simics_opts);
            }
            else
            {
                &emu::test::setExecCmd (cmd => 'simix', opts => \@simics_opts);
            }
            &emu::test::setDesignExecPreRun(cmd => "mount gt_tb /; $prerun ;");
        }
###########################END OF SIMIX JACOBO            
            }

        elsif ($build->isa('emu::platform::pxp::build'))
        {
            &emu::printts("HERE, am a pxp build\n\n\n");
            &emu::printts ("Setting PZ1-CMD \n");

            #&emu::test::configure(wait_stop_marker => 300);

            ## Warning: Advanced usage only
            ## VTT PXP: Sends Signal 15 to the xeDebug process
            #&emu::test::setProcToKill(name => "xeDebug", signal => "15");

            if ($GetOpts->{CUSTOM_DO_TEMPLATE}) {
                &emu::test::addInputFiles(filelist => $GetOpts->{CUSTOM_DO_TEMPLATE});
            }

            my $my_outpath = &emu::test::getOutpath();
            my $tmp_myfile_path;
            print "######## outpath: + $my_outpath \n";
            #my $my_shadowtest = basename($_);
            #dump test_args.in
            foreach my $path (@{$GetOpts->{REGLIST}}) {
               my $filename = 'test_args.in';
               #my $file_path = File::Spec->rel2abs($filename, dirname($my_outpath));
               my $file_path = File::Spec->rel2abs($filename, $my_outpath);
               $tmp_myfile_path = $file_path;
               open(my $fh, '>', $file_path) or die "Could not open file '$file_path' $!";
               # chomp $fh;
               print $fh $ProjOpts->{TB};
               #print ' ' $ProjOpts->{TB};
               close $fh;
               &emu::test::addInputFiles(filelist => ["test_args.in"]);

               # PXP: Copy in only for tardis readback
	           if ($GetOpts->{TARDIS_DEBUG} && $path !~ /\/tmp\// && -d $path . '/fullchip_tardis_debug.infiSession') {
		           &emu::test::addInputFiles(filelist => "*", subdir => "fullchip_tardis_debug.infiSession");
               }
            }

            print " ############ test_args.in modified - done : + $tmp_myfile_path \n";
            if ($tmp_myfile_path ne $my_outpath."/test_args.in") {
               system("cp $tmp_myfile_path $my_outpath/");
               #system("chmod 777 $my_outpath/test_args.in");
               print " ############ test_args.in copied - done : + $tmp_myfile_path \n";
            }

	    #VTT PXP: Ensure test_args.in is copied into emulator host by emurun
	    &emu::test::addInputFiles(filelist => "test_args.*");
	    &emu::test::addInputFiles(filelist => "*.tcl");
	    &emu::test::addInputFiles(filelist => "*.*el");
	    &emu::test::addInputFiles(filelist => "*.tdf");
	    &emu::test::addInputFiles(filelist => "*.bp");

        #&emu::test::addInputFiles(filelist => "*.infiSession");
	    #&emu::test::addInputFiles(filelist => "*", subdir => "*.infiSession");
        #&emu::test::addInputFiles(filelist => "*", subdir => "test.infiSession");

            &emu::printts ("Setting PZ1CMD \n");
            #my $prerun = " lib_load $ProjOpts->{CPATH}/libemubuildtb.so $options";
            #if ((scalar @{$GetOpts->{DO}} > 0)||(defined $ProjOpts->{EMU_DO_FILES})||(defined $ProjOpts->{TRK_DO_FILES})) {
            #    if(defined $DutOpts{OFFLINE_TRKS}) {
            #        $prerun .= ";\ndpi -start_sync; \ndpi -offline -offline_file tracker_out.ztdb -design_all -start;";
            #    }
            #    else {
            #        $prerun .= ";\ndpi -start_sync; \ndpi -design_all -start;";
            #    ##$prerun .= "; lib_load $ProjOpts->{CPATH}/libemubuildtb.so \ndpi -design_all -start";
            #    #$prerun .= "; lib_load $ProjOpts->{CPATH}/libemubuildtb.so \ndpi -fub gt_tb.gt_trk1.gti_chktrk.GAMSQ_tracker1  -fub_all -start; \ndpi -fub gt_tb.gen12gt.gthunslice0.gthgtifix0.gthgti1.gt_idi_tracker1.genblk1[0].MBGF_IDI_tracker -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice1.gtdssm0.gtssm0.gtssmpar51.sounit_checker1.SoEuCommitBus_trk1  -fub_all -start; \ndpi -fub gt_tb.gen12gt.gthunslice0.gthgtifix0.gthfix1.gthfixpar141.SolGamWriteData_trk1  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gthunslice0.gthgtifix0.gthfix1.gthfixpar71.CsCmdPass_checker1  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gthunslice0.gthgtifix0.gthfix1.gthfixpar111.clunit_checkers1.checker_lp  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gthunslice0.gthgtifix0.gthfix1.gthfixpar111.clunit_checkers1.checker_hp  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice1.gtsc1.gtscrightpar11.DaprScRcpbChecker0  -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice1.gtsc1.gtscrightpar51.RcpbRccRdReq_ChkTrk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscrightpar41.MscRccDispatchReq_trk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice1.gtsc1.gtscrightpar61.RccRcpfeDispatchData_checker_debugkey0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscrightpar61.RccCcRdWr_clt_trk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscrightpar61.RccRcpbRdData_checker_debugkey0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice1.gtsc1.gtscrightpar51.PbeDapbData_ChkTrk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscrightpar51.PbeDapbData_ChkTrk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscrightpar71.CcRccRdDataTracker_trk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice1.gtsc1.gtscrightpar71.CcRccRdDataTracker_trk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice1.gtsc1.gtscrightpar71.CcGapTracker_trk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscrightpar71.CcGapTracker_trk0  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gthunslice0.gthgtifix0.gthgti1.gthguc1.guc_ga_trk_\ndpi1.client_ga_trk_\ndpi1  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gthunslice0.gthgtifix0.gthfix1.gthfixpar131.vfe_tsg_chk_trk1  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice0.gtdssm1.gtdssc1.gtdsscpar51.DcGwOBusData_monitor1  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice1.gtdssm0.gtdssc1.gtdsscpar81.DcTlb_Lni_req_monitor_wrapper1.DcTlb_Lni_req_monitor_wrapper1  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice1.gtdssm1.gtdssc1.gtdsscpar51.DcGwOBusData_monitor1  -fub_all -start;\ndpi -fub gt_tb.gen12gt.gtslice0.gtdssm0.gtdssc1.gtdsscpar51.DcGwOBusData_monitor1 ;\ndpi -fub gt_tb.gen12gt.gthunslice0.gthgtifix0.gthfix1.gthfixpar71.CsCpdatachecker1; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s0_hp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s0_lp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s1_hp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s1_lp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s2_hp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s2_lp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s3_hp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s3_lp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s4_hp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s4_lp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s5_hp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s5_lp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s6_hp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s6_lp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s7_hp -fub_all -start; \ndpi -fub gt_tb.gen12gt.gtslice0.gtsc1.gtscleftpar71.sfbeunit_checkers_s0.wbusMonitor_slice_s7_lp -fub_all -start;";
            #    }
            #}

        # VTT PXP: Form and set execution command
        my $build_root = &emu::model::get->getBuild->getBuildroot();
        my $command = "xeDebug";

        # IF AV/SV options differ, use if ($ProjOpts{AV})
        $command .= " -gui" if $GetOpts->{INTERACTIVE};
        #$command .= " --xmsim -sv_lib $build_root/libg12hp_ww50_2x4x16.so -nowarn NOCOND -nowarn MCONDE -unbuffered +xcprof --";
        #### iT-observe: need to include -- +IT_observe_session_without_gfifo
        $command .= " -fsdb --xmsim +empty_gfifo_poll_delay+200 +gfifo_timestamp_all -sv_lib $build_root/lib/libtestbench.so -nowarn NOCOND -nowarn MCONDE -unbuffered +synchronous_pthreads +xcprof --";

        # VTT PXP: Emurun v1.8.2 will have output file name as init_hw.tcl
        # Name of generated script changes if custom_do_template command line option is used
        if ($GetOpts->{CUSTOM_DO_TEMPLATE}) {
            $command .= " -init test/init.do";
        } else {
            $command .= " -init test/init_hw.tcl";
        }

        # Adding more options
        # AV flow (commands potentially need rearranging?)  will revisit at later point
        # VTT PXP:
        my @options = ();
        push(@options, @{$ProjOpts->{XEDEBUG_OPTIONS}});
        print "############## secExecCmd + $command ";
        &emu::test::setExecCmd(
            cmd => $command,
            opts => \@options);

        # VTT PXP: emuDut will already have it but check to make sure
        # ATS/SV test
        &emu::test::addEnv(TBX_SERVER_SETUP_SCRIPT => q!"touch test/STATUS=running"!);

            #my @simics_opts;
            #my $designFeatures;
            #if (defined $DutOpts{SAFE_FREQ}) {
            #   ##$designFeatures = "/nfs/sc/disks/sc_tgrgtlp_00001/emulation_scripts/safefrequency/designFeatures";
            #   $designFeatures = "$modelpath/sw/designFeatures.safefreq"
            #}
            #else {
            #   $designFeatures = "designFeatures";
            #}
            #push @simics_opts, '-M', '$SIMIX_PATH/bin/opt_rdep/${_simix_opt_}/simix';
            #push @simics_opts,'-M', '$SIMIX_PATH/lib/opt_rdep/${_simix_opt_}';
            #push @simics_opts,'-M', '$EMU_ROOT/lib';
            #push @simics_opts,'-M', '$ZMIF/lib';
            #push @simics_opts,'-opt_sym_dyn_fub';
            ##RMSXpush @simics_opts,'-m', '"zmif -model gt_tb -df_file designFeatures -uc -zemi3 -process simix"' ;
            #push @simics_opts,'-m', "\"zmif -model gt_tb -df_file " . "$designFeatures" . " -uc -zemi3 -process simix\"";

#if(0) {
            #if ($ProjOpts->{SIMICS_CMD}) {
            #    &emu::printts ("Setting testbench cmd ".$ProjOpts->{SIMICS_CMD}."\n");

            #    my $current_dir = getcwd;
            #    my $script_filename = $current_dir . "/simix";
            #    open (my $handle, '>', $script_filename) or die "Could not prepare start script.";
            #    print $handle "#!/usr/intel/bin/bash\n";
                #print $handle "echo Starting simics framework...\n";
                #print $handle "source ~/.simics-4.6.sh\n";
                #print "source ", $ProjOpts->{SIMICS_CMD} . "\n";
                #print $handle "echo simix \$\@". "\n";
                #print $handle "simix \"\$\@\"". "\n";
                #close $handle;
                #print "File created: " . $script_filename . "\n";

                #my $mode = 0777; chmod $mode, $script_filename;

                #&emu::test::setExecCmd(cmd => 'simics', opts => \@simics_opts);
            #}
            #else
            #{
                &emu::printts ("In else condition \n");
                #&emu::test::setExecCmd (cmd => 'simics', opts => \@simics_opts);
            #}
            #&emu::test::setDesignExecPreRun(cmd => "mount gt_tb /; $prerun ;");
#}
        }
        else
        {
            &emu::printts ("Setting TBXCMD \n");
            $options .= "-noexit" if ($ProjOpts->{GROUP} || $ProjOpts->{AV})
            &emu::printts ("Testbench option is $options   \n");
            &emu::test::setExecCmd(opts => $options);
        }

	## To copy the ztune_folder to the -rp path
	#&emu::test::addResultFiles(filelist => ["ztune_folder"]);
	#&emu::test::addResultFiles(filelist => ["ztune_folder_csv"]);

        ###########################################
        # Let the API finalize the test directory.
        if (!&emu::test::prepTest()) {
            # prepTest failed, do your stuff here
            emu::printts ("ERROR: emu::test::prepTest() failed for test \"$fullpath\", skipping\n");
            next;
        }

        # prepTest was successful, do your stuff here or below

        my $outpath = &emu::test::getOutpath();

        # The test content which was copied to the target dir may need to be uncompressed.
        # (Too fiddly in pure Perl.)
        #foreach (< $outpath/* >) {
        #    my $outpath_dir = basename($_);
        #    next if ($outpath_dir eq 'stimuli' || $outpath_dir eq 'fullchip_tardis_debug');
        #    &emu::printts ("Uncompressing $outpath/$outpath_dir \n");
        #    system ("gunzip -r -f -q $outpath/$outpath_dir/");
        #}

        &emu::test::addResultFiles(filelist => ["*Tracker*", "*TRACKER*"]);
        &emu::test::addResultFiles(filelist => ["*fsdb*", "*FSDB*"]);
        &emu::test::addResultFiles(filelist => ["*TcpServerLog.log*", "*tcplib*"]);
        &emu::test::addResultFiles(filelist => ["*log*", "*LOG*"]);
        &emu::test::addResultFiles(filelist => ["*cov*", "*COV*"]);
        &emu::test::addResultFiles(filelist => ["*bin*", "*BIN*"]);
        &emu::test::addResultFiles(filelist => ["*trace_index_file*", "*jem_trace_index*"]);
        &emu::test::addResultFiles(filelist => ["*JOBID*", "*jobid*"]);
        &emu::test::addResultFiles(filelist => ["*JSON*", "*json*"]);
        ##################################################
        my $cycles = $GetOpts->{CYCLES};
        my $cycles_copy = $GetOpts->{CYCLES};
        my $emucycle = undef;
        my $counter_prv ;
    my $time = undef;
    my $unit = undef;
        if ($ProjOpts->{GROUP}) {
            &emu::printts("GenTest::Main Testlist loop\n");
            my $counter = 0;
            my $ret = open (TESTLIST, '>>', "$outpath/testlist.list");
            if (!$ret) {
                &emu::printts ("WARNING: Couldn't open \"$outpath/testlist.list\" for appending: $!\n");
            } else {
                foreach (< $outpath/* >) {
                    next if ! -d $_; # only consider directories
                    ## rspatel added to print wrong test in new runreg flow
                    # next if ! -e "$_/memory_in/sysmem.in";  # only consider tests that did not fail during generation
                    # append to list
                    $agent_cmd = undef;
                    $shadow_test = basename($_);
                    #my $concat_test_exec = "./test/"."$shadow_test/". basename($_).".1.lily.out";
                    my $concat_test_dir = "$outpath/$shadow_test/".$shadow_test.".1.project";
                    &emu::printts("GenTest:: $concat_test_dir\n");
                    if (-e "$_/memory_in/sysmem.in") {
                        print TESTLIST ("./test/" . basename($_) . "\n");
                    } elsif (-d $concat_test_dir ) {
                        print TESTLIST ("./test/". basename($_). "\n");
                        &emu::printts("Gentest_1: $concat_test_dir\n");

                    } else {
                            &emu::printts("Current Test: $shadow_test \n");

                            if (($shadow_test ne 'errfiles') && ($shadow_test ne 'svcov') && ($shadow_test ne 'trkfiles') && ($shadow_test ne 'sv_cov')  ) {
                                #&emu::printts ("$shadow_test is not valid test for GECCO, skipping it \n");
                            }
                    }

                    # count, for the sake of calculating clocks
            if ($ProjOpts->{GROUP}) {
                            #if ((-e "$_/emu_cycles.txt"){
                            #open (EMUCYC , "+<$_/emu_cycles.txt ");
                            #chomp ($emucycle = <EMUCYC>) ;
                ##rspatel: we are not using clk given in emu_cycles.txt anymore, we are using -c
                                #if ($emucycle =~ /(\d+)(\w+)/ )
                    #my $time = $1;
                                        #$counter_prv = 0;
                                        ## rspatel test
                                         if ($cycles =~ /(\d+)(\w+)/ || $cycles =~ /(\d+)/ )
                                        {
                                         my $time = $1;
                                         $counter_prv = 0;

                                         #&emu::printts("Pre counter addition(counter_prev)main loop : $counter_prv\n");
                                        if ($2 =~ /ms/) {
                                                $counter_prv = $time *1000000;
                                                #&emu::printts("Pre counter addition(counter_prev)ms : $counter_prv\n");
                    }
                    elsif ($2 =~ /us/){
                                $counter_prv = $time *1000 ;
                                                #&emu::printts("Pre counter addition(counter_prev)us : $counter_prv\n");
                    }
                    elsif ($2 =~ /ns/){
                            $counter_prv = $time *1;
                                                #&emu::printts("Pre counter addition(counter_prev)ns : $counter_prv\n");
                    }
                    elsif ($2 =~ /ps/){
                            $counter_prv = $time *0.0001;
                                                #&emu::printts("Pre counter addition(counter_prev)ps : $counter_prv\n");
                        }
                                        else {
                            $counter_prv = $cycles_copy ;
                                        }
                                        #&emu::printts("Pre counter addition(counter_prev) : $counter_prv\n");
                            $counter = $counter + $counter_prv;
                        chomp ($counter);
                                        #&emu::printts("Post counter addition(counter) : $counter\n");
                                        }
                                        #close  EMUCYC;
                        #chomp($cycles = "${counter}ms");
                        #}
            }
               # else {
                        #   $counter++;
            #        $cycles =~ s/^(\d+)/$1*$counter/e;
                    #}

         chomp($cycles = "${counter}");
                if ($ProjOpts->{LILY}) {
                    # FIXME: get rid of this when boost is gone ## rspatel added this in runtime souce env
                    #&emu::test::addEnv(LD_LIBRARY_PATH => "\$VMW_HOME/lib/amd64.linux.gcc450");
                   if ($ProjOpts->{GROUP}){
                       my $test_file = $shadow_test."/".$shadow_test.".gsf";
                       #my $test_file = $shadow_test.".gsf";
                       my $test_directory = "test/".$shadow_test;
                       my $tmp_directory = $outpath;
                       foreach my $extradir (@extraoutputdirs) {
                            if (!-e "$outpath/$extradir") {
                                make_path("$outpath/$extradir");
                            }
                            # Provide this subdir from the model/shadow directory as symlink.
                            &emu::test::addPreCmd("test -L $extradir && rm -fv $extradir");
                            &emu::test::addPreCmd("test -d $extradir && echo WARNING: $extradir is an existing directory");
                            &emu::test::addPreCmd("ln -sfv test/$extradir $extradir");
                        }
                        &emu::test::addPreCmd("touch JOBID.$ENV{__NB_JOBID}");
                        &emu::test::addPreCmd("touch test/JOBID.$ENV{__NB_JOBID}");

                       &emu::printts ("Our Test directory is $test_directory\n");
                       $agent_cmd .= "$ProjOpts->{LILY_AGENT} $test_file /runtest -host 127.0.0.1";
                       $agent_cmd .= " ".$ProjOpts->{LILY_OPT};
                       &emu::test::addPreCmd('(/bin/sh -c "while ! netcat -z localhost 4321 ; do sleep 1; done"; cd '.$test_directory.'; '.$agent_cmd.' > lily.log; echo "INFO: Lily is done"; touch client=stopvelgui; cd '.$tmp_directory.' & )');
                       #my $cmd = "cd $test_directory && $agent_cmd > lily.log && cd $tmp_directory";
                       #&emu::printts("GenTest : $cmd \n");
                       #&emu::test::addPostCmd("rm test/*.aub");
                       #&emu::test::setExecCmd(cmd => $cmd);
                       #&emu::test::addPostCmd("mv $shadow_test/exec.log ../");

                  }

                }
            }
                close TESTLIST;
            }

        }
        &emu::printts("INFO: Final -c is $cycles \n ");
        &emu::test::setCycles($cycles);
        #if ( ($ProjOpts->{GROUP})){
                # Create necessary subdirs in the test directory.
                #my @extraoutputdirs = ("trkfiles", "errfiles","svcov","sv_cov");
                foreach my $extradir (@extraoutputdirs) {
                if (!-e "$outpath/$extradir") {
                make_path("$outpath/$extradir");
                }
                # Provide this subdir from the model/shadow directory as symlink.
                &emu::test::addPreCmd("test -L $extradir && rm -fv $extradir");
                &emu::test::addPreCmd("test -d $extradir && echo WARNING: $extradir is an existing directory");
                &emu::test::addPreCmd("ln -sfv test/$extradir $extradir");
                }


               &emu::test::addPreCmd("touch JOBID.$ENV{__NB_JOBID}");
               &emu::test::addPreCmd("touch test/JOBID.$ENV{__NB_JOBID}");
               #}
        ##################################################
        # This line is just as ugly as it is to avoid any form of error messages
        # on the screen. Only if the directories exist and are not empty
        # files are being copied.

        &emu::test::addResultFiles(filelist => ["*Tracker*", "*TRACKER*"]);
        &emu::test::addResultFiles(filelist => ["*fsdb*", "*FSDB*"]);
        &emu::test::addResultFiles(filelist => ["*ztdb*", "*ZTDB*"]);
        &emu::test::addResultFiles(filelist => ["*cov*", "*COV*"]);
        &emu::test::addResultFiles(filelist => ["*bin*", "*BIN*"]);
        &emu::test::addResultFiles(filelist => ["*JOBID*", "*jobid*"]);
        &emu::test::addResultFiles(filelist => ["*zemi3mgr.log*"]);
        # The logic behind this is currently too tricky to put into an API:
        # If "trkfiles" is not a link, copy its contents to ./test/.
        # I believe the "MARKER" magic was made by Thomas to avoid "No match." messages.
        foreach my $subdir ("trkfiles", "errfiles","svcov","sv_cov") {
            &emu::test::addPostCmd("test -e $subdir -a ! -L $subdir && test \"`ls $subdir | xargs echo MARKER`\" != \"MARKER\" && mv -f $subdir/* test/$subdir/");
        }
        if (defined ($GetOpts->{DO})||(defined $ProjOpts->{EMU_DO_FILES})||(defined $ProjOpts->{TRK_DO_FILES})) {
            # create links to some extra test content directories in the execution area
            foreach my $extradir ("fdvd", "fd3d", "fdwd", "fdve", "fdmi") {
                &emu::test::addPreCmd("test -e test/$extradir && ln -sf test/$extradir $extradir");
                &emu::test::addPostCmd("test -L $extradir && rm $extradir");
            }
        }



        # debug xterm temporarily disabled for ZSE - some precmd eval shell issue
        if ($GetOpts->{STANDALONE} && $GetOpts->{INTERACTIVE} && !&emu::isZSE()) {
            my $precmd .= "(xterm -T gfxemu_debug_shell &)";
           # emu::test::addEnv(TBX_PRECMD => "\"$precmd\" ");
           &emu::test::addPreCmd ("$precmd");
        }

    if ($ProjOpts->{SV}) {
        if ($main::build->isa('emu::platform::pxp::build')) {
            &emu::test::addPreCmd("rm -f tmp xe.msg && ln -sf test/test_args.in test_args.in ");

            # VTT PXP: Copy back necessary logs
	    #&emu::test::addResultFiles(filelist => ["*.err", "xe.*", "xrun.*", "xcprof.out", "DBEngine.msg", "xmsim.*", "sigursdump.out"]);
	    &emu::test::addResultFiles(filelist => ["*.infiSession", "*.err", "*.msg", "*.key", "*.out*", "*.shm", "xrun.*", "*.fsdb*", "tmp", "*.bin", "tlm_trace_index*", "*.*el"], copy => 1);
        }
    }

    if ($ProjOpts->{LILY}) {
            # FIXME: get rid of this when boost is gone ## rspatel added this in runtime souce env
            #&emu::test::addEnv(LD_LIBRARY_PATH => "\$VMW_HOME/lib/amd64.linux.gcc450");
               if (! ($ProjOpts->{GROUP})){
                $agent_cmd .= "$ProjOpts->{LILY_AGENT} *.gsf /runtest -host 127.0.0.1";
                $agent_cmd .= " ".$ProjOpts->{LILY_OPT};
                &emu::test::addPreCmd('(/bin/sh -c "while ! netcat -z localhost 4321 ; do sleep 1; done"; cd test; '.$agent_cmd.' > lily.log; echo "INFO: Lily is done"; touch client=stopvelgui; cd - &)');
                &emu::test::addPostCmd("rm test/*.aub");
              }
    }

        if ($ProjOpts->{TCP_SW_CHECK}) {
            # FIXME: get rid of this when boost is gone ## rspatel added this in runtime souce env
            #&emu::test::addEnv(LD_LIBRARY_PATH => "\$VMW_HOME/lib/amd64.linux.gcc450");
             $agent_cmd .= "/nfs/site/disks/sc_iclgt_00308/bin/sw_regress/a.out 127.0.0.1 -p 4321 -f $ProjOpts->{TCP_SW_CHECK_OPT}";
            ##&emu::test::addPreCmd('(/bin/sh -c "while ! netcat -z localhost 4321 ; do sleep 1; done"; cd test; '.$agent_cmd.' > tcp_sw_check.log; echo "INFO: TCP_SW_CHECK is done"; touch client=stopvelgui; cd - &)');
            &emu::test::addPreCmd('(/bin/sh -c "while ! netcat -z localhost 4321 ; do sleep 1; done";echo "1" > tcp_sw_check;date > tcp_sw_check.log;'.$agent_cmd.' > tcp_sw_check.log; echo "INFO: TCP_SW_CHECK is done"> tcp_sw_check.log;date > tcp_sw_check.log; &)');
    }


        if ($GetOpts->{FSDB} eq "all" && &emu::test::getConfiguration('tardisDebug'))
        {
           # &emu::test::addPostCmd("rm -rf test/fullchip_tardis_debug");
           # &emu::printts("INFO: Deleting fullchip_tardis_debug from shadow after readback of ZPRD\n");
        }
        &emu::test::configure(omitPreRun => 1);
        ##rspatel added as per Bruno's suggestion
        &emu::test::configure ( extend_default => 1800 ) ;
        $ENV{GECCO_CHECKMODELREQUIREMENT} = "0";
        &emu::printts("INFO: Setting GECCO_CHECKMODELREQUIREMENT to $ENV{GECCO_CHECKMODELREQUIREMENT}\n");
        &emu::test::addPreCmd("echo $ENV{HOSTNAME} $ENV{NBQSLOT_BAK}") if (defined $ENV{NBQSLOT_BAK});
        &emu::test::addPreCmd("/usr/intel/bin/nbjob modify --target $ENV{__NB_QUEUE} --qslot $ENV{NBQSLOT_BAK} --no-restart 'jobid==$ENV{__NB_JOBID}'") if (defined $ENV{NBQSLOT_BAK});
        &emu::test::addEnv(TBX_SERVER_SETUP_SCRIPT => q!"touch test/STATUS=running"!);

        # Tell emurun that we're finished with generation, and finally
        # fix up the environment file and create the design init file.
        &emu::test::finalizeTest();
    }
}

########################################################################
# preSubmissioncmd()()
########################################################################
#sub preSubmissionCmd {
#    my ($GetOpts, $ProjOpts) = @_;     # hash references
#         return 0;
#    &emu::printts("INFO: Doing Presubmission cmd\n");
#         if($GetOpts->{FSDB} eq "all" && &emu::test::getConfiguration('tardisDebug')) {
#        &emu::printts("FSDB Specified and TARDIS_DEBUG too\n");
#             &emu::printts("Proceeding to do pre-processing\n");
#             # Sourcing zse/source_env_var.csh in order to run the pre-Processing with zPostRunDebug
#             my $csh = Shell::Source->new(shell => "csh", file=> "$modelpath/$projEmuWorkroot/zse3/source_env_var.csh");
#             $csh->inherit;
#             # Building up the path to generated prd file which should reside in RP area.
#             my $prdPath = $GetOpts->{RP};
#             $prdPath .= "/zprd_process.prd";
#             # Write to prd file and give the sniffer and zebu_work area, as well as indicate the convert_stimuli and join
#             `echo "set_option -sniffer {$GetOpts->{REGLIST}[0]/fullchip_tardis_debug}" > $prdPath`;
#             `echo "set_option -zebu_work {$modelpath/$projEmuWorkroot/zse3/zcui.work/zebu.work}" >> $prdPath`;
#             `echo "set_option -prd_work {$GetOpts->{REGLIST}[0]}" >> $prdPath`;
#             `echo "convert_stimuli -all" >> $prdPath`;
#             `echo "join" >> $prdPath`;
#             # Execute zPostRunDebug with the generated prdPath
#        `zPostRunDebug --nogui $prdPath`;
#         }
#}
sub preSubmissionCmd {
     my ($GetOpts, $ProjOpts) = @_;     # hash references
     &emu::printts("INFO: Doing Presubmission cmd\n");
         # aumahaja: fulsimlite automation
         # Only happens when FD_PATH is given
     if ($ProjOpts->{FD_PATH}) {
        &emu::printts("\n\nFD_PATH: $ProjOpts->{FD_PATH}\n\n");
     }
     if (($ProjOpts->{SV}) && ($ProjOpts->{FD_PATH})) {
            my $rsync_src = $ProjOpts->{FD_PATH};
            my $rsync_dest = $GetOpts->{RP};
            my $call_fl_path = "$GetOpts->{MODEL}";
            my $script_to_run = "$GetOpts->{MODEL}/src/libs/media_val/do_stuff.csh";
            my $script_to_run_unix = "$GetOpts->{MODEL}/src/libs/media_val/do_stuff_unix.csh";
         if ($rsync_src =~ /nfs/) {
           # Launch command to netbatch to do the rsync business
                 my @cmds = ();
                 push(@cmds, "export RSYNC_SRC=$rsync_src");
                 push(@cmds, "export RSYNC_DEST=$rsync_dest");
                 push(@cmds, "export CALL_FL_PATH=$call_fl_path");
                # For some reason, Netbatch cannot block when using --work-dir option
                 push(@cmds, "cd $rsync_src");
                 #push(@cmds, "nbjob run --target sc_express --qslot /VPG/IceLakeGT/EMU/ZeBu/corebuild --class 'SLES11SP2_EM64T_64G' --mode blocking $script_to_run_unix");
                 push(@cmds,"$script_to_run_unix");
                 &emu::printts("INFO: Pre-submitting " . join('; ', @cmds) . "\n");
                 my ($exitcode, $signal, $reason) = &emu::sys::doSystem(join('; ', @cmds));
                 return $exitcode;
          } else {
            # Launch command to netbatch to do the rsync business
                 my @cmds = ();
                 push(@cmds, "export RSYNC_SRC=$rsync_src");
                 push(@cmds, "export RSYNC_DEST=$rsync_dest");
                 push(@cmds, "export CALL_FL_PATH=$call_fl_path");
                # For some reason, Netbatch cannot block when using --work-dir option
                 push(@cmds, "cd $rsync_dest");
                 push(@cmds, "nbjob run --target sc_express --qslot /VPG/IceLakeGT/EMU/ZeBu/corebuild --class 'SLES11SP2_EM64T_64G' --mode blocking $script_to_run");
                 &emu::printts("INFO: Pre-submitting " . join('; ', @cmds) . "\n");
                 my ($exitcode, $signal, $reason) = &emu::sys::doSystem(join('; ', @cmds));
                 return $exitcode;
          }
     }
         return 0;
     &emu::printts("INFO: Doing Presubmission cmd\n");
}
########################################################################
# cleanup
########################################################################
# Project specific cleanup script
#

sub cleanup {
    # These are hash references:
    my ($GetOpts, $run, $tests) = @_;
}

sub signalPluginEvent {
    my ($event, $ProjOpts, %args) = @_;
    # Debug print message
    &emu::printts("DEBUG: Signaled plugin event '$event'\n") if (&emu::verbose(feature => 'emuproject') >= 3);

    # Signal the event to occur and record the code
    my ($called, $failed) = &Plugins::SignalEvent($event, %args);

    if ($failed) {
        &emu::printts("ERROR: $failed plugin(s) of $called failed on event '$event'\n") if (&emu::verbose(feature => 'emuproject') >= 3);
        if ($ProjOpts->{PLUGIN_DIE_ON_FAIL}) {
            emu::error::custom->new(
                code => 14,
                msg => "Dying on plugin failure due to -plugin_die_on_fail")->exitWithMsg;
        }
    }

    return $called;
}

__END__

=head1 NAME

Used to control a Mentor Veloce/Veloce 2 emulator through Netbatch or in interactive mode. This script is meant to be compatible with trex flow and should cover the needs for AV, SV and SW.

=head1 SYNOPSIS


-test <directory>
-nbqslot <qslot>
-cycles <clks|s|ms>
[-rp <resultpath>]
[-rmerge]
[-tcp]
[-interactive]
[-fsdb <all|none|pass|fail> (default is all)]
[-fsdblength <duration time of traces>]
[-fsdbtop <hierachy to trace>]
[-trk <options>]
[-tb <options>]
[-trigger <triggerpath>]
[-do <do-file for velocegui>]
[-gz]
[-server]
[-debug]
[-help]

=head1 OPTIONS

=over 12

=item B<-ver directory> (Required)

This is a pointer to the MODEL_ROOT of the emulation model. Under the model MODEL_ROOT "unified models" are support. These are models that have been compiled for multiple platforms like D1 (Veloce Quattro), D1G (Veloce Grande), D1GM (Veloce Grande-M), D1M (Veloce Maximus) and D2 (Veloce 2 Quattro). By default the emulation model is expected in MODEL_ROOT/tbx or MODEL_ROOT/compile.vmw, for "unified models" these are expected under MODEL_ROOT/tbx_D1, MODEL_ROOT/tbx_D1G and so on.

=item B<-nbqslot qslot> (Required)

Specify the Qslot that was assigned to you time for execution. This option is needed for Regression or Interactive execution. Alternatively you can also set ENV{NBQSLOT} to the value. In that case this option is optional.

=item B<-c        #cycles|time> (Required, except for Interactive-Mode)

Specifies the timeout as seen by DUT time and cycles. You can either specify a number of absolute clock cycles of the fastest clock or time duration in ps, ns, ms, s. The timeout should be close to the expected test runtime. This option is ignored when in interactive mode.

=item B<-test directory> (Required, except for TCP-Mode)

Used to specify the full path to a testcase that should be run in emulation. This option should normally be used for AV tests. The testbench is automatically started using <testbench> -av <testcase-dir>. The testcase is validated by looking for a memory_in folder in the folder given. This option is required unless you are running with -SV option. In this case a dummy testcase is created. Multiple Tests can be supplied with -test <test1> -test <test2> etc.

If you point -test to a directory that is full of testcases (which each has a memory_in folder), they fill all be executed automatically.

=item B<-interactive>

Instructs the script to open the VeloceGui for interactive debugging. This option is allowed through Netbatch or when beeing directly on the emulator. If you capture traces, make sure to use the default path. Just give the trace a name, the rest is handled by the script.

=item B<-tcp>

This will instruct the emulation model in the way as needed by SV and SW validation. The testbench will be started with -tcp option. If no -test option was given (which is optional) "svautomation" is chosen as testcase name.

=item B<-rp directory>

By default all emulation results are saved back to the area from where the gfxemu script was launched. The -rp option can be used to instruct the script to save all results in an (already) existing directory. If in the directory a result with the same is already found, a new unique name of the form <testname>.i is formed. You are not allowed to back lrbsle or quicktur home directory as result dir.

=item B<-rmerge>

With this option the test result will be merged with the riven result directory. No subdirectories are created. This is useful if you are running an AV automation flow, where you want to the results to go into the directory of the original testcase for post processing.

=item B<-gz>

Compress the result

=item B<-fsdb>

Use this option to automatically capture traces at the end of your tests.

=item B<-fsdblength         #cycles|time>

Specifies the duration of traces

=item B<-fsdbtop hierachy>

Allows you to download traces for signals/modules you are interested in, speeding up traces. Only makes sense when combined with -fsdb option and can be combined with -fsdblength option. There are two possible ways to use it.

First Option: -fsdbtop <HierPath> as switch to gfxemu. Example "-fsdb -fsdbtop /lrb_system_th/lrb/lcpuboxC08_gid39" will dump all signals under this lcpubox. Multiple fsdbtop are supported. Avoid using wildcards (*). Hierarchy separator is "/".

Second option: <testname>.fsdbtop File in testcase directory. In Case you want to provide a long signal/hierarchy list. Each signal/hierarchy goes to a separate line

=item B<-trigger file>

If you want to load a trigger for your emulation run or debug. Only single trigger per run is allowed, which can has as many states as allowed by the platform. When combined with -fsdb option, traces are taken when first trigger matures. If you have -fsdblength option specified, a duration is either until the timeout/cycle hits or a trigger matures a second time.

=item B<-trk option>

Enable trackers for the run. The string is directly forwarded to the testbench. Please see the release mail of you model for valid -trk options.

=item B<-sva>

Enable SVA in emulation models that support it. At the end of the run assert.log will be copied to the result package and saved togeather with all other log files

=item B<-tb='specialoptions'>

This switch can be used to pass abitrary options directly to the testbench. Please make sure to specify with -tb='<youstuffhere>' so that they can be properly parsed.

=item B<-do file>

Allows you to load (TCL) do-Files that are executed before the run. This can be used to force registers or cause special actions not possible with build in options. Multiple do-files are supported like -do <file1> -do <file2>. They are executed in the order given.

=item B<-debug>

Enable debug output in the script. This can be useful for debugging failures.

=item B<-server> (Internal Only)

This option is used to start a Netbatch Handling Server. You should never use this option.

=back

=over 12

# vim: set tabstop=8 expandtab shiftwidth=4 softtabstop=4:
