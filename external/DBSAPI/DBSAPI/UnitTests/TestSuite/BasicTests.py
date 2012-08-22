import os, sys, time
from threading import Thread
import unittest
import DBSAPI.dbsApi
from DBSAPI.dbsApiException import *



instance={
			"dev1_intlxx":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_local_xx/servlet/DBSServlet",
			"dev1_intlxx_writer":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_local_xx_writer/servlet/DBSServlet",
			"dev1_intlxx_admin":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_local_xx_admin/servlet/DBSServlet",
			"dev1_intlyy":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_local_yy/servlet/DBSServlet",
			"dev1_intlyy_writer":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_local_yy_writer/servlet/DBSServlet",
			"dev1_intlyy_admin":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_local_yy_admin/servlet/DBSServlet",
			"dev1_intg":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_global/servlet/DBSServlet",
			"dev1_intg_writer":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_global_writer/servlet/DBSServlet",
			"dev1_intg_admin":"http://vocmsvm05.cern.ch:8880/cms_dbs_int_global_admin/servlet/DBSServlet",
			"dev2_intlxx":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_local_xx/servlet/DBSServlet",
			"dev2_intlxx_writer":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_local_xx_writer/servlet/DBSServlet",
			"dev2_intlxx_admin":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_local_xx_admin/servlet/DBSServlet",
			"dev2_intlyy":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_local_yy/servlet/DBSServlet",
			"dev2_intlyy_writer":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_local_yy_writer/servlet/DBSServlet",
			"dev2_intlyy_admin":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_local_yy_admin/servlet/DBSServlet",
			"dev2_intg":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_global/servlet/DBSServlet",
			"dev2_intg_writer":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_global_writer/servlet/DBSServlet",
			"dev2_intg_admin":"http://vocmsvm06.cern.ch:8880/cms_dbs_int_global_admin/servlet/DBSServlet",
			"dev1_206":"http://vocmsvm05.cern.ch:8880/DBS_2_0_6/servlet/DBSServlet",
			"dev2_208":"http://vocmsvm06.cern.ch:8880/DBS/servlet/DBSServlet",
			"dev2_206":"http://vocmsvm06.cern.ch:8880/DBS_2_0_6/servlet/DBSServlet",
			"dev2_205":"http://vocmsvm06.cern.ch:8880/DBS_2_0_5/servlet/DBSServlet",
			"prodg":"http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
			"prodl1":"http://cmsdbsprod.cern.ch/cms_dbs_prod_local_01/servlet/DBSServlet"
			
		}

def getAbbr(url):
	abbr=None
	for a, u in instance.items():
		if u == url:
			abbr=a
	return abbr	
		

class TestSequence(unittest.TestCase):
    pass




class runall:
	def __init__(self, script, logfile):
		self.script = script
		self.logfile = logfile
	def run(self):
		command="./"+self.script + " 1>/dev/null 2>&1"
		date=str(int(time.time()))
		os.system(command)
		for dir in os.listdir("."):
			if dir.endswith(date):
				command="cp "+ dir + "/result.txt " +self.logfile
				print command
				os.system(command)
																			


class validate:
	def __init__(self, module, logfile, verbosity):
		self.module = module
		self.logfile = logfile
		self.verbosity = verbosity
	def run(self):
		suite=unittest.TestLoader().loadTestsFromModule(__import__(self.module))
		fsock=open(self.logfile, "w")
		unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite)


class ql:
	def __init__(self, url, qfile, logfile, verbosity):
		self.url=url
		self.api=DBSAPI.dbsApi.DbsApi({"url":url})
		self.qfile=qfile
		self.logfile=logfile
		self.verbosity=verbosity
		
	def ql_test_generator(self, api, query):
		def test(self):
			q=query.strip()
			api.executeQuery(q)
		return test

	def run(self):
		qList=open(self.qfile).readlines()
		qListMod=[]

		for q in qList:
			if not q.startswith("#") and q!="" and q not in qListMod:
				qListMod.append(q)

		suite_ql=unittest.TestSuite()
		for q in qListMod:
			test_name='test_ql_%s' % qListMod.index(q)
			test = self.ql_test_generator(self.api, q)
			setattr(TestSequence, test_name, test)

			testcase=TestSequence(test_name)
			testcase._TestCase__testMethodDoc=q
			suite_ql.addTest(testcase)

		fsock=open(self.logfile, "w")
		unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite_ql)
		


