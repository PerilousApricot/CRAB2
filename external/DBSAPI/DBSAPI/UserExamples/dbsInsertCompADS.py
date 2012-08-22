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
from DBSAPI.dbsCompositeAnalysisDataset import DbsCompositeAnalysisDataset
from DBSAPI.dbsAnalysisDataset import DbsAnalysisDataset

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

ads1 = DbsAnalysisDataset(
	Name='/TestPrimary_001_20070926_15h03m39s/TestProcessed_20070926_15h03m39s/GEN-SIM/TestAnalysisDSDef_005_20070926_15h03m39s'
	)

ads2 = DbsAnalysisDataset(
	Name='/TestPrimary_001_20070927_15h34m26s/TestProcessed_20070927_15h34m26s/GEN-SIM/TestAnalysisDSDef_005_20070927_15h34m26s',
	Version='1',
	)

compAds = DbsCompositeAnalysisDataset(
		Name="TestCompAnalysisDS2",
		Description="Test Composite ADS",
                ADSList=[ads1, ads2],
                )
try:
    #api.insertFiles (proc, [myfile1], block)
    api.createCompADS(compAds)
    print "DONE", compAds

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


print "Done"

