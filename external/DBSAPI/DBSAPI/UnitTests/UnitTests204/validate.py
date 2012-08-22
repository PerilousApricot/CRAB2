import random
import os
import unittest
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsApiException import *
from DBSAPI.dbsAlgorithm import DbsAlgorithm
from DBSAPI.dbsFileBlock import DbsFileBlock
from DBSAPI.dbsRun import DbsRun
from DBSAPI.dbsFile import DbsFile
from DBSAPI.dbsLumiSection import DbsLumiSection
from DBSAPI.dbsQueryableParameterSet import DbsQueryableParameterSet
from DBSAPI.dbsPrimaryDataset import DbsPrimaryDataset
from DBSAPI.dbsProcessedDataset import DbsProcessedDataset
from DBSAPI.dbsDQFlag import DbsDQFlag
from DBSAPI.dbsRunLumiDQ import DbsRunLumiDQ

from DBSAPI.dbsOptions import DbsOptionParser


optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)
 
isGlobal = api.getServerInfo()['InstanceName']
def genRandom():
	return  os.popen('uuidgen').readline().strip()

ran = genRandom()
primName = 'test_Primary_' + ran
primType = 'test'

algoExe1 = 'test_Exe1_' + ran
algoVer1 = 'test_Ver1_' + ran
algoFam1 = 'test_Fam1_' + ran
psHash1 = 'test_Hash1_' + ran
psName1 = 'test_Pname1_' + ran
psVer1 = 'test_Pver1_' + ran
psType1 = 'test_Ptype1_' + ran
psAnno1 = 'test_Panno1_' + ran
psCon1 = 'test_Con1_' + ran

algoExe2 = 'test_Exe2_' + ran
algoVer2 = 'test_Ver2_' + ran
algoFam2 = 'test_Fam2_' + ran
psHash2 = 'test_Hash2_' + ran
psName2 = 'test_Pname2_' + ran
psVer2 = 'test_Pver2_' + ran
psType2 = 'test_Ptype2_' + ran
psAnno2 = 'test_Panno2_' + ran
psCon2 = 'test_Con2_' + ran

algoExeM = 'test_ExeM_' + ran
algoVerM = 'test_VerM_' + ran
algoFamM = 'test_FamM_' + ran
psHashM = 'test_HashM_' + ran
psNameM = 'test_PnameM_' + ran
psVerM = 'test_PverM_' + ran
psTypeM = 'test_PtypeM_' + ran
psAnnoM = 'test_PannoM_' + ran
psConM = 'test_ConM_' + ran



runNumber = random.choice(range(10000))
runNumEvents = 1200
numLumi = 1234
totalLumi = 3456
storeNum = 8907
startRun = 23456
endRun = 12345

invalidStatus = 'INVALID'
validStatus = 'VALID'
procName1 = 'test_processed_1_' + ran
procName2 = 'test_processed_2_' + ran
procNameM = 'test_processed_M_' + ran
phyGrp = 'BPositive'
procStatus = validStatus
tier1 = 'GEN'
tier2 = 'SIM'
era = 'test_Era_' + ran
tag = 'test_Tag_' + ran
path1 = '/' + primName + '/' + procName1 + '/' + tier1 + '-' + tier2
path2 = '/' + primName + '/' + procName2 + '/' + tier1 + '-' + tier2
pathM = '/' + primName + '/' + procNameM + '/' + tier1 + '-' + tier2

lsNumber1 = random.choice(range(10000))
stEvNum1 = 1234
endEvNum1 = 3234
stLumiTime1 = 67890
endLumiTime1 = 98990

lsNumber2 = random.choice(range(10000))
stEvNum2 = 2234
endEvNum2 = 3239
stLumiTime2 = 47890
endLumiTime2 = 88990

se1 = 'test_se1_' + ran
se2 = 'test_se2_' + ran
seM = 'test_seM_' + ran
blockName1 = path1 + '#' + str(random.choice(range(10000)))
blockName2 = path2 + '#' + str(random.choice(range(10000)))
blockNameM = pathM + '#' + str(random.choice(range(10000)))

