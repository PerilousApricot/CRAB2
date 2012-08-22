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
  
  # List all storage elements
  print ""
  print "deleting storage element (replica from Block)  ...."
  print api.deleteReplicaFromBlock("/QCD_Pt_120_170/CMSSW_1_2_3-Spring07-JetMet-1174666666/GEN-SIM#a7ae4f12-9af9-4d2a-9bec-cfa047cc488e", "sc.cr.cnaf.infn.it")
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

