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
  print api.deleteProcDS("/tW_inclusive/CMSSW_1_6_9-2l2nu_SkimPres-tW_inclusive/USER")
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

