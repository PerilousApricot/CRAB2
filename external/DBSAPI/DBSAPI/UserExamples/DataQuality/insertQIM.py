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
api.insertSubSystem(name="Tracker_Global", parent="CMS")
#
api.insertSubSystem(name="TIB_Local", parent="Tracker_Global")
api.insertSubSystem(name="TIB_Power", parent="TIB_Local")  
api.insertSubSystem(name="TIB_Cooling", parent="TIB_Local") 
api.insertSubSystem(name="TIB_DCS", parent="TIB_Local")  
api.insertSubSystem(name="TIB_DAQ", parent="TIB_Local")  
api.insertSubSystem(name="TIB_Online_DQM", parent="TIB_Local")  
api.insertSubSystem(name="TIB_Offline_DQM", parent="TIB_Local")  
api.insertSubSystem(name="TIB_Percentage", parent="TIB_Local") 

api.insertSubSystem(name="TOB_Local", parent="Tracker_Global") 
api.insertSubSystem(name="TOB_Power", parent="TOB_Local")  
api.insertSubSystem(name="TOB_Cooling", parent="TOB_Local")  
api.insertSubSystem(name="TOB_DCS", parent="TOB_Local")  
api.insertSubSystem(name="TOB_DAQ", parent="TOB_Local")  
api.insertSubSystem(name="TOB_Online_DQM", parent="TOB_Local")  
api.insertSubSystem(name="TOB_Offline_DQM", parent="TOB_Local")  
api.insertSubSystem(name="TOB_Percentage", parent="TOB_Local") 

api.insertSubSystem(name="TEC_Local", parent="Tracker_Global") 
api.insertSubSystem(name="TEC_Power", parent="TEC_Local")  
api.insertSubSystem(name="TEC_Cooling", parent="TEC_Local")  
api.insertSubSystem(name="TEC_DCS", parent="TEC_Local")  
api.insertSubSystem(name="TEC_DAQ", parent="TEC_Local")  
api.insertSubSystem(name="TEC_Online_DQM", parent="TEC_Local")  
api.insertSubSystem(name="TEC_Offline_DQM", parent="TEC_Local")  
api.insertSubSystem(name="TEC_Percentage", parent="TEC_Local") 

api.insertSubSystem(name="TID_Local", parent="Tracker_Global") 
api.insertSubSystem(name="TID_Power", parent="TID_Local")  
api.insertSubSystem(name="TID_Cooling", parent="TID_Local")  
api.insertSubSystem(name="TID_DCS", parent="TID_Local")  
api.insertSubSystem(name="TID_DAQ", parent="TID_Local")  
api.insertSubSystem(name="TID_Online_DQM", parent="TID_Local")  
api.insertSubSystem(name="TID_Offline_DQM", parent="TID_Local")  
api.insertSubSystem(name="TID_Percentage", parent="TID_Local") 

api.insertSubSystem(name="PXB_Local", parent="Tracker_Global") 
api.insertSubSystem(name="PXB_Power", parent="PXB_Local")  
api.insertSubSystem(name="PXB_Cooling", parent="PXB_Local")  
api.insertSubSystem(name="PXB_DCS", parent="PXB_Local")  
api.insertSubSystem(name="PXB_DAQ", parent="PXB_Local")  
api.insertSubSystem(name="PXB_Online_DQM", parent="PXB_Local")  
api.insertSubSystem(name="PXB_Offline_DQM", parent="PXB_Local")  
api.insertSubSystem(name="PXB_Percentage", parent="PXB_Local") 

api.insertSubSystem(name="PXF_Local", parent="Tracker_Global") 
api.insertSubSystem(name="PXF_Power", parent="PXF_Local")  
api.insertSubSystem(name="PXF_Cooling", parent="PXF_Local")  
api.insertSubSystem(name="PXF_DCS", parent="PXF_Local")  
api.insertSubSystem(name="PXF_DAQ", parent="PXF_Local")  
api.insertSubSystem(name="PXF_Online_DQM", parent="PXF_Local")  
api.insertSubSystem(name="PXF_Offline_DQM", parent="PXF_Local")  
api.insertSubSystem(name="PXF_Percentage", parent="PXF_Local") 
#
#
api.insertSubSystem(name="MUON_Global", parent="CMS")
#
api.insertSubSystem(name="CSC_Local", parent="MUON_Global")
api.insertSubSystem(name="CSC_Power", parent="CSC_Local")  
api.insertSubSystem(name="CSC_Cooling", parent="CSC_Local")  
api.insertSubSystem(name="CSC_DCS", parent="CSC_Local")  
api.insertSubSystem(name="CSC_DAQ", parent="CSC_Local")  
api.insertSubSystem(name="CSC_Online_DQM", parent="CSC_Local")  
api.insertSubSystem(name="CSC_Offline_DQM", parent="CSC_Local")  
api.insertSubSystem(name="CSC_Percentage", parent="CSC_Local") 

