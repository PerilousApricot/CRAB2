#!/usr/bin/env python
#
import time
import sys
import random
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser

dstURL = sys.argv[1]

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
args = {}
args['url'] = dstURL 
args['mode']='POST'
api = DbsApi(args)

try:
	
	print "\n\nListing Datasets "
	paths = api.listDatasetPaths()
	ranIndex = random.randint(1,len(paths))
	#myDataset = paths[ranIndex]
	myDataset = "/Wjets-sherpa/Summer08_IDEAL_V12_v1/GEN-SIM-RAW"
	print "Selected dataset is %s", myDataset

	print "\nListing Blocks "
	blocks = api.listBlocks(myDataset)
	#print blocks
	
	print "\n Listing Files "
	files = api.listFiles(path = myDataset, retriveList=["all"])
	#print files
	#for path in paths:
	#	print path
	

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


print "Done"
