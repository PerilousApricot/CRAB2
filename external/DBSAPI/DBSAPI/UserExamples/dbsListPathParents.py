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
  paths=['/zz3j-alpgen/CMSSW_1_6_7-HLT-1205907476/GEN-SIM-DIGI-RECO',
	'/zz3j-alpgen/CMSSW_1_6_7-CSA07-1205907722/RECO',
	'/zz3j-alpgen/CMSSW_1_6_7-CSA07-1205736930/GEN-SIM-DIGI-RAW',
	'/zz3j-alpgen/CMSSW_1_4_9-CSA07-4131/GEN-SIM',
	'/zz2j-alpgen/CMSSW_1_6_7-HLT-1205617522/GEN-SIM-DIGI-RECO',
	'/zz2j-alpgen/CMSSW_1_6_7-CSA07-1205618250/RECO',
	'/zz2j-alpgen/CMSSW_1_6_7-CSA07-1205616825/GEN-SIM-DIGI-RAW',
	'/zz2j-alpgen/CMSSW_1_4_9-CSA07-4130/GEN-SIM',
	'/zz1j-alpgen/CMSSW_1_6_7-HLT-1205617620/GEN-SIM-DIGI-RECO',
	'/zz1j-alpgen/CMSSW_1_6_7-CSA07-1205618302/RECO',
	'/zz1j-alpgen/CMSSW_1_6_7-CSA07-1205616888/GEN-SIM-DIGI-RAW',
	'/zz1j-alpgen/CMSSW_1_4_9-CSA07-4129/GEN-SIM',
	'/SUSY_LM2-sftsht/Summer08_IDEAL_V9_v1/GEN-SIM-RAW',
	'/SUSY_LM2-sftsht/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RECO',
	'/SUSY_LM2-sftsht/Summer08_IDEAL_V11_redigi_v1/GEN-SIM-RAW',
	'/SUSY_LM2-sftsht/Summer08_IDEAL_V11_redigi_v1/AODSIM',
	'/Bd2PiKp/CMSSW_1_6_7-HLT-1193400518/GEN-SIM-DIGI-RECO',
	'/Bd2PiKp/CMSSW_1_6_7-CSA07-3206/GEN-SIM-DIGI-RAW',
	'/Bd2PiKp/CMSSW_1_6_7-CSA07-1193556527/RECO',
	'/Bd2PiKp/CMSSW_1_4_6-CSA07-2921/GEN-SIM']
  #paths=['/Bd2PiKp/CMSSW_1_6_7-CSA07-1193556527/RECO']
  print "Processed Datasets:"
  for aPath in paths:
	print aPath
  	print api.listPathParents(aPath)
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

