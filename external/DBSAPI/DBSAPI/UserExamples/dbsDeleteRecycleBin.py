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
  
  print ""
  print "deleting proc dataset and moving it into recycle bin."
  #print api.deleteProcDS("/This_is_a_test_primary_63424b0a-7986-4e5a-85d6-70eb4b91e8e7/CHILD_This_is_a_test_processed_63424b0a-7986-4e5a-85d6-70eb4b91e8e7/SIM")
  #print api.deleteRecycleBin("/AH115bb_tau_tau_2l/Summer08_IDEAL_V9_v1/GEN-SIM-RECO", "/AH115bb_tau_tau_2l/Summer08_IDEAL_V9_v1/GEN-SIM-RECO#845505c9-f47f-41f6-b786-e13c74515756")
  print api.deleteRecycleBin("/AH115bb_tau_tau_2l/Summer08_IDEAL_V9_v1/GEN-SIM-RECO", "/AH115bb_tau_tau_2l/Summer08_IDEAL_V9_v1/GEN-SIM-RECO#b84c9340-1c74-4fc2-a26f-2f1ed0164863")

  print api.deleteRecycleBin("/AH115bb_tau_tau_2l/Summer08_IDEAL_V9_v1/GEN-SIM-RAW", "/AH115bb_tau_tau_2l/Summer08_IDEAL_V9_v1/GEN-SIM-RAW#7f0e573b-9200-41a7-a8af-76268ab3f970")
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

