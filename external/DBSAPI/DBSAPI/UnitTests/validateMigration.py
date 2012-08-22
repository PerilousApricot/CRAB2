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
"""
srcURL = sys.argv[1]
dstURL = sys.argv[2]
path = sys.argv[3]
"""
#srcURL = "http://cmssrv48.fnal.gov:8383/DBS/servlet/DBSServlet"
#srcURL = "http://cmsdbsdev1.cern.ch:8880/DBSANZ/servlet/DBSServlet"
#dstURL = "http://cmssrv48.fnal.gov:8383/DBSlocal/servlet/DBSServlet"
#path = "/DY_mumu_10/CMSSW_1_3_1-Spring07-1349/GEN-SIM-DIGI-RECO"
#path = "/Cosmics/Commissioning08-MW32_v1/RAW"

srcURL = "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet"
#dstURL = "http://cmssrv48.fnal.gov:8383/DBSlocal/servlet/DBSServlet"
#dstURL = "http://vocmsvm05.cern.ch:8880/INT2RG_admin/servlet/DBSServlet"
dstURL = "http://cmssrv17.fnal.gov:8989/DBSTEST/servlet/DBSServlet"
#path = "/DY_mumu_10/CMSSW_1_3_1-Spring07-1349/GEN-SIM-DIGI-RECO"
#path = "/Cosmics/Commissioning08-MW32_v1/RAW"
#path = "/RelValSinglePiPt100/CMSSW_3_0_0_pre7_IDEAL_30X_v1/GEN-SIM-RECO"
path = "/RelValSinglePiPt100/CMSSW_3_0_0_pre7_IDEAL_30X_v1/GEN-SIM-RECO"

try:
	optManager  = DbsOptionParser()
	(opts,args) = optManager.getOpt()
	args = {}
	args['url']=dstURL
	args['mode']='POST'
	api = DbsApi(args)
      
	#api = DbsApi(opts.__dict__)
	block = ""
	if len(sys.argv) > 4 :
		block = sys.argv[4]

	api.migrateDatasetContents(srcURL, dstURL, path, block , False, True)

except DbsApiException, ex:
	print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
	if ex.getErrorCode() not in (None, ""):
		print "DBS Exception Error Code: ", ex.getErrorCode()
print "Done"

args = {}
args['url'] = srcURL 
args['mode']='POST'
args['version']='DBS_2_0_9'
srcApi = DbsApi(args)
args['url'] = dstURL 
args['version']='DBS_2_0_9'
dstApi = DbsApi(args)
pathTokens = path.split("/")
primName = pathTokens[1]
procName = pathTokens[2]

class Test_001(unittest.TestCase):
	def testPrimary(self):
		print 'testPrimary'
		primarySrcList = srcApi.listPrimaryDatasets(primName)
		primaryDstList = dstApi.listPrimaryDatasets(primName)
		valid.assertPrimary(self, primarySrcList[0], primaryDstList[0])	

class Test_002(unittest.TestCase):
	def testProcessed(self):
		print 'testProcessed'
		procSrcList = srcApi.listProcessedDatasets(patternPrim = primName, patternProc = procName)
		procDstList = dstApi.listProcessedDatasets(patternPrim = primName, patternProc = procName, patternDT=pathTokens[3])
		#print processedInDBS
		print '\n\n\nprocSrcList',procSrcList
		print '\n\n\nprocDstList',procDstList
		valid.assertProc(self, procSrcList[0], procDstList[0])
		for i in range(len(procSrcList[0]['AlgoList'])):
			valid.assertAlgo(self, procSrcList[0]['AlgoList'][i], procDstList[0]['AlgoList'][i])

			
		parentSrcList = srcApi.listDatasetParents(path)
		parentDstList = dstApi.listDatasetParents(path)
		parentSrcList.sort(key=lambda obj: obj['Name'])
		parentDstList.sort(key=lambda obj: obj['Name'])
		for i in range(len(parentSrcList)):
			self.assertEqual(parentSrcList[i]['PrimaryDataset']['Name'], parentDstList[i]['PrimaryDataset']['Name'])
			self.assertEqual(parentSrcList[i]['Name'], parentDstList[i]['Name'])
				
class Test_003(unittest.TestCase):
	def testBlock(self):
		print 'testBlock'
		blockSrcList = srcApi.listBlocks(path)
		blockDstList = dstApi.listBlocks(path)
		blockSrcList.sort(key=lambda obj: obj['Name'])
		blockDstList.sort(key=lambda obj: obj['Name'])
		for i in range(len(blockSrcList)):
			valid.assertBlock(self, blockSrcList[i], blockDstList[i])


			#Block Parentage test can only be applied to new servers
			parentSrcBlock = srcApi.listBlockParents(blockSrcList[i])
			parentDstBlock = srcApi.listBlockParents(blockDstList[i])
			parentSrcBlock.sort(key=lambda obj: obj['Name'])
			parentDstBlock.sort(key=lambda obj: obj['Name'])
			for j in range(len(parentDstBlock)):
				valid.assertBlock(self, parentSrcBlock[j], parentDstBlock[j])

		


class Test_004(unittest.TestCase):
	def testRun(self):
		print 'testRun'
		runSrcList = srcApi.listRuns(path)
		runDstList = dstApi.listRuns(path)
		runSrcList.sort(key=lambda obj: obj['RunNumber'])
		runDstList.sort(key=lambda obj: obj['RunNumber'])
		#print runSrcList
		for i in range(len(runSrcList)):
		#for runInDBS in runList:
			valid.assertRun(self, runSrcList[i], runDstList[i])

class Test_005(unittest.TestCase):
	def test_01_File(self):
		print 'testFile'

		fileSrcList = srcApi.listFiles(path = path, retriveList = ['all'], otherDetails = True)
		fileDstList = dstApi.listFiles(path = path, retriveList = ['all'], otherDetails = True)
		fileSrcList.sort(key=lambda obj: obj['LogicalFileName'])
		fileDstList.sort(key=lambda obj: obj['LogicalFileName'])

		
		for i in range(len(fileSrcList)):
			valid.assertFile(self, fileSrcList[i], fileDstList[i])

			algoSrcList = fileSrcList[i]['AlgoList']
			algoDstList = fileDstList[i]['AlgoList']
			algoSrcList.sort(key=lambda obj: obj['ApplicationFamily'])
			algoDstList.sort(key=lambda obj: obj['ApplicationFamily'])
			#print algoSrcList
			#print "_______________________"
			#print algoDstList
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
			#print runSrcList
			#print "____________________________________________"
			#print runDstList
			for j in range(len(runSrcList)):
				valid.assertRun(self, runSrcList[j], runDstList[j])



if __name__ == '__main__':

        unittest.main()


