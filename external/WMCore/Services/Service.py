#!/usr/bin/env python
"""
_Service_

A Service talks to some http(s) accessible service that provides information and
caches the result of these queries. The cache will be refreshed if the file is 
older than a timeout set in the instance of Service. 

It has a cache path (defaults to /tmp), cache duration, an endpoint (the url the 
service exists on) a logger and an accept type (json, xml etc) and method 
(GET/POST). 

The Service satisfies two caching cases:

1. set a defined query, cache results, poll for new ones
2. use a changing query, cache results to a file depending on the query, poll
   for new ones

Data maybe passed to the remote service either via adding the query string to 
the URL (for GET's) or by passing a dictionary to either the service constructor
(case 1.) or by passing the data as a dictionary to the refreshCache, 
forceCache, clearCache calls. By default the cache lasts 30 minutes.

Calling refreshCache/forceRefresh will return an open file object, the cache
file. Once done with it you should close the object.

The service has a default timeout to receive a response from the remote service 
of 30 seconds. Over ride this by passing in a timeout via the configuration 
dict, set to None if you want to turn off the timeout.

If you just want to retrieve the data without caching use the Requests class
directly.

TODO: support etags, respect server expires (e.g. update self['cacheduration'] 
to the expires set on the server if server expires > self['cacheduration'])   
"""

__revision__ = "$Id: Service.py,v 1.46 2010/06/02 12:30:24 spiga Exp $"
__version__ = "$Revision: 1.46 $"

SECURE_SERVICES = ('https',)

import datetime
import os
import urllib
from urlparse import urlparse
import time
import socket
from httplib import HTTPException
from WMCore.Services.Requests import Requests
from WMCore.WMException import WMException

