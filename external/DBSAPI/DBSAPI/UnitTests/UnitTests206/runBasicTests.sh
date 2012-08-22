#!/bin/sh
echo "This test can take some time. Please wait..."



#Modify test parameteres here

#Testing instance... Need to be admin to run the deletion tests
abbr=dev2_intlyy_admin

tests="runAll-validate-qlTest-migrate"
verbosities="1-2-1-2"


#These instances are used for migration, 0->1, 1->2, 2->3
abbr_migrate="prodg-dev2_intlyy_writer-dev2_intg_writer-dev2_206"

#Log files
#logdir="."
logdir=$DBS_LOGS_DIR
clientversion=204patch1
serverversion=206pre6



#No need to modify below
DATE=`date '+%y%m%d_%I%M'`
validatelog=$logdir/validate__${abbr}${serverversion}__${clientversion}__$DATE.log
qltestlog=$logdir/qltest__${abbr}${serverversion}__${clientversion}__$DATE.log
runalltestlog=$logdir/runalltest__${abbr}${serverversion}__${clientversion}__$DATE.log
migratelog=$logdir/migrate__${clientversion}__$DATE.log

logfiles="$runalltestlog-$validatelog-$qltestlog-$migratelog"


python runBasicTests.py $abbr $tests $logfiles $verbosities $abbr_migrate > runBasicTests.log 2>&1 

dt=`date +%m%h`
runAllLogDir=`ls -dt $dt* | head -1`
cp $runAllLogDir/result.txt $runalltestlog


echo "You can check the output log files :"
echo $validatelog
echo $qltestlog
echo $runalltestlog
echo $migratelog
