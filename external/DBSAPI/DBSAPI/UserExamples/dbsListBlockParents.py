#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
# API Unit tests for the DBS JavaServer.
import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser

try:
  optManager  = DbsOptionParser()
  (opts,args) = optManager.getOpt()
  api = DbsApi(opts.__dict__)
  for dataset in api.listDatasetPaths():
	print "\n %s" %str(dataset)
	print "Dataset parent: %s" %str(api.listPathParents)
  	for block in api.listBlocks(dataset):
		print "block: %s" %str(block['Name'])
  		for parent in api.listBlockParents(block_name=block['Name']):
     			print "Parent:  %s" % str(parent['Name'])

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


