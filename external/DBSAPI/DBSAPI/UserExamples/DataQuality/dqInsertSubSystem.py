#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi

if __name__ == "__main__":

  try:
    optManager  = DbsOptionParser()
    (opts,args) = optManager.getOpt()

    api = DbsApi(opts.__dict__)

    #Add a new SubSystem
    

    #api.insertSubSystem(name="ECAL", parent="CMS")
    #api.insertSubSystem(name="ECAL+", parent="ECAL")
    #api.insertSubSystem(name="ECAL-", parent="ECAL")

    #api.insertSubSystem(name="HCAL", parent="CMS")
    #api.insertSubSystem(name="HCAL+", parent="HCAL")
    #api.insertSubSystem(name="HCAL-", parent="HCAL")

    #api.insertSubSystem(name="HB", parent="HCAL")
    #api.insertSubSystem(name="HF", parent="HCAL")

    api.insertSubSystem(name="XYZ_Percentage", parent="CMS")

    #subSys = api.listSubSystems()
    #for aSub in subSys:
    #	print "Name: %s, Parent: %s" %(aSub['Name'], aSub['Parent'])


  except DbsApiException, ex:
    print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
    if ex.getErrorCode() not in (None, ""):
      print "DBS Exception Error Code: ", ex.getErrorCode()

