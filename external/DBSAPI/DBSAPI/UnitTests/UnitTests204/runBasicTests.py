import os, sys, time
from threading import Thread
import unittest
import DBSAPI.dbsApi


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

def ql_test_generator(api, query):
	def test(self):
		q=query.strip()
		api.executeQuery(q)
	return test

def mig_test_generator(api, src_url, dst_url, dataset):
	def test(self):
		path=dataset.strip()
		api.migrateDatasetContents(src_url, dst_url, path, "", False, True)
	return test



class dbstest(Thread):
	def __init__(self, url, test, logfile=None, verbosity=1, url_list=[]):
		Thread.__init__(self)
		self.test = test
		self.logfile = logfile
		self.verbosity = verbosity
		self.api = DBSAPI.dbsApi.DbsApi({"url":url})
		self.url_list=url_list

	def run(self):

	
		if self.test=="runAll":
			os.system("./runAllTests.sh")
			
		elif self.test=="validate":
			suite=unittest.TestLoader().loadTestsFromModule(__import__("validate"))
			fsock=open(self.logfile, "w")
			unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite)

			
		elif self.test=="qlTest":
			qList=open("queries.txt").readlines()
			qListMod=[]

			for q in qList:
				if not q.startswith("#") and q!="" and q not in qListMod:
					qListMod.append(q)

			suite_ql=unittest.TestSuite()
			for q in qListMod:
				test_name='test_ql_%s' % qListMod.index(q)
				test = ql_test_generator(self.api, q)
				setattr(TestSequence, test_name, test)

				testcase=TestSequence(test_name)
				testcase._TestCase__testMethodDoc=q
				suite_ql.addTest(testcase)

			fsock=open(self.logfile, "w")
			unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite_ql)

		elif self.test=="migrate":
			datasetList=open("datasets.txt").readlines()
			datasetListMod=[]

			for path in datasetList:
				if not path.startswith("#") and path!="" and path not in datasetListMod:
					datasetListMod.append(path)

			suite_migrate=unittest.TestSuite()
			for path in datasetListMod:
					for i in range(len(self.url_list)-1):
						test_name='test_migrate_%s_%s' % (datasetListMod.index(path), i)
						test = mig_test_generator(self.api, self.url_list[i], self.url_list[i+1], path)
						setattr(TestSequence, test_name, test)

						testcase=TestSequence(test_name)
						doc="Migrate " + path.strip() + "  from  "+ getAbbr(self.url_list[i]) + "  to  " + getAbbr(self.url_list[i+1])	
						testcase._TestCase__testMethodDoc=doc
						suite_migrate.addTest(testcase)

			fsock=open(self.logfile, "w")
			unittest.TextTestRunner(stream=fsock, verbosity=self.verbosity).run(suite_migrate)


		else:
			print "Unknown Test ", selt.test

if __name__=="__main__":
	#test instance
	dbs_url=instance[sys.argv[1]]
	dbs_tests=sys.argv[2].split("-")
	dbs_logfiles=sys.argv[3].split("-")
	dbs_verbosities=sys.argv[4].split("-")
	dbs_abbrs=sys.argv[5].split("-")
	
	dbs_verbose=[]
	dbs_urls=[]
	
	for v in dbs_verbosities:
		dbs_verbose.append(int(v))
	
	for abbr in dbs_abbrs:
		dbs_urls.append(instance[abbr])
		
	if len(dbs_tests) == len(dbs_logfiles) and len(dbs_tests) == len(dbs_verbosities) and len(dbs_urls) > 1:
		for i in range(len(dbs_tests)):
			current=dbstest(dbs_url, dbs_tests[i], dbs_logfiles[i], dbs_verbose[i], dbs_urls)
			current.start()
	else:
		print "Check the runBasicTests.sh file."
