#!/usr/intel/bin/perl5.10-threads-64
# -*- mode: cperl; cperl-indent-level: 4; cperl-close-paren-offset: 4; cperl-continued-statement-offset: 4; cperl-indent-parens-as-block: t; cperl-tab-always-indent: t; -*-
#------------------------------------------------------------------------------
#
#   ****
#   ****  (C) Copyright 2011-2012 by Intel GmbH
#   ****   proprietary and confidential
#
#
#   Project         :  GECCO
#   File name       :  $URL: https://subversion.jf.intel.com/iag/pve/emu/gecco/trunk/bin/emuProject_gfx.pm $
#   Revision        :  $Revision: 10776 $
#   Author          :  $Author: $
#
#   Description     :  GECCO Project Script
#------------------------------------------------------------------------------

package emuProject;

use warnings;
use strict;

use FindBin; # core module to find the path to the (this) script, which is where we expect emu.pm
use lib "$FindBin::Bin";

use emu;
use Pod::Usage;
use Getopt::Long;
use Cwd;
use Cwd 'realpath';
use File::Copy;
use File::Basename;
use File::Path qw(make_path remove_tree);
use IO::Tee;
use Filesys::DfPortable qw(dfportable);


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
  modelFilter
  valTest
  genTest
  );

# feel free to use your own project versioning scheme here, it just needs
# to be meaningful to you
our $VERSION = '0.5';
(my $svn_version = '$Revision: 10776 $') =~ s/[^\d\.]//g;
my $version = "$VERSION (SVN: $svn_version)";

our $projName = "gfx";      ## <--- You need to adapt this!
our $projEmuWorkroot = undef;
our $projTestbench = undef;

our $projMailOnError = "gfxauto\@intel.com";

my $emuDutFile = undef;
my $GetOpts_ext = undef;
########################################################################
## module specific local variables #####################################
########################################################################

our %ProjOpts = (
    DO              => undef,
    DUT             => undef,
    TARGET          => undef,
    CONTEXT         => "GT_CFG_6X16",
    AV              => 0,
    RESTRICT        => ".*",
    SV              => 0,
    SAVE            => "all",
    TRK             => undef,
    LIST            => undef,
    TB              => undef,
    SEED            => 0,
    TRIGGER         => undef,
    SVA             => undef,
    GROUP           => 0,
    EMULATOR        => undef,
    RUNLIMIT        => 42300,
    LOADLIMIT       => 42300,
    NOCLEAN         => 0,
    DUMP            => 0,
    TCP_SW_CHECK    => 0,
    TCP_SW_CHECK_OPT    => "NO TEST PATH GIVEN. PLEASE FIX IT",
    LILY            => 0,
    LILY_OPT        => undef,
    LILY_AGENT      => undef,
    SIMICS_CMD      => undef,
    CPATH           => "./lib",
    EMUL_PERF       => undef,   # for perf runs
    HD_PROCESS      => 0,   # For post processing Gem based hang tracker - Keith
    RB_ENABLE       => 0,   # for Readback automation - Keith
    RB_ENABLE_CHK     => 0,   # for Readback automation - Keith
    EMAIL           => undef,   # for email on job completion - Keith
    EMU_DO_FILES    => undef,
    TRK_DO_FILES    => undef,
    GSC_FW_PATHS    => undef,
    CFG_XML         => undef,
    FD_PATH     => undef,
    COV_EN     => undef,
    BIGTEST         => 0,
    OFFLINE_WAVE    => 0,
    XEDEBUG_OPTIONS   => [],
	PLUGIN            => undef,
	PLUGIN_ARGUMENTS  => undef,
    ifdef ZRCIEMUL:
    ZRCI              => undef,
    ZRCI_DO           => undef,
    ZRCI_TEMPLATE     => undef,
    UPF               => undef,
    ENABLESCRAMBLING => undef,
    ZTUNE              => undef,
    ZTUNECSV              => undef,
    endif
    );
 
