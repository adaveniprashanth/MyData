#!/usr/intel/bin/perl
use strict ; 
use warnings;




my $val_dir = "/nfs/site/disks/lnl_soc_disk_001/ashish/soc_improvment";
my $snapshot_model="/nfs/site/disks/lnl_soc_regress_001/ashish/soc_package/snapshot_model/LNL/ww43p4_LNL_SOC_RTL1p0_post_rev1_snapshot";
my $previous_pkg_path="/nfs/site/disks/lnl_soc_regress_001/ashish/soc_package/LNL_IPX_UPLOAD/RTL1p0/xe2lpm_media_common-22ww24e-package/smedia_top/";
my $fulsim_tool_path="/nfs/site/disks/cobalt_lnl_release/ReleaseBinaries/Cobalt/LNL/220207-66629";
my $interactive_paths="$val_dir"."/gk_regress/ww43p4_LNL_SOC_RTL1p0_post_rev1_snapshot/sm/MEDIA_LPM_1VD1VE_SD.o3c.vpi.sipdfx.gtsynth.goldenrpt.default64/INTERACTIVE";

sub val_dir{
	return $val_dir;
}
sub snapshot_model{
	return $snapshot_model;
}
sub previous_pkg_path{
	return $previous_pkg_path;
}
sub fulsim_tool_path{
	return $fulsim_tool_path;
}
sub interactive_paths{
	return $interactive_paths;
}
1;