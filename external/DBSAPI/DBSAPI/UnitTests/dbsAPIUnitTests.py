import unittest
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsUtil import *

from DBSAPI.dbsPrimaryDataset import DbsPrimaryDataset
from DBSAPI.dbsAlgorithm import DbsAlgorithm
from DBSAPI.dbsFileBlock import DbsFileBlock
from DBSAPI.dbsRun import DbsRun
from DBSAPI.dbsFile import DbsFile
from DBSAPI.dbsLumiSection import DbsLumiSection
from DBSAPI.dbsQueryableParameterSet import DbsQueryableParameterSet
from DBSAPI.dbsProcessedDataset import DbsProcessedDataset
from DBSAPI.dbsDQFlag import DbsDQFlag
from DBSAPI.dbsRunLumiDQ import DbsRunLumiDQ
from DBSAPI.dbsFileProcessingQuality import DbsFileProcessingQuality
from DBSAPI.dbsAnalysisDatasetDefinition import DbsAnalysisDatasetDefinition


import datetime
import time

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

serverInfo = api.getServerInfo()
isMYSQL = serverInfo['InstanceType']
isGlobal = serverInfo['InstanceName']


mytime = time.strftime("_%Y%m%d_%Hh%Mm%Ss",time.localtime())
# excep = False
primary = 'TestPrimary_001' + mytime
pri1 = DbsPrimaryDataset (Name = primary, Type="test")
# except = False
primary = 'TestPrimary_002' + mytime
pri2 = DbsPrimaryDataset (Name = primary, Type="test")
# excep = True
pri3 = DbsPrimaryDataset () 
# excep = True
pri4 = DbsPrimaryDataset (Name = "Test Het", Type="test") 
# excep = True
pri5 = DbsPrimaryDataset (Name = "Test;Het", Type="test") 
# excep = True
pri6 = DbsPrimaryDataset (Name = "Test*Het", Type="test") 
# / is allowed  excep = False
pri7 = DbsPrimaryDataset (Name = "Ta/estHet", Type="test") 

# excep = False
algo1 = DbsAlgorithm (
	ExecutableName="TestExe01",
	ApplicationVersion= "TestVersion01" + mytime,
	ApplicationFamily="AppFamily01",
	ParameterSetID=DbsQueryableParameterSet(
	Hash="001234565798685",	Name="MyFirstParam01",	
	Version="V001",Type="test",	Annotation="This is test",
	Content="int a={},b={c=1,, d=33}, f={}, x, y, x") 
	)
# excep = False
# No version type
algo2 = DbsAlgorithm (
	ExecutableName="TestExe01",
	ApplicationVersion= "TestVersion011" + mytime,
	ApplicationFamily="AppFamily011",
	ParameterSetID=DbsQueryableParameterSet(
	Hash="001234565798685",	Name="MyFirstParam01", 
	Annotation="This is test",
	Content="int a= {}, b={c=1, d=33}, f={}, x, y, x")
	)
# excep = False
# Selection based on HASh, But hash is missing, must raise exception
# No Hash version type
algo3 = DbsAlgorithm (
	ExecutableName="TestExe01",
	ApplicationVersion= "TestVersion011" + mytime,
	ApplicationFamily="AppFamily011",
	ParameterSetID=DbsQueryableParameterSet(
	Name="MyFirstParam01", 
	Annotation="This is test",
	Content="int a= {}, b={c=1, d=33}, f={}, x, y, x")
	)
#No PSet_Hash, must give default PSet Hash

