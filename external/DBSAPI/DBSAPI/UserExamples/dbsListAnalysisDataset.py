#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
#
import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser

try:
  optManager  = DbsOptionParser()
  (opts,args) = optManager.getOpt()
  api = DbsApi(opts.__dict__)
  
  print "Analysis Daatset...."
  #for analysis in api.listAnalysisDataset("*t005", "/test_primary_001/TestProcessedDS001/SIM"):
  #for analysis in api.listAnalysisDataset(version=1):
  #for analysis in api.listAnalysisDataset(path="/RelVal131QCD_pt600_800/CMSSW_1_3_1-1176201507/GEN-SIM-DIGI-RECO", version=0):
  for analysis in api.listAnalysisDataset():
     #print "  %s" % analysis
     print "  %s, %s" % (analysis['Name'], analysis['Version'])
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

