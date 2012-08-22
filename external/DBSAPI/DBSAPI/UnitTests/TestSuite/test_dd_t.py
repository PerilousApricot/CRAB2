#!/usr/bin/env python
#pylint: disable-msg=C0301,C0103

"""
Unit test for Data Discovery
"""

import unittest
import httplib
import urllib
import urllib2
import types
import os

def parseDDoutput(ddoutput, dataset):
    for line in ddoutput.split('\n'):
#        if  line.find('contains ') != -1 and line.find('located at') != -1:
#            yield line
        if  line.find('Found ') != -1:
            yield line
        if  line.find('<b>%s</b><br/>' % dataset) != -1:
            yield line

def call(url, params, dataset):
    data   = urllib2.urlopen(url, urllib.urlencode(params, doseq=True))
    result = data.read()
    res = [i for i in parseDDoutput(result, dataset)]
    return res

class testDD(unittest.TestCase):
    """
    A test class for Data Discovery
    """
    def setUp(self):
        """
        set up
        """
        self.ddurl   = os.environ['DD_TEST_URL'] + '/aSearch'
        self.dbsinst = os.environ['DD_TEST_DBSINSTANCE']
        self.dataset = os.environ['DD_TEST_DATASET']
        self.params  = {'caseSensitive':'on', 'userMode':'user',
                        'sortOrder':'', 'sortName':'',
                        'grid':0, 'method':'dbsapi',
                        'dbsInst':self.dbsinst, '_idx':0,
                        'pagerStep':1, 'userInput': ''}

    def test_DD(self): 
        params = dict(self.params)
        params['userInput'] = 'find block.dataset where dataset=%s' % self.dataset
        result = call(self.ddurl, params, self.dataset)
        result.sort()
        expect = ['Found 1 results.', '<b>%s</b><br/>' % self.dataset]
        expect.sort()
        self.assertEqual(expect, result)


#
# main
#
if __name__ == '__main__':
    unittest.main()

