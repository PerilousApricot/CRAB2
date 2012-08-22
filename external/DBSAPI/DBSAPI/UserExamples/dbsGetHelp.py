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

try:
  optManager  = DbsOptionParser()
  (opts,args) = optManager.getOpt()
  api = DbsApi(opts.__dict__)
  
  myList = api.getHelp("")
  for kw in myList:
	  print 'ENTITY\t ' + kw['name']
	  attrList = kw['attrs']
	  print 'ATTRIBUTES'
	  for attr in attrList:
		  toPrint = '\t' + kw['name'] + '.' + attr
		  print toPrint
	  examples = kw['examples']
	  print 'EXAMPLES'
	  for aex in examples:
		  print aex['desc']
		  print aex['query']
		  print '__________________________________________________________________________'
	  print '\n\n'
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

