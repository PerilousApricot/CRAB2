#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
#
import sys
import random
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsPrimaryDataset import DbsPrimaryDataset
from DBSAPI.dbsFileBlock import DbsFileBlock
from DBSAPI.dbsProcessedDataset import DbsProcessedDataset
from DBSAPI.dbsOptions import DbsOptionParser


optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)


block = DbsFileBlock (
	Name="/SiStripCommissioning08-edm/Online/RAW#e7fff7a5-7681-4361-8dd1-cd568eafd362"
	#Name="/Wmunu/CMSSW_1_6_0-HLT-1191261655/GEN-SIM-DIGI-RECO#0c8376b7-3467-48e5-ace1-31f53492d6c1"
         )

print "Opening a block %s" % block

try:
    print api.openBlock (block)
    #print api.closeBlock (block)
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


print "Done"