api.insertSubSystem(name="RPC_Local", parent="MUON_Global")
api.insertSubSystem(name="RPC_Power", parent="RPC_Local")  
api.insertSubSystem(name="RPC_Cooling", parent="RPC_Local")  
api.insertSubSystem(name="RPC_DCS", parent="RPC_Local")  
api.insertSubSystem(name="RPC_DAQ", parent="RPC_Local")  
api.insertSubSystem(name="RPC_Online_DQM", parent="RPC_Local")  
api.insertSubSystem(name="RPC_Offline_DQM", parent="RPC_Local")  
api.insertSubSystem(name="RPC_Percentage", parent="RPC_Local") 

api.insertSubSystem(name="DT_Local", parent="MUON_Global") 
api.insertSubSystem(name="DT_Power", parent="DT_Local")   
api.insertSubSystem(name="DT_Cooling", parent="DT_Local")  
api.insertSubSystem(name="DT_DCS", parent="DT_Local")  
api.insertSubSystem(name="DT_DAQ", parent="DT_Local")  
api.insertSubSystem(name="DT_Online_DQM", parent="DT_Local")  
api.insertSubSystem(name="DT_Offline_DQM", parent="DT_Local")  
api.insertSubSystem(name="DT_Percentage", parent="DT_Local") 
#
#
api.insertSubSystem(name="ECAL_Global", parent="CMS") 
#
api.insertSubSystem(name="EB_Local", parent="ECAL_Global")
api.insertSubSystem(name="EB_Power", parent="EB_Local")  
api.insertSubSystem(name="EB_Cooling", parent="EB_Local")  
api.insertSubSystem(name="EB_DCS", parent="EB_Local")  
api.insertSubSystem(name="EB_DAQ", parent="EB_Local")  
api.insertSubSystem(name="EB_Online_DQM", parent="EB_Local")  
api.insertSubSystem(name="EB_Offline_DQM", parent="EB_Local")  
api.insertSubSystem(name="EB_Percentage", parent="EB_Local") 
#
api.insertSubSystem(name="EE_Local", parent="ECAL_Global") 
api.insertSubSystem(name="EE_Power", parent="EE_Local")  
api.insertSubSystem(name="EE_Cooling", parent="EE_Local")  
api.insertSubSystem(name="EE_DCS", parent="EE_Local")  
api.insertSubSystem(name="EE_DAQ", parent="EE_Local")  
api.insertSubSystem(name="EE_Online_DQM", parent="EE_Local")  
api.insertSubSystem(name="EE_Offline_DQM", parent="EE_Local")  
api.insertSubSystem(name="EE_Percentage", parent="EE_Local") 

api.insertSubSystem(name="ES_Local", parent="ECAL_Global") 
api.insertSubSystem(name="ES_Power", parent="ES_Local")  
api.insertSubSystem(name="ES_Cooling", parent="ES_Local")  
api.insertSubSystem(name="ES_DCS", parent="ES_Local")  
api.insertSubSystem(name="ES_DAQ", parent="ES_Local")  
api.insertSubSystem(name="ES_Online_DQM", parent="ES_Local")  
api.insertSubSystem(name="ES_Offline_DQM", parent="ES_Local")  
api.insertSubSystem(name="ES_Percentage", parent="ES_Local") 

#
#
api.insertSubSystem(name="HCAL_Global", parent="CMS") 
api.insertSubSystem(name="HB_Local", parent="HCAL_Global") 
api.insertSubSystem(name="HB_Power", parent="HB_Local")  
api.insertSubSystem(name="HB_Cooling", parent="HB_Local")  
api.insertSubSystem(name="HB_DCS", parent="HB_Local")  
api.insertSubSystem(name="HB_DAQ", parent="HB_Local")  
api.insertSubSystem(name="HB_Online_DQM", parent="HB_Local")  
api.insertSubSystem(name="HB_Offline_DQM", parent="HB_Local")  
api.insertSubSystem(name="HB_Percentage", parent="HB_Local") 

api.insertSubSystem(name="HE_Local", parent="HCAL_Global") 
api.insertSubSystem(name="HE_Power", parent="HE_Local")  
api.insertSubSystem(name="HE_Cooling", parent="HE_Local")  
api.insertSubSystem(name="HE_DCS", parent="HE_Local")  
api.insertSubSystem(name="HE_DAQ", parent="HE_Local")  
api.insertSubSystem(name="HE_Online_DQM", parent="HE_Local")  
api.insertSubSystem(name="HE_Offline_DQM", parent="HE_Local")  
api.insertSubSystem(name="HE_Percentage", parent="HE_Local") 

api.insertSubSystem(name="HF_Local", parent="HCAL_Global") 
api.insertSubSystem(name="HF_Power", parent="HF_Local")  
api.insertSubSystem(name="HF_Cooling", parent="HF_Local")  
api.insertSubSystem(name="HF_DCS", parent="HF_Local")  
api.insertSubSystem(name="HF_DAQ", parent="HF_Local")  
api.insertSubSystem(name="HF_Online_DQM", parent="HF_Local")  
api.insertSubSystem(name="HF_Offline_DQM", parent="HF_Local")  
api.insertSubSystem(name="HF_Percentage", parent="HF_Local") 


# Lets just list all the subsystems that we have added
subSys = api.listSubSystems()
for aSub in subSys:
     print "Name: %s, Parent: %s" %(aSub['Name'], aSub['Parent'])


