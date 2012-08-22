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

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:

    adsxml="""<?xml version='1.0' standalone='yes'?>
<!-- DBS Version 1 -->
<dbs>
<analysis_dataset name='TESTADS' description='This is just a test' type='TEST' status='NEW' physics_group_name='RelVal' created_by='anzar' creation_date='1023456'/>
<src url='http://cmssrv17.fnal.gov:8989/DBSADSTEST01/servlet/DBSServlet' />
<dataset path='/QCD_Pt_50_80/CMSSW_1_4_4-CSA07-1962/GEN-SIM' />
<analysis_dataset_def name='TESTADSDEF' query='patternPrim: QCD_Pt_50_80, patternDT: GEN-SIM, patternProc: CMSSW_1_4_4-CSA07-1962' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/EC870B01-4124-DC11-9829-00E0813266D4.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/D47F0CCB-4024-DC11-A9C0-00E08134C270.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/CCED8A7A-3924-DC11-BBC5-00E081325AE8.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/CABE9EE0-4024-DC11-B6DC-00E081345B98.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/A8843C2B-3C24-DC11-9367-00E08134C2C8.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/A042D65D-C923-DC11-8D6A-00E081339574.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/829FF0CD-4024-DC11-A023-00E0813395C0.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/62A966BE-8624-DC11-B4D9-00E081325D08.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/4E94C89B-3424-DC11-9D93-00E08133CD90.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/12E282D6-3C24-DC11-B92A-00E081328944.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/040424A4-9624-DC11-9E32-00E0813266D4.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/E88C5D03-4124-DC11-8D9E-00E08132879C.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/C2F0E955-3D24-DC11-8B7F-00E08133CD9E.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/A09EF847-3D24-DC11-962C-00E081345B98.root' />
<file lfn='/store/mc/2007/6/21/CSA07-QCD_Pt_50_80-1962/0002/88FB87FD-BD23-DC11-A73D-00E0813267E6.root' />
</dbs>
    """

    api.createAnalysisDatasetFromLFNs(adsxml)

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

