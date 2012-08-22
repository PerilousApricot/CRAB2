import sys
import optparse
import unittest
import DBSAPI.dbsApi

class DbsTestOptionParser(optparse.OptionParser):
	
	def __init__(self):
		optparse.OptionParser.__init__(self, usage="python %prog --command [options]; command =delete, migrate, run or validate")
		self.add_option("--verbosity", action="store", type="int", default=2, dest="verbosity", help="specify the verbosity level, e.g. --verbosity=1")
		self.add_option("--logfile", action="store", type="string", dest="logfile", help="specify the log output file, e.g. --logfile=output.log")
		self.add_option("--url", action="store", type="string", dest="url", help="specify the instance url, e.g. --url=http://cmsdbsdev2.cern.ch:8880/DBS_2_0_6/servlet/DBSServlet")
		self.add_option("--src_url", action="store", type="string", dest="src_url", help="specify the source url for migration, e.g. --src_url=http://cmsdbsdev2.cern.ch:8880/DBS_2_0_6/servlet/DBSServlet")
		self.add_option("--dst_url", action="store", type="string", dest="dst_url", help="specify the destination url for migration, e.g. --src_url=http://cmsdbsdev2.cern.ch:8880/DBS_2_0_6/servlet/DBSServlet")
		self.add_option("--dataset", action="store", type="string", dest="dataset", help="specify the dataset, e.g. --dataset=/A/B/C")
		self.add_option("--block", action="store", type="string", dest="block", help="specify the block, e.g. --block=/A/B/C#11111")
		self.add_option("--apiversion", action="store", type="string", dest="apiversion", help="specify the apiversion (formally), e.g. --apiversion=DBS_2_0_4")
		self.add_option("--qfile", action="store", type="string", dest="qfile", help="specify the file with queries, e.g. --qfile=queries.txt")
	
	def parse_args(self):
		return optparse.OptionParser.parse_args(self)
	
	def getOpt(self):
		return self.parse_args()


class TestSequence(unittest.TestCase):
	pass

def test_generator(api, query):
	def test(self):
		q=query.strip()
		api.executeQuery(q)
	return test


class DbsApiTester:
	def __init__(self, opts):
		self.opts    = opts
		dict 		 = {"url":opts.url, "version":opts.apiversion}
		self.api     = DBSAPI.dbsApi.DbsApi(dict)

	def deleteData(self):
		if self.opts.dataset in ("", None) or self.opts.url in ("", None):
			print "usage: dbstest delete --url=<url> --dataset=<dataset> --block=<block(optional)>"
		else:
		
			if self.opts.logfile not in ("", None):
				fsock=open(self.opts.logfile, "w")
				sys.stdout = fsock
				sys.stderr = fsock				
		
			if self.opts.block in ("", None):
				print "deleting dataset ", self.opts.dataset, " from ", self.opts.url, "..." 
				self.api.deleteProcDS(self.opts.dataset)
			else:
				print "deleting block ", self.opts.block, " from ", self.opts.url, "..." 
				self.api.deleteBlock(self.opts.dataset, self.opts.block)
							
							
			if self.opts.logfile not in ("", None):
				sys.stdout = sys.__stdout__
				sys.stderr = sys.__stderr__				


	def migrateData(self):
		if self.opts.src_url in ("", None) or self.opts.dst_url in ("", None) or self.opts.dataset in ("", None):
			print "usage: dbstest migrate --src_url=<src_url> --dst_url=<dst_url> --dataset=<dataset>"
		else:
			if self.opts.logfile not in ("", None):
				fsock=open(self.opts.logfile, "w")
				sys.stdout = fsock
				sys.stderr = fsock				
				
			self.api.migrateDatasetContents(self.opts.src_url, self.opts.dst_url, self.opts.dataset, "", False, True)
			
			if self.opts.logfile not in ("", None):
				sys.stdout = sys.__stdout__
				sys.stderr = sys.__stderr__				
		

	def runQueries(self):
		if self.opts.qfile in ("", None) or self.opts.url in ("", None):
			print "usage: dbstest run --url=<url> --qfile=<qfile> --logfile=<logfile(optional)> --verbosity=<verbosity(optional)>"
		else:
			qList=open(self.opts.qfile).readlines()
			qListMod=[]

			for q in qList:
				if not q.startswith("#") and q!="" and q not in qListMod:
					qListMod.append(q)

			suite=unittest.TestSuite()
			for q in qListMod:
				test_name='test_%s' % qListMod.index(q)
				test = test_generator(self.api, q)
				setattr(TestSequence, test_name, test)

				testcase=TestSequence(test_name)
				testcase._TestCase__testMethodDoc=q
				suite.addTest(testcase)

			if self.opts.logfile in ("", None):
				unittest.TextTestRunner(verbosity=self.opts.verbosity).run(suite)
			else:
				print "This test can take a while. Please wait..."
				fsock=open(self.opts.logfile, "w")
				unittest.TextTestRunner(stream=fsock, verbosity=self.opts.verbosity).run(suite)
		
	def runValidation(self, v=1, f=""):
		
		suite=unittest.TestLoader().loadTestsFromModule(__import__("validate"))
		if f in ("", None):
			unittest.TextTestRunner(verbosity=int(v)).run(suite)
		else:
			print "This test can take a while. Please wait..."
			fsock=open(f, "w")
			unittest.TextTestRunner(stream=fsock, verbosity=v).run(suite)


if __name__=="__main__":

	optManager=DbsTestOptionParser()
	(opts, args) = optManager.getOpt()

	if len(args)==0:
		print "use: dbstest command --<parameters>, where command=run, migrate, delete or validate"
	else:
		command=args[0]
		tester=DbsApiTester(opts)
		if (command=="run"): tester.runQueries()
		elif(command=="migrate"): tester.migrateData()
		elif(command=="delete"): tester.deleteData()
		elif(command=="validate"):
			print "\nusage: dbstest validate <verbosity (optional)> <outputfile (optional)> \n\n"	
			if len(args)==1: tester.runValidation()
			elif len(args)==2: tester.runValidation(args[1])
			elif len(args)==3: tester.runValidation(args[1], args[2])
		else: print "unknown command: ", command
