#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: dqListFilesByDQ 1.3 2006/10/26 18:26:04 afaq Exp $"
#
#
import optparse
import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
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

      self.add_option("--query", action="store", type="string", dest="query",
		help="query in tag1=value1&tag2=value2... format")



if __name__ == "__main__":

        try:
                optManager  = DbsDQOptionParser()
                (opts,args) = optManager.parse_args()
                opts = opts.__dict__

		if opts['url'] in ('', None, 'BADURL'):
                        configDict = DbsConfig(opts)
                        opts['url'] = str(configDict.url())

                #if opts['url'] in ('', None, 'BADURL'):
                #        print "You must specify a valid DBS URL, use --url= or --help"
                #        sys.exit(0)

		if opts['query'] in (None, ""):
			print "You must specify a query, Use --query=, look at --help"
			sys.exit(0)

                api = DbsApi(opts)

		files=api.listFilesForRunLumiDQ(opts['query'])

		for afile in files:
			print afile['LogicalFileName']

        except DbsApiException, ex:
                print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
                if ex.getErrorCode() not in (None, ""):
                        print "DBS Exception Error Code: ", ex.getErrorCode()



"""
#-------------------------------------------------------------------------------
# Sub-Sub System Flag
flag1 = DbsDQFlag (
        Name = "HCAL+",
        Value = "GOOD",
        )
# Sub-Sub System Flag
flag2 = DbsDQFlag (
        Name = "HCAL-",
        Value = "GOOD",
        )

# Sub System Flag (Including sub-sub system flags)
flag3 = DbsDQFlag (
        Name = "HCAL",
        Value = "GOOD",
	#Well no one stops you from specifying Sub Flags
	#SubSysFlagList = [flag11, flag12]
        )
#-------------------------------------------------------------------------------

#Create RunDQ Object, for RunNumber , RunNumber  already exists in DBS

run_dq_search_criteria = DbsRunLumiDQ (
        RunNumber=1,
	#LumiSectionNumber can be part of this serach criteria
        LumiSectionNumber=123,
        #DQFlagList = [flag1]
        DQFlagList = [flag1, flag2, flag3]
        )

try:

    # One can pass a LIST of DbsRunLumiDQ Objects, that tells the API
    # What Runs/LumiSections to Look for and what Flags to look for
    # If the Objects are prepared with "hierarch or NOT, they will be pulled 
    # in hierarch.	

    # Mind that run_dq_search_criteria is just one object, API takes a LIST of such objects
    # So you must pass it as list


   files=api.listFilesForRunLumiDQ(runLumiDQList=[run_dq_search_criteria])
   #files=api.listFilesForRunLumiDQ( )
   print files


except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"
"""