# excep = True
# No App Fam
algo4 = DbsAlgorithm (
	ExecutableName="TestExe01",
	ApplicationVersion= "TestVersion01" + mytime, 
	ParameterSetID=DbsQueryableParameterSet(
	Hash="001234565798685",	Name="MyFirstParam01",
	Version="V001",Type="test", Annotation="This is test",
	Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
	)
# excep = True
# No App Version
algo5 = DbsAlgorithm (
	ExecutableName="TestExe01",
	ApplicationFamily="AppFamily01",
	ParameterSetID=DbsQueryableParameterSet(
	Hash="001234565798685",	Name="MyFirstParam01",
	Version="V001",Type="test", Annotation="This is test",
	Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
	)

# excep = True
# No Executable Name 
algo6 = DbsAlgorithm (
	ApplicationVersion= "TestVersion01" + mytime,
	ApplicationFamily="AppFamily01",
	ParameterSetID=DbsQueryableParameterSet(
	Hash="001234565798685",	Name="MyFirstParam01",
	Version="V001",Type="test", Annotation="This is test",
	Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
	)

# excep = False
# No ParamSet
algo7 = DbsAlgorithm (
	ExecutableName="TestExe01",
	ApplicationVersion= "TestVersion01" + mytime,
	ApplicationFamily="AppFamily01"
	)

# excep = True
# Space in ExecutableName
algo8 = DbsAlgorithm (
	ExecutableName="TestE xe01",
	ApplicationVersion= "TestVersion01" + mytime,
	ApplicationFamily="AppFamily01",
	ParameterSetID=DbsQueryableParameterSet(
	Hash="001234565798685", Name="MyFirstParam01",
	Version="V001",Type="test", Annotation="This is test",
	Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
	)
# excep = False
# / in Version
algo8 = DbsAlgorithm (
	ExecutableName="TestExe01",
	ApplicationVersion= "TestVersion01" + mytime,
	ApplicationFamily="AppFamily01",
	ParameterSetID=DbsQueryableParameterSet(
	Hash="001234565798685", Name="MyFirstParam01",
	Version="V00/1",Type="test", Annotation="This is	test",
	Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
	)
# excep = True
# ; in App Fam
algo9 = DbsAlgorithm (
    ExecutableName="TestExe01",
    ApplicationVersion= "TestVersion01" + mytime,
    ApplicationFamily="App;Family01",
    ParameterSetID=DbsQueryableParameterSet(
    Hash="001234565798685", Name="MyFirstParam01",
    Version="V001",Type="test", Annotation="This is test",
    Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
    )

# excep = True
# Space in Hash long Executable name long name
algo10 = DbsAlgorithm (
    ExecutableName="TestEDDDe01",
    ApplicationVersion= "TestVersion01" + mytime,
    ApplicationFamily="AppFamily01",
    ParameterSetID=DbsQueryableParameterSet(
    Hash="00123 4565798685", Name="MyaaaaddddffFirstParam01",
    Version="V001",Type="test", Annotation="This is test",
    Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
    )
    
# excep = True
# ; in ExecutableName Name
algo11 = DbsAlgorithm (
    ExecutableName="Test;Exe01",
    ApplicationVersion= "TeswwwtVersion01" + mytime,
    ApplicationFamily="AppFamily01",
    ParameterSetID=DbsQueryableParameterSet(
    Hash="001234565798685", Name="MyFirstP;aram01",
    Version="V001",Type="test", Annotation="This is test",
    Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
    )

# excep = True
# * in App Fam
algo12 = DbsAlgorithm (
    ExecutableName="Testaae01",
    ApplicationVersion= "TestVeggrsion01" + mytime,
    ApplicationFamily="AppFami*ly01",
    ParameterSetID=DbsQueryableParameterSet(
    Hash="001234565798685",Name="MyFirstParam01",
    Version="V001",Type="test", Annotation="This is test",
    Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
    )
    
# excep = True
# a * in Hash
algo13 = DbsAlgorithm (
    ExecutableName="Testaae01",
    ApplicationVersion= "TestVeggrsion01" + mytime,
    ApplicationFamily="AppFamily01",
    ParameterSetID=DbsQueryableParameterSet(
    Hash="001234a5*65798685",Name="MyFirstParam01",
    Version="V001",Type="test", Annotation="This is test",
    Content="int a={},b={c=1,, d=33}, f={}, x, y, x")
    )
#tierName1 = "HIT" + mytime
tierName1 = "GEN"
#tierName2 = "SIM" + mytime
tierName2 = "SIM"


runNumber1 = 101 + int(time.time()%10000)
runNumber2 = 102 + int(time.time()%10000)
runNumber3 = 103 + int(time.time()%10000)
# excep = False
run1 = DbsRun (
    RunNumber=runNumber1,
    NumberOfEvents= 100,
    NumberOfLumiSections= 20,
    TotalLuminosity= 2222,
    StoreNumber= 123,
    StartOfRun= 1234,
    EndOfRun= 1234,
)
# excep = False
run2 = DbsRun (
    RunNumber=runNumber2,
    NumberOfEvents= 100,
    NumberOfLumiSections= 20,
    TotalLuminosity= 2222,
    StoreNumber= 123,
    StartOfRun= 1234,
    EndOfRun= 1234,
)
# excep = True
run3 = DbsRun (
    RunNumber=runNumber3,
    StartOfRun= 1234)
# excep = True
run4 = DbsRun (
    RunNumber=runNumber3,
    StartOfRun= 123)
# excep = True
run5 = DbsRun (
    RunNumber=runNumber3,
    EndOfRun= 1234)
# excep = False
run6 = DbsRun (
    RunNumber=runNumber1,
    NumberOfEvents= 9999,
    NumberOfLumiSections= 20,
    TotalLuminosity= 2222,
    StoreNumber= 123,
    StartOfRun= 1234,
    EndOfRun= 1234
)
# excep = True
run7 = DbsRun (RunNumber=111111)


lumiNumber1 = 111 + int(time.time()%10000)
lumiNumber2 = 112 + int(time.time()%10000)
lumiNumber3 = 113 + int(time.time()%10000)
# excep = False

lumi1 = DbsLumiSection (
    LumiSectionNumber=lumiNumber1,
    StartEventNumber=100,
    EndEventNumber=200,
    LumiStartTime=1234,
    LumiEndTime=1234,
    RunNumber=runNumber1,
    )

# excep = False
lumi2 = DbsLumiSection (
    LumiSectionNumber=lumiNumber2,
	StartEventNumber=100,
	EndEventNumber=200,
	RunNumber=runNumber1)
# excep = True
lumi3 = DbsLumiSection (startEventNumber=100)
# excep = True
lumi4 = DbsLumiSection (startEventNumber='10 0')
# excep = True
# comment out
lumi5 = DbsLumiSection (
    LumiSectionNumber=lumiNumber3,
	StartEventNumber=100,
	EndEventNumber=200,
	LumiStartTime=2233,
	RunNumber=runNumber1,
	)
# excep = True
# comment out
lumi6 = DbsLumiSection (
    LumiSectionNumber=lumiNumber3,
	StartEventNumber=100,
	EndEventNumber=200,
	LumiStartTime=1234,
	RunNumber=runNumber1,
	)
# excep = True
# comment out
lumi7 = DbsLumiSection (
    LumiSectionNumber=lumiNumber3,
	StartEventNumber=100,
	EndEventNumber=200,
	LumiStartTime=1234,
	RunNumber=runNumber1,
	)

#***********************insertLumiSection API tests***************************"


#***********************updateLumiSection API tests***************************"

# excep = False

lumi8 = DbsLumiSection (
    LumiSectionNumber=lumiNumber1,
	StartEventNumber=1001,
	EndEventNumber=2001,
	LumiStartTime=1232224,
	LumiEndTime=1234444,
	RunNumber=runNumber1,
	)

# excep = False

lumi9 = DbsLumiSection (
    LumiSectionNumber=lumiNumber2,
	EndEventNumber=200222,
	RunNumber=runNumber1)
# excep = True

lumi10 = DbsLumiSection (startEventNumber=100)
# excep = True

lumi11 = DbsLumiSection (startEventNumber='10 0')


#***********************updateLumiSection API tests***************************"


#***********************insertProcessedDataset API tests**************************"
tierList = [tierName1, tierName2]
# excep = False

proc1 = DbsProcessedDataset(
        PrimaryDataset=pri1,
		Name="TestProcessed" + mytime,
		PhysicsGroup="BPositive",
		Status="VALID",
		TierList=tierList,
		AlgoList=[algo1, algo2],
        RunsList=[runNumber1],
)
# excep = False

proc2 = DbsProcessedDataset(PrimaryDataset=pri2,
		Name="TestProcessed" + mytime,
		PhysicsGroup="BPositive",
		Status="VALID",
		TierList=tierList,
		AlgoList=[algo1, algo2],
                RunsList=[runNumber1],
                )
#apiObj.run(proc3, excep = False)
# excep = True
# comment out
proc3 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProcessed1" + mytime)
# excep = True

proc4 = DbsProcessedDataset(PrimaryDataset=DbsPrimaryDataset (Name = "Ta estHet", Type="test"),
		Name="TestProcessed2" + mytime)
# excep = True

proc5 = DbsProcessedDataset(PrimaryDataset=DbsPrimaryDataset (Name = "Ta*estHet", Type="test"),
		Name="TestProcessed2" + mytime)
# excep = True

proc6 = DbsProcessedDataset(PrimaryDataset=DbsPrimaryDataset (Name = "Taes;tHet", Type="test"),
		Name="TestProcessed2" + mytime)
# excep = True

proc7 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProce ssed2" + mytime)
# excep = True

proc8 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProce*ssed2" + mytime)
# excep = True

proc9 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProce/ssed2" + mytime)
# excep = True

proc10 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestPro;cessed2" + mytime)
# excep = True

proc11 = DbsProcessedDataset(Name="TestProcessed2" + mytime)
# excep = True

proc12 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProcesssssssed" + mytime,
		PhysicsGroup="BPosit*aive")
# excep = True

proc13 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProcewwwwwwwed" + mytime,
		PhysicsGroup="BPosit;aive")
# excep = True

algo14 = DbsAlgorithm (ExecutableName="TeaaaaaastExe011", 
		ApplicationVersion= "TestVersaaaaaaaaion011" + mytime, 
		ApplicationFamily="AppFamilaaaaaaay011", 
		ParameterSetID=DbsQueryableParameterSet(Hash="001234565798685", 
							Name="MyFirstaaaaaParam01" 
			                              )
	)
# excep = True

proc14 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProceqqqqqqd" + mytime,
		AlgoList=[algo14])

algo15 = DbsAlgorithm (ExecutableName="Teaaaaa/tExe011", 
		ApplicationVersion= "TestVersaaaaaaaaion011" + mytime, 
		ApplicationFamily="AppFamilaaaaaaay011", 
		ParameterSetID=DbsQueryableParameterSet(Hash="001234565798685", 
							Name="MyFirstaaaaaParam01" 
			                              )
	)
# excep = True

proc15 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProceqqqqqqd" + mytime,
		AlgoList=[algo15])


algo16 = DbsAlgorithm (ExecutableName="TeaaaaatExe011", 
		ParameterSetID=DbsQueryableParameterSet(Hash="001234565798685", 
							Name="MyFirstaaaaaParam01" 
			                              )
	)
# excep = True
    
proc16 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProceqqqqqqd" + mytime,
		AlgoList=[algo16])


algo17 = DbsAlgorithm (ExecutableName="TeaaaaatExe011", 
		ApplicationVersion= "TestVersaaaaaaaaion011" + mytime, 
		ApplicationFamily="AppFamilaaaaaaay011")
# excep = True

proc17 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProceqqqqqqd" + mytime,
		AlgoList=[algo17])

#***********************insertProcessedDataset API tests***************************"

path = "/" + str(proc1['PrimaryDataset']['Name']) + "/" + str(proc1['Name']) + "/" + str(proc1['TierList'][0])+ "-"+str(proc1['TierList'][1])

#***********************insertProcessedDataset API tests***************************")
#***********************insertParentInPD API tests***************************")
#***********************insertParentInPD API tests***************************"
#**********************insertAlgoInPD API tests***************************"

algo18 = DbsAlgorithm (ExecutableName="Does", 
		ApplicationVersion= "Not" + mytime, 
		ApplicationFamily="Exist", 
		ParameterSetID=DbsQueryableParameterSet(
        Name="001234565798685", 
		Version="V001", Type="test", Annotation="This is test",
        Content="int a= {}, b={c=1, d=33}, f={}, x, y, x")
	)


#***********************insertAlgoInPD API tests***************************"
#***********************insertRunInPD API tests***************************")
#***********************insertRunInPD API tests***************************")
#***********************updateProcDSStatus API tests***************************")
#***********************updateProcDSStatus API tests***************************")
#***********************insertBlock API tests***************************")
###path = "/" + str(proc1['PrimaryDataset']['Name']) + "/" + str(proc1['TierList'][0]) + "/" + str(proc1['Name'])
###blockName =  "/"+ mytime + "this/isatestblock#016712"
blockName =   path + "#016712"
blockName1 =   path + "#016713"
blockName2 =   path + "#016714"
###blockName1 =  "/"+ mytime + "this/isatestskljblock#016712"
###blockName2 =  "/"+ mytime + "thislkss/isatestskljblock#016712"
block = DbsFileBlock (Path = path)
block1 = DbsFileBlock (Name = blockName)
block2 = DbsFileBlock (Name= blockName1)
block3 = DbsFileBlock (Name= blockName2)
#***********************insertBlock API tests***************************")
#***********************insertFiles API tests***************************")
lfn1 = '1111-0909-9767-8764' + mytime
lfn2 = '1111-0909-9767-876411' + mytime
file1= DbsFile (
		Checksum= '999',
		LogicalFileName= lfn1,
		#QueryableMetadata= 'This is a test file',
		NumberOfEvents= 10000,
		FileSize= 12340,
		Status= 'VALID',
		ValidationStatus = 'VALID',
		FileType= 'EDM',
		LumiList= [lumi1, lumi2],
		TierList= tierList,
		AlgoList = [algo1, algo2],
		)

file2= DbsFile (
		Checksum= '999',
		LogicalFileName= lfn2,
		#QueryableMetadata= 'This is a test file',
		NumberOfEvents= 10000,
		FileSize= 12340,
		Status= 'VALID',
		ValidationStatus = 'VALID',
		FileType= 'EDM',
		LumiList= [lumi1, lumi2],
		TierList= tierList,
		AlgoList = [algo1, algo2],
		)


file3 = DbsFile (LogicalFileName= '1111-0909-9767-8764222' + mytime,
		Checksum= '999',
		NumberOfEvents= 10000,
                Status= 'VALID',
		FileSize= 12340)

file4 = DbsFile (LogicalFileName= '1111*-0909-9767-8764222' + mytime,
		Checksum= '999',
		NumberOfEvents= 10000,
                Status= 'VALID',
		FileSize= 12340)

file5 = DbsFile (LogicalFileName= '1111;-0909-9767-8764222' + mytime,
		Checksum= '999',
		NumberOfEvents= 10000,
                Status= 'VALID', 
		FileSize= 12340)

file6 = DbsFile (LogicalFileName= '1111-0909-9767-876411111' + mytime,
		NumberOfEvents= 10000,
                Status= 'VALID',
		Checksum= '999',
		FileSize= 12340)
proc18 = DbsProcessedDataset(PrimaryDataset=pri1,
		Name="TestProcessxxxxxxxxxxxxx" + mytime,
                Status= 'VALID',
		TierList=tierList)


block4 = DbsFileBlock (Name = "/" + mytime + "xxxxxxxxxxxxxxxxthis/isatestblock#016712")

file7 = DbsFile (LogicalFileName= '1111-0909-9767-876411111' + mytime,
		ParentList = [lfn1,lfn2],
		Checksum= '999',
		NumberOfEvents= 10000,
                Status= 'VALID',
		FileSize= 12340,
		TierList=tierList
		)

file8 = DbsFile (LogicalFileName= '1111-0909-9767-87641234545' + mytime,
		ParentList = [lfn1,'doesnotexists'],
		NumberOfEvents= 10000,
		Checksum= '999',
                Status= 'VALID',
		FileSize= 12340,
		TierList=tierList)

#***********************insertFiles API tests***************************")

#***********************updateFileStatus API tests***************************")


#***********************updateFileStatus API tests***************************")

#***********************updateFileMetaData API tests***************************")



#***********************updateFileMetaData API tests***************************")


adef = DbsAnalysisDatasetDefinition(Name="TestAnalysisDSDef_005" + mytime,
		ProcessedDatasetPath=path,
		FileList=[file1['LogicalFileName'], file2['LogicalFileName']],
		AlgoList = [algo1, algo2],
		TierList= tierList,
		AnalysisDSList=[],
		LumiRangeList=[('1', '4444'), ('5000', '90000')],
		RunRangeList=[('0', '5000'), ('6000', '99999')],
		UserCut="get all blah blah from x=1, y=6, z=j, lumi=all",
		Description="This is a test Analysis Dataset" + mytime,
		)
		    
###apiObj = DbsUnitTestApi(api.createAnalysisDatasetDefinition, f)
###apiObj.setVerboseLevel(opts.verbose)
##***********************createAnalysisDatasetDefinition API tests***************************")
##
###apiObj.run(adef, excep = False)
###apiObj.run(adef, excep = True)
##
##adef1 = DbsAnalysisDatasetDefinition(Name="TestAnalysisDSDef_006" + mytime,
##		ProcessedDatasetPath=path,
##		Description="This is a test Analysis Dataset" + mytime,
##		)
##
###apiObj.run(adef1, excep = False)
##
##adef1 = DbsAnalysisDatasetDefinition(Name="TestAnalysisDSDef_007" + mytime)
###apiObj.run(adef1, excep = True)
##
##adef1 = DbsAnalysisDatasetDefinition(Name="TestAnalysisDSDe  f_006" + mytime)
###apiObj.run(adef1, excep = True)
##
##
##***********************createAnalysisDatasetDefinition API tests***************************")
##
##
###apiObj = DbsUnitTestApi(api.createAnalysisDataset, f)
###apiObj.setVerboseLevel(opts.verbose)
##***********************createAnalysisDataset API tests***************************")
#

##ads = DbsAnalysisDataset(
#                            Annotation='testdataset' +mytime,
#                            Type='TEST',
#                            Status='NEW',
#                            PhysicsGroup='BPositive'
#                           )
#
###apiObj.run(ads, adef['Name'] , excep = False)
###apiObj.run(ads, adef['Name'] , excep = False)
#
##ads1 = DbsAnalysisDataset(
#                            Annotation='testdataset' +mytime,
#                            PhysicsGroup='BPositive')
###apiObj.run(ads1, adef['Name'] , excep = False)
#
##ads1 = DbsAnalysisDataset(Name='TestAnalysisDaaaataset0056' + mytime,
#                            PhysicsGroup='BPositive')
###apiObj.run(ads1, adef['Name'] , excep = True)
#
##ads1 = DbsAnalysisDataset(Name='TestAnalysiqqqqsDataset0056' + mytime,
#                            Annotation='testdataset' +mytime,)
###apiObj.run(ads1, adef['Name'] , excep = True)
#
##ads1 = DbsAnalysisDataset(Name='TestAnalysisDataset0  056' + mytime,
#                            Annotation='testdataset' +mytime,
#                            PhysicsGroup='BPositive' )
###apiObj.run(ads1, adef['Name'] , excep = True)
#
##apiObj.run(adef['Name'] , excep = True)
##apiObj.run(ads1, 'Should_not_exists' , excep = True)

#***********************createAnalysisDataset API tests***************************")

#if isGlobal != "GLOBAL":
	#***********************addReplicaToBlock API tests***************************")


	#***********************addReplicaToBlock API tests***************************")
	#***********************deleteReplicaFromBlock API tests***************************")


	#***********************deleteReplicaFromBlock API tests***************************")

	#***********************renameSE API tests***************************")
	#***********************renameSE API tests***************************")


#***********************closeBlock API tests***************************")


#***********************closeBlock API tests***************************")

#**********************insertFileProcQuality API tests***************************")
fileQualityObj = DbsFileProcessingQuality(
        ParentFile=file1['LogicalFileName'],
        ChildDataset=get_path(proc1),
        ProcessingStatus='FAILED',
        FailedEventCount=5,
        Description="This is a test",
        FailedEventList=[1,2,3,4,5]
        )

#**********************insertFileProcQuality API tests***************************")


# Store ONE path that could be used by next LIST test cases
#pathfile.write(path)
#blockfile.write(blockName)
#lfnfile.write(lfn2)

###########################
class Test_insertPrimaryDatasetAPI(unittest.TestCase):
    def test_insertPrimary(self):
        print "insertPrimary"
        try:
            api.insertPrimaryDataset(pri1)			
            api.insertPrimaryDataset(pri2)
            api.insertPrimaryDataset(pri7)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.insertPrimaryDataset,pri3)
        self.assertRaises(DbsApiException,api.insertPrimaryDataset,pri4)
        self.assertRaises(DbsApiException,api.insertPrimaryDataset,pri5)
        self.assertRaises(DbsApiException,api.insertPrimaryDataset,pri6)
#		try:
#			api.insertPrimaryDataset(pri3)
#			api.insertPrimaryDataset(pri4)
#			api.insertPrimaryDataset(pri5)
#			api.insertPrimaryDataset(pri6)
#		except DbsApiException:
#			pass
#		except DbsApiException:
#			self.fail('Unexpected exception thrown:', )
#		else:
#			self.fail('ExpectedException not thrown')
		

class Test_insertAlgorithmAPI(unittest.TestCase):    
    def test_insertAlgorithm(self):
        print "insertAlgorithm"
        try:
            api.insertAlgorithm(algo1)
            api.insertAlgorithm(algo2)
            api.insertAlgorithm(algo3)
            api.insertAlgorithm(algo7)
            api.insertAlgorithm(algo8)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#            self.fail('ExpectedException not thrown')
            
        self.assertRaises(DbsApiException,api.insertAlgorithm,algo4)
        self.assertRaises(DbsApiException,api.insertAlgorithm,algo5)
        self.assertRaises(DbsApiException,api.insertAlgorithm,algo6)
#        self.assertRaises(DbsApiException,api.insertAlgorithm,algo7)
        self.assertRaises(DbsApiException,api.insertAlgorithm,algo9)
        self.assertRaises(DbsApiException,api.insertAlgorithm,algo10)
        self.assertRaises(DbsApiException,api.insertAlgorithm,algo11)
        self.assertRaises(DbsApiException,api.insertAlgorithm,algo12)
        self.assertRaises(DbsApiException,api.insertAlgorithm,algo13)

class Test_insertTierAPI(unittest.TestCase):
    def test_insertTier(self):
        print "insertTier"
        try:
            api.insertTier(tierName1)
            api.insertTier(tierName1)
            api.insertTier(tierName2)    
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#            self.fail('ExpectedException not thrown')
            
        self.assertRaises(DbsApiException,api.insertTier,"")
        self.assertRaises(DbsApiException,api.insertTier,"sjhd*lk")
        self.assertRaises(DbsApiException,api.insertTier,"sjhd;lk")
        self.assertRaises(DbsApiException,api.insertTier,"sjhd lk")
        
class Test_insertRunAPI(unittest.TestCase):
    def test_insertRun(self):
        print "insertRun"
        try:
            api.insertRun(run1)
            api.insertRun(run2)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#            self.fail('ExpectedException not thrown')
            
        self.assertRaises(DbsApiException,api.insertRun,run3)
        self.assertRaises(DbsApiException,api.insertRun,run4)
        self.assertRaises(DbsApiException,api.insertRun,run5)
        
class Test_updateRunAPI(unittest.TestCase):
    def test_updateRun(self):
        print "updateRun"
        try:
            api.updateRun(run6)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#            self.fail('ExpectedException not thrown')

        self.assertRaises(DbsApiException,api.updateRun,run7)

class Test_insertLumiSectionAPI(unittest.TestCase):
    def test_insertLumiSection(self):
        print "insertLumiSection"
        try:
            api.insertLumiSection(lumi1)
            api.insertLumiSection(lumi2)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.insertLumiSection,lumi3)
        self.assertRaises(DbsApiException,api.insertLumiSection,lumi4)
#        self.assertRaises(DbsApiException,api.insertLumiSection,lumi5)
#        self.assertRaises(DbsApiException,api.insertLumiSection,lumi6)
#        self.assertRaises(DbsApiException,api.insertLumiSection,lumi7)
        
class Test_updateLumiSectionAPI(unittest.TestCase):
    def test_updateLumiSectionAPI(self):
        print "updateLumiSectionAPI"
        try:
            api.updateLumiSection(lumi8)
            api.updateLumiSection(lumi9)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.updateLumiSection,lumi10)
        self.assertRaises(DbsApiException,api.updateLumiSection,lumi11)
        
class Test_insertProcessedDatasetAPI(unittest.TestCase):
    def test_insertProcessedDataset(self):
        print "insertProcessedDataset"
        try:
            api.insertProcessedDataset(proc1)
            api.insertProcessedDataset(proc2)
#            api.insertProcessedDataset(proc3)
            
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc4)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc5)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc6)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc7)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc8)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc9)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc10)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc11)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc12)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc13)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc14)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc15)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc16)
        self.assertRaises(DbsApiException,api.insertProcessedDataset,proc17)
        
class Test_insertParentInPDAPI(unittest.TestCase):
    def test_insertParentInPD(self):
        print "insertParentInPD"
        try:
            api.insertParentInPD(proc1,proc2)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.insertParentInPD,proc1, "")
        self.assertRaises(DbsApiException,api.insertParentInPD,proc1, "/Does/Not/Exist")
        self.assertRaises(DbsApiException,api.insertParentInPD,"/Does/Not/Exist",proc3)
        self.assertRaises(DbsApiException,api.insertParentInPD,proc1, "sjhd lk")
        self.assertRaises(DbsApiException,api.insertParentInPD,proc1, "abd;def")
        
class Test_insertAlgoInPDAPI(unittest.TestCase):
    def test_insertAlgoInPD(self):
        print "insertAlgoInPD"
        try:
            api.insertAlgoInPD(proc1,algo1)
            api.insertAlgoInPD(proc1,algo2)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.insertAlgoInPD,"/Does/Not/Exist",algo1)
        self.assertRaises(DbsApiException,api.insertAlgoInPD,proc1,algo18)

class Test_insertRunInPDAPI(unittest.TestCase):
    def test_insertRunInPD(self):
        print "insertRunInPD"
        try:
            api.insertRunInPD(proc1,runNumber2)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.insertRunInPD,proc1,runNumber3)
        self.assertRaises(DbsApiException,api.insertRunInPD,"/Does/Not/Exist",runNumber1)
        self.assertRaises(DbsApiException,api.insertRunInPD,proc1,"123456")
        self.assertRaises(DbsApiException,api.insertRunInPD,proc1,"123a456")
        
class Test_updateProcDSStatusAPI(unittest.TestCase):
    def test_updateProcDSStatus(self):
        print "updateProcDSStatus"
        try:
            api.updateProcDSStatus(proc1,"INVALID")
            api.updateProcDSStatus(path,"INVALID")
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.updateProcDSStatus,"/aa/does/notexist","INVALID")
        self.assertRaises(DbsApiException,api.updateProcDSStatus,path,"IN;VALID")
        
class Test_dbsApiUpdateProcDSDescAPI(unittest.TestCase):
    def test_dbsApiUpdateProcDSDesc(self):
        print "dbsApiUpdateProcDSDesc"
        try:
            api.dbsApiUpdateProcDSDesc(path,"this dataset description changed after dataset inserted into DB")
        except DbsApiException:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.dbsApiUpdateProcDSDesc ,path,"this dataset description changed after dataset inserted into DB")



