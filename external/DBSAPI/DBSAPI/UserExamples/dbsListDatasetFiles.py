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

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)
  
try :
	# A PATH +ve case
  	print "Trying Good PATH"
  	for afile in api.listDatasetFiles(datasetPath="/RelVal131QCD_pt600_800/CMSSW_1_3_1-1176201507/GEN-SIM-DIGI-RECO"):
     		print "PATH  %s" % afile['LogicalFileName']

except DbsApiException, ex:
  	print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  	if ex.getErrorCode() not in (None, ""):
    		print "DBS Exception Error Code: ", ex.getErrorCode()

try :
  	print "Trying Good ADS"
  	# An ADS +ve case
  	for afile in api.listDatasetFiles(datasetPath="/RelVal131QCD_pt600_800/CMSSW_1_3_1-1176201507/GEN-SIM-DIGI-RECO/ALLFILES"):
     		print "ADS  %s" % afile['LogicalFileName']

except DbsApiException, ex:
        print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
        if ex.getErrorCode() not in (None, ""):
                print "DBS Exception Error Code: ", ex.getErrorCode()

try :
  	print "Trying WRONG PATH"
  	# A PATH -ve case (No existent Path)
  	for afile in api.listDatasetFiles(datasetPath="/RelVal131QCD0/CMSSW_1_3_1/GEN-SIM-DIGI-RECO"):
     		print "  %s" % afile['LogicalFileName']

except DbsApiException, ex:
        print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
        if ex.getErrorCode() not in (None, ""):
                print "DBS Exception Error Code: ", ex.getErrorCode()
	print "GOOD Error was expected"
  
try :
  	print "Trying WRONG ADS"
  	# An ADS -ve case (Non existent ADS)
  	for afile in api.listDatasetFiles(datasetPath="/RelVal131QCD_pt600_800/CMSSW_1_3_1-1176201507/GENSIMDIGIRECO/NOTALLFILES"):
     		print "  %s" % afile['LogicalFileName']
	print "GOOD Error was expected"

except DbsApiException, ex:
        print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
        if ex.getErrorCode() not in (None, ""):
                print "DBS Exception Error Code: ", ex.getErrorCode()
	print "GOOD Error was expected"

try :
  	print "Just a random string"
  	# An ADS -ve case (Non existent ADS)
  	for afile in api.listDatasetFiles(datasetPath="JustARandomString"):
     		print "  %s" % afile['LogicalFileName']
	print "GOOD Error was expected"

except DbsApiException, ex:
        print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
        if ex.getErrorCode() not in (None, ""):
           print "DBS Exception Error Code: ", ex.getErrorCode()
	print "GOOD Error was expected"
