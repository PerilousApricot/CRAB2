
import unittest
import httplib
import urllib
import urllib2
import types
import time
import os
import sys
from xml.dom.minidom import parse, parseString
import string
#from listdbsinstances import Generator

ql1 = "find dataset where site != srm.cern.ch "
ql2 = "find dataset where dataset like *"
ql3 = "find run where  run.number > 1"
ql4 = "find release where release>CMSSW_1_6_7" 
ql5 = "find file where release > CMSSW_1_6_7 and site like *.fnal.gov"
qllist = [ql1,ql2,ql3,ql4,ql5]

class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    def __init__(self, key, cert):
        urllib2.HTTPSHandler.__init__(self)
        self.key = key
        self.cert = cert
    def https_open(self, req):
        return  self.do_open(self.getConnection, req)
    def getConnection(self, host, timeout=300):
        return httplib.HTTPSConnection(host, key_file=self.key,cert_file=self.cert)
def getKeyCert():
    # First presendence to HOST Certificate, RARE
    if os.environ.has_key('X509_HOST_CERT'):
        proxy = os.environ['X509_HOST_CERT']
        key = os.environ['X509_HOST_KEY']
    # Second preference to User Proxy, very common
    elif os.environ.has_key('X509_USER_PROXY'):
        proxy = os.environ['X509_USER_PROXY']
        key = proxy
    # Third preference to User Cert/Proxy combinition
    elif os.environ.has_key('X509_USER_CERT'):
        proxy = os.environ['X509_USER_CERT']
        key = os.environ['X509_USER_KEY']
    # Worst case, look for proxy at default location /tmp/x509up_u$uid
    else :
        uid = os.getuid()
        proxy = '/tmp/x509up_u'+str(uid)
        key = proxy
    #Set but not found
    if not os.path.exists(proxy) or not os.path.exists(key):
        raise Exception("Required Proxy for Secure Call not found for user '%s', please do init your proxy" %os.getlogin())
    # All looks OK, still doesn't gurantee proxy's validity etc.
    return key, proxy

class urlGenerator :
    def __init__(self,type,machines,dnsname):
        self.instype = []
        self.machines = []

        self.prefix_r = "http://"
        self.prefix_w = "https://"
        self.middle_r = ".cern.ch/"
        self.middle_w = ".cern.ch:8443/"
        self.url_suffix_r = "/servlet/DBSServlet"
        self.url_suffix_w = "_writer/servlet/DBSServlet"
        self.url_suffix_a = "_admin/servlet/DBSServlet"
        self.reader_stuff = [self.prefix_r,self.middle_r,self.url_suffix_r]
        self.writer_stuff = [self.prefix_w,self.middle_w,self.url_suffix_w]
        self.admin_stuff = [self.prefix_w,self.middle_w,self.url_suffix_a]
        self.prod = ['cmsdbsprod','cmsdbs1','cmsdbs2']
        self.t0 = ['cmst0dbs1','cmst0dbs1','cmst0dbs2']
        self.instancelist = [
            "cms_dbs_prod_global",
            "cms_dbs_prod_local_01",
            "cms_dbs_prod_local_02",
            "cms_dbs_prod_local_03",
            "cms_dbs_prod_local_04",
            #"cms_dbs_prod_local_05",
            "cms_dbs_prod_local_06",
            "cms_dbs_prod_local_07",
            "cms_dbs_prod_local_08",
            "cms_dbs_prod_local_09",
            "cms_dbs_prod_local_10",
            "cms_dbs_ph_analysis_01",
            "cms_dbs_ph_analysis_02",
            "cms_dbs_caf_analysis_01",
            "cms_dbs_prod_tier0",
            "cms_dbs_int_tier0"
        ]#,"cms_dbs_int_global"]
        self.instype= type
        if dnsname:
            self.machines = machines
        else:
            for machine in machines:
                if machine == 'cmsdbsprod':
                    self.machines.append('cmsdbs1')
                    self.machines.append('cmsdbs2')
                elif machine == 'cmst0dbs':
                    self.machines.append('cmst0dbs1')
                    self.machines.append('cmst0dbs2')
                elif machine in self.t0:
                    self.machines.append(machine)
                else:self.machines.append(machine)
    def stuff_url(self,machine,type,instance):
        if type == 'reader':
            return "%s%s%s%s%s"%(self.reader_stuff[0],machine,self.reader_stuff[1],instance,self.reader_stuff[2])
        elif type == 'writer':
            return "%s%s%s%s%s"%(self.writer_stuff[0],machine,self.writer_stuff[1],instance,self.writer_stuff[2])
        elif type == 'admin':
            return "%s%s%s%s%s"%(self.admin_stuff[0],machine,self.admin_stuff[1],instance,self.admin_stuff[2])
    def getserverlist(self):
        serverlist=[]
        for machine in self.machines:
            for instance_name in self.instancelist:
                if instance_name != "cms_dbs_prod_tier0" and instance_name != "cms_dbs_int_tier0" and machine in self.prod:
                    for type in self.instype:
                        serverlist.append(self.stuff_url(machine,type,instance_name))
                elif (instance_name == "cms_dbs_prod_tier0" or instance_name == "cms_dbs_int_tier0" ) and machine in self.t0:
                    for type in self.instype:
                        serverlist.append(self.stuff_url(machine,type,instance_name))
        return serverlist