class Test_insertBlockAPI(unittest.TestCase):
    def test_insertBlock(self):
        print "insertBlock"
        try:
            api.insertBlock(path)
            api.insertBlock(path,blockName)
            api.insertBlock(path,block)
            api.insertBlock(proc1,block)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.insertBlock,path, "/" + mytime + "this/isatestblock016712")
        self.assertRaises(DbsApiException,api.insertBlock,"/absssssssc/dessssssf/hijaaaaaaa")
        self.assertRaises(DbsApiException,api.insertBlock,"/abcaaaa/deaaaaaaf/hiaaaaaaaj","/this/isatestblock#016712")
        self.assertRaises(DbsApiException,api.insertBlock,path,"/thisisatestblock#016712")
        self.assertRaises(DbsApiException,api.insertBlock,path,"/thisis atestblock#016712")
        self.assertRaises(DbsApiException,api.insertBlock,path,"thisisat/ae/stblock#016712",block3)
        self.assertRaises(DbsApiException,api.insertBlock,"/ddd/hd*/hdhd")
        self.assertRaises(DbsApiException,api.insertBlock,"/dd d/hd/hdhd")
        self.assertRaises(DbsApiException,api.insertBlock,"/ddd/hd/hd;hd")
        
class Test_insertFilesAPI(unittest.TestCase):
    def test_insertFiles(self):
        print "insertFiles"
        try:
            api.insertFiles(proc1,[file1,file2],block1)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.insertFiles,proc1,[file3],block1)
        self.assertRaises(DbsApiException,api.insertFiles,proc1,[file4],block1)
        self.assertRaises(DbsApiException,api.insertFiles,proc1,[file5],block1)
        self.assertRaises(DbsApiException,api.insertFiles,proc18,[file6],block1)
        self.assertRaises(DbsApiException,api.insertFiles,proc1,[file6],block4)
        self.assertRaises(DbsApiException,api.insertFiles,proc1,[file7],block1)
        self.assertRaises(DbsApiException,api.insertFiles,proc1,[file8],block1)
        
class Test_updateFileStatusAPI(unittest.TestCase):
    def test_updateFileStatus(self):
        print "updateFileStatus"
        try:
            api.updateFileStatus(lfn1,"VALID")
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.updateFileStatus,lfn1,"DOESNOTEXIST")
        self.assertRaises(DbsApiException,api.updateFileStatus,"DO;ESNOTEXIST","VALID")
        self.assertRaises(DbsApiException,api.updateFileStatus,"DO/ESNOTEXIST","VALID")
        self.assertRaises(DbsApiException,api.updateFileStatus,lfn1,"VA;LID")
        self.assertRaises(DbsApiException,api.updateFileStatus,lfn1,"VA/LID")

