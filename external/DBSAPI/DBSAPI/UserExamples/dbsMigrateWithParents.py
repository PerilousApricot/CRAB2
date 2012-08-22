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
	# These dummy values are required to create the DbsApi object so let them here
	args['url']='http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet' 
	args['version']='DBS_2_0_8'
	args['mode']='POST'
	api = DbsApi(args)

	srcURL = sys.argv[1]
	dstURL = sys.argv[2]
	path = sys.argv[3]
	block = ""
	if len(sys.argv) > 4 :
		block = sys.argv[4]

	api.migrateDatasetContents(srcURL, dstURL, path, block , False, True)

except DbsApiException, ex:
	print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
	if ex.getErrorCode() not in (None, ""):
		print "DBS Exception Error Code: ", ex.getErrorCode()
print "Done"
			
