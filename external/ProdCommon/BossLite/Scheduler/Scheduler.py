#!/usr/bin/env python
"""
_Scheduler_

"""
from ProdCommon.BossLite.DbObjects.Job import Job
from ProdCommon.BossLite.DbObjects.Task import Task
from ProdCommon.BossLite.DbObjects.RunningJob import RunningJob
from ProdCommon.BossLite.Common.Exceptions import SchedulerError
import time

__version__ = "$Id: Scheduler.py,v 1.48 2010/08/09 16:18:08 spiga Exp $"
__revision__ = "$Revision: 1.48 $"


##########################################################################
class Scheduler(object):
    """
    Upper layer for scheduler interaction

    """

    def __init__(self, scheduler, parameters = None):
        """
        initialization
        """

        # define scheduler parameters
        self.scheduler = scheduler
        defaults = {'user_proxy' : '', 'service' : '', 'config' : '' }
        if parameters is not None :
            defaults.update( parameters )
        self.parameters = defaults

        # load scheduler plugin
        try:
            module =  __import__(
                'ProdCommon.BossLite.Scheduler.' + self.scheduler, \
                globals(), locals(), [self.scheduler]
                )
            schedClass = vars(module)[self.scheduler]
            self.schedObj = schedClass( **self.parameters )
        except KeyError, e:
            msg = 'Scheduler interface' + self.scheduler + 'not found'
            raise SchedulerError(msg, str(e))
        except Exception, e:
            raise SchedulerError(e.__class__.__name__, str(e))


    ##########################################################################
    def submit ( self, obj, requirements='' ) :
        """
        set up submission parameters and submit
        """

        # check the proxy
        self.schedObj.checkUserProxy()

        # delegate submission to scheduler plugin
        jobAttributes, bulkId, service = self.schedObj.submit(\
            obj, requirements, \
            self.parameters['config'], self.parameters['service']\
            )
        timestamp = int( time.time() )

        # the object passed is a job
        if type( obj ) == Job and self.schedObj.valid(obj.runningJob):
            obj.runningJob['schedulerId'] = jobAttributes[ obj['name'] ]
            obj.runningJob['status'] = 'S'
            obj.runningJob['submissionTime'] = timestamp
            obj.runningJob['statusScheduler'] = 'Submitted'
            obj.runningJob['state'] = 'SubSuccess'
            obj.runningJob['schedulerParentId'] = obj.runningJob['schedulerId']
            obj.runningJob['scheduler'] = self.scheduler
            obj.runningJob['service'] = service
            obj.runningJob['processStatus'] = 'not_handled'

        # update multiple jobs of a task
        elif type( obj ) == Task :

            # error messages collector
            errors = ''

            for job in obj.jobs :

                # skip jobs not requested for action
                if job.runningJob is None or job.runningJob.active == False :
                    continue

                # evaluate errors:
                elif job.runningJob.isError() :
                    errors += str( job.runningJob.errors )
                    continue

                # set scheduler id
                job.runningJob['schedulerId'] = jobAttributes[ job['name'] ]
                if job.runningJob['schedulerId'] is None :
                    job.runningJob.errors.append(
                        "Unknown Error: missing schedulerId")
                    continue

                # update success jobs
                job.runningJob['status'] = 'S'
                job.runningJob['submissionTime'] = timestamp
                job.runningJob['scheduler'] = self.scheduler
                job.runningJob['service'] = service
                job.runningJob['statusScheduler'] = 'Submitted'
                job.runningJob['state'] = 'SubSuccess'
                job.runningJob['processStatus'] = 'not_handled'
                if bulkId is None :
                    job.runningJob['schedulerParentId'] = \
                                                  job.runningJob['schedulerId']
                else:
                    job.runningJob['schedulerParentId'] = bulkId

            # handle errors
            if errors != '' :
                raise SchedulerError('interaction failed for some jobs', \
                                     errors )

        # unknown object type
        else:
            raise SchedulerError('wrong argument type', str( type(obj) ))


    ##########################################################################

    def jobDescription ( self, obj, requirements='' ) :
        """
        retrieve scheduler specific job description
        """

        return self.schedObj.jobDescription(
            obj, requirements = requirements,  \
            config = self.parameters['config'], \
            service = self.parameters['service'] )


    ##########################################################################
    def query(self, obj, objType='node') :
        """
        query status and eventually other scheduler related information
        """

        # check the proxy
        self.schedObj.checkUserProxy()

        # error messages collector
        errors = ''

        # delegate query to scheduler plugin
        self.schedObj.query( obj, self.parameters['service'], objType )

        # handle errors
        for job in obj.jobs :

            # evaluate errors:
            if job.runningJob.isError() :
                errors += str( job.runningJob.errors )
                continue

        # handle errors
        if errors != '' :
            raise SchedulerError('interaction failed for some jobs', errors )

    ##########################################################################
    def getOutput( self, obj, outdir ):
        """
        retrieve output or just put it in the destination directory
        """

        # check the proxy
        self.schedObj.checkUserProxy()

        # perform action
        self.schedObj.getOutput( obj, outdir )
        timestamp = int( time.time() )

        # the object passed is a runningJob
        if type(obj) == RunningJob and self.schedObj.valid(obj):
            obj['status'] = 'E'
            obj['closed'] = 'Y'
            obj['getOutputTime'] = timestamp
            obj['statusScheduler'] = "Retrieved"

        # the object passed is a job
        elif type(obj) == Job and self.schedObj.valid(obj.runningJob):
            obj.runningJob['status'] = 'E'
            obj.runningJob['closed'] = 'Y'
            obj.runningJob['getOutputTime'] = timestamp
            obj.runningJob['statusScheduler'] = "Retrieved"

        # the object passed is a Task
        elif type(obj) == Task :

            # error messages collector
            errors = ''

            # update objects
            for job in obj.jobs:

                # skip jobs not requested for action
                if not self.schedObj.valid(job.runningJob) :
                    continue

                # evaluate errors: if not, update
                if job.runningJob.isError() :
                    errors += str( job.runningJob.errors )
                else :
                    job.runningJob['status'] = 'E'
                    job.runningJob['closed'] = 'Y'
                    job.runningJob['getOutputTime'] = timestamp
                    job.runningJob['statusScheduler'] = "Retrieved"

            # handle errors
            if errors != '' :
                raise SchedulerError('interaction failed for some jobs', \
                                     errors )

        # unknown object type
        else:
            raise SchedulerError('wrong argument type', str( type(obj) ))


    ##########################################################################
    def kill( self, obj ):
        """
        kill the job instance
        """

        # check the proxy
        self.schedObj.checkUserProxy()

        # avoid kill of finished jobs
        restore = False
        if 'SD' not in self.schedObj.invalidList:
            self.schedObj.invalidList.append( 'SD')
            restore = True

        # perform action
        try:
            self.schedObj.kill( obj )
        except:
            if restore:
                self.schedObj.invalidList.remove( 'SD')
            raise

        # restoring invalidList
        if restore:
            self.schedObj.invalidList.remove( 'SD')
        # timestamp = int( time.time() )

        # the object passed is a runningJob
        if type(obj) == RunningJob and self.schedObj.valid(obj):
            obj['status'] = 'K'
            obj['statusScheduler'] = "Cancelled by user"

        # the object passed is a job
        elif type(obj) == Job and self.schedObj.valid(obj.runningJob):
            obj.runningJob['status'] = 'K'
            obj.runningJob['statusScheduler'] = "Cancelled by user"

        # the object passed is a Task
        elif type(obj) == Task :

            # error messages collector
            errors = ''

            # update objects
            for job in obj.jobs:

                # skip jobs not requested for action
                if not self.schedObj.valid(job.runningJob) :
                    continue

                # evaluate errors: if not, update
                if job.runningJob.isError() :
                    errors += str( job.runningJob.errors )
                else :
                    job.runningJob['status'] = 'K'
                    job.runningJob['statusScheduler'] = "Cancelled by user"

            # handle errors
            if errors != '' :
                raise SchedulerError('interaction failed for some jobs', \
                                     errors )

        # unknown object type
        else:
            raise SchedulerError('wrong argument type', str( type(obj) ))


    ##########################################################################
    def postMortem ( self, obj, outfile ) :
        """
        execute any post mortem command such as logging-info
        """

        # check the proxy
        self.schedObj.checkUserProxy()

        # the object passed is a runningJob
        if type(obj) == RunningJob :
            self.schedObj.postMortem(
                obj['schedulerId'], outfile, self.parameters['service']
                )

        # the object passed is a job
        elif type(obj) == Job :
            self.schedObj.postMortem( obj.runningJob['schedulerId'], \
                                      outfile, self.parameters['service']
                )

        # the object passed is a Task
        elif type(obj) == Task :
            for job in obj.jobs:
                if job.runningJob is None:
                    continue
                self.schedObj.postMortem( job.runningJob['schedulerId'], \
                                          outfile, self.parameters['service'] )

        # unknown object type
        else:
            raise SchedulerError('wrong argument type', str( type(obj) ))


    ##########################################################################
    def matchResources ( self, obj, requirements='' ) :
        """
        perform a resources discovery
        """

        # check the proxy
        self.schedObj.checkUserProxy()

        return self.schedObj.matchResources( obj, requirements, \
                                             self.parameters['config'], \
                                             self.parameters['service'] )


    ##########################################################################
    def purgeService( self, obj ) :
        """
        purge the service used by the scheduler from job files
        not available for every scheduler
        """

        # check the proxy
        self.schedObj.checkUserProxy()

        # perform action
        self.schedObj.purgeService( obj  )
        timestamp = int( time.time() )

        # the object passed is a runningJob
        if type(obj) == RunningJob and self.schedObj.valid(obj):
            obj['status'] = 'E'
            obj['closed'] = 'Y'
            obj['getOutputTime'] = timestamp
            obj['statusScheduler'] = "Cleared"

        # the object passed is a job
        elif type(obj) == Job and self.schedObj.valid(obj.runningJob):
            obj.runningJob['status'] = 'E'
            obj.runningJob['closed'] = 'Y'
            obj.runningJob['getOutputTime'] = timestamp
            obj.runningJob['statusScheduler'] = "Cleared"

        # the object passed is a Task
        elif type(obj) == Task :

            # error messages collector
            errors = ''

            # update objects
            for job in obj.jobs:

                # skip jobs not requested for action
                if not self.schedObj.valid(job.runningJob) :
                    continue

                # evaluate errors: if not, update
                if job.runningJob.isError() :
                    errors += str( job.runningJob.errors )
                else :
                    job.runningJob['status'] = 'E'
                    job.runningJob['closed'] = 'Y'
                    job.runningJob['getOutputTime'] = timestamp
                    job.runningJob['statusScheduler'] = "Cleared"

            # handle errors
            if errors != '' :
                raise SchedulerError('interaction failed for some jobs', \
                                     errors )

        # unknown object type
        else:
            raise SchedulerError('wrong argument type', str( type(obj) ))



