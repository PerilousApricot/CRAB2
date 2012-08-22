#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: setDQ.py 1.3 2006/10/26 18:26:04 afaq Exp $"
#
import sys, optparse
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsDQFlag import DbsDQFlag
from DBSAPI.dbsRunLumiDQ import DbsRunLumiDQ
from DBSAPI.dbsConfig import DbsConfig


class DbsDQOptionParser(optparse.OptionParser):
  """
     OptionParser is main class to parse options.
  """

  def __init__(self):

      optparse.OptionParser.__init__(self, usage="%prog --help or %prog --command [options]", 
		version="%prog 0.0.1", conflict_handler="resolve")

      self.add_option("--url=",action="store", type="string", dest="url", 
           help="specify URL, e.g. --url=http://cmssrv17.fnal.gov:8989/DBS/servlet/DBSServlet, If no url is provided default url from dbs.config is attempted")

      self.add_option("--dataset", action="store", type="string", dest="dataset", help="specify a valid dataset path")

      self.add_option("--run", action="store", type="int", dest="run", help="specify a valid run number")

      self.add_option("--flag", action="store", type="string", dest="flag", help="Quality Information Mask")

      self.add_option("--value", action="store", type="string", dest="value", 
		help="Value can be GOOD, BAD and UNKNOWN or a INTEGER value")



if __name__ == "__main__":

	try:
		optManager  = DbsDQOptionParser()
		(opts,args) = optManager.parse_args()
		opts = opts.__dict__

		if opts['url'] in ('', None, 'BADURL'):
                        configDict = DbsConfig(opts)
                        opts['url'] = str(configDict.url())

		#if opts['url'] in ('', None, 'BADURL'):
		#	print "You must specify a valid DBS URL, use --url= or --help"
		#	sys.exit(0)

                if opts['dataset'] in ('', None):
                        print "You must specify a valid dataset path, use --run= or --help"
                        sys.exit(0)

                if opts['run'] in ('', None):
                        print "You must specify a valid run number, use --run= or --help"
                        sys.exit(0)

                if opts['flag'] in ('', None):
                        print "You must specify a valid QIM, use --flag= or --help"
                        sys.exit(0)

                if opts['value'] in ('', None):
                        print "You must specify a valid value: GOOD, BAD, UNKNOWN or a INTEGER value, use --value= or --help"
                        sys.exit(0)

		flag = DbsDQFlag (
			Name = opts['flag'],
			Value = opts['value'],
			)
		run_dq = DbsRunLumiDQ (
			RunNumber=opts['run'],
			#LumiSectionNumber=123,
			DQFlagList = [flag]
			)

		api = DbsApi(opts)

		api.updateRunLumiDQ(opts['dataset'], [run_dq])
		print "%s is set %s for run: %s" %(opts['flag'], opts['value'], opts['run'])

		
	except DbsApiException, ex:
  		print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  		if ex.getErrorCode() not in (None, ""):
    			print "DBS Exception Error Code: ", ex.getErrorCode()


