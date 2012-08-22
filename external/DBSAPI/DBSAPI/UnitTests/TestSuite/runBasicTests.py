import sys, os
from time import strftime
import ConfigParser
import BasicTests

class DbsUnitTest:
	def __init__(self, configfile):
		self.config = ConfigParser.RawConfigParser()
		self.config.read(configfile)
		self.time=strftime("%Y%m%d_%H%M%S")
		
		self.url=self.config.get('common','url')
		self.schedule=self.config.get('common', 'schedule').split("*")

	def genlogfile(self, test):
		logfile=self.config.get('common', 'log_directory')+ "/" + self.config.get(test, 'logfile')+"__"+ self.config.get('common', 'abbreviation')+"__"+ self.config.get('common', 'server_version')+"__"+ self.config.get('common', 'client_version')+"__"+ self.time+".log"
		return logfile

	def dbstest(self, testname):
		if(testname=='runall'):
			script=self.config.get('runall','script')
			logfile=self.genlogfile('runall')
			BasicTests.runall(script, logfile).run()
			
		elif (testname=='validate'):
			module=self.config.get('validate','module')
			logfile=self.genlogfile('validate')
			verbosity=self.config.getint('validate', 'verbosity')
			BasicTests.validate(module, logfile, verbosity).run()
			
		elif (testname=='ql'):
			url=self.config.get('common','url')
			qfile=self.config.get('ql', 'qfile')
			logfile=self.genlogfile('ql')
			verbosity=self.config.getint('ql', 'verbosity')
			BasicTests.ql(url, qfile, logfile, verbosity).run()
			
		elif (testname=='migrate'):
			url=self.config.get('common', 'url')
			dfile=self.config.get('migrate', 'dfile')
			dataset=self.config.get('migrate', 'dataset')
			logfile=self.genlogfile('migrate')
			verbosity=self.config.getint('migrate', 'verbosity')
			BasicTests.migrate(url, dfile, dataset, logfile, verbosity).run()
		
		elif (testname=='dd'):
			module=self.config.get('dd','module')
			logfile=self.genlogfile('dd')
			verbosity=self.config.getint('dd', 'verbosity')
			ddurl=self.config.get('dd', 'ddurl')
			ddinstance=self.config.get('dd', 'ddinstance')
			dataset=self.config.get('dd', 'dataset')
			BasicTests.dd(module, logfile, verbosity, ddurl, ddinstance, dataset).run()
			
		elif (testname=='views'):
			module=self.config.get('views','module')
			logfile=self.genlogfile('views')
			verbosity=self.config.getint('views', 'verbosity')
			url=self.config.get('common', 'url')
			dbs_test_ver=self.config.get('views', 'dbs_test_ver')
			BasicTests.views(module, logfile, verbosity, url, dbs_test_ver).run()
		else:
			print "UNKNOWN TEST", testname
			
	def run(self, logfile):
		print "List of tests to be performed:", self.schedule 
		print "Start..."
		fsock=open(logfile, "w")
		for test in self.schedule:
			print test	
			save_stdout=sys.stdout
			save_stderr=sys.stderr
			sys.stdout=fsock
			sys.stderr=fsock
			self.dbstest(test)
			sys.stdout=save_stdout
			sys.stderr=save_stderr
			print self.genlogfile(test)
			print ""

if __name__=="__main__":
	DbsUnitTest(sys.argv[1]).run(sys.argv[2])
