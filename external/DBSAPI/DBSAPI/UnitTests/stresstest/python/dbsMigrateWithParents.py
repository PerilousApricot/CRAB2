#!/usr/bin/env python
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
import sys
import os
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi


try:
	optManager  = DbsOptionParser()
	(opts,args) = optManager.getOpt()
	args = {}
	args['url']='http://cmssrv17.fnal.gov:8989/DBS_1_0_5_STABLE/servlet/DBSServlet' 
	#args['version']='DBS_1_0_7'
	args['mode']='POST'
	api = DbsApi(args)
      
	#api = DbsApi(opts.__dict__)
	srcURL = sys.argv[1]
	dstURL = sys.argv[2]
	path = sys.argv[3]
	block = ""
	if len(sys.argv) > 4 :
		block = sys.argv[4]

	api.migrateDatasetContents(srcURL, dstURL, path, block , False, True)
	#print api.listPrimaryDatasets();

except DbsApiException, ex:
	print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
	if ex.getErrorCode() not in (None, ""):
		print "DBS Exception Error Code: ", ex.getErrorCode()
print "Done"
			