#head1 FUNCTIONS AND HELPERS - projOptions
 
#=head2 projOptions
 
#Called by Emurun to get the options parsed and do some checks both at submission, and when it lands
#on the remote machine.
#Handle the options not handled by emurun.
#To do this, you must
#- Call GetOptions()
#- Pass them to the local hash %ProjOpts - set defaults above!
#=cut
 
##################################################################################################### 
################################## prjOption ######################################################## 
##################################################################################################### 
# Handle the options not handled by emurun.
# To do this, you must
# - call GetOptions()
# - pass them to the local hash %ProjOpts - set defaults above!


sub projOptions() {


    # This function parameter is basically a hack, to be able to pass
    # the "-av" and "-sv"/"-tcp" options back to emurun and the server
    # for handling a special cases there.
    my ($GetOpts) = @_;     # hash reference
    $GetOpts_ext = $GetOpts;

    # handle command line
    Getopt::Long::Configure(qw(pass_through));
    GetOptions (
        'do:s'                => sub { push @{$ProjOpts{DO}}, &emu::sys::getAbsPath(path => $_[1]); },
        'd|dut=s'             => \$ProjOpts{DUT},
        'T|target=s'          => \$ProjOpts{TARGET},
        'context=s'           => \$ProjOpts{CONTEXT},
        'av|rmerge'           => \$ProjOpts{AV},
        'restrict=s'         => \$ProjOpts{RESTRICT},
        'sv|tcp'              => \$ProjOpts{SV},
        'save:s'              => \$ProjOpts{SAVE},
        'trken=s'             => \$ProjOpts{TRK},
        'list=s'             => \$ProjOpts{LIST},
        'tb:s'                => \$ProjOpts{TB},
        'seed=i'              => \$ProjOpts{SEED},
        'trigger:s'           => \$ProjOpts{TRIGGER},
        'sva'                 => \$ProjOpts{SVA},
	ifdef ZRCIEMUL
        'upf'                 => \$ProjOpts{UPF},
        'enablescrambling'    => \$ProjOpts{ENABLESCRAMBLING},
	endif
        'dump'                => \$ProjOpts{DUMP},
        'grp|group'           => \$ProjOpts{GROUP},
        'blk|block'           => sub { &emu::setNetbatchMode("interactive") },
        'emulator=s'          => \$ProjOpts{EMULATOR},
        'runlimit=i'          => \$ProjOpts{RUNLIMIT},
        'loadlimit=i'         => \$ProjOpts{LOADLIMIT},
        'noclean'             => \$ProjOpts{NOCLEAN},
        'tcp_sw_check'        => \$ProjOpts{TCP_SW_CHECK},
        'tcp_sw_check_opt:s'  => \$ProjOpts{TCP_SW_CHECK_OPT},
        'lily'                => \$ProjOpts{LILY},
        'lily_opt:s'          => \$ProjOpts{LILY_OPT},
        'lily_agent:s'        => \$ProjOpts{LILY_AGENT},
        'simics_cmd=s'        => \$ProjOpts{SIMICS_CMD},
        'cpath:s'             => \$ProjOpts{CPATH},
        'emul_perf'           => \$ProjOpts{EMUL_PERF},
        'readback'            => \$ProjOpts{RB_ENABLE}, # for Readback automation - Keith
        'readback_chk'        => \$ProjOpts{RB_ENABLE_CHK}, # for Readback automation regression - Keith
        'HD_process'          => \$ProjOpts{HD_PROCESS}, # For post processing Gem based hang tracker - Keith
        'email=s'               => \$ProjOpts{EMAIL}, # For email on job completion - Keith
        'emu_do_files=s'      => sub { push @{$ProjOpts{EMU_DO_FILES}}, &emu::sys::getAbsPath(path => $_[1]); },
        'fd_path=s'           => \$ProjOpts{FD_PATH},
        'cov_enable'           => \$ProjOpts{COV_EN},
        'trk_do_files=s'      => sub { push @{$ProjOpts{TRK_DO_FILES}}, &emu::sys::getAbsPath(path => $_[1]); },
        'cfg_xml=s'           => sub { push @{$ProjOpts{CFG_XML}}, &emu::sys::getAbsPath(path => $_[1]); },
        'gsc_fw_paths=s'      => sub { push @{$ProjOpts{GSC_FW_PATHS}}, &emu::sys::getAbsPath(path => $_[1]); },
        'bigtest=s'           => \$ProjOpts{BIGTEST},
        'offline_wave'        => \$ProjOpts{OFFLINE_WAVE}, # To generate offline waves for Z1 - Dharmesh
        'xedebug_options=s@'  => \$ProjOpts{XEDEBUG_OPTIONS},
		'plugin=s'	          => \$ProjOpts{PLUGIN},
		'plugin_arguments=s'  => \$ProjOpts{PLUGIN_ARGUMENTS},
	ifdef ZRCIEMUL
        'zrci!'           => \$ProjOpts{ZRCI},
                'zrci_do:s'       => \$ProjOpts{ZRCI_DO},
        'zrci_template:s' => \$ProjOpts{ZRCI_TEMPLATE},
        'ztune!'           => \$ProjOpts{ZTUNE},
        'ztune_csv!'       => \$ProjOpts{ZTUNECSV},
        'streaming!'       => \$ProjOpts{STREAMING},
	endif
    );

    ifdef ZRCIEMUL
    if (!$GetOpts->{TARDIS_DEBUG_REPLAY}) {
        $ProjOpts{ZRCI} = 1;
       if (!$ProjOpts{ZRCI_TEMPLATE}) {
            $ProjOpts{ZRCI_TEMPLATE} = "/nfs/site/disks/mtl_emu_model_disk_003/CommonScripts/zRCI/zRCI_Template.do.V2";
       }     
        $GetOpts->{CUSTOM_DO_TEMPLATE} = $ProjOpts{ZRCI_TEMPLATE};
    }
    endif

   if (defined &emu::test::setOfflineConvertUserLines) {
        my @custom_lines = ();
        push(@custom_lines, "set_option -pre_global_cmd {nbjob run --target fm_express --qslot /VPG/All/SLE/zse --class 32G --mode interactive }");
        &emu::test::setOfflineConvertUserLines(\@custom_lines);
    }

	if(defined $ProjOpts{PLUGIN} and -e $ProjOpts{PLUGIN}){
        print "Loading plugin...\n";
		&Plugins::LoadPlugin($ProjOpts{PLUGIN});
    }

   # Activate standalone run mode
           $ENV{NB_DEDICATED} = 1;
           $ENV{MODEL} = $GetOpts->{MODEL};
           $GetOpts->{CLIENT} = 0;
           $GetOpts->{STANDALONE} = 1;

## For printing model's custom help messages
    if ($GetOpts->{HELP})
    {
       print "Running Model Profile Script : $GetOpts->{MODEL}/sw/cnl_model_profile_gk -model $GetOpts->{MODEL} -modeltype gt -csv -stats -usage -output_path `pwd` \n";
       system("$GetOpts->{MODEL}/sw/cnl_model_profile_gk -model $GetOpts->{MODEL} -modeltype gt -csv -stats -usage -output_path `pwd` ");
       print "\n";
    }

    pod2usage(-exitstatus => 0,
        -input => __FILE__)
        if ($GetOpts->{HELP});


    pod2usage(-exitstatus => 2,
        -message    => "ERROR: please specify a DUT",
        -input => __FILE__)
      unless (defined $ProjOpts{DUT});


if (defined $GetOpts->{RP} ) {
 if (!-e $GetOpts->{RP})
{
&emu::printts("INFO: $GetOpts->{RP} does not exist. Creating directory\n");
system("mkdir -p $GetOpts->{RP}");
system("chmod -R 777 $GetOpts->{RP}");
}
}
####    if (defined $GetOpts->{RP} ) {
####    chomp (my $report_disk_path = "$GetOpts->{RP}" );
####    my $df2 = dfportable("$report_disk_path", 1024 * 1024 * 1024 );
####    &emu::printts ("INFO: Report disk space is $df2->{bavail} GB \n");
####
####    pod2usage(-exitstatus => 2,
####        -message    => "ERROR: Please use another area to save the report, current report area have disk space less than 1GB",
####        -input => __FILE__)
####      unless ($df2->{bavail} >= 1  );
####     }
 if ( $ProjOpts{LILY})

{
     pod2usage(-exitstatus => 2,
        -message    => "ERROR: Please specify absolute path to  Lilyagent",
        -input => __FILE__)
      unless (defined $ProjOpts{LILY_AGENT});

}




    pod2usage(-exitstatus => 2,
        -message    => "ERROR: please specify a target",
        -input => __FILE__)
      unless (defined $ProjOpts{TARGET});

                &emu::verbose(feature => 'test');

    # Allow comma and semicolon separated lists
    @{$ProjOpts{DO}}      = split (/[,;]/,join(',',@{$ProjOpts{DO}}))      if (defined @{$ProjOpts{DO}});

    # ensure all input files exist
    if (&emu::isStage(stage => 'submission')) {
        foreach my $file (@{$ProjOpts{DO}}) {
            pod2usage(-exitstatus => 2,
                -message    => "ERROR: Input file $file does not exist or is not readable\n",
                -input => __FILE__)
                    unless (-r $file);
        }
    }



    # In some cases we don't ever care about the results.
    # This ideally goes to the valTest() function where
    # e.g. all passing tests could be deleted right away.
    if ($ProjOpts{SAVE} =~ /none/) {
        &emu::test::configure(resultSkipCopyBack => 1);
    }

    # Merge the results directly with the result path,
    # otherwise GECCO will automatically find a unique
    # name inside the result folder and store all
    # data into that subfolder.
    if ($ProjOpts{AV}) {
        &emu::test::configure(resultMergeIntoResultpath => 1);
       #rspatel commnted as per neelay's suggestion
       # emu::test::configure(resultMergeIntoResultpath => 0);
    }


    if ($GetOpts->{INTERACTIVE}) {
        &emu::verbose(feature => "testbench", level => 1);
    }

    if ($ProjOpts{AV}) {
        if ($ProjOpts{GROUP}) {
            &emu::printts("INFO: Setting runLimit to 24 Hours for AV -bundle mode from emuproject.pm file \n");
            &emu::test::configure(execLimit => $ProjOpts{RUNLIMIT});
        &emu::printts ("runlimit :\"$ProjOpts{RUNLIMIT}\"\n");
        }

        if ($GetOpts->{FSDB} ne "none" ) {
            &emu::printts("INFO: Setting execLimit to 12 Hours for AV Capture job from emuproject.pm file \n");
            &emu::test::configure(execLimit => 42300 );
         }
     }


    if ($ProjOpts{SV}) {
        # Gfx SV Automation jobs can't be resubmitted, so set a limit.
         &emu::misc::setJobProperties("IterationLimit=1");
         &emu::test::configure(stop_default=> 7200);
         &emu::test::configure(prepLimit=> 7200);
         &emu::printts ("INFO: setting execlimit to:\"$ProjOpts{RUNLIMIT}\"\n");
         &emu::test::configure(execLimit => $ProjOpts{RUNLIMIT});
         &emu::printts("INFO: Setting Model Load Limit Time to $ProjOpts{LOADLIMIT}\n");
         &emu::test::configure(modelLoadLimit => $ProjOpts{LOADLIMIT});

        # If no testcase is given, create a default "dummy" testcase.
        if (!defined @{$GetOpts->{REGLIST}}) {
            if (-e "$GetOpts->{MODEL}/sw/testcase_svmode") {
                push (@{$GetOpts->{REGLIST}}, "$GetOpts->{MODEL}/sw/testcase_svmode");
            } else {
                # Only a fake folder
                my $svautopath = "/tmp/svautomation";
                if (!-e $svautopath){
		make_path($svautopath);
	        system("chmod -R 777 $svautopath ");
		}
                #make_path("$svautopath/memory_in") if (!-e "$svautopath/memory_in");
                push (@{$GetOpts->{REGLIST}}, $svautopath);
            }
        }
    }

    if (defined $ProjOpts{EMULATOR}) {
        $ENV{'NBCLASSAPPEND'} = "server=='$ProjOpts{EMULATOR}'";
    }

    if (defined $ProjOpts{EMAIL}) {
       #print"Email to:$ProjOpts{EMAIL}\n";
       $projMailOnError = $ProjOpts{EMAIL};
    }

   my $emuDutFileName = $GetOpts->{MODEL}."/sw/emuDut.$ProjOpts{DUT}.pm";
    if (-e $emuDutFileName) {
        my $emuDutFile = &emu::doLoadProject(
            namespace => "emu",
            file => $emuDutFileName,
            funcs => qw(genTest dutOptions),
        );

        die "Failed to load DUT file" if (!$emuDutFile);

        &emu::printts("INFO: Loaded DUT file \"$emuDutFile\"\n");

        eval { &emuDut::dutOptions($GetOpts, \%ProjOpts); };
        &emu::printts ("ERROR: Executing dutOptions(): $@") if ($@);
    }
    $projEmuWorkroot = "bld/$ProjOpts{DUT}/$ProjOpts{CONTEXT}.$ProjOpts{TARGET}/emulation";
    #$GetOpts->{MODEL}->addLocator(builddir=>["zse*"]);


 
}
##################################################################################################### 
################################## END OF prjOption ######################################################## 
##################################################################################################### 


