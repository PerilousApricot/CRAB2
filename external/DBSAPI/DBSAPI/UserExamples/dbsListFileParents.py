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
  
  try:
   # List all parents of the file
   print ""
   #for file in api.listFileParents("/store/relval/CMSSW_2_1_0_pre10/RelValSingleMuPt1/GEN-SIM-DIGI-RAW-HLTDEBUG/IDEAL_V5_v2/0000/B0342E93-965C-DD11-AC96-0019DB29C614.root"):
   for file in api.listFileParents("NEW_TEST0006_20080731_11h32m58s"):
     print "  %s" % file['LogicalFileName']
  except DbsDatabaseError,e:
   print e
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