class Test_updateFileMetaDataAPI(unittest.TestCase):
    def test_updateFileMetaData(self):
        print "updateFileMetaData"
        try:
            api.updateFileMetaData(lfn1,"VALID")
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.updateFileMetaData,lfn1,"")
        self.assertRaises(DbsApiException,api.updateFileMetaData,"DOESNOTEXIST","abcd")
        self.assertRaises(DbsApiException,api.updateFileMetaData,"DO;ESNOTEXIST","abcd")
        self.assertRaises(DbsApiException,api.updateFileMetaData,"DO/ESNOTEXIST","abcd")
        self.assertRaises(DbsApiException,api.updateFileMetaData,lfn1,"INVA;LID")
        self.assertRaises(DbsApiException,api.updateFileMetaData,lfn1,"INVA/LID")
        
class Test_closeBlockAPI(unittest.TestCase):
    def test_closeBlock(self):
        print "closeBlock"
        try:
            api.closeBlock(block1)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
        self.assertRaises(DbsApiException,api.closeBlock,"DOESNOTEXIST")
        self.assertRaises(DbsApiException,api.closeBlock,"abcd;edf")
        self.assertRaises(DbsApiException,api.closeBlock,"/does/no/exit#1234")

class Test_insertFileProcQualityAPI(unittest.TestCase):
    def test_insertFileProcQuality(self):
        print "insertFileProcQuality"
        try:
            api.insertFileProcQuality(fileQualityObj)
        except DbsApiException:
            self.fail("Expected no Error")
#            self.fail('Unexpected exception thrown:', )
#        else:
#			self.fail('ExpectedException not thrown')
      
###########
## MYSQL ##
###########
class Test_addReplicaToBlockAPI(unittest.TestCase):
    def test_addReplicaToBlock(self):
        if isGlobal != "GLOBAL":
            print "addReplicaToBlock"
            try:
                api.addReplicaToBlock(block1,"MySE1")
                api.addReplicaToBlock(block1,"MySE2")
            except DbsApiException:
                self.fail("Expected no Error")
#                self.fail('Unexpected exception thrown:', )
#            else:
#				self.fail('ExpectedException not thrown')
            self.assertRaises(DbsApiException,api.addReplicaToBlock,block1,"My;SE")
            self.assertRaises(DbsApiException,api.addReplicaToBlock,"/does/not/eist#1234","MySE1")
        else: pass

class Test_deleteReplicaFromBlockAPI(unittest.TestCase):
    def test_deleteReplicaFromBlock(self):
        if isGlobal != "GLOBAL":
            print "deleteReplicaFromBlock"
            try:
                api.deleteReplicaFromBlock(block1, "MySE1")
            except DbsApiException:
                self.fail("Expected no Error")
#                self.fail('Unexpected exception thrown:', )
#            else:
#				self.fail('ExpectedException not thrown')
            self.assertRaises(DbsApiException,api.deleteReplicaFromBlock,block1,"My;SE")
            self.assertRaises(DbsApiException,api.deleteReplicaFromBlock,block1, "DOESNOTEXIST")
            self.assertRaises(DbsApiException,api.deleteReplicaFromBlock,"/does/not/eist#1234","MySE1")
        else: pass
            
class Test_renameSEAPI(unittest.TestCase):
    def test_renameSE(self):
        if isGlobal != "GLOBAL":
            print "renameSE"
            try:
                api.renameSE("MySE2", "MySE2New" + mytime)
            except DbsApiException:
                self.fail("Expected no Error")
#                self.fail('Unexpected exception thrown:', )
#            else:
#				self.fail('ExpectedException not thrown')
            self.assertRaises(DbsApiException,api.renameSE,"DOESNOTEXIST", "MySE")
            self.assertRaises(DbsApiException,api.renameSE,"abcd;edf","ANTHING")
            self.assertRaises(DbsApiException,api.renameSE,"/does/no","MySE1")           
        else: pass

class Test_listPrimaryDatasetsAPI(unittest.TestCase):
    def test_listPrimaryDatasets(self):
        print "listPrimaryDatasets"
        try:
            api.listPrimaryDatasets("*")
            api.listPrimaryDatasets("*test*")
            api.listPrimaryDatasets("")
            api.listPrimaryDatasets("abc*")
            api.listPrimaryDatasets("ab/bc")
            api.listPrimaryDatasets("//*/ab/bc")
            api.listPrimaryDatasets()
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listPrimaryDatasets,"abc bc")
        self.assertRaises(TypeError,api.listPrimaryDatasets,"","")
        self.assertRaises(DbsApiException,api.listPrimaryDatasets,"ab;bc")

class Test_listAlgorithmsAPI(unittest.TestCase):
    def test_listAlgorithms(self):
        print "listAlgorithms"
        try:
            api.listAlgorithms("*","*")
            api.listAlgorithms()
            api.listAlgorithms("MyVersion22","sss")
            api.listAlgorithms("MyVersion22","","")
            api.listAlgorithms("MyVersion12","MyFamily12","MyExe12")
            api.listAlgorithms("*","*12","MyExe12","*")
            api.listAlgorithms("/*")
            api.listAlgorithms("*","abcd/jdg")
            
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listAlgorithms,"My Version22","sss")
        self.assertRaises(DbsApiException,api.listAlgorithms,"ab;2","sss")
        self.assertRaises(DbsApiException,api.listAlgorithms,"ab","s;")
        self.assertRaises(TypeError,api.listAlgorithms,"*","*","","","")
        
class Test_listProcessedDatasetsAPI(unittest.TestCase):
    def test_listProcessedDatasets(self):
        print "listProcessedDatasets"
        try:
            api.listProcessedDatasets("*","*")
            api.listProcessedDatasets()
            api.listProcessedDatasets("abc","sss")
            api.listProcessedDatasets("","","","","","*1*","")
            api.listProcessedDatasets("","","","","","MyExe1","")
            api.listProcessedDatasets("","","","","","MyExe1")
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listProcessedDatasets,"*","*","ex;e")
        self.assertRaises(TypeError,api.listProcessedDatasets,"","","","","","","","")
                                                                                                                                                
class Test_listBlocksAPI(unittest.TestCase):
    def test_listBlocks(self):
        print "listBlocks"
        try:
            api.listBlocks(path)
            api.listBlocks("")
        except:
            self.fail("Expected no Error")
            
        self.assertRaises(DbsApiException,api.listBlocks,"/*/*/anzar-procds-01")
        self.assertRaises(DbsApiException,api.listBlocks,"/Primaryaaaaa/sdldljd/slkdscds-05")
        self.assertRaises(DbsApiException,api.listBlocks,"/*/sssjd/slkdscds-05")
        self.assertRaises(DbsApiException,api.listBlocks,"/abd def/sssjd/slkdscds-05")
        self.assertRaises(DbsApiException,api.listBlocks,"/Primary;DS_ANZAR_01/test-tier-01/anzar-procds-05")
        self.assertRaises(DbsApiException,api.listBlocks,"/sjh","")

