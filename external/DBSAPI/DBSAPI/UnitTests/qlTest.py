import sys
import unittest
import DBSAPI.dbsApi

class TestSequence(unittest.TestCase):
	pass	

def test_generator(dbsurl, query):
	def test(self):
		q=query.strip()
		api=DBSAPI.dbsApi.DbsApi({'url':dbsurl})
		api.executeQuery(q)
	return test

if __name__=="__main__":
	if(len(sys.argv)<2):
		print "please use: python qlTest <dbsurl> <output.log>"
		
	else:
		print "This test can take a while. please wait..."
		dbsurl=sys.argv[1]
	
		qList = open('queries.txt').readlines()
		qListMod=[]

		for q in qList:
			if not q.startswith("#") and q!="" and q not in qListMod:
				qListMod.append(q)
	
		suite=unittest.TestSuite()
		for q in qListMod:
			test_name='test_%s' % qListMod.index(q)
			test = test_generator(dbsurl, q)
			setattr(TestSequence, test_name, test)

			testcase=TestSequence(test_name)
			testcase._TestCase__testMethodDoc=q
			suite.addTest(testcase)

		if(len(sys.argv)>2):
			fsock=open(sys.argv[2], 'w')
			unittest.TextTestRunner(verbosity=2, stream=fsock).run(suite)
		else:
			unittest.TextTestRunner(verbosity=2).run(suite)
