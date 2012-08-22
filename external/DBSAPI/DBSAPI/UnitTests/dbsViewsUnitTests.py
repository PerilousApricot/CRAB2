#!/usr/bin/env python
#pylint: disable-msg=C0301,C0103

"""
Unit test for DBS views
"""

import unittest
import httplib
import urllib
import urllib2
import types
import time
import os
import sys
from xml.dom.minidom import parse, parseString

from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsUtil import *

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

def parseDBSoutput(data, exclude=None):
    """
    DBS XML parser for DBS server DBS_2_0_6 and later
    """
    dom  = parseString(data)
    datalist = []
    for node in dom.getElementsByTagName('row'):
        olist = []
        for child in node.childNodes:
            subnode = child.firstChild
            if  not subnode:
                continue
            data = subnode.data
            tag = subnode.parentNode.tagName
            if  exclude:
                if  exclude != tag:
                    #if  tag.lower().find('creationdate') != -1:
                    #    data = timeformat(data)
                    olist.append((tag, data))
            else:
                olist.append((tag, data))
#            print "tag ", subnode.parentNode.tagName
#            print "data", data
#            olist.append((subnode.parentNode.tagName,data))
        if  olist:
            if  len(olist) == 1:
                datalist.append(olist[-1])
            else:
                datalist.append(olist)
    return datalist

def timeformat(itime):
    """Return time in CEST timezone as DBS server does"""
    num = eval(itime)
    return time.strftime("%Y-%m-%d %H:%M:%S CEST", time.gmtime(num+60*60*2))

def call(url, params, check=None):
    data   = urllib2.urlopen(url, urllib.urlencode(params, doseq=True))
    result = data.read()
    if  check and result.find('exception') != -1:
        raise Exception(result)
    return result

class testDBS(unittest.TestCase):
    """
    A test class for the DAS DBS module
    """
    def setUp(self):
        """
        set up DAS core module
        """
        self.url = "http://vocmsvm05.cern.ch:8880/cms_dbs_int_global_writer/servlet/DBSServlet"
        self.url = "http://vocmsvm05.cern.ch:8880/CMS_DBS/servlet/DBSServlet"
        self.ver = 'DBS_2_0_6'
	self.url = api.url() 	 
	self.ver = api.version()
	
        #self.url = os.environ['DBS_TEST_URL']
        #self.ver = os.environ['DBS_TEST_VER']
        self.params = {'apiversion':self.ver,
                       'api':'executeSummary','begin':'0','end':'1'}

    def test_no_executeSummary(self): 
        params = dict(self.params)
        params['query'] = 'find dataset where dataset like *CRUZET4*'
        result = call(self.url, params)
        expect = """<?xml version='1.0' standalone='yes'?>\n<!-- DBS Version 1 -->\n<dbs>\n<exception message=' ____________ API Invoked executeSummary____________\nInvalid API'  code ='1018' detail ='The api executeSummary provided by the client is not valid'/>\n\n<stack_trace>\n</stack_trace>\n</dbs>\n"""
        self.assertRaises(Exception, expect, result)

    def test_unboundquery_executeSummary(self): 
        params = dict(self.params)
        params['query'] = 'find dataset where dataset like *CRUZET4*'
        params['begin'] = ''
        params['end'] = ''
        result = call(self.url, params)
        expect = """<?xml version='1.0' standalone='yes'?>\n<!-- DBS Version 1 -->\n<dbs>\n<exception message=' ____________ API Invoked executeSummary____________\nInvalid API'  code ='4000' detail ='Unbound query is not allowed in summary view'/>\n\n<stack_trace>\n</stack_trace>\n</dbs>\n" != "<?xml version='1.0' standalone='yes'?>\n<!-- DBS Version 1 -->\n<dbs>\n<exception message=' ____________ API Invoked executeSummary____________\nUnexpected execution exception'  code ='4000' detail ='Unbound query is not allowed in summary view'/>\n\n<stack_trace>\n</stack_trace>\n</dbs>\n"""
        self.assertRaises(Exception, expect, result)

    def test_toowiderange_executeSummary(self): 
        params = dict(self.params)
        params['query'] = 'find dataset where dataset like *CRUZET4*'
        params['begin'] = '0'
        params['end'] = '200'
        result = call(self.url, params)
        expect = """<?xml version='1.0' standalone='yes'?>\n<!-- DBS Version 1 -->\n<dbs>\n<exception message=' ____________ API Invoked executeSummary____________\nInvalid API'  code ='4000' detail ='Too wide range for summary view'/>\n\n<stack_trace>\n</stack_trace>\n</dbs>\n" != "<?xml version='1.0' standalone='yes'?>\n<!-- DBS Version 1 -->\n<dbs>\n<exception message=' ____________ API Invoked executeSummary____________\nUnexpected execution exception'  code ='4000' detail ='Too wide range for summary view'/>\n\n<stack_trace>\n</stack_trace>\n</dbs>\n"""
        self.assertRaises(Exception, expect, result)

    def test_executeSummary_noparams(self): 
        params = dict(self.params)
