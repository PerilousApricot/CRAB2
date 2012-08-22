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


def isIn(aparent, parentList):
	for i in parentList:
		#print "checking ---> %s " %i['LogicalFileName']
		if i['LogicalFileName'] == aparent['LogicalFileName']:
			return True
	return False
	

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:
	#unmerged1 = sys.argv[1]
	#unmerged2 = sys.argv[2]
	merged1 = sys.argv[1]
	merged2 = sys.argv[2]

	merged2FileList = api.listFiles(path = merged2, retriveList=['retrive_parent'])
	merged1FileList = api.listFiles(path = merged1, retriveList=['retrive_parent'])
	#unmerged1FileList = api.listFiles(path = unmerged1, retriveList=['retrive_child'])
	for afile in merged2FileList:
		aFileLFN = afile['LogicalFileName']
		print "Checking File %s in Merged dataset2" %aFileLFN
		parentListM2 = afile['ParentList']
		for aparent in parentListM2:
			aparentLFN = aparent['LogicalFileName']
			print "Getting  parent of %s ( is grandparent of original file)" %aparentLFN
			tmpParentList = api.listFiles(patternLFN=aparentLFN, retriveList=['retrive_parent'])
			for atmpParent in tmpParentList:
				grandParentList = atmpParent['ParentList']
				for agrandParent in grandParentList:
					print "Going to check the grand parent %s" %agrandParent['LogicalFileName']
					for aFileInM1 in merged1FileList:
						parentListM1 = aFileInM1['ParentList']
						#print "checking the grandparent in %s" %parentListM1
						if isIn(agrandParent, parentListM1):
							fileM1LFN = aFileInM1['LogicalFileName']
							print '__________________________________________________________'
							print 'INSERTING the real parent %s in Merged dataset2' %fileM1LFN
							print '__________________________________________________________\n\n'
							api.insertFileParent(aFileLFN, fileM1LFN)
						else:
							print "Grand parent  and parent did not match"

			if not isIn(aparent, merged1FileList):
				print '****************************************************************************'
				print 'DELETING the parent %s from Merged dataset2' %aparentLFN
				print '****************************************************************************\n\n'
				api.deleteFileParent(aFileLFN, aparentLFN)
			
	# Delete all the parents of merged1 dataset
	for afile in merged1FileList:
		print "Cheking File %s in Merged dataset1" %afile['LogicalFileName']
		parentList = afile['ParentList']
		for aparent in parentList:
			print '****************************************************************************'
			print 'DELETING the parent %s from Merged dataset1' %aparent['LogicalFileName']
			print '****************************************************************************\n\n'
			api.deleteFileParent(afile['LogicalFileName'], aparent['LogicalFileName'])



except DbsApiException, ex:
	print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
	if ex.getErrorCode() not in (None, ""):
		print "DBS Exception Error Code: ", ex.getErrorCode()
print "Done"
			
