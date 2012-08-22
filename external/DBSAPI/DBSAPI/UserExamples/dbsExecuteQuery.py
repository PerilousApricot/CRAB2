#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
#
import sys, optparse
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsDQFlag import DbsDQFlag
from DBSAPI.dbsRunLumiDQ import DbsRunLumiDQ
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsConfig import DbsConfig
#
#
class DbsQueryOptionParser(optparse.OptionParser):
  """
     OptionParser is main class to parse options.
  """

  def __init__(self):

      optparse.OptionParser.__init__(self, usage="%prog --help or %prog --command [options]",
                version="%prog 0.0.1", conflict_handler="resolve")

      self.add_option("--url=",action="store", type="string", dest="url", 
           help="specify URL, e.g. --url=http://cmssrv17.fnal.gov:8989/DBS/servlet/DBSServlet, If no url is provided default url from dbs.config is attempted")

      self.add_option("--query", action="store", type="string", dest="query", default="",
                help="query in tag1=value1&tag2=value2... format")


if __name__ == "__main__":

        try:
                optManager  = DbsQueryOptionParser()
                (opts,args) = optManager.parse_args()
                opts = opts.__dict__

                if opts['url'] in ('', None, 'BADURL'):
			configDict = DbsConfig(opts)
			opts['url'] = str(configDict.url())

                if opts['query'] in (None, ""):
                        print "You must specify a query, Use --query=, look at --help"
                        sys.exit(0)

                api = DbsApi(opts)
		print opts['query']
		#print api.executeQuery(opts['query'], 2, 5, "query")
		#print api.executeQuery(opts['query'], 1,5,type="exe")
		#print api.executeQuery(opts['query'], ignoreCase=False)
		print api.executeQuery(opts['query'])
  		#print api.executeQuery("select file,ls where path=/GlobalMar08-Express/Online/RAW")

	except DbsApiException, ex:
  		print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  		if ex.getErrorCode() not in (None, ""):
    			print "DBS Exception Error Code: ", ex.getErrorCode()      
			print "I am herererrrrrrrrrrrrrrrrrrrrrrr->>>>>>>>>>>>>>>"