#        params['query'] = 'find dataset where dataset like *CRUZET4*'
        params['query'] = 'find dataset where dataset like *KKKKKK*'
        result = call(self.url, params)
#        expect = """<?xml version='1.0' standalone='yes'?>\n<!-- DBS Version 1 -->\n<dbs>\n<summary_view>\n<exception>\njava.sql.SQLException: ORA-00936: missing expression\n\n</exception>\n</summary_view>\n<SUCCESS/>\n</dbs>\n"""
        expect = """<?xml version='1.0' standalone='yes'?>\n<!-- DBS Version 1 -->\n<dbs>\n<summary_view>\n</summary_view>\n<results>\n</results>\n<SUCCESS/>\n</dbs>\n"""
        self.assertEqual(expect, result)
#        self.assertRaises(Exception, expect, result)

    def test_executeSummary_releasesummary(self): 
        selkeys= ['release', 'algo.createdate', 'algo.createby',
                  'algo.family', 'algo.exe']
#        cond   = "release lile *"
#        query  = "find "+','.join(selkeys)+" where " + cond
        cond   = ''
        query  = "find "+','.join(selkeys)

        # call executeQuery
        params = dict(self.params)
        params['query'] = query
        params['api'] = 'executeQuery'
        result = call(self.url, params, check=True)

        dbs_query = []
        for item in parseDBSoutput(result):
            for key, val in item:
                dbs_query.append(val)

        # call executeSummary
        if  cond:
            query ="find release where " + cond
        else:
            query ="find release"
        params['query'] = query
        params['api'] = 'executeSummary'
        result = call(self.url, params, check=True)
        dbs_summary = []
        for item in parseDBSoutput(result, exclude='release'):
            for key, val in item:
                dbs_summary.append(val)
        self.assertEqual(dbs_query, dbs_summary)

    def test_executeSummary_filesummary(self): 
        selkeys= ['file', 'file.createdate', 'file.createby', 'file.checksum', 
                  'file.numevents', 'file.size', 'file.type', 'file.status']
        cond   = "dataset=/test_Primary*"
        query  = "find "+','.join(selkeys)+" where " + cond

        # call executeQuery
        params = dict(self.params)
        params['query'] = query
        params['api'] = 'executeQuery'
        result = call(self.url, params)
        dbs_query = []
        for item in parseDBSoutput(result):
            for key, val in item:
                dbs_query.append(val)

        # call executeSummary
        query ="find file where " + cond
        params['query'] = query
        params['api'] = 'executeSummary'
        result = call(self.url, params, check=True)
        dbs_summary = []
        for item in parseDBSoutput(result, exclude='file'):
            for key, val in item:
                dbs_summary.append(val)
        self.assertEqual(dbs_query, dbs_summary)

    def test_executeSummary_runsummary(self): 
