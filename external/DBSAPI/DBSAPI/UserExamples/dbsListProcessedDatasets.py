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

try:
  optManager  = DbsOptionParser()
  (opts,args) = optManager.getOpt()
  api = DbsApi(opts.__dict__)
  
  # List all parameter sets
  print "Processed Datasets:"
  #for proc in api.listProcessedDatasets("test_primary_001", "*", "TestProcessedDS002"):
  #for proc in api.listProcessedDatasets(patternPrim="Cosmics",  patternProc = "Commissioning08-CRUZET4_v1"):
  #/RelValMinBias/CMSSW_2_1_2_STARTUP_V5_v3/GEN-SIM-RECO
  path = '/test_primary_001/*/*'
  params = path.split('/')
  for proc in api.listProcessedDatasets(patternPrim=params[1],  patternProc = params[2]):
     """
     algoList =  proc['AlgoList']
     for aAlgo in algoList:
	     print aAlgo['ApplicationVersion']
	     print aAlgo['ParameterSetID']['Hash']
	     print aAlgo['ApplicationFamily']
	     print aAlgo['ExecutableName']
	     tmpAlgoList =  api.listAlgorithms( patternVer=aAlgo['ApplicationVersion'], patternFam=aAlgo['ApplicationFamily'], patternExe=aAlgo['ExecutableName'], patternPS=aAlgo['ParameterSetID']['Hash'])
	     for atmpAlgo in tmpAlgoList :
		     print atmpAlgo['ParameterSetID']['Content']
     """
     print proc
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

