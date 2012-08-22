#!/bin/bash
user_id=`id -u anzar`
x509proxy="/tmp/x509up_u${user_id}"
echo $x509proxy

dbsrw=https://cmsdbsprod.cern.ch:8443/cms_dbs_prod_global_writer/servlet/DBSServlet
dbsro=http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet

echo "Testing access to DBS API via DBS CLI, running 'dbs lsd'"
python ../dbsCommandLine.py -c lsd --url=${dbsro}
echo "Testing access to DBS QL via DBS CLI, running 'dbs search --query=\"find dataset\""
python ../dbsCommandLine.py -c search --query="find dataset" --url=${dbsro}

if [ -f ${x509proxy} ] 
then 
	echo "You must have a valid proxy for next test, Testing access to DBS R/W, running 'dbs search --query=\"find dataset\""
	python ../dbsCommandLine.py -c search --query="find dataset" --url=${dbsrw}
fi

