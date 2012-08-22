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
from DBSAPI.dbsRun import DbsRun
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:
	"""
	for aRun in range(23000, 24000):

        	run = DbsRun (
                	RunNumber=aRun,
                	NumberOfEvents= 100,
               		NumberOfLumiSections= 20,
                	TotalLuminosity= 2222,
                	StoreNumber= 123,
                	StartOfRun= 12345,
                	EndOfRun= 45678,
                	)

    		print "Creating run", aRun
	
    		api.insertRun (run)

	run = DbsRun (
                RunNumber=1,
                NumberOfEvents= 100,
                NumberOfLumiSections= 20,
                TotalLuminosity= 2222,
                StoreNumber= 123,
                StartOfRun= 12345,
                EndOfRun= 45678,
                )

	"""

	run = DbsRun (
                RunNumber=1,
                NumberOfEvents= 0,
                TotalLuminosity= 0,
                StoreNumber= 0,
                )


	api.insertRun (run)


except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


print "Done"

