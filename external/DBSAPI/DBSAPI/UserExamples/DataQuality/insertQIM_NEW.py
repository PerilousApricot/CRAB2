from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()

api = DbsApi(opts.__dict__)

#Add a new SubSystem
#
#
api.insertSubSystem(name="SiStrip_Global", parent="CMS")
#
api.insertSubSystem(name="SiStrip_Performance", parent="SiStrip_Global")
#
api.insertSubSystem(name="TIB_Global", parent="SiStrip_Global")
api.insertSubSystem(name="TIB_OnlineDQM", parent="TIB_Global")
api.insertSubSystem(name="TIB_Performance", parent="TIB_Global")

api.insertSubSystem(name="TOB_Global", parent="SiStrip_Global")
api.insertSubSystem(name="TOB_OnlineDQM", parent="TOB_Global")
api.insertSubSystem(name="TOB_Performance", parent="TOB_Global")

api.insertSubSystem(name="TIDB_Global", parent="SiStrip_Global")
api.insertSubSystem(name="TIDB_OnlineDQM", parent="TIDB_Global")
api.insertSubSystem(name="TIDB_Performance", parent="TIDB_Global")

api.insertSubSystem(name="TIDF_Global", parent="SiStrip_Global")
api.insertSubSystem(name="TIDF_OnlineDQM", parent="TIDF_Global")
api.insertSubSystem(name="TIDF_Performance", parent="TIDF_Global")

api.insertSubSystem(name="TECB_Global", parent="SiStrip_Global")
api.insertSubSystem(name="TECB_OnlineDQM", parent="TECB_Global")
api.insertSubSystem(name="TECB_Performance", parent="TECB_Global")

api.insertSubSystem(name="TECF_Global", parent="SiStrip_Global")
api.insertSubSystem(name="TECF_OnlineDQM", parent="TECF_Global")
api.insertSubSystem(name="TECF_Performance", parent="TECF_Global")

# Lets just list all the subsystems that we have added
subSys = api.listSubSystems()
for aSub in subSys:
     print "Name: %s, Parent: %s" %(aSub['Name'], aSub['Parent'])