class Test_listStorageElementsAPI(unittest.TestCase):
    def test_listStorageElements(self):
        print "listStorageElements"
        try:
            api.listStorageElements(path)
            api.listStorageElements("")
            api.listStorageElements("*")
            api.listStorageElements(storage_element_name="*")
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listStorageElements,"/sdd;/*")
        
class Test_listRunsAPI(unittest.TestCase):
    def test_listRuns(self):
        print "listRuns"
        try:
            api.listRuns(path)
        except:
            self.fail("Expected no Error")   
        self.assertRaises(TypeError,api.listRuns)
        self.assertRaises(DbsApiException,api.listRuns,"")
        self.assertRaises(DbsApiException,api.listRuns,"/*/*/anzar-procds-01")
        self.assertRaises(DbsApiException,api.listRuns,"/Primaryaaaaa/sdldljd/slkdscds-05")
        self.assertRaises(DbsApiException,api.listRuns,"/*/sssjd/slkdscds-05")
        self.assertRaises(DbsApiException,api.listRuns,"/abd def/sssjd/slkdscds-05")
        self.assertRaises(DbsApiException,api.listRuns,"/Primary;DS_ANZAR_01/test-tier-01/anzar-procds-05")
        self.assertRaises(TypeError,api.listRuns,"/sjh","")
        
        
class Test_listTiersAPI(unittest.TestCase):
    def test_listTiers(self):
        print "listTiers"
        try:
            api.listTiers(path)
        except:
            self.fail("Expected no Error")
        self.assertRaises(TypeError,api.listTiers)
        self.assertRaises(DbsApiException,api.listTiers,"")
        self.assertRaises(DbsApiException,api.listTiers,"/*/*/anzar-procds-01")
        self.assertRaises(DbsApiException,api.listTiers,"/Primaryaaaaa/sdldljd/slkdscds-05")
        self.assertRaises(DbsApiException,api.listTiers,"/abd def/sssjd/slkdscds-05")
        self.assertRaises(DbsApiException,api.listTiers,"/Primary;DS_ANZAR_01/test-tier-01/anzar-procds-05")
        self.assertRaises(TypeError,api.listTiers,"/sjh","")

class Test_listFilesAPI(unittest.TestCase):
    def test_listFiles(self):
        print "listFiles"
        try:
            api.listFiles(path,"", "", [], "","","", "")
            api.listFiles("","", "", [], "", blockName,"", "")
            api.listFiles(path,"", "", [],"", blockName,"*", "")
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listFiles,"","", "",[],"", "/PrimaryDS_ANZAR_01/anzardjhk", "", "")
        self.assertRaises(DbsApiException,api.listFiles,"","", "",[],"", "/Pr;imaryDS_ANZAR_01/anzardjhk", "", "")
        self.assertRaises(DbsApiException,api.listFiles,"/dsds/", "","", [],"", "","","")
        self.assertRaises(DbsApiException,api.listFiles,"/dsds//", "","", [],"", "","")
        self.assertRaises(DbsApiException,api.listFiles,"/dsds/a b/de","", "", [],"", "","")
        self.assertRaises(DbsApiException,api.listFiles,"", "", "",[],"", "","*")
        
class Test_listFileParentsAPI(unittest.TestCase):
    def test_listFileParents(self):
        print "listFileParents"
        try:
            api.listFileParents(lfn2)
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listFileParents,lfn2 +".nowaythiswillexist")
        self.assertRaises(DbsApiException,api.listFileParents,lfn2 +"noway thiswillexist")
        self.assertRaises(DbsApiException,api.listFileParents,lfn2 +"noway;thiswillexist")
        self.assertRaises(TypeError,api.listFileParents,lfn2,"")
        
class Test_listFileAlgorithmsAPI(unittest.TestCase):
    def test_listFileAlgorithms(self):
        print "listFileAlgorithms"
        try:
            api.listFileAlgorithms(lfn2)
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listFileAlgorithms,lfn2 +".nowaythiswillexist")
        self.assertRaises(DbsApiException,api.listFileAlgorithms,lfn2 +"noway thiswillexist")
        self.assertRaises(DbsApiException,api.listFileAlgorithms,lfn2 +"noway;thiswillexist")
        self.assertRaises(TypeError,api.listFileAlgorithms,lfn2,"")
        
class Test_listFileLumisAPI(unittest.TestCase):
    def test_listFileLumis(self):
        print "listFileLumis"
        try:
            api.listFileLumis(lfn2)
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listFileLumis,lfn2 +".nowaythiswillexist")        
        self.assertRaises(DbsApiException,api.listFileLumis,lfn2 +"noway thiswillexist")        
        self.assertRaises(DbsApiException,api.listFileLumis,lfn2 +"noway;thiswillexist")        
        self.assertRaises(TypeError,api.listFileLumis,lfn2,"")
        
            
class Test_listLFNsAPI(unittest.TestCase):
    def test_listLFNs(self):
        print "listLFNs"
        try:
            api.listLFNs(path)
            api.listLFNs(path,"a")
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listLFNs,".nowaythiswillexist"+path)
        
class Test_listAnalysisDatasetDefinitionAPI(unittest.TestCase):
    def test_listAnalysisDatasetDefinition(self):
        print "listAnalysisDatasetDefinition"
        try:
            api.listAnalysisDatasetDefinition()
            api.listAnalysisDatasetDefinition("*")
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listAnalysisDatasetDefinition,"this;xist")
        self.assertRaises(TypeError,api.listAnalysisDatasetDefinition,"ahsdef","")

class Test_listAnalysisDatasetAPI(unittest.TestCase):
    def test_listAnalysisDataset(self):
        print "listAnalysisDataset"
        try:
            api.listAnalysisDataset()
            api.listAnalysisDataset("*")
#            api.listAnalysisDataset("*",path)
        except:
            self.fail("Expected no Error")

        self.assertRaises(DbsApiException,api.listAnalysisDataset,"*","/this/will/notexist")
#        self.assertRaises(DbsApiException,api.listAnalysisDataset,"ahs def", path)
#        self.assertRaises(DbsApiException,api.listAnalysisDataset,"ahs*",path,"")
        
class Test_listDatasetParentsAPI(unittest.TestCase):
    def test_listDatasetParents(self):
        print "listDatasetParents"
        try:
            api.listDatasetParents(path)
        except:
            self.fail("Expected no Error")
#        self.assertRaises(DbsApiException,api.listDatasetParents,"")
        self.assertRaises(DbsApiException,api.listDatasetParents,"/this/will/notexist")
        self.assertRaises(DbsApiException,api.listDatasetParents,"ahs def")
        self.assertRaises(DbsApiException,api.listDatasetParents,"ahs*")
        
