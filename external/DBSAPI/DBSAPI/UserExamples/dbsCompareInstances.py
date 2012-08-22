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

import pdb

try:

  if (len(sys.argv) < 3) :
      print "You need to provide Local instance and Global instance URLs"
      sys.exit(1)

  localArgs={}
  globalArgs={}

  localArgs['url']=sys.argv[1] 
  apiLocal = DbsApi(localArgs)

  globalArgs['url']=sys.argv[1]
  globalApi = DbsApi(globalArgs)

  print "List ALL Processed Datasets from : %s " % localArgs['url']
  localDatasets = apiLocal.listProcessedDatasets("*")
  # Let us see if this dataset is in Global already
  for localProc in localDatasets:

	partialName = "/%s/%s" % (localProc['PrimaryDataset']['Name'], localProc['Name'])

	print "*** Testing for Dataset %s/* " %partialName

	globalCounterPart = globalApi.listProcessedDatasets(patternPrim=localProc['PrimaryDataset']['Name'], 
								patternProc=localProc['Name'])

        if globalCounterPart in (None, []):
		print "*** WARNING: Dataset %s is not found in Global, is it not transferred yet ?" %partialName
		continue

	#if localProc['RunsList'] != globalCounterPart[0]['RunsList']:
	#	print "*** WARNING: Dataset %s RunsList mismatch, Runs added later ?" %partialName
	
        if localProc['PhysicsGroup'] != globalCounterPart[0]['PhysicsGroup']:
                print "*** ERROR: Dataset %s PhysicsGroup mismatch" %partialName
		print "Details: localInstance['PhysicsGroup']: %s" %str(localProc['PhysicsGroup'])
		print "Details: globalInstance['PhysicsGroup']: %s" %str(globalCounterPart[0]['PhysicsGroup'])	
	
	if localProc['TierList'] != globalCounterPart[0]['TierList']:
                print "*** WARNING: Dataset %s TierList mismatch, Tiers added later ?" %partialName
		print "Details: localInstance['TierList']: %s" %str(globalCounterPart[0]['TierList'])
		print "Details: globalInstance['TierList']: %s" %str(localProc['TierList'])
					
        if localProc['PathList'] != globalCounterPart[0]['PathList']:
                print "*** WARNING: Dataset %s PathList mismatch, Paths added later ?" %partialName
		print "Details: localInstance['PathList']: %s" %str(localProc['PathList'])
		print "Details: globalInstance['PathList']: %s" %str(globalCounterPart[0]['PathList'])
		
	for anAlgo in localProc['AlgoList']:
		if anAlgo not in globalCounterPart[0]['AlgoList']:
			print "*** WARNING: Dataset %s AlgoList mismatch, Algo added later ?" %partialName

	#Compare Parentage
        #List Blocks
	#  Check closed blocks vs Open blocks 
        #Compare files

	
 

 			
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

