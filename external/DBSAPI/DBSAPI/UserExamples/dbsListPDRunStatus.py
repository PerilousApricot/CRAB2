#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsRun import DbsRun
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:
    #select Dataset, Complete from ProcDSRuns where Run=361;
    #run=62243
    run=""
    path='/Cosmics/BeamCommissioning08_CRUZET4_V4P_CSCSkim_trial_v3/RECO'
    for runStatus in api.listProcDSRunStatus(path, run):
	print "RunNumber: "+str(runStatus['RunNumber'])+" Status:"+str(runStatus['Done'])


except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()



