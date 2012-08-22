#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
#
import sys
#from dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi

try:
  optManager  = DbsOptionParser()
  (opts,args) = optManager.getOpt()

  args={}
  args['url']='http://cmssrv49.fnal.gov:8989/DBSTEST/servlet/DBSServlet' 
  args['version']='DBS_2_0_9'
  args['mode']='POST'
  args['level']='INFO'
  api = DbsApi(args)

  #api = DbsApi(opts.__dict__)

  # List all parameter sets
  print ""
  print "Primary Datasets"
  for primary in api.listPrimaryDatasets('*'):
  #for primary in api.listPrimaryDatasets(''):
     print "  %s" % primary
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()      

print "Done"

