#!/usr/bin/env python
#
# $Revision: 1.1 $"
# $Id: dbsListRecycleBin.py,v 1.1 2009/05/12 18:44:27 yuyi Exp $"
#
#
# Unit tests for the DBS CGI implementation.

import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser

try:
  optManager  = DbsOptionParser()
  (opts,args) = optManager.getOpt()
  api = DbsApi(opts.__dict__)

  print "listRecycleBin...."
  for dataset in api.listRecycleBin('/Minbias/CMSSW_1_8_0_pre8-RelVal-1202227044-HLT-SpecialTracking/GEN-SIM-DIGI-RECO'):
     print "  %s" % dataset
  for dataset in api.listRecycleBin():
     print "  %s" % dataset
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()
print "Done"