fileName1 = 'test_file_name_1_' + ran
fileCkecksum1 = 'test_cksum_1_' + ran
fileNumEvents1 = 34567
fileSize1 = 123987
fileStatus1 = validStatus
fileValidStatus1 = validStatus
fileType1 = 'EDM'

fileName2 = 'test_file_name_2_' + ran
fileNumEvents2 = 84567
fileCkecksum2 = 'test_cksum_2_' + ran
fileSize2 = 122657
fileStatus2 = validStatus
fileValidStatus2 = validStatus
fileType2 = 'STREAMER'

fileNameM = 'test_file_name_M_' + ran
fileNumEventsM = 234567
fileCkecksumM = 'test_cksum_M_' + ran
fileSizeM = 56322657
fileStatusM = validStatus
fileValidStatusM = validStatus
fileTypeM = 'STREAMER'

qim_name1="Tracker_Global"
qim_name2="TIB_Local"
qim_name3="TIB_Power"
qim_int="TIB_Percentage"

primObj = DbsPrimaryDataset (Name = primName, Type = primType)
algoObj1 = DbsAlgorithm (
		ExecutableName = algoExe1,
		ApplicationVersion = algoVer1,
		ApplicationFamily = algoFam1,
		ParameterSetID=DbsQueryableParameterSet(
			Hash = psHash1,
			Name = psName1,
			Version = psVer1,
			Type = psType1,
			Annotation = psAnno1,
			Content = psCon1
			)
		)
algoObj2 = DbsAlgorithm (
		ExecutableName = algoExe2,
		ApplicationVersion = algoVer2,
		ApplicationFamily = algoFam2,
		ParameterSetID=DbsQueryableParameterSet(
			Hash = psHash2,
			Name = psName2,
			Version = psVer2,
			Type = psType2,
			Annotation = psAnno2,
			Content = psCon2
			)
		)

algoObjM = DbsAlgorithm (
		ExecutableName = algoExeM,
		ApplicationVersion = algoVerM,
		ApplicationFamily = algoFamM,
		ParameterSetID=DbsQueryableParameterSet(
			Hash = psHashM,
			Name = psNameM,
			Version = psVerM,
			Type = psTypeM,
			Annotation = psAnnoM,
			Content = psConM
			)
		)

runObj = DbsRun (
		RunNumber = runNumber,
		NumberOfEvents = runNumEvents,
		NumberOfLumiSections = numLumi,
		TotalLuminosity = totalLumi,
		StoreNumber = storeNum,
		StartOfRun = startRun,
		EndOfRun = endRun,
		)

procObj1 = DbsProcessedDataset (
		PrimaryDataset = primObj, 
		Name = procName1, 
		AcquisitionEra = era,
		GlobalTag = tag,
		PhysicsGroup = phyGrp,
		Status = procStatus,
		TierList = [tier1, tier2],
		AlgoList = [algoObj1, algoObj2],
		XtCrossSection=1.1
		)

procObj2 = DbsProcessedDataset (
		PrimaryDataset = primObj, 
		Name = procName2, 
		AcquisitionEra = era,
		GlobalTag = tag,
		PhysicsGroup = phyGrp,
		Status = procStatus,
		TierList = [tier1, tier2],
		AlgoList = [algoObj1, algoObj2],
		ParentList = [path1],
		RunsList = [runNumber],
		XtCrossSection=2.2
		)

procObjM = DbsProcessedDataset (
		PrimaryDataset = primObj, 
		Name = procNameM, 
		AcquisitionEra = era,
		GlobalTag = tag,
		PhysicsGroup = phyGrp,
		Status = procStatus,
		TierList = [tier1, tier2],
		AlgoList = [algoObjM],
		RunsList = [runNumber],
		XtCrossSection=3.3
		)

lumiObj1 = DbsLumiSection (
		LumiSectionNumber = lsNumber1,
		StartEventNumber = stEvNum1,
		EndEventNumber = endEvNum1,
		LumiStartTime = stLumiTime1,
		LumiEndTime = endLumiTime1,
		RunNumber = runNumber,
		)

