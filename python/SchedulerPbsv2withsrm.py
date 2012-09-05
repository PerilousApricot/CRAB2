from Scheduler import Scheduler
from SchedulerPbsv2 import SchedulerPbsv2

# wrapper around PBS to enable using PBS with SRM
class SchedulerPbsv2withsrm(SchedulerPbsv2):
    def __init__(self):
        Scheduler.__init__(self,"PBSV2WITHSRM")
