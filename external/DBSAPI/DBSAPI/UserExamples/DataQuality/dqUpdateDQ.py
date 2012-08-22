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

def print_flags_nice(dqHierarchyList):
    for aDQ in dqHierarchyList:
        print "\nRunNumber: ", aDQ['RunNumber']
        print "LumiSectionNumber: ", aDQ['LumiSectionNumber']
        for aSubDQ in aDQ['DQFlagList']:
                print "      ", aSubDQ['Name'], aSubDQ['Value']
                for aSubSubDQ in aSubDQ['SubSysFlagList']:
                        print "                ", aSubSubDQ['Name'], aSubSubDQ['Value']


#-------------------------------------------------------------------------------
# Sub-Sub System Flag (Making it Unknown)
flag1 = DbsDQFlag (
        Name = "HCAL+",
        Value = "GOOD",
        )

# Sub-Sub System Flag  (Making it BAD)
flag2 = DbsDQFlag (
        Name = "HCAL-",
        Value = "BAD",
        )

# Sub System Flag (NO Change)
flag3 = DbsDQFlag (
        Name = "HCAL",
        Value = "UNKNOWN",
        #Well no one stops you from specifying Sub Flags
        #SubSysFlagList = [flag11, flag12]
        )
#-------------------------------------------------------------------------------

#Create RunDQ Object, for RunNumber , RunNumber  already exists in DBS
#Several Flags of same Run
run_dq = DbsRunLumiDQ (
        RunNumber=1,
	#LumiSectionNumber can be part of this serach criteria
        #LumiSectionNumber=123,
        #DQFlagList = [flag1]
        DQFlagList = [flag1, flag2, flag3]
        )

run_search = DbsRunLumiDQ (
        RunNumber=1
	)

try:

    print "List B4 Update"
    dqHierarchyList = api.listRunLumiDQ(  [run_search]  )
    print_flags_nice(dqHierarchyList)

    # Update One Flag of one Run, Update Several Flags of a Runs
    # Update Several Flags of Several Runs
    dqHierarchyList =  api.updateRunLumiDQ([run_dq])
    
    print "\n\nList AFTER Update"
    dqHierarchyList =  api.listRunLumiDQ(  [run_search]  )
    print_flags_nice(dqHierarchyList)

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

