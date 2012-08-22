#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
import sys, optparse
import xml.sax, xml.sax.handler
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsOptions import DbsOptionParser
from xml.sax import SAXParseException
#
#
if __name__ == "__main__":

    # Query DBS
    try:
  	optManager  = DbsOptionParser()
  	(opts,args) = optManager.getOpt()
  	api = DbsApi(opts.__dict__)
	query="find file where dataset=/Commissioning2008Ecal-A/Online/RAW and run=39457 and lumi=1"
	xmldata = api.executeQuery(query)

    except DbsApiException, ex:
  		print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  		if ex.getErrorCode() not in (None, ""):
    			print "DBS Exception Error Code: ", ex.getErrorCode()      

    # Parse the resulting xml output.
    files = []
    try:
      class Handler (xml.sax.handler.ContentHandler):

        def startElement(self, name, attrs):
          if name == 'result':
            files.append(str(attrs['FILES_LOGICALFILENAME']))

      xml.sax.parseString (xmldata, Handler ())
    except SAXParseException, ex:
      msg = "Unable to parse XML response from DBS Server"
      msg += "\n  Server has not responded as desired, try setting level=DBSDEBUG"
      raise DbsBadXMLData(args=msg, code="5999")

    #files contain the resultant files in DBS
    for afile in files:
	print afile



