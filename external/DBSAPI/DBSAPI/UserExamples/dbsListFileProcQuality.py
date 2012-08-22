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
from DBSAPI.dbsFileProcessingQuality import DbsFileProcessingQuality
optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:

    lfn='/store/data/BeamCommissioning08/Cosmics/RAW/v1/000/062/571/B60CBD20-1C82-DD11-84E2-00161757BF42.root'
    path=''
    print api.listFileProcQuality(lfn, path)
    print "SUCCESS"

    lfn=''
    path='/Cosmics/BeamCommissioning08-v1/RAW'
    print api.listFileProcQuality(lfn, path)
    print "SUCCESS"

    lfn='/store/data/BeamCommissioning08/Cosmics/RAW/v1/000/062/571/B60CBD20-1C82-DD11-84E2-00161757BF42.root'
    path='/Cosmics/BeamCommissioning08-v1/RAW'
    print api.listFileProcQuality(lfn, path)
    print "SUCCESS"

    #This will fail#########
    lfn=''
    path=''
    #print api.listFileProcQuality(lfn, path)


except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()






print "Done"