class Service(dict):
    
    def __init__(self, dict = {}):
        #The following should read the configuration class
        for a in ['logger', 'endpoint']:
            assert a in dict.keys(), "Can't have a service without a %s" % a

        scheme = ''
        netloc = ''
        path = ''
        
        # then split the endpoint into netloc and basepath
        endpoint = urlparse(dict['endpoint'])
        
        try:
            #Only works on python 2.5 or above
            scheme = endpoint.scheme
            netloc = endpoint.netloc
            path = endpoint.path
        except AttributeError:
            scheme, netloc, path = endpoint[:3]

        #set up defaults
        self.setdefault("inputdata", {})
        self.setdefault("cachepath", '/tmp')
        self.setdefault("cacheduration", 0.5)
        self.setdefault("maxcachereuse", 24.0)
        self.supportVerbList = ('GET', 'POST', 'PUT', 'DELETE')
        # this value should be only set when whole service class uses
        # the same verb ('GET', 'POST', 'PUT', 'DELETE')
        self.setdefault("method", None)
        
        #Set a timeout for the socket
        self.setdefault("timeout", 30)

        # then update with the incoming dict
        self.update(dict)

        # Get the request class, to instatiate later
        # Is this a secure service - add other schemes as we need them
        if self.get('secure', False) or scheme in SECURE_SERVICES:
            # only bring in ssl stuff if we really need it
            from WMCore.Services.Requests import SecureRequests
            requests = SecureRequests
        else:
            requests = Requests

        try:
            if path and not path.endswith('/'):
                path += '/'
            self.setdefault("basepath", path)
            # Instantiate a Request
            self.setdefault("requests", requests(netloc, dict))
        except WMException, ex:
            msg = str(ex)
            self["logger"].exception(msg)
            raise WMException(msg)
        
        self['logger'].debug("""Service initialised (%s):
\t host: %s, basepath: %s (%s)\n\t cache: %s (duration %s hours, max reuse %s hours)""" %
                  (self, self["requests"]["host"], self["basepath"],
                   self["requests"]["accept_type"], self["cachepath"],
                   self["cacheduration"], self["maxcachereuse"]))
    
    def _makeHash(self, inputdata, hash):
        """
        make hash from complex data combination of list and dict.
        TODO: maybe it is better just jsonize and make hash for json string. 
        """
        for key, value in inputdata.items():
            hash += key.__hash__()
            if type(value) == list:
                self._makeHashFromList(value, hash)
            elif type(value) == dict:
                self._makeHash(value, hash)
        return hash     
    
    def _makeHashFromList(self, inputList, hash):
        for value in inputList:
            if type(value) == dict:
                self._makeHash(value, hash)
            elif type(value) == list:
                self._makeHashFromList(value, hash)
            else:
                #assuming non other complex value come here
                hash += value.__hash__()
        return hash
    
    def cacheFileName(self, cachefile, verb='GET', inputdata = {}):
        """
        Calculate the cache filename for a given query.
        """
        
        hash = 0
        if inputdata:
            hash = self._makeHash(inputdata, hash)
        else:
            hash = self._makeHash(self['inputdata'], hash)
        cachefile = "%s/%s_%s_%s" % (self["cachepath"], hash, verb, cachefile)

        return cachefile

    def refreshCache(self, cachefile, url='', inputdata = {}, openfile=True, 
                     encoder = True, decoder= True, verb = 'GET', contentType = None):
        """
        See if the cache has expired. If it has make a new request to the 
        service for the input data. Return the cachefile as an open file object.  
        """
        verb = self._verbCheck(verb)
        
        t = datetime.datetime.now() - datetime.timedelta(hours = self['cacheduration'])
        cachefile = self.cacheFileName(cachefile, verb, inputdata)
        
        
        if not os.path.exists(cachefile) or os.path.getmtime(cachefile) < time.mktime(t.timetuple()):
            self['logger'].debug("%s expired, refreshing cache" % cachefile)
            self.getData(cachefile, url, inputdata, encoder, decoder, verb, contentType)

        if openfile:
            return open(cachefile, 'r')
        else:
            return cachefile

    def forceRefresh(self, cachefile, url='', inputdata = {}, encoder = True, 
                     decoder = True, verb = 'GET', contentType = None):
        """
        Make a new request to the service for the input data, regardless of the 
        cache statue. Return the cachefile as an open file object.  
        """
        verb = self._verbCheck(verb)
        
        cachefile = self.cacheFileName(cachefile, verb, inputdata)

        self['logger'].debug("Forcing cache refresh of %s" % cachefile)
        self.getData(cachefile, url, inputdata, encoder, decoder, verb, contentType)
        return open(cachefile, 'r')

    def clearCache(self, cachefile, inputdata = {}, verb = 'GET'):
        """
        Delete the cache file.
        """
        verb = self._verbCheck(verb)

        cachefile = self.cacheFileName(cachefile, verb, inputdata)
        try:
            os.remove(cachefile)
        except OSError: # File doesn't exist
            return

    def getData(self, cachefile, url, inputdata = {}, encoder = True, decoder = True, 
                verb = 'GET', contentType = None):
        """
        Takes the already generated *full* path to cachefile and the url of the 
        resource. Don't need to call self.cacheFileName(cachefile, verb, inputdata)
        here.
        """
        verb = self._verbCheck(verb)
        # Set the timeout
        deftimeout = socket.getdefaulttimeout()
        socket.setdefaulttimeout(self['timeout'])

        # Nested form for version < 2.5 
        try:
            try:
                # Get the data
                if not inputdata:
                    inputdata = self["inputdata"]
                #prepend the basepath
                url = self["basepath"] + str(url)
                self['logger'].debug('getData: \n\turl: %s\n\tdata: %s' % \
                                     (url, inputdata))
                data, status, reason = self["requests"].makeRequest(uri = url,
                                                        verb = verb,
                                                        data = inputdata,
                                                        encoder = encoder,
                                                        decoder = decoder,
                                                        contentType = contentType)
                
                # Don't need to prepend the cachepath, the methods calling 
                # getData have done that for us 
                f = open(cachefile, 'w')
                f.write(str(data))
                f.close()
            except HTTPException, he:
                if not os.path.exists(cachefile):
                    msg = 'The cachefile %s does not exist and the service at %s is'
                    msg += ' unavailable - it returned %s because %s'
                    msg = msg % (cachefile, he.url, he.status, he.reason)
                    self['logger'].warning(msg)
                    raise he
                else:
                    cache_age = os.path.getmtime(cachefile)
                    t = datetime.datetime.now() - datetime.timedelta(hours = self.get('maxcachereuse', 24))
                    cache_dead = cache_age < time.mktime(t.timetuple())
                    if self.get('usestalecache', False) and not cache_dead:
                        # If usestalecache is set the previous version of the cache file 
                        # should be returned, with a suitable message in the log
                        self['logger'].warning('Returning stale cache data')
                        self['logger'].info('%s returned %s because %s' % (he.url, 
                                                                           he.status,
                                                                           he.reason))
                        self['logger'].info('cache file (%s) was created on %s' % (
                                                                            cachefile,
                                                                            cache_age))
                    else:
                        if cache_dead:
                            msg = 'The cachefile %s is dead (5 times older than cache '
                            msg += 'duration), and the service at %s is unavailable - '
                            msg += 'it returned %s because %s'
                            msg = msg % (cachefile, he.url, he.status, he.reason)
                            self['logger'].warning(msg)
                        elif self.get('usestalecache', False) == False:
                            msg = 'The cachefile %s is stale and the service at %s is'
                            msg += ' unavailable - it returned %s because %s'
                            msg = msg % (cachefile, he.url, he.status, he.reason)
                            self['logger'].warning(msg)
                        raise he
                    
        finally:
            # Reset the timeout to it's original value
            socket.setdefaulttimeout(deftimeout)
            
    def _verbCheck(self, verb='GET'):
        if verb.upper() in self.supportVerbList:
            return verb.upper()
        elif self['method'].upper() in self.supportVerbList:
            return self['method'].upper()
        else:
            raise TypeError, 'verb parameter needs to be set'
        
