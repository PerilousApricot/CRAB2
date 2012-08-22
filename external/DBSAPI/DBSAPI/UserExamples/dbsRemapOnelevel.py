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




optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:
	merged1 = sys.argv[1]

	merged1FileList = api.listFiles(path = merged1, retriveList=['retrive_parent'])
	#unmerged1FileList = api.listFiles(path = unmerged1, retriveList=['retrive_child'])
	for afile in merged1FileList:
		aFileLFN = afile['LogicalFileName']
		print "Checking File %s in Merged dataset1" %aFileLFN
		parentListM1 = afile['ParentList']
		for aparent in parentListM1:
			aparentLFN = aparent['LogicalFileName']
			print "Getting  parent of %s ( is grandparent of original file)" %aparentLFN
			tmpParentList = api.listFiles(patternLFN=aparentLFN, retriveList=['retrive_parent'])
			for atmpParent in tmpParentList:
				grandParentList = atmpParent['ParentList']
				for agrandParent in grandParentList:
					print '__________________________________________________________'
					print 'INSERTING the real parent %s in Merged dataset1' %agrandParent['LogicalFileName']
					print '__________________________________________________________\n\n'
					api.insertFileParent(aFileLFN, agrandParent['LogicalFileName'])


			print '****************************************************************************'
			print 'DELETING the parent %s from Merged dataset1' %aparentLFN
			print '****************************************************************************\n\n'
			api.deleteFileParent(aFileLFN, aparentLFN)
			


except DbsApiException, ex:
	print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
	if ex.getErrorCode() not in (None, ""):
		print "DBS Exception Error Code: ", ex.getErrorCode()
print "Done"
			
