import unittest
import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsUtil import *

import datetime
import time


optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

serverInfo = api.getServerInfo()
isMYSQL = serverInfo['InstanceType']
isGlobal = serverInfo['InstanceName']

qList = open('queries.txt').readlines()
qListMod=[]

for q in qList:
    if not q.startswith("#") and q!="" and q not in qListMod:
        if q.find(" dq") != -1:
            if isMYSQL == "MYSQL":
                continue
        qListMod.append(q)
suite=unittest.TestSuite()

class TestSequence(unittest.TestCase):
	pass	

def test_generator( query):
    def test(self):
        q=query.strip()
        api.executeQuery(q)
    return test
        

def fillsuite():
    for q in qListMod:
        test_name='test_%s' % qListMod.index(q)
        test = test_generator( q)
        setattr(TestSequence, test_name, test)
        testcase=TestSequence(test_name)
        testcase._TestCase__testMethodDoc=q
        suite.addTest(testcase)
    return suite
    
if __name__=="__main__":
    fillsuite()
    print "Test begin"        
    unittest.TextTestRunner(verbosity=2).run(suite)
