#!/usr/bin/env python
#
# Revision: $"
# Id: $"
#
import sys, optparse
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsConfig import DbsConfig
from DBSAPI.dbsAnalysisDatasetDefinition import DbsAnalysisDatasetDefinition
from DBSAPI.dbsAnalysisDataset import DbsAnalysisDataset
from xml.sax.saxutils import escape, unescape

class DbsDQOptionParser(optparse.OptionParser):
  """
     OptionParser is main class to parse options.
  """
  def __init__(self):

      optparse.OptionParser.__init__(self, usage="%prog --help or %prog --command [options]", 
		version="%prog 0.0.1", conflict_handler="resolve")

      self.add_option("--url=",action="store", type="string", dest="url", default="https://cmsdbsprod.cern.ch:8443/cms_dbs_prod_global_writer/servlet/DBSServlet", 
           help="specify URL, DEFAULT is --url=https://cmsdbsprod.cern.ch:8443/cms_dbs_prod_global_writer/servlet/DBSServlet")

      self.add_option("--dataset", action="store", type="string", dest="dataset", help="REQUIRED: specify a valid dataset path")

      self.add_option("--query", action="store", type="string", dest="query", help="REQUIRED: specify a valid dbs QL query")

      self.add_option("--storetemplatequery", action="store", default="", type="string", dest="storetemplatequery", help="Specify a valid name for the query to be saved (TEMPLATE ADS definition, if name is already in use the query will be re-used from DBS)")

      self.add_option("--storequery", action="store", default="", type="string", dest="storequery", help="Specify a valid name for the query to be saved (CONCRETE ADS definition, if name is already in use the query will be re used from DBS)")

      self.add_option("--description", action="store", type="string", dest="desc", help="REQUIRED: specify a string description of what this ADS Definition is for.")
	
if __name__ == "__main__":

		optManager  = DbsDQOptionParser()
		(opts,args) = optManager.parse_args()
		opts = opts.__dict__
		
		url=opts['url']
		dataset=opts['dataset']
		query=opts['query']
		storetemplatequery=opts['storetemplatequery']
		storequery=opts['storequery']
		desc=opts['desc']


		if url in ('', None, 'BADURL'):
                        configDict = DbsConfig(opts)
                        opts['url'] = str(configDict.url())

                if dataset in ('', None):
                        print "You MUST specify a valid dataset path, use --dataset= or --help"
                        sys.exit(1)
		if query in ('', None):
                        print "You MUST specify a valid query, use --query= or --help"
                        sys.exit(1)
		
		if storetemplatequery in ('', None) and storequery in ('', None):
                        print "You MUST specify a valid storequery or storetemplatequery , use --storequery= , --storetemplatequery or --help"
                        sys.exit(1)

		if not storetemplatequery in ('', None) and not storequery in ('', None):
			print "You cannot specify both storequery and storetemplatequery at the same time use --help"
			sys.exit(1)
		if desc in ('', None):
			print "You MUST give a reasonable description of the ADS Definition that you are creating"
			sys.exit(1)

		api = DbsApi(opts)

		if not storetemplatequery in ('', None) :
			adsdef = DbsAnalysisDatasetDefinition (
					Name=storetemplatequery,
                                        #ProcessedDatasetPath=martQ['PATH'],  #No path for template query
                                        UserInput=escape(query),
                                        SQLQuery=escape(query),
                                        Description=desc
                        		)

			ads = DbsAnalysisDataset(
					Type='TEST',
					Status='NEW',
					PhysicsGroup='RelVal',
					Path=dataset,
					Description="scripted"
					)		
		else:
			adsdef = DbsAnalysisDatasetDefinition (
					Name=storequery,
					ProcessedDatasetPath=dataset,
					UserInput=escape(query),
					SQLQuery=escape(query),
					Description=storequery,
					)
			ads = DbsAnalysisDataset(
					Type='TEST',
					Status='NEW',
					PhysicsGroup='RelVal',
					#Path=dataset, NO NEED to provide PATH in CONCRETE definition
					#Description=desc
					)
		try:
			api.createAnalysisDatasetDefinition (adsdef)
		except DbsApiException, ex:
                	if ex.getErrorMessage().find("Already Exists") < 0:
				print ex
			print "WARNING ....ADS DEF ALREADY EXISTS, Will be RE USED from DBS..and query provided here will NOT be used..."	
                	print "Processing, please wait..."
		try:
			api.createAnalysisDataset(ads, storetemplatequery)	
		except DbsApiException, ex:
  			print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  			if ex.getErrorCode() not in (None, ""):
    				print "DBS Exception Error Code: ", ex.getErrorCode()


