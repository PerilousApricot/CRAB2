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
from DBSAPI.dbsRun import DbsRun
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

                            
run = DbsRun (
         RunNumber=1111,
         NumberOfEvents= 100,
         NumberOfLumiSections= 20,
         TotalLuminosity= 2222,
         StoreNumber= 123,
         StartOfRun= 0,
         EndOfRun= 0,
         )
 
try:
    print "Creating a run"
    api.insertRun (run)

    print "adding it to proc DS"
    #api.insertRunInPD ("/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_4_6-CSA07-2119/GEN-SIM", 1111)
    api.insertRunInPD ("/mcTestCeballos_z2jet_VBFHiggsTo2Taugen-alpgen/CMSSW_1_6_7-CSA07-1195931857/GEN-SIM-DIGI-RAW", 1111)

    print "Result: %s" % run

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


print "Done"

