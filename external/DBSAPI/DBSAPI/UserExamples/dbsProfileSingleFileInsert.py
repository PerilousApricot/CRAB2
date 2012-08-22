#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
#
import sys, os
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsAlgorithm import DbsAlgorithm
from DBSAPI.dbsFileBlock import DbsFileBlock
from DBSAPI.dbsFile import DbsFile
from DBSAPI.dbsLumiSection import DbsLumiSection
from DBSAPI.dbsQueryableParameterSet import DbsQueryableParameterSet
from DBSAPI.dbsPrimaryDataset import DbsPrimaryDataset
from DBSAPI.dbsProcessedDataset import DbsProcessedDataset
from DBSAPI.dbsOptions import DbsOptionParser

import profile
import hotshot, hotshot.stats

HOW_MANY_FILES=10

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

algo = DbsAlgorithm (
         ExecutableName="TestExe01",
         ApplicationVersion= "TestVersion01",
         ApplicationFamily="AppFamily01",
         ParameterSetID=DbsQueryableParameterSet(
           Hash="001234565798685",
           )
         )
primary = DbsPrimaryDataset (Name = "test_primary_001")
proc = DbsProcessedDataset (
        PrimaryDataset=primary, 
        Name="TestProcessedDS001", 
        PhysicsGroup="BPositive",
        Status="Valid",
        TierList=['GEN', 'SIM'],
        AlgoList=[algo],
        )

lumi1 = DbsLumiSection (
         LumiSectionNumber=1222,
         StartEventNumber=100,
         EndEventNumber=200,
         LumiStartTime=1234,
         LumiEndTime=1234,
         RunNumber=1,
         )
lumi2 = DbsLumiSection (
         LumiSectionNumber=1333,
         StartEventNumber=100,
         EndEventNumber=200,
         LumiStartTime=1234,
         LumiEndTime=1234,
         RunNumber=1,
         )

lumi3 = DbsLumiSection (
         LumiSectionNumber=1333,
         StartEventNumber=100,
         EndEventNumber=200,
         LumiStartTime=1233,
         LumiEndTime=1234,
         RunNumber=1,
         )

myfile1= DbsFile (
        Checksum= '999',
        NumberOfEvents= 10000,
        FileSize= 12340,
        Status= 'VALID',
	ValidationStatus = 'VALID',
        FileType= 'EDM',
        Dataset= proc,
        AlgoList = [algo],
        LumiList= [lumi1, lumi2],
        TierList= ['GEN', 'SIM'],
	BranchHash="001234565798685",
        #ParentList = ['NEW_TEST0003']  
         )

# Make a choice
block = DbsFileBlock (
         StorageElement=['test1', 'test3'],
         )

block['Name']="/test_primary_001/TestProcessedDS001/GEN-SIM#12345-"+str(HOW_MANY_FILES)
print "Inserting Files Into", api.insertBlock (proc, block)
#print "Wait........"
try:
    each_call=[]
    time_taken=0.0
    for i in range(HOW_MANY_FILES):
	rnd=str(os.popen('uuidgen').readline().strip())
        myfile1['LogicalFileName'] = 'NEW_TEST'+rnd
	#print myfile1['LogicalFileName']
	prf=rnd+'.prof'
	p = hotshot.Profile(prf)
    	#Insert in a Block	
    	out=p.run("api.insertFiles (proc, [myfile1], block)")
        stats = hotshot.stats.load(prf)
        stats.strip_dirs()
        stats.sort_stats('time', 'calls')
        #stats.print_stats(1)
	time_taken += stats.total_tt
	each_call.append(stats.total_tt)

    print "\nTotal Time Taken: ", time_taken, "seconds"
    print "\nTime Per File Insertion: ", time_taken/HOW_MANY_FILES, "seconds\n"	
    each_call.sort()
    med = ( each_call[((len(each_call)-1)/2)]+each_call[((len(each_call)+1)/2)] ) / 2
    print "\nMEDIAN:  %s " %str(med)
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