lumiObj2 = DbsLumiSection (
		LumiSectionNumber = lsNumber2,
		StartEventNumber = stEvNum2,
		EndEventNumber = endEvNum2,
		LumiStartTime = stLumiTime2,
		LumiEndTime = endLumiTime2,
		RunNumber = runNumber,
		)


blockObj1 = DbsFileBlock (
		Name = blockName1
		)

blockObj2 = DbsFileBlock (
		Name = blockName2
		)

blockObjM = DbsFileBlock (
		Name = blockNameM
		)

fileObj1 = DbsFile (
		Checksum = fileCkecksum1,
		LogicalFileName = fileName1,
		NumberOfEvents = fileNumEvents1,
		FileSize = fileSize1,
		Status = fileStatus1,
		ValidationStatus = fileValidStatus1,
		FileType = fileType1,
		Dataset = procObj1,
		AlgoList = [algoObj1],
		LumiList = [lumiObj1],
		TierList = [tier1, tier2],
		AutoCrossSection=1.0
		)

fileObj2 = DbsFile (
		Checksum = fileCkecksum2,
		LogicalFileName = fileName2,
		NumberOfEvents = fileNumEvents2,
		FileSize = fileSize2,
		Status = fileStatus2,
		ValidationStatus = fileValidStatus2,
		FileType = fileType2,
		Dataset = procObj2,
		AlgoList = [algoObj2],
		LumiList = [lumiObj2],
		TierList = [tier1, tier2],
		ParentList = [fileName1],
		AutoCrossSection=2.0
		)

fileObjM = DbsFile (
		Checksum = fileCkecksumM,
		LogicalFileName = fileNameM,
		NumberOfEvents = fileNumEventsM,
		FileSize = fileSizeM,
		Status = fileStatusM,
		ValidationStatus = fileValidStatusM,
		FileType = fileTypeM,
		Dataset = procObjM,
		AlgoList = [algoObjM],
		TierList = [tier1, tier2],
		Block = blockObjM,
		AutoCrossSection=3.0
		)

qim_value_g = "GOOD"
qim_value_b = "BAD"
qim_value_u = "UNKNOWN"
qim_value_i = 100

qim_flag_g = DbsDQFlag (
                        Name = qim_name1,
                        Value = qim_value_g,
                        )
qim_flag_b = DbsDQFlag (
                        Name = qim_name2,
                        Value = qim_value_b,
                        )

qim_flag_u = DbsDQFlag (
                        Name = qim_name3,
                        Value = qim_value_u,
                        )

qim_flag_int = DbsDQFlag (
                        Name = qim_int,
                        Value = str(qim_value_i),
                        )
run_dq = DbsRunLumiDQ (
                        RunNumber=runNumber,
			#LumiSectionNumber=lsNumber1,
                        DQFlagList = [qim_flag_g, qim_flag_b, qim_flag_u, qim_flag_int]
                        )

run_dq_search_criteria = DbsRunLumiDQ (
				RunNumber=runNumber,
                                #LumiSectionNumber=lsNumber1,
                                DQFlagList = [qim_flag_g, qim_flag_b, qim_flag_u, qim_flag_int]
                        )

def assertAlgo(test, algoIn1, algoIn2):
	test.assertEqual(algoIn1['ExecutableName'], algoIn2['ExecutableName'])
	test.assertEqual(algoIn1['ApplicationVersion'], algoIn2['ApplicationVersion'])
	test.assertEqual(algoIn1['ApplicationFamily'], algoIn2['ApplicationFamily'])
	test.assertEqual(algoIn1['ParameterSetID']['Hash'], algoIn2['ParameterSetID']['Hash'])

def assertAlgoPS(test, algoIn1, algoIn2):
	assertAlgo(test, algoIn1, algoIn2)
	test.assertEqual(algoIn1['ParameterSetID']['Hash'], algoIn2['ParameterSetID']['Hash'])
	test.assertEqual(algoIn1['ParameterSetID']['Name'], algoIn2['ParameterSetID']['Name'])
	test.assertEqual(algoIn1['ParameterSetID']['Version'], algoIn2['ParameterSetID']['Version'])
	test.assertEqual(algoIn1['ParameterSetID']['Type'], algoIn2['ParameterSetID']['Type'])
	test.assertEqual(algoIn1['ParameterSetID']['Annotation'], algoIn2['ParameterSetID']['Annotation'])
	test.assertEqual(algoIn1['ParameterSetID']['Content'], algoIn2['ParameterSetID']['Content'])