#        selkeys= ['run', 'run.createdate', 'run.createby', 'run.moddate', 
#                  'run.modby', 'run.totlumi', 'run.store', 'run.starttime',
#                  'run.endtime', 'run.numevents', 'lumi.startevnum', 
#                  'lumi.endevnum', 'count(lumi.evnum)']
        # we reduce runsummary query, by removing count(lumi.evnum) since QL
        # has problems with that in this query
        selkeys= ['run', 'run.createdate', 'run.createby', 'run.moddate', 
                  'run.modby', 'run.totlumi', 'run.store', 'run.starttime',
                  'run.endtime', 'run.numevents', 'lumi.startevnum', 
                  'lumi.endevnum']
        cond   = "run = 1"
        query  = "find "+','.join(selkeys)+" where " + cond

        # call executeQuery
        params = dict(self.params)
        params['query'] = query
        params['api'] = 'executeQuery'
        result = call(self.url, params, check=True)
        dbs_query = []
        for item in parseDBSoutput(result):
            itemlist = []
            for key, val in item:
                itemlist.append(val)
            dbs_query.append(itemlist)

        # call executeSummary
        query ="find run where " + cond
        params['query'] = query
        params['api'] = 'executeSummary'
        result = call(self.url, params, check=True)
        dbs_summary = []
        for item in parseDBSoutput(result, exclude='run'):
            itemlist = []
            for key, val in item[:-1]: # we take up-to-last element, see above
		## From DBS_2_0_9 moddate IS in unix-time format so we do not need this conversion
		## AA -- 10/09/2009
                # moddate is not conerted by DBS code to DBS time format and
                # returned as sec since epoch
                #if  key.upper().find('MODIFICATIONDATE') != -1:
                #    val = time.strftime("%Y-%m-%d %H:%M:%S CEST", 
                #                time.gmtime(int(val)+2*60*60))
                itemlist.append(val)
            dbs_summary.append(itemlist)
        self.assertEqual(dbs_query, dbs_summary)

    def test_executeSummary_sitesummary(self): 
#        selkeys= ['site', 'site.createdate', 'site.createby', 
#                  'count(block.dataset)'] 
# TODO: use short list without count, since LEFT/OUTER JOIN problem in DBS QL
        selkeys= ['site']
        cond   = "site like *"
        query  = "find "+','.join(selkeys)+" where " + cond

        # call executeQuery
        params = dict(self.params)
        params['query'] = query
        params['api'] = 'executeQuery'
        result = call(self.url, params, check=True)
        dbs_query = []
        for item in parseDBSoutput(result):
            itemlist = []
#            for key, val in item:
#                itemlist.append(val)
            itemlist.append(item[1])
            dbs_query.append(itemlist)

        # call executeSummary
        query ="find site where " + cond
        params['query'] = query
        params['api'] = 'executeSummary'
        result = call(self.url, params, check=True)
        dbs_summary = []
        for item in parseDBSoutput(result, exclude='site'):
            itemlist = []
            for key, val in item[:1]: # use short list, see above comment
                itemlist.append(val)
            dbs_summary.append(itemlist)
        self.assertEqual(dbs_query, dbs_summary)

    def test_executeSummary_primdssummary(self): 
        selkeys= ['primds', 'primds.createdate', 'primds.createby', 
                  'datatype', 'count(procds)'] 
        cond   = "primds like * order by primds asc"
        query  = "find "+','.join(selkeys)+" where " + cond

        # call executeQuery
        params = dict(self.params)
        params['query'] = query
        params['api'] = 'executeQuery'
        result = call(self.url, params, check=True)
        dbs_query = []
        for item in parseDBSoutput(result):
            for key, val in item:
                dbs_query.append(val)

        # call executeSummary
        query ="find primds where " + cond
        params['query'] = query
        params['api'] = 'executeSummary'
        params['sortKey'] = 'Name'
        params['sortOrder'] = 'asc'
        result = call(self.url, params, check=True)
        dbs_summary = []
        for item in parseDBSoutput(result, exclude='primds'):
            for key, val in item:
                dbs_summary.append(val)
        self.assertEqual(dbs_query, dbs_summary)

    def test_executeSummary_procdssummary(self): 
