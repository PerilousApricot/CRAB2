#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsRunLumiDQ import DbsRunLumiDQ
import sys

def getRunDQ(api, runNumber, topSubs):

  try:

    run_dq_search_criteria = DbsRunLumiDQ (
        RunNumber=int(runNumber)
    )

    dqHierarchyList =  api.listRunLumiDQ(  runLumiDQList=[run_dq_search_criteria]  )

    row={}

    # Even if there are no flags, just print UNKNOW on each of them 
    #if len(dqHierarchyList) <= 0:
        #print "No DQ information for this run found"
    #	return ""

    for aDQ in dqHierarchyList:
	#Just the top level falgs
        for aSubDQ in aDQ['DQFlagList']:
                if aSubDQ['Name'] in topSubs:
			row[aSubDQ['Name']] = aSubDQ['Value']

    rundq= " | " + str(runNumber)+ " | "
    for aSubSys in topSubs:
            if aSubSys in row.keys():
	    	rundq += row[aSubSys] + " | "
	    else: 
		rundq += " UNKNOWN |"
    return rundq

  except DbsApiException, ex:
    print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
    if ex.getErrorCode() not in (None, ""):
      print "DBS Exception Error Code: ", ex.getErrorCode()



if __name__ == "__main__":

  try:
    optManager  = DbsOptionParser()
    (opts,args) = optManager.getOpt()

    api = DbsApi(opts.__dict__)

    if len(sys.argv) < 2 :
	print "USAGE: python "+sys.argv[0]+ " <datasetPath>"
	sys.exit(0)
    else:
	datasetName=sys.argv[1]
    #datasetName="/GlobalCruzet1-A/Online-CMSSW_2_0_4/RAW"
    datasetRunList=api.listRuns(datasetName)

    q=""
    header=" | " + datasetName+" | "
    topSubs=[]
    subSys = api.listSubSystems()
    for aSub in subSys:
        if ( aSub['Parent'] == 'CMS' ):
                #print aSub['Name']
                #header +=" | " + aSub['Name']
                topSubs.append(aSub['Name'])

    for aSubSys in topSubs:
        header += aSubSys + " | "

    print header


    for runNumber in datasetRunList:
	dqRow=getRunDQ(api, runNumber['RunNumber'], topSubs)
	if dqRow not in ("", " "): print dqRow



  except DbsApiException, ex:
    print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
    if ex.getErrorCode() not in (None, ""):
      print "DBS Exception Error Code: ", ex.getErrorCode()