def assertProc(test, procIn1, procIn2):
	test.assertEqual(procIn1['Name'], procIn2['Name'])
	test.assertEqual(procIn1['PrimaryDataset']['Name'], procIn2['PrimaryDataset']['Name'])
	test.assertEqual(procIn1['AcquisitionEra'], procIn2['AcquisitionEra'])
	test.assertEqual(procIn1['GlobalTag'], procIn2['GlobalTag'])
	test.assertEqual(procIn1['PhysicsGroup'], procIn2['PhysicsGroup'])
	test.assertEqual(procIn1['Status'], procIn2['Status'])
	test.assertEqual(procIn1['XtCrossSection'], procIn2['XtCrossSection'])

def assertRun(test, runIn1, runIn2):
	test.assertEqual(runIn1['RunNumber'], runIn2['RunNumber'])
	test.assertEqual(runIn1['NumberOfEvents'], runIn2['NumberOfEvents'])
	test.assertEqual(runIn1['NumberOfLumiSections'], runIn2['NumberOfLumiSections'])
	test.assertEqual(runIn1['TotalLuminosity'], runIn2['TotalLuminosity'])
	test.assertEqual(runIn1['StoreNumber'], runIn2['StoreNumber'])
	test.assertEqual(runIn1['StartOfRun'], runIn2['StartOfRun'])
	test.assertEqual(runIn1['EndOfRun'], runIn2['EndOfRun'])

def assertFile(test, fileIn1, fileIn2):
	test.assertEqual(fileIn1['Checksum'], fileIn2['Checksum'])
	test.assertEqual(fileIn1['LogicalFileName'], fileIn2['LogicalFileName'])
	test.assertEqual(fileIn1['NumberOfEvents'], fileIn2['NumberOfEvents'])
	test.assertEqual(fileIn1['FileSize'], fileIn2['FileSize'])
	test.assertEqual(fileIn1['Status'], fileIn2['Status'])
	#test.assertEqual(fileIn1['ValidationStatus'], fileIn2['ValidationStatus'])
	test.assertEqual(fileIn1['FileType'], fileIn2['FileType'])
	test.assertEqual(fileIn1['AutoCrossSection'], fileIn2['AutoCrossSection'])
	
def assertLumi(test, lumiIn1, lumiIn2):
	test.assertEqual(lumiIn1['LumiSectionNumber'], lumiIn2['LumiSectionNumber'])
	test.assertEqual(lumiIn1['StartEventNumber'], lumiIn2['StartEventNumber'])
	test.assertEqual(lumiIn1['EndEventNumber'], lumiIn2['EndEventNumber'])
	test.assertEqual(lumiIn1['LumiStartTime'], lumiIn2['LumiStartTime'])
	test.assertEqual(lumiIn1['LumiEndTime'], lumiIn2['LumiEndTime'])
	test.assertEqual(lumiIn1['RunNumber'], lumiIn2['RunNumber'])
	


class Test1(unittest.TestCase):
	def testPrimary(self):
		print 'testPrimary'
		api.insertPrimaryDataset (primObj)
		primaryList = api.listPrimaryDatasets(primName)
		self.assertEqual(len(primaryList), 1)
		for primaryInDBS in primaryList:
			self.assertEqual(primName, primaryInDBS['Name'])
			self.assertEqual(primType, primaryInDBS['Type'])

class Test2(unittest.TestCase):
	def testAlgorithm(self):
		print 'testAlgorithm'
		api.insertAlgorithm (algoObj1)
		algoList = api.listAlgorithms(patternVer = algoVer1, patternFam = algoFam1, patternExe = algoExe1, patternPS = psHash1)
		self.assertEqual(len(algoList), 1)
		for algoInDBS in algoList:
			assertAlgoPS(self, algoObj1, algoInDBS)


