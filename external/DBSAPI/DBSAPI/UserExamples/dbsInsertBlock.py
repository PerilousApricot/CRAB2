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

primary = DbsPrimaryDataset (Name = "test_primary_001a")

proc = DbsProcessedDataset (
         PrimaryDataset=primary,
         TierList=['GEN', 'SIM'],
	 Path='/test_primary_001/TestProcessedDS001/GEN-SIM'
         #Name="TestProcessedDSWithADSParent",
         )

block = DbsFileBlock (
         #Name="/test_primary_001/TestProcessedDSWithADSParent/GEN-SIM#12345"
         Name="/test_primary_001/TestProcessedDS001/GEN-SIM#12345"
         )

print "Creating block %s" % block

try:
    # ALL Valid Options below
    #print api.insertBlock (proc)
    #print api.insertBlock (proc, block)
    #print api.insertBlock ("/test_primary_001/TestProcessedDS001/GEN-SIM", "/test_primary_001/TestProcessedDS001/GEN-SIM#123456")
    print api.insertBlock ("/test_primary_001/TestProcessedDS001/GEN-SIM", "/test_primary_001/TestProcessedDS001/GEN-SIM#123456" , ['se1', 'se2', 'se3'])

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

