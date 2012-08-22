#!/usr/bin/env python
#
import sys
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi

try:
  #optManager  = DbsOptionParser()
  #(opts,args) = optManager.getOpt()

  srcURL="http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet"
  dstURL="https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_admin/servlet/DBSServlet"

  argsSrc={}
  argsSrc['url']=srcURL
  argsSrc['version']="DB_2_0_8"  
  apiSrc = DbsApi(argsSrc)

  argsDst={}
  argsDst['url']=dstURL
  argsDst['version']="DB_2_0_8"  
  apiDst = DbsApi(argsDst)
  
  bad_datasets=['/ppMuMuX/Summer09-MC_31X_V3-v1/GEN-SIM-RECO',
		'/QCD_EMEnriched_Pt30to80/Summer09-MC_31X_V3-v1/GEN-SIM-RECO',
		'/QCD_Pt80/Summer09-MC_31X_V3-v1/GEN-SIM-RECO',
		'/TTbar/Summer09-MC_31X_V3-v1/GEN-SIM-RECO',
		'/Wenu/Summer09-MC_31X_V3-v1/GEN-SIM-RECO',
		'/Zee/Summer09-MC_31X_V3-v1/GEN-SIM-RECO',
		'/Zmumu/Summer09-MC_31X_V3-v1/GEN-SIM-RECO']

  for adataset in bad_datasets:
  	# Mark this dataset as VALID		
	apiDst.updateProcDSStatus(adataset, "VALID") 	
	# Migrate immedate parents of this dataset
	apiSrc.migrateDatasetContents(srcURL, dstURL, adataset, "" , False, True)	
	# RE-INSERTION of processed dataset SHOULD create the processed dataset with parents !!!
	token = adataset.split("/")
    	orig_ds = apiSrc.listProcessedDatasets(token[1], token[3], token[2])
    	#Create the dataset at destination
    	api.insertProcessedDataset (proc)


except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()      

print "Done"