class Test3(unittest.TestCase):
	def testProcessed(self):
		print 'testProcessed'
		api.insertPrimaryDataset (primObj)
		api.insertAlgorithm (algoObj1)
		api.insertAlgorithm (algoObj2)

	
		api.insertRun (runObj)
		api.insertProcessedDataset (procObj1)
		api.insertProcessedDataset (procObj2)
		procList = api.listProcessedDatasets(patternPrim = primName, patternProc = procName2)
		self.assertEqual(len(procList), 1)
		for processedInDBS in procList:
			#print processedInDBS
			assertProc(self, procObj2, processedInDBS)
			self.assertEqual(len(processedInDBS['AlgoList']), 2)
			for algoInDBS in processedInDBS['AlgoList']:
				if(algoInDBS['ExecutableName'] == algoExe1):
					assertAlgo(self, algoObj1, algoInDBS)
				else:
					if (algoInDBS['ExecutableName'] == algoExe2):
						assertAlgo(self, algoObj2, algoInDBS)
					else:
						print 'algo %s is not expected', algoInDBS
						self.assertEqual(1, 2)


			self.assertEqual(len(processedInDBS['TierList']), 2)
			for tierInDBS in processedInDBS['TierList']:
				if(tierInDBS != tier1 and tierInDBS != tier2):
					print 'tier %s is not expected', tierInDBS
					self.assertEqual(1, 2)
					
		
			parentList = api.listPathParents(procObj2)	
			#parentList = api.listDatasetParents(procObj2)
			# 2 ka parent is 1
			#FIXME
			#self.assertEqual(len(parentList), 1)
			for parentProcInDBS in parentList:
				self.assertEqual(primName, parentProcInDBS['PrimaryDataset']['Name'])
				self.assertEqual(procName1, parentProcInDBS['Name'])
				


class Test4(unittest.TestCase):
	def testBlock(self):
		print 'testBlock'
		api.insertBlock (procObj1, blockObj1, [se1, se2])
		api.insertBlock (procObj2, blockObj2, [se2])
		blockList = api.listBlocks(procObj1)
		self.assertEqual(len(blockList), 1)
		for blockInDBS in api.listBlocks(procObj1):
			#print blockInDBS
			self.assertEqual(blockName1, blockInDBS['Name'])
			self.assertEqual(path1, blockInDBS['Path'])
			if isGlobal != "GLOBAL": 
				self.assertEqual(len(blockInDBS['StorageElementList']), 2)
				for seInDBS in blockInDBS['StorageElementList']:
					if(seInDBS['Name'] != se1 and seInDBS['Name'] != se2):
						print 'storage element %s is not expected', seInDBS
						self.assertEqual(1, 2)

				


class Test5(unittest.TestCase):
	def testRun(self):
		print 'testRun'
		runList = api.listRuns(procObj2)
		self.assertEqual(len(runList), 1)
		for runInDBS in runList:
			assertRun(self, runObj, runInDBS)

