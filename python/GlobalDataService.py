#!/usr/bin/env python

from ProdCommon.SiteDB.CmsSiteMapper import CmsSEMap

data_service_prefix     = 'root://xrootd.unl.edu/'
cms_se = CmsSEMap()
# Sites that can handle being read FROM
global_data_svc_hosts   = cms_se.match("T2_US_*","cmseos.fnal.gov")
# Sites that can have jobs sent TO them
global_data_svc_targets = cms_se.match("T2_US_*,T3_US_Omaha,T3_US_Vanderbilt_EC2")

# helper functions for the global data service
def modifyJobFilenames( job ):
    new_files = []
    for file in job[0].split(','):
        if file.find("://") >= 0:
            new_files.append(file)
        else:
            new_files.append(data_service_prefix + file)
    job[0] = ','.join(new_files)

def modifyPossibleJobLocations( job ):
    # logic: If there is a copy of the block at any of the global_data_hosts
    # sites, then set the "available sites" to anything in USCMS.
    site_list = job['dlsDestination']
    site_set = set(site_list)
    site_set.intersection_update(global_data_svc_hosts)
    if site_set:
        job['dlsDestination'] = global_data_svc_targets

def modifyPossibleBlockLocations( unsorted_sites ):
    # logic: If there is a copy of the block at any of the global_data_svc
    # sites, then set the "available sites" to anything in USCMS. 
    for block, site_list in unsorted_sites.items():
        site_set = set(site_list)
        site_set.intersection_update(global_data_svc_hosts)
        if site_set:
            unsorted_sites[block] = list(global_data_svc_targets)
        else:
            unsorted_sites[block] = []