class migrate:
	def __init__(self, url, dfile, dataset, logfile, verbosity):
		self.url=url
		self.api=DBSAPI.dbsApi.DbsApi({"url":url})
		self.dfile=dfile
		self.dataset=dataset
		self.logfile=logfile
		self.verbosity=verbosity
		
	def mig_test_generator(self, api, dst_url, dataset, withoutParents):
		def test(self):
			path=dataset.strip()
			src_url="http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet"
			api.migrateDatasetContents(src_url, dst_url, path, "", withoutParents, True)
		return test
	
	def mig_test_generator_1(self, api, dst_url, dataset, withoutParents):
		def test(self):
			path=dataset.strip()
			src_url="http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet"
			try:
				api.migrateDatasetContents(src_url, dst_url, path, "", withoutParents, True)
				print "Trying..."
			except DbsBadResponse:
				print "Expected exception raised"
				pass
			else:
				fail("Did not raise DbsBadResponse")
		return test
	
	def run(self):
		datasetList=open(self.dfile).readlines()
		datasetListMod=[]

		for path in datasetList:
			if not path.startswith("#") and path!="" and path not in datasetListMod:
				datasetListMod.append(path)

		fsock=open(self.logfile, "w")
		suite_migrate_0=unittest.TestSuite()
		suite_migrate_1=unittest.TestSuite()
		suite_migrate_2=unittest.TestSuite()
		
		#simple migration with parents of datasets from global to this instance
		for path in datasetListMod:
			test_name='test_migrate_%s' % (datasetListMod.index(path))
			test = self.mig_test_generator(self.api, self.url, path, False)
			setattr(TestSequence, test_name, test)

			testcase=TestSequence(test_name)
			doc="Migrate " + path.strip()	
			testcase._TestCase__testMethodDoc=doc
			suite_migrate_0.addTest(testcase)
		unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite_migrate_0)

		#migration without parents
		#run only if the dataset does not exist
		path=self.dataset
		primproctier=path.split("/")
		prim=primproctier[1]
		proc=primproctier[2]
		tier=primproctier[3]
		exists = (len(self.api.listProcessedDatasets(prim, tier, proc))==1)
		print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", path, primproctier, prim, proc, tier, exists
		if not exists:
			test_name='test_migrate_wothout_parents'
			test = self.mig_test_generator(self.api, self.url, path, True)
			setattr(TestSequence, test_name, test)
			testcase=TestSequence(test_name)
			doc="Migrate without Parents, " + path.strip()
			testcase._TestCase__testMethodDoc=doc
			suite_migrate_1.addTest(testcase)
			migrate_1=unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite_migrate_1)
			exists=migrate_1.wasSuccessful()

		#migration without parents the existing dataset
		test_name='test_existing_migrate_wothout_parents'
		test = self.mig_test_generator_1(self.api, self.url, path, True)
		setattr(TestSequence, test_name, test)
		testcase=TestSequence(test_name)
		doc="Migrate EXISTING Dataset without Parents, " + path.strip()
		testcase._TestCase__testMethodDoc=doc
		suite_migrate_2.addTest(testcase)
		if exists:
			unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite_migrate_2)



class dd:
	def __init__(self, module, logfile, verbosity, ddurl, ddinstance, dataset):
		self.module=module
		self.logfile=logfile
		self.verbosity=verbosity
		os.environ['DD_TEST_URL']=ddurl
		os.environ['DD_TEST_DBSINSTANCE']=ddinstance
		os.environ['DD_TEST_DATASET']=dataset
		
	def run(self):
		suite=unittest.TestLoader().loadTestsFromModule(__import__(self.module))
		fsock=open(self.logfile, "w")
		unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite)
		
class views:
	def __init__(self, module, logfile, verbosity, url, dbs_test_ver):
		self.module=module
		self.logfile=logfile
		self.verbosity=verbosity
		os.environ['DBS_TEST_URL']=url
		os.environ['DBS_TEST_VER']=dbs_test_ver
		
	def run(self):
		suite=unittest.TestLoader().loadTestsFromModule(__import__(self.module))
		fsock=open(self.logfile, "w")
		unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite)
		
