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
  print "deleting a block and moving it into recycle bin."
  #print api.deleteBlock("/TestPrimary_001_20071116_13h32m06s/TestProcessed_20071116_13h32m06s/GEN-SIM", "/TestPrimary_001_20071116_13h32m06s/TestProcessed_20071116_13h32m06s/GEN-SIM#016714")
  print api.undeleteBlock("/TestPrimary_001_20071116_13h32m06s/TestProcessed_20071116_13h32m06s/GEN-SIM", "/TestPrimary_001_20071116_13h32m06s/TestProcessed_20071116_13h32m06s/GEN-SIM#016714")
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

