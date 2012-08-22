#!/usr/bin/env python
#
# Revision: $"
# Id: $"
#
import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:
	api.updateProcDSDesc("/TTbar-mcatnlo/Summer09-MC_31X_V3-v1/GEN-SIM-RAW", "Support Request 111878")

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


print "Description Changed"

