#!/usr/bin/env python
"""
_SizeBased_

Suze based splitting algorithm that will produce a set of jobs for each file,
or a a set of files for each job.

"""

__revision__ = "$Id: SizeBased.py,v 1.7 2010/03/31 21:35:30 sfoulkes Exp $"
__version__  = "$Revision: 1.7 $"

import logging

from WMCore.JobSplitting.JobFactory import JobFactory
from WMCore.DataStructs.Fileset import Fileset
from WMCore.Services.UUID import makeUUID

class SizeBased(JobFactory):
    def algorithm(self, *args, **kwargs):
        """
        _algorithm_
        
        Implement size splitting algorithm.

        
        kwargs can take:
        size_per_job 
        """
        sizePerJob = kwargs.get("size_per_job", 1000)
        locationDict = self.sortByLocation()

        for location in locationDict.keys():
            self.newGroup()
            fileList     = locationDict[location]
            self.newJob(name = makeUUID())
            currentSize = 0
            
            for f in fileList:
                sizeOfFile = f['size']
                if sizeOfFile > sizePerJob:
                    if currentSize > 0:
                        self.newJob(name = makeUUID())
                    self.currentJob.addFile(f)
                    currentSize += sizeOfFile

                else:
                    if currentSize + sizeOfFile > sizePerJob:
                        #Create new jobs, because we are out of room
                        self.newJob(name = makeUUID())
                        currentSize = 0

                    if currentSize + sizeOfFile <= sizePerJob:
                    
                        if not self.currentJob:
                            self.newJob(name = makeUUID())
                        #Add if it will be smaller
                        self.currentJob.addFile(f)
                        currentSize += sizeOfFile