class Test_listDatasetContents(unittest.TestCase):
    def test_listDatasetContents(self):
        print "listDatasetContents"
        try:
            api.listDatasetContents(path,blockName)
        except:
            self.fail("Expected no Error")
        self.assertRaises(DbsApiException,api.listDatasetContents,path,"")
        self.assertRaises(DbsApiException,api.listDatasetContents,"",blockName)
        self.assertRaises(DbsApiException,api.listDatasetContents,"/this/will/notexist",blockName)
        self.assertRaises(DbsApiException,api.listDatasetContents,"ahs def","")
        self.assertRaises(DbsApiException,api.listDatasetContents,"ahs*", blockName)
        self.assertRaises(DbsApiException,api.listDatasetContents,path, "noeixts")
        self.assertRaises(DbsApiException,api.listDatasetContents,path, "/no/ei/xts#1234")
        
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_insertPrimaryDatasetAPI))
    suite.addTest(unittest.makeSuite(Test_insertAlgorithmAPI))
    suite.addTest(unittest.makeSuite(Test_insertTierAPI))
    suite.addTest(unittest.makeSuite(Test_insertRunAPI))
    suite.addTest(unittest.makeSuite(Test_updateRunAPI))
    suite.addTest(unittest.makeSuite(Test_insertLumiSectionAPI))
    suite.addTest(unittest.makeSuite(Test_updateLumiSectionAPI))
    suite.addTest(unittest.makeSuite(Test_insertProcessedDatasetAPI))
    suite.addTest(unittest.makeSuite(Test_insertParentInPDAPI))
    suite.addTest(unittest.makeSuite(Test_insertAlgoInPDAPI))
    suite.addTest(unittest.makeSuite(Test_insertRunInPDAPI))
    suite.addTest(unittest.makeSuite(Test_updateProcDSStatusAPI))
    suite.addTest(unittest.makeSuite(Test_insertBlockAPI))
    suite.addTest(unittest.makeSuite(Test_insertFilesAPI))
    suite.addTest(unittest.makeSuite(Test_updateFileStatusAPI))
    suite.addTest(unittest.makeSuite(Test_updateFileMetaDataAPI))
    suite.addTest(unittest.makeSuite(Test_closeBlockAPI))
    suite.addTest(unittest.makeSuite(Test_insertFileProcQualityAPI))
    suite.addTest(unittest.makeSuite(Test_addReplicaToBlockAPI))
    suite.addTest(unittest.makeSuite(Test_deleteReplicaFromBlockAPI))
    suite.addTest(unittest.makeSuite(Test_renameSEAPI)) 
    suite.addTest(unittest.makeSuite(Test_listPrimaryDatasetsAPI))
    suite.addTest(unittest.makeSuite(Test_listAlgorithmsAPI))
    suite.addTest(unittest.makeSuite(Test_listProcessedDatasetsAPI))
    suite.addTest(unittest.makeSuite(Test_listBlocksAPI))
    suite.addTest(unittest.makeSuite(Test_listStorageElementsAPI))
    suite.addTest(unittest.makeSuite(Test_listRunsAPI))
    suite.addTest(unittest.makeSuite(Test_listTiersAPI))
    suite.addTest(unittest.makeSuite(Test_listFilesAPI))
    suite.addTest(unittest.makeSuite(Test_listFileParentsAPI))
    suite.addTest(unittest.makeSuite(Test_listFileAlgorithmsAPI))
    suite.addTest(unittest.makeSuite(Test_listFileLumisAPI))
    suite.addTest(unittest.makeSuite(Test_listLFNsAPI))
    suite.addTest(unittest.makeSuite(Test_listAnalysisDatasetDefinitionAPI))
    suite.addTest(unittest.makeSuite(Test_listAnalysisDatasetAPI))
    suite.addTest(unittest.makeSuite(Test_listDatasetParentsAPI))
    
    suite.addTest(unittest.makeSuite(Test_listDatasetContents))
    return suite
			
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_insertPrimaryDatasetAPI))
    suite.addTest(unittest.makeSuite(Test_insertAlgorithmAPI))
    suite.addTest(unittest.makeSuite(Test_insertTierAPI))
    suite.addTest(unittest.makeSuite(Test_insertRunAPI))
    suite.addTest(unittest.makeSuite(Test_updateRunAPI))
    suite.addTest(unittest.makeSuite(Test_insertLumiSectionAPI))
    suite.addTest(unittest.makeSuite(Test_updateLumiSectionAPI))
    suite.addTest(unittest.makeSuite(Test_insertProcessedDatasetAPI))
    suite.addTest(unittest.makeSuite(Test_insertParentInPDAPI))
    suite.addTest(unittest.makeSuite(Test_insertAlgoInPDAPI))
    suite.addTest(unittest.makeSuite(Test_insertRunInPDAPI))
    suite.addTest(unittest.makeSuite(Test_updateProcDSStatusAPI))
    suite.addTest(unittest.makeSuite(Test_insertBlockAPI))
    suite.addTest(unittest.makeSuite(Test_insertFilesAPI))
    suite.addTest(unittest.makeSuite(Test_updateFileStatusAPI))
    suite.addTest(unittest.makeSuite(Test_updateFileMetaDataAPI))
    suite.addTest(unittest.makeSuite(Test_closeBlockAPI))
    suite.addTest(unittest.makeSuite(Test_insertFileProcQualityAPI))
    suite.addTest(unittest.makeSuite(Test_addReplicaToBlockAPI))
    suite.addTest(unittest.makeSuite(Test_deleteReplicaFromBlockAPI))
    suite.addTest(unittest.makeSuite(Test_renameSEAPI))
    suite.addTest(unittest.makeSuite(Test_listPrimaryDatasetsAPI))
    suite.addTest(unittest.makeSuite(Test_listAlgorithmsAPI))
    suite.addTest(unittest.makeSuite(Test_listProcessedDatasetsAPI))
    suite.addTest(unittest.makeSuite(Test_listBlocksAPI))
    suite.addTest(unittest.makeSuite(Test_listStorageElementsAPI))
    suite.addTest(unittest.makeSuite(Test_listRunsAPI))
    suite.addTest(unittest.makeSuite(Test_listTiersAPI))
    suite.addTest(unittest.makeSuite(Test_listFilesAPI))
    suite.addTest(unittest.makeSuite(Test_listFileParentsAPI))
    suite.addTest(unittest.makeSuite(Test_listFileAlgorithmsAPI))
    suite.addTest(unittest.makeSuite(Test_listFileLumisAPI))
    suite.addTest(unittest.makeSuite(Test_listLFNsAPI))
    suite.addTest(unittest.makeSuite(Test_listAnalysisDatasetDefinitionAPI))
    suite.addTest(unittest.makeSuite(Test_listAnalysisDatasetAPI))
    suite.addTest(unittest.makeSuite(Test_listDatasetParentsAPI))
    
    suite.addTest(unittest.makeSuite(Test_listDatasetContents))
    runner = unittest.TextTestRunner()
    runner.run(suite)	
#    unittest.main()