##################################################################################################### 
################################### modelFilter  ######################################################## 
##################################################################################################### 

sub modelFilter {
    my $path = shift;

    if ($path !~ m/$ProjOpts{RESTRICT}$/) {

        # AUTO_TEST: VALIDATED
        &emu::printts("INFO: Filtering out $path, due to -restrict $ProjOpts{RESTRICT}\n");
        return 1;
    }
    return 0;
}

#####################################################################################################
################################### END OF modelFilter  ########################################################
#####################################################################################################

#ifdef ZRCIEMUL 

=head1 FUNCTIONS AND HELPERS - genTest
 
=head2 genTest
 
Called by Emurun to generate the 1 or more tests, usually given by the -test argument. For Spark,
 
=cut
 
##################################################################################################### 
################################### genTest  ######################################################## 
##################################################################################################### 
sub genTest {
    eval { &emuDut::genTest($GetOpts_ext, \%ProjOpts); };
    &emu::printts ("ERROR: Executing genTest(): $@") if ($@);
}
 
##################################################################################################### 
################################## END OF genTest  ######################################################## 
##################################################################################################### 

else
# sub modelFilter {
#    my $path = shift;
#
#    if (!defined $ProjOpts{SKU}) {
#        return 0 if ($path =~ /(compile.vmw)|(tbx_.*)/);
#    } else {
#        # Code for SKU handling could go here
#    }
#
#    return 1;
# }
#endif
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

 
##################################################################################################### 
################################### valTest  ######################################################## 
##################################################################################################### 
sub valTest {
   my %res;

   my $stop_reason = &emu::test::getConfiguration('stopReason');
   if (defined $stop_reason && $stop_reason eq "pass") {
      &emu::test::configure(resultSkipCopyBack => 1);
   }

   my $scriptFile = "wrapper_HD_processXe2.csh";
   if($ProjOpts{RB_ENABLE} && $GetOpts_ext->{TARDIS_DEBUG}) {
      $scriptFile = "wrapper_HD_RB_processXe2.csh";
      # If Readback is enabled use the combined HD/RB script
   }

   if($ProjOpts{RB_ENABLE_CHK} && $GetOpts_ext->{TARDIS_DEBUG}) {
      $scriptFile = "wrapper_Regress_readback.csh";
      # Small auto Readback for checkouts
   }
   # $ProjOpts{HD_PROCESS} implies -postscript and -offline_rsync for zPRD and Z1(other runs)
   # $ProjOpts{{OFFLINE_WAVE} for Z1 readback only also implies -postscript and -offline_rsync
   if($ProjOpts{OFFLINE_WAVE} || $ProjOpts{HD_PROCESS} ) {
       #$GetOpts_ext->{OFFLINE_RSYNC} = 1;
       $GetOpts_ext->{POSTSCRIPT} = 1;
   }

   if ($GetOpts_ext->{OFFLINE_RSYNC}) {
       $GetOpts_ext->{OFFLINE_RSYNC} = 1;
   }

   # HD_PROCESS settings are the default for regular offline_rsync as well
   my %options;
   if ($ProjOpts{HD_PROCESS} || $GetOpts_ext->{OFFLINE_RSYNC}) {
	   &emu::printts("Keith: HD_PROCESS set for offline rsync and postscript\n");
	   use Data::Dumper;
	   %options = (
	   POSTSCRIPT_SETTINGS  => {
	      SCRIPT_PATTERN => [$scriptFile],
	      FM => {
		 POOL => "fm_interactive",
		 SLOT => "/VPG/All/VAL/GT",
		 CLASS => "64G && SLES12",
	      },
	      OFFLINE_RSYNC =>  ['*']}
	   );
   }

  # Palladium - offline waves
   if($ProjOpts{OFFLINE_WAVE}) {
	   &emu::printts("OFFLINE_WAVE set for Z1 readback\n");
	   my $scriptFile = "waves_postprocess.csh";
	   %options = (
	   POSTSCRIPT_SETTINGS  => {
	      SCRIPT_PATTERN => [$scriptFile],
	      FM => {
		 POOL => "fm_critical",
		 SLOT => "/VPG/TigerLakeGT/cadence_testing",
		 CLASS => "SLES11 && 450G",
	      },
		OFFLINE_RSYNC =>  ['*']});
   }

   my $options_hash_ref = \%options;

   my %args = (
      path => undef,
      testname => undef,
      testnameunique => undef,
      modelname => undef,
      testpath => undef,
      resultpath => undef,
      modelroot => undef,
      modelname => undef,
      sourceenv => undef,
      cycles => 0,
      frequecy => 0,
      efficiency => 0,
      platform => undef,
      @_,
   );

   eval { %res = &emuDut::valTest($GetOpts_ext, \%ProjOpts, @_); };

   if ((($ProjOpts{SV}) && ($ProjOpts{LILY})) || $ProjOpts{PLUGIN}) {
      eval { %res = &emuDut::valTest($GetOpts_ext, \%ProjOpts, @_); };
      &emu::printts ("ERROR: Executing valTest(): $@") if ($@);
   }elsif ($ProjOpts{SV}){
           $res{code} = 0;
   }else {
      eval { %res = &emuDut::valTest($GetOpts_ext, \%ProjOpts, @_); };
      &emu::printts ("ERROR: Executing valTest(): $@") if ($@);
   }

   if( $GetOpts_ext->{POSTSCRIPT}  ||  $GetOpts_ext->{OFFLINE_RSYNC}) {
      &emu::printts("OFFLINE RSYNC and/or POSTSCRIPT set\n");
      if (!defined $options_hash_ref->{POSTSCRIPT_SETTINGS}) {
         &emu::printts("WARNING: Missing POSTSCRIPT_SETTINGS in options.yml, post scripts will not be run\n");
      }
      else {
         $res{postscript} = &emu::schedule::addPostScript(
         test => $args{test},
         settings => $options_hash_ref->{POSTSCRIPT_SETTINGS},
         sourceenv => $args{sourceenv},
         resultpath => $args{resultpath},
         path => $args{path},
         postscript => $GetOpts_ext->{POSTSCRIPT},
         offline_rsync => $GetOpts_ext->{OFFLINE_RSYNC});
         if (!defined $res{postscript}) {
            &emu::printts("WARNING: No gecco_postscript.csh was created, post scripts will not be run\n");
         }
      }
      ######## READBACK POST PROCESSING END ########
   }


   return %res;
}

