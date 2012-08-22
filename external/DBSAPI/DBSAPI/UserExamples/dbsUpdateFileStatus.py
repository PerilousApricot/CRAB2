#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:
	api.updateFileStatus("/store/mc/Summer08/QCDpt470/GEN-SIM-RECO/IDEAL_V9_v1/0012/A23474CA-96A6-DD11-9EF9-001EC9B215F6.root", "VALID", "Support Request 106590")
	api.updateFileStatus("/store/mc/Summer08/TkAlCosmics4T/RECO/COSMMC_21X_V1_v1/0011/0AF26679-BAC0-DD11-B6A2-001EC9AA9978.root", "VALID", "Support Request 106590")
	api.updateFileStatus("/store/mc/Summer08/TkAlCosmics4T/RECO/COSMMC_21X_V1_v1/0013/62158696-27C4-DD11-B54E-001EC9AA9AD1.root", "VALID", "Support Request 106590")
	api.updateFileStatus("/store/mc/Summer08/TkAlCosmics4T/RECO/COSMMC_21X_V1_v1/0013/BCF4CC09-48C4-DD11-ADD2-001EC9AA9F31.root", "VALID", "Support Request 106590")
	api.updateFileStatus("/store/user/sdas/CMSSW_1_6_12_ReRECO_RECOSIM_100pb_QCD_Pt_30_50_CMSSW_1_6_0_01fc443369e7cd95fd75ebacc8c4eba9/qcd_reco_1062.root", "VALID", "Support Request 106590")
	api.updateFileStatus("/store/user/sdas/CMSSW_1_6_12_ReRECO_RECOSIM_100pb_QCD_Pt_30_50_CMSSW_1_6_0_01fc443369e7cd95fd75ebacc8c4eba9/qcd_reco_224.root", "VALID", "Support Request 106590")


except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()


print "Done"

