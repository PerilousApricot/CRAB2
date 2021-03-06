
import os, re, string, socket, xml.sax, xml.sax.handler
import base64
from xml.sax.saxutils import escape
from cStringIO import StringIO

from dbsException import DbsException
from dbsApiException import *

##import logging
import inspect

##from dbsLogger import **

from dbsUtil import *

def dbsApiImplInsertSubSystem(self, name, parent="CMS"):
    """
    This API is used to insert a new subsystem, for now it is just a preliminary api
    to insert single Sub-System but later will be modified to 
    add several Sub and SubSubSystems in one go.

    params:
        version: the NAME you would like to give to your version
    """

    funcInfo = inspect.getframeinfo(inspect.currentframe())
    ###logging.log(DBSDEBUG, "Api call invoked %s" % str(funcInfo[2]))
    
    xmlinput  = "<?xml version='1.0' standalone='yes'?>"
    xmlinput += "<dbs>"
    xmlinput += "<sub_system name='"+str(name)+"' parent='"+parent+"' />"
    xmlinput += "</dbs>"
    
    ###logging.log(DBSDEBUG, xmlinput)

    data = self._server._call ({ 'api' : 'insertSubSystem',
                                        'xmlinput': xmlinput,
                                         }, 'GET')

    ###logging.log(DBSDEBUG, data)
  #-------------------------------------------------------------------