##################################################################################################### 
################################### END OF valTest  ######################################################## 
##################################################################################################### 


########################################################################
#ifndef ZRCIEMUL
# genTest()
########################################################################
sub genTest {
    eval { &emuDut::genTest($GetOpts_ext, \%ProjOpts); };
    &emu::printts ("ERROR: Executing genTest(): $@") if ($@);
}
endif
########################################################################
# cleanup
########################################################################
# Project specific cleanup script
#

#ifdef ZRCIEMUL
=head1 FUNCTION AND HELPERS - preSubmissionCmd
 
=head2 preSubmissionCmd
 
TODO : Optional to set this
Called by Emurun right before setting up the submission command.
 
=cut
#endif

##################################################################################################### 
################################### preSubmissionCmd  ######################################################## 
##################################################################################################### 
 

sub preSubmissionCmd {
    my $rc = 0;

    eval { $rc = &emuDut::preSubmissionCmd($GetOpts_ext, \%ProjOpts); };
    &emu::printts ("ERROR: Executing preSubmissionCmd(): $@") if ($@);

    return $rc;
}
 
##################################################################################################### 
################################### END OF preSubmissionCmd  ######################################################## 
##################################################################################################### 


#ifdef ZRCIEMUL
=head2 postSubmissionCmd
 
