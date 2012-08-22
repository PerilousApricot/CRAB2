#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import *
import time

try:
    optManager  = DbsOptionParser()
    (opts,args) = optManager.getOpt()

    api = DbsApi(opts.__dict__)
    versions = api.listDQVersions()
    for aVer in versions:
	print "Version: %s, CreationDate: %s" \
	   % (aVer[0], time.strftime("%a, %d %b %Y %H:%M:%S GMT",time.gmtime(long(aVer[1]))))

except DbsApiException, ex:
    print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
    if ex.getErrorCode() not in (None, ""):
      print "DBS Exception Error Code: ", ex.getErrorCode()

