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
flag11 = DbsDQFlag (
        Name = "HCAL+",
        Value = "GOOD",
        )
# Sub-Sub System Flag
flag12 = DbsDQFlag (
        Name = "HCAL-",
        Value = "GOOD",
        )

# Sub System Flag (Including sub-sub system flags)
flag1 = DbsDQFlag (
        Name = "HCAL",
        Value = "GOOD",
	SubSysFlagList = [flag11, flag12]
        )
#-------------------------------------------------------------------------------

# Sub-Sub System Flag
flag21 = DbsDQFlag (
        Name = "ECAL+",
        Value = "GOOD",
        )
# Sub-Sub System Flag
flag22 = DbsDQFlag (
        Name = "ECAL-",
        Value = "GOOD",
        )

# Sub System Flag (Including sub-sub system flags)
flag2 = DbsDQFlag (
        Name = "ECAL",
        Value = "GOOD",
        SubSysFlagList = [flag21, flag22]
        )
#-------------------------------------------------------------------------------

# Sub System Flag (Including sub-sub system flags)
flag_nosub = DbsDQFlag (
        Name = "NOSUB",
        Value = "BAD",
        )
#-------------------------------------------------------------------------------

#Create RunDQ Object, for RunNumber 1, RunNumber 1 already exists in DBS

lumi_dq1 = DbsRunLumiDQ (
        RunNumber=1,
        LumiSectionNumber=123,
        DQFlagList = [flag1, flag2, flag_nosub]
	)

run_dq1 = DbsRunLumiDQ (
        RunNumber=1,
        #LumiSectionNumber=123,
        DQFlagList = [flag1, flag2, flag_nosub]
        )

try:
    # Single Run, Multiple Flags (Some sub systems have sub-sub systems, some don't)
    api.insertRunLumiDQ( [run_dq1] )
    # Single LumiSection, with in a Run (Some sub systems have sub-sub systems, some don't)
    api.insertRunLumiDQ( [lumi_dq1])

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

