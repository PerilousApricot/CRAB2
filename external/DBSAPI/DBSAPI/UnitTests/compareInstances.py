#!/usr/bin/env python
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
import sys
import os
import unittest	
import validate as valid
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi

class TestFunctions(unittest.TestCase):
	def setUp(self):
		print "Do nothing"
	def testNothing(self):
		print "Do nothing"

class CompareInstances(unittest.TestCase):

        def __init__(self):
		#, srcURL, dstURL):
		try:
			srcURL = "http://cmsdbsdev1.cern.ch:8880/DBSANZ/servlet/DBSServlet"
			dstURL = "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet"
	
        		optManager  = DbsOptionParser()
        		(opts,args) = optManager.getOpt()
        		args = {}
        		args['url']=srcURL
        		args['mode']='POST'
			args['version']='DBS_2_0_5'
        		self.srcApi = DbsApi(args)
			args['url']=dstURL
			self.dstApi = DbsApi(args)

		except DbsApiException, ex:
			print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
			if ex.getErrorCode() not in (None, ""):
				print "DBS Exception Error Code: ", ex.getErrorCode()

	def run(self):
		count=0
	       	paths = self.srcApi.listDatasetPaths()
		for path in paths:
			self.path=path
			print "Now processing : %s " % path
			pathTokens = path.split("/")
			self.primName = pathTokens[1]
			self.procName = pathTokens[2]
			try:
				self.testPrimary()
                        except DbsApiException, ex:
                                print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
                                if ex.getErrorCode() not in (None, ""):
                                        print "DBS Exception Error Code: ", ex.getErrorCode()
                        except AssertionError, ex:
                                print "FAILED testPrimary"
				print "Exception %s" %str(ex)
                        except:
                                print "FAILED testPrimary, unknown error"
			try:
				self.testProcessed()
                        except DbsApiException, ex:
                                print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
                                if ex.getErrorCode() not in (None, ""):
                                        print "DBS Exception Error Code: ", ex.getErrorCode()
                        except AssertionError, ex:
                                print "FAILED testProcessed"
				print "Exception %s" %str(ex)
                        except:
                                print "FAILED testProcessed, unknown error"
                        try:

				self.testBlock()
                        except DbsApiException, ex:
                                print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
                                if ex.getErrorCode() not in (None, ""):
                                        print "DBS Exception Error Code: ", ex.getErrorCode()
                        except AssertionError, ex:
                                print "FAILED testBlock"
				print "Exception %s" %str(ex)
                        except:
                                print "FAILED testBlock, unknown error"
			"""
                        try:
				self.testRun()
				
                        except DbsApiException, ex:
                                print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
                                if ex.getErrorCode() not in (None, ""):
                                        print "DBS Exception Error Code: ", ex.getErrorCode()
                        except AssertionError, ex:
                                print "FAILED testRun"
				print "Exception %s" %str(ex)
                        except:
                                print "FAILED testRun, unknown error"
			"""
                        try:
				self.testFile()
               		except DbsApiException, ex:
                       		print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
                       		if ex.getErrorCode() not in (None, ""):
                               		print "DBS Exception Error Code: ", ex.getErrorCode()	
               		except AssertionError, ex:
                       		print "FAILED testFile"
				print "Exception %s" %str(ex)
               		except:
                       		print "FAILED testFile, unknown error"
				print "back..."

			if count > 10: break
			count += 1
			print "Done"

	def testPrimary(self):
		print 'testPrimary'
		primarySrcList = self.srcApi.listPrimaryDatasets(self.primName)
		primaryDstList = self.dstApi.listPrimaryDatasets(self.primName)
		valid.assertPrimary(self, primarySrcList[0], primaryDstList[0])	

	def testProcessed(self):
		print 'testProcessed'
		procSrcList = self.srcApi.listProcessedDatasets(patternPrim = self.primName, patternProc = self.procName)
		procDstList = self.dstApi.listProcessedDatasets(patternPrim = self.primName, patternProc = self.procName)
		valid.assertProc(self, procSrcList[0], procDstList[0])
		for i in range(len(procSrcList[0]['AlgoList'])):
			valid.assertAlgo(self, procSrcList[0]['AlgoList'][i], procDstList[0]['AlgoList'][i])
			
		parentSrcList = self.srcApi.listDatasetParents(self.path)
		parentDstList = self.dstApi.listDatasetParents(self.path)
		parentSrcList.sort(key=lambda obj: obj['Name'])
		parentDstList.sort(key=lambda obj: obj['Name'])
		for i in range(len(parentSrcList)):
			self.assertEqual(parentSrcList[i]['PrimaryDataset']['Name'], parentDstList[i]['PrimaryDataset']['Name'])
			self.assertEqual(parentSrcList[i]['Name'], parentDstList[i]['Name'])
		
	def testBlock(self):
		print 'testBlock'
		blockSrcList = self.srcApi.listBlocks(self.path)
		blockDstList = self.dstApi.listBlocks(self.path)
		blockSrcList.sort(key=lambda obj: obj['Name'])
		blockDstList.sort(key=lambda obj: obj['Name'])
		for i in range(len(blockSrcList)):
			valid.assertBlock(self, blockSrcList[i], blockDstList[i])

			#Block Parentage test can only be applied to new servers
			parentSrcBlock = self.srcApi.listBlockParents(blockSrcList[i])
			parentDstBlock = self.srcApi.listBlockParents(blockDstList[i])
			parentSrcBlock.sort(key=lambda obj: obj['Name'])
			parentDstBlock.sort(key=lambda obj: obj['Name'])
			for j in range(len(parentDstBlock)):
				valid.assertBlock(self, parentSrcBlock[j], parentDstBlock[j])

	def testRun(self):
		print 'testRun'
		runSrcList = self.srcApi.listRuns(self.path)
		runDstList = self.dstApi.listRuns(self.path)
		runSrcList.sort(key=lambda obj: obj['RunNumber'])
		runDstList.sort(key=lambda obj: obj['RunNumber'])
		#print runSrcList
		for i in range(len(runSrcList)):
		#for runInDBS in runList:
			valid.assertRun(self, runSrcList[i], runDstList[i])

	def testFile(self):
		print 'testFile'

		fileSrcList = self.srcApi.listFiles(path = self.path, retriveList = ['all'], otherDetails = True)
		fileDstList = self.dstApi.listFiles(path = self.path, retriveList = ['all'], otherDetails = True)
		fileSrcList.sort(key=lambda obj: obj['LogicalFileName'])
		fileDstList.sort(key=lambda obj: obj['LogicalFileName'])

		for i in range(len(fileSrcList)):
			valid.assertFile(self, fileSrcList[i], fileDstList[i])

			algoSrcList = fileSrcList[i]['AlgoList']
			algoDstList = fileDstList[i]['AlgoList']
			for j in range(len(algoSrcList)):
				valid.assertAlgo(self, algoSrcList[j], algoDstList[j])

			lumiSrcList = fileSrcList[i]['LumiList']
			lumiDstList = fileDstList[i]['LumiList']
			lumiSrcList.sort(key=lambda obj: obj['LumiSectionNumber'])
			lumiDstList.sort(key=lambda obj: obj['LumiSectionNumber'])
			for j in range(len(lumiSrcList)):
				valid.assertLumi(self, lumiSrcList[j], lumiSrcList[j])


			parentSrcList = fileSrcList[i]['ParentList']
			parentDstList = fileDstList[i]['ParentList']
			parentSrcList.sort(key=lambda obj: obj['LogicalFileName'])
			parentDstList.sort(key=lambda obj: obj['LogicalFileName'])
			for j in range(len(parentSrcList)):
				valid.assertFile(self, parentSrcList[j], parentDstList[j])

			runSrcList = fileSrcList[i]['RunsList']	
			runDstList = fileDstList[i]['RunsList']	

			runSrcList.sort(key=lambda obj: obj['RunNumber'])
			runDstList.sort(key=lambda obj: obj['RunNumber'])
			for j in range(len(runSrcList)):
				valid.assertRun(self, runSrcList[j], runDstList[j])



if __name__ == '__main__':
	#unittest.main()
	compare=CompareInstances()
	compare.run()

