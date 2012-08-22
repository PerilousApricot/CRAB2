import random
import os
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser


optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

serverInfo = api.getServerInfo()
isMYSQL = serverInfo['InstanceType']
isGlobal = serverInfo['InstanceName']
 
def testAllQueriesInFile(qFile = 'queries.txt'):
		qList = open(qFile).readlines()
		for aQuery in qList:
			aQuery = aQuery.strip()
			if aQuery.find(" dq") != -1:
                                if isMYSQL=="MYSQL":
                                      print "Skipping DQ queries for MySQL instance"
                                      continue

			try: 
			    if not aQuery.startswith('#'):
				print aQuery,
				api.executeQuery(aQuery)
				print '   <<<<<<<< PASSED >>>>>>>>'
			except:
				print '   <<<<<<<< FAILED >>>>>>>>'
testAllQueriesInFile()