def parseoutput(data, exclude=None):
    """
    DBS XML parser for DBS server DBS_2_0_6 and later
    """
    dom  = parseString(data)
    datalist = []
    nodes = dom.getElementsByTagName('row')
    for node in nodes:
        olist = []
        for child in node.childNodes:
            subnode = child.firstChild
            if not subnode:
                continue
            data = subnode.data
            tag = subnode.parentNode.tagName
            if exclude:
                if exclude != tag:
                    if tag.lower().find('creationdate') != -1:
                        data = timeformat(data)
                    olist.append((tag,data))
            else: 
                olist.append((tag,data))
        if olist:
            if len(olist) == 1:
                datalist.append(olist[-1])
            else:
                datalist.append(olist)
    if nodes == []:
        success = dom.getElementsByTagName('SUCCESS')
        if success:
            datalist.append(('Success','with no match'))
    return datalist

def call(url, params, check=None):
    data   = urllib2.urlopen(url, urllib.urlencode(params, doseq=True))
    result = data.read()
    if  check and result.find('exception') != -1:
        raise Exception(result)
    return result
class Test_QLPostDeploy(unittest.TestCase):
    pass
def test_generator(url,version):
    def test_QL(self):
        print "=========== testing %s ==========="%url
        params =  {'apiversion':version,'api':'executeQuery','begin':'0','end':'1'}
        sign = False
        for ql in qllist:
            params['query'] = ql
            result = call(url, params)
            datas = parseoutput(result)
            
            if datas != []:
                #print "=".join("%s"% k for k in datas[0])
                sys.stdout.write(" .")
		sys.stdout.flush()
		#print " ."
            else:
		sys.stdout.write(" E")
		sys.stdout.flush()
                sign = True
	sys.stdout.write("\n")
        if sign:  raise Exception("Failed in query ==> %s"%ql)
	
    return test_QL
                                                       

def suite(type,machines,dnsname=False):
    suite = unittest.TestSuite()
    gen = urlGenerator(type,machines,dnsname)
    lists = gen.getserverlist()
    for url in lists:
        
        test_name = 'test_%url' % lists.index(url)
        test = test_generator(url,version)
        setattr(Test_QLPostDeploy,test_name,test)
        testcase = Test_QLPostDeploy(test_name)
        testcase._TestCase__testMethodDoc=url
        suite.addTest(testcase)
    return suite
        
def usage():
    progName = os.path.basename(sys.argv[0])
    print "Usage:"
    print "python  %s --instype=<reader|writer|admin|all> --machine=<cmsdbsprod|cmst0dbs|cmsdbs<1|2>|cmst0dbs<1|2>|all> -dnsname" %progName
    print " "
if __name__ == '__main__':
    instype = None
    machine = None
    dnsname = False
    version = "DBS_2_0_6"
    for a in sys.argv[1:]:
        arg = string.split(a, "=")
        if arg[0] == "--instype":
            instype =  arg[1]
        elif arg[0] == "--machine":
            machine =  arg[1]
        elif arg[0] == "-dnsname":
            dnsname = True
        elif arg[0] =="-h" or arg[0] == "--help":
            usage()
            sys.exit(1)
        else:
            print "Ignoring unrecognized argument: %s" % a
    if instype == 'all' or instype == None:
        type = ['reader','writer','admin']
    else: type = [instype]
    if machine == 'all' or machine == None:
        machines = ['cmsdbsprod','cmst0dbs']
    else: machines = [machine]
    if type.count('writer')+type.count('admin') != 0:
        key,cert = getKeyCert()
        opener = urllib2.build_opener(HTTPSClientAuthHandler(key,cert))
        urllib2.install_opener(opener)        
    Suite = suite(type,machines,dnsname)
    runner = unittest.TextTestRunner()
    runner.run(Suite)
    




