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
from DBSAPI.dbsRun import DbsRun
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

                            
print "Adding a TIER"

try:

    lfn = 'TEST_LFN_1_c7141b3d-3212-4030-bb08-dc977dbe6e25'
    api.insertTierInFile (lfn, 'GEN')
    api.insertTierInFile (lfn, 'SIM')
    api.insertTierInFile (lfn, 'DIGI')
    api.insertTierInFile (lfn, 'RECO')

    print "Result: %s" % 'GEN' 

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