class Test6(unittest.TestCase):
	def testFile(self):
		print 'testFile'
		api.insertFiles(procObj1, [fileObj1], blockObj1)
		api.insertFiles(procObj2, [fileObj2], blockObj2)
		fileList = api.listFiles(path = path2, retriveList = ['all'], otherDetails = True)
		self.assertEqual(len(fileList), 1)
		for fileInDBS in fileList:
			assertFile(self, fileObj2, fileInDBS)
			algoList = fileInDBS['AlgoList']
			self.assertEqual(len(algoList), 1)
			for algoInDBS in algoList:
				assertAlgo(self, algoObj2, algoInDBS)

			lumiList = fileInDBS['LumiList']
			self.assertEqual(len(lumiList), 1)
			for lumiInDBS in lumiList:
				assertLumi(self, lumiObj2, lumiInDBS)
		
			#tierList = fileInDBS['TierList']
			#self.assertEqual(len(tierList), 2)
			#for tierInDBS in tierList:
			#	if(tierInDBS != tier1 and tierInDBS != tier2):
			#		print 'tier %s is not expected', tierInDBS
			#		self.assertEqual(1, 2)

			parentList = fileInDBS['ParentList']
			self.assertEqual(len(parentList), 1)
			for parentInDBS in parentList:
				#print fileObj1
				#print parentInDBS
				assertFile(self, fileObj1, parentInDBS)

			runList = fileInDBS['RunsList']	
			self.assertEqual(len(runList), 1)
			for runInDBS in runList:
				self.assertEqual(2, runInDBS['NumberOfLumiSections'])
				runInDBS['NumberOfLumiSections'] = runObj['NumberOfLumiSections']
				assertRun(self, runObj, runInDBS)

	def testParentOfProcDS(self):
		print 'testParentOfProcDS'
		parentList = api.listDatasetParents(procObj2)
		self.assertEqual(len(parentList), 1)
		for parentProcInDBS in parentList:
			self.assertEqual(primName, parentProcInDBS['PrimaryDataset']['Name'])
			self.assertEqual(procName1, parentProcInDBS['Name'])


	def testInvalidFile(self):
		print 'testInvalidFile'
		api.updateFileStatus(fileName1, invalidStatus, "No Description")
		fileList = api.listFiles(path = path1, retriveList = ['all'])
		self.assertEqual(len(fileList), 1)
		for fileInDBS in fileList:
			self.assertEqual(invalidStatus, fileInDBS['Status'])

		fileList = api.listFiles(path = path1)
		self.assertEqual(len(fileList), 0)

		api.updateFileStatus(fileName1, validStatus, "No Description")
		fileList = api.listFiles(path = path1)
		self.assertEqual(len(fileList), 1)

class Test7(unittest.TestCase):
	def testMergedProcessed(self):
		print 'testMergedProcessed'

		api.insertMergedDataset (procObj2, procNameM, algoObjM)
		procList = api.listProcessedDatasets(patternPrim = primName, patternProc = procNameM)
		self.assertEqual(len(procList), 1)
		for processedInDBS in procList:
			# Auto CRosss section for Merged Datasets will not be equal
			processedInDBS['XtCrossSection']=procObjM['XtCrossSection']
			assertProc(self, procObjM, processedInDBS)
			self.assertEqual(len(processedInDBS['AlgoList']), 3)
			
			for algoInDBS in processedInDBS['AlgoList']:
				if(algoInDBS['ExecutableName'] == algoExe1):
					assertAlgo(self, algoObj1, algoInDBS)
				else:
					if (algoInDBS['ExecutableName'] == algoExe2):
						assertAlgo(self, algoObj2, algoInDBS)
					else:
						if (algoInDBS['ExecutableName'] == algoExeM):
							assertAlgo(self, algoObjM, algoInDBS)
						else:
							print 'algo %s is not expected', algoInDBS
							self.assertEqual(1, 2)


			self.assertEqual(len(processedInDBS['TierList']), 2)
			for tierInDBS in processedInDBS['TierList']:
				if(tierInDBS != tier1 and tierInDBS != tier2):
					print 'tier %s is not expected', tierInDBS
					self.assertEqual(1, 2)
					
				
