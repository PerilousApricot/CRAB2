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

def print_flags_nice(dataset, dqHierarchyList):
    if len(dqHierarchyList) <= 0:
        print "No DQ information for this dataset/run found"
    print dataset
    for aDQ in dqHierarchyList:
        print "\nRunNumber: ", aDQ['RunNumber']
        print "LumiSectionNumber: ", aDQ['LumiSectionNumber']
        for aSubDQ in aDQ['DQFlagList']:
                print "      ", aSubDQ['Name'], aSubDQ['Value']
                for aSubSubDQ in aSubDQ['SubSysFlagList']:
                        print "                ", aSubSubDQ['Name'], aSubSubDQ['Value']
                        for abSubSubDQ in aSubSubDQ['SubSysFlagList'] :
                                print "                               ", abSubSubDQ['Name'], abSubSubDQ['Value']



class DbsDQOptionParser(optparse.OptionParser):
  """
     OptionParser is main class to parse options.
  """
  def __init__(self):

      optparse.OptionParser.__init__(self, usage="%prog --help or %prog --command [options]", 
		version="%prog 0.0.1", conflict_handler="resolve")

      self.add_option("--url=",action="store", type="string", dest="url", 
           help="specify URL, e.g. --url=http://cmssrv17.fnal.gov:8989/DBS/servlet/DBSServlet, If no url is provided default url from dbs.config is attempted")

      self.add_option("--dataset", action="store", type="string", dest="dataset", help="REQUIRED: specify a valid dataset path")

      self.add_option("--run", action="store", type="int", dest="run", help="specify a valid run number")

      self.add_option("--dqversion", action="store", default="", type="string", dest="dqversion", help="specify a version tag")

if __name__ == "__main__":

	try:
		optManager  = DbsDQOptionParser()
		(opts,args) = optManager.parse_args()
		opts = opts.__dict__

		url=opts['url']
		dataset=opts['dataset']
		run=opts['run']
		dqversion=opts['dqversion']


		if url in ('', None, 'BADURL'):
                        configDict = DbsConfig(opts)
                        opts['url'] = str(configDict.url())

                if dataset in ('', None):
                        print "You MUST specify a valid dataset path, use --dataset= or --help"
                        sys.exit(0)
		
		if run not in (None, ''):
			run_dq_search_criteria = DbsRunLumiDQ (
        			RunNumber=opts['run'],
        			#LumiSectionNumber can be part of this serach criteria
        			#LumiSectionNumber=123,
        			#DQFlagList = [flag1]
        			#DQFlagList = [flag1, flag2, flag3]
        		)
		else: run_dq_search_criteria = []

		api = DbsApi(opts)
		dqHierarchyList =  api.listRunLumiDQ(dataset=dataset, runLumiDQList=[run_dq_search_criteria], dqVersion=dqversion  )
    		print_flags_nice(opts['dataset'], dqHierarchyList)

	except DbsApiException, ex:
  		print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  		if ex.getErrorCode() not in (None, ""):
    			print "DBS Exception Error Code: ", ex.getErrorCode()


