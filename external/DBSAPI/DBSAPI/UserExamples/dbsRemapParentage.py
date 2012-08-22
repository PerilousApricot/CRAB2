#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:
    print api.remap('/RelValSingleMuPt10/CMSSW_2_1_0_pre10_IDEAL_V5_v4/GEN-SIM-DIGI-RAW-HLTDEBUG', '/RelValSingleMuPt10/CMSSW_2_1_0_pre10_IDEAL_V5_v4/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO', '/RelValSingleMuPt10/CMSSW_2_1_0_pre10_IDEAL_V5_v4/GEN-SIM-DIGI-RAW-HLTDEBUG#870b391e-5590-40c5-a063-8109b1a23a8f')


except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


print "Done"

