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
from DBSAPI.dbsBranchInfo import DbsBranchInfo
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

branchInfo = DbsBranchInfo(
		Hash="001234565798685",
		Description="This is a test",
		Content="<Branch><Branch Name='testbranch01'/><Branch Name='testbranch02'/></Branch>",
		BranchList=['testbranch01', 'testbranch02']
		)
 
#print "Creating an algorithm %s" % algo

try:
    api.insertBranchInfo(branchInfo)

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

