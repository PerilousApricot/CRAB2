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
from DBSAPI.dbsPrimaryDataset import DbsPrimaryDataset
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsDQFlag import DbsDQFlag
from DBSAPI.dbsRunLumiDQ import DbsRunLumiDQ

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

#-------------------------------------------------------------------------------
# Sub-Sub System Flag
flag1 = DbsDQFlag (
        Name = "HCAL+",
        Value = "GOOD",
        )
# Sub-Sub System Flag
flag2 = DbsDQFlag (
        Name = "HCAL-",
        Value = "GOOD",
        )

# Sub System Flag 
flag3 = DbsDQFlag (
        Name = "HCAL",
        Value = "GOOD",
	#Well no one stops you from specifying Sub Flags
	#SubSysFlagList = [flag11, flag12]
        )
#-------------------------------------------------------------------------------

#Create a LIST of these DQ Flags
dqFlagList = [flag1, flag2, flag3]

try:

    # Lets say for RunNumber 1, LumiSection Number 1 to 10 we need to have THESE Flags set
    api.insertLumiRangeDQ(runNumber=10, startLumi=6, endLumi=10, dqFlagList=dqFlagList)

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