class Test8(unittest.TestCase):
	def testMergedFile(self):
		print 'testMergedFile'
		api.insertBlock (procObjM, blockObjM, [seM])
		#print fileName1
		#print fileName2
		#print fileObjM
		api.insertMergedFile([fileName1, fileName2], fileObjM)
		fileList = api.listFiles(path = pathM, retriveList = ['all'], otherDetails = True)
		self.assertEqual(len(fileList), 1)
		for fileInDBS in fileList:
			assertFile(self, fileObjM, fileInDBS)
			algoList = fileInDBS['AlgoList']
			self.assertEqual(len(algoList), 3)
			for algoInDBS in algoList:
				if(algoInDBS['ExecutableName'] == algoExe1):
					assertAlgo(self, algoObj1, algoInDBS)
				else:
					if (algoInDBS['ExecutableName'] == algoExe2):
						assertAlgo(self, algoObj2, algoInDBS)
					else:
						if (algoInDBS['ExecutableName'] == algoExeM):
							assertAlgo(self, algoObjM, algoInDBS)
						else:
							print 'algo %s is not expected', algoInDBS
							self.assertEqual(1, 2)


			lumiList = fileInDBS['LumiList']
			self.assertEqual(len(lumiList), 2)
			for lumiInDBS in lumiList:
				if(lumiInDBS['LumiSectionNumber'] == lsNumber1):
					assertLumi(self, lumiObj1, lumiInDBS)
				else:
					if(lumiInDBS['LumiSectionNumber'] == lsNumber2):
						assertLumi(self, lumiObj2, lumiInDBS)
					else:
						print 'lumi %s is not expected', lumiInDBS
						self.assertEqual(1, 2)

					
		
			#tierList = fileInDBS['TierList']
			#self.assertEqual(len(tierList), 2)
			#for tierInDBS in tierList:
			#	if(tierInDBS != tier1 and tierInDBS != tier2):
			#		print 'tier %s is not expected', tierInDBS
			#		self.assertEqual(1, 2)

			parentList = fileInDBS['ParentList']
			#print parentList
			self.assertEqual(len(parentList), 1)
			for parentInDBS in parentList:
				if(parentInDBS['LogicalFileName'] == fileName1):
					assertFile(self, fileObj1, parentInDBS)
				else:
					if(parentInDBS['LogicalFileName'] == fileName2):	
						assertFile(self, fileObj2, parentInDBS)
					else:
						print 'file %s is not expected', parentInDBS
						self.assertEqual(1, 2)

			runList = fileInDBS['RunsList']	
			self.assertEqual(len(runList), 1)
			for runInDBS in runList:
				self.assertEqual(2, runInDBS['NumberOfLumiSections'])
				runInDBS['NumberOfLumiSections'] = runObj['NumberOfLumiSections']
				assertRun(self, runObj, runInDBS)

class Test9(unittest.TestCase):
        def test_01_QIM(self):
		print "testQIM"
		api.insertSubSystem(qim_name1, parent="CMS")
		api.insertSubSystem(qim_name2, parent=qim_name1)
		api.insertSubSystem(qim_name3, parent=qim_name1)
		api.insertSubSystem(qim_int, parent=qim_name1)

		subSys = api.listSubSystems()

		subSysNames=[x['Name'] for x in subSys]

		if qim_name1 not in subSysNames \
			or  qim_name2 not in subSysNames \
				or qim_name3 not in subSysNames \
					or qim_int not in subSysNames:
				print "Unable to add QIMs properly, insertSubSystem failed"
                        	self.assertEqual(1, 2)

	def test_02_InsertValues(self):	
		print "testInsertValues"
                api.insertRunLumiDQ( procObj2 , [run_dq] )
                #dqHierarchyList =  api.listRunLumiDQ(dataset=procObj2, runLumiDQList=[run_dq_search_criteria], dqVersion=dqversion  )
                dqHierarchyList =  api.listRunLumiDQ(dataset=procObj2, runLumiDQList=[run_dq_search_criteria] )

		self.assertEqual(len(dqHierarchyList), 1)
    		for aDQ in dqHierarchyList:
			self.assertEqual(len(aDQ['DQFlagList']), 1)
        		for aSubDQ in aDQ['DQFlagList']:
				if aSubDQ['Name'] == qim_name1:
					self.assertEqual(aSubDQ['Value'], qim_value_g)
				self.assertEqual(len(aSubDQ['SubSysFlagList']), 3)
                		for aSubSubDQ in aSubDQ['SubSysFlagList']:
					if aSubSubDQ['Name'] == qim_name2:
						self.assertEqual(aSubSubDQ['Value'], qim_value_b)
                             	   	elif aSubSubDQ['Name'] == qim_name3:
                                        	self.assertEqual(aSubSubDQ['Value'], qim_value_u)
                                	elif aSubSubDQ['Name'] == qim_int:
                                        	self.assertEqual(aSubSubDQ['Value'], str(qim_value_i))
					else:
						print "Unable to Add/Retrieve QIM Values, insertRunLumiDQ/listRunLumiDQ APIs failed"
	                                	self.assertEqual(1, 2)



if __name__ == '__main__':

        unittest.main()