#        selkeys= ['procds', 'procds.createdate', 'procds.createby', 
#                  'count(block.dataset)', 'sum(block.size)',
#                  'sum(block.numfiles)', 'sum(block.numevents)'] 
# TODO: disable full look-up for this view, since DBS QL doesn't support
# combined count and sum
        selkeys= ['procds', 'procds.createdate', 'procds.createby']
        cond   = "procds like *"
        query  = "find "+','.join(selkeys)+" where " + cond

        # call executeQuery
        params = dict(self.params)
        params['query'] = query
        params['api'] = 'executeQuery'
        result = call(self.url, params, check=True)
        dbs_query = []
        for item in parseDBSoutput(result):
            itemlist = []
            for key, val in item:
                itemlist.append(val)
            dbs_query.append(itemlist)

        # call executeSummary
        query ="find procds where " + cond
        params['query'] = query
        params['api'] = 'executeSummary'
        result = call(self.url, params, check=True)
        dbs_summary = []
        for item in parseDBSoutput(result, exclude='procds'):
            itemlist = []
            for key, val in item[:3]: # see above disabled fields
                itemlist.append(val)
            dbs_summary.append(itemlist)
        self.assertEqual(dbs_query, dbs_summary)

    def test_executeSummary_tiersummary(self): 
#        selkeys= ['tier', 'tier.createdate', 'tier.createby', 
#                  'count(block.dataset)']
# TODO: disable full look-up of this view, since DBS QL doesn't use LEFT OUTER
# JOIN
        selkeys= ['tier', 'tier.createdate', 'tier.createby']
        cond   = "tier like *"
        query  = "find "+','.join(selkeys)+" where " + cond

        # call executeQuery
        params = dict(self.params)
        params['query'] = query
        params['api'] = 'executeQuery'
        result = call(self.url, params, check=True)
        dbs_query = []
        for item in parseDBSoutput(result):
            for key, val in item:
                dbs_query.append(val)

        # call executeSummary
        query ="find tier where " + cond
        params['query'] = query
        params['api'] = 'executeSummary'
        result = call(self.url, params, check=True)
        dbs_summary = []
        for item in parseDBSoutput(result, exclude='tier'):
            for key, val in item[:3]: # use disabled fields, see above
                dbs_summary.append(val)
        self.assertEqual(dbs_query, dbs_summary)

    def test_executeSummary_datasetsummary(self): 
#        selkeys= ['dataset', 'dataset.createdate', 'dataset.createby', 
#                  'sum(block.size)', 'count(block.dataset)', 'sum(block.numfiles)',
#                  'sum(block.numevents)', 'sum(site)' ]
        # TODO: disable full datasetsummary look-up since DBS QL doesn't support
        # multiple combinations of sum and count, so we'll only look-up first
        # 4 fields
        selkeys= ['dataset', 'dataset.createdate', 'dataset.createby', 
                  'sum(block.size)']
        cond   = "dataset like * order by dataset desc"
        query  = "find "+','.join(selkeys)+" where " + cond

        # call executeQuery
        params = dict(self.params)
        params['query'] = query
        params['api'] = 'executeQuery'
        result = call(self.url, params, check=True)

        dbs_query = []
        for item in parseDBSoutput(result):
            itemlist = []
            for key, val in item:
                itemlist.append(val)
            dbs_query.append(itemlist)

        # call executeSummary
        query ="find dataset where " + "dataset like * order by dataset asc"
        ###########query ="find dataset where dataset like *CRUZET4*"
        params['query'] = query
        params['api'] = 'executeSummary'
        params['sortKey'] = 'Path'
        #params['sortOrder'] = 'desc'
        params['sortOrder'] = 'desc'
        result = call(self.url, params, check=True)
        dbs_summary = []
        for item in parseDBSoutput(result, exclude='dataset'):
            itemlist = []
            for key, val in item[:4]: # we take first 4 elements see above
                itemlist.append(val)
            dbs_summary.append(itemlist)
        self.assertEqual(str(dbs_query), str(dbs_summary))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testDBS))
    return suite
#
# main
#
if __name__ == '__main__':
    unittest.main()