TODO : Optional to set this
Called by Emurun after sending the submission command.
If job is submitted in blocking mode it is called after job completes
If job is submitted in submit and forget mode, it is called right after job submission
 
=cut
##################################################################################################### 
################################### postSubmissionCmd  ######################################################## 
##################################################################################################### 

#endif




########################################################################
# postSubmissioncmd()
########################################################################
sub postSubmissionCmd {
    my $GetOpts        = shift;
    my $run_hash_ref   = shift;
    my $tests_hash_ref = shift;
    my $exitcode       = shift;
    if ($GetOpts_ext->{OFFLINE_RSYNC_WO_NB}) {
        if (-e "gecco_postscript.csh") {
            &emu::printts("INFO: Offline rsync started\n");
            system("gecco_postscript.csh");
            &emu::printts("INFO: Offline rsync finished\n");
        } else {
            &emu::printts("INFO: Offline rsync w/o NB requested, but no gecco_postscript.csh found to execute\n");
        }
    }
}

########################################################################
# cleanup
########################################################################





##################################################################################################### 
################################## CleanUp  ######################################################## 
##################################################################################################### 


sub cleanup {
    # These are hash references:
    my ($GetOpts, $run, $tests) = @_;
}



##################################################################################################### 
################################## END OF CleanUp  ######################################################## 
##################################################################################################### 



__END__


#####################################################################################################
################################## Flags Description  ########################################################
#####################################################################################################


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

=item B<-restrict REGEX>

Hooks into the filtering function, which can restrict available builds to match the restricted path.
The value given here can be a regular expression, and if it matches any portion of the build's path
then that model will be usable.


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
=item B<-emurun_command>

Refer to <Model_Name>_usage.txt file generated for model download instructions

# vim: set tabstop=8 expandtab shiftwidth=4 softtabstop=4:
