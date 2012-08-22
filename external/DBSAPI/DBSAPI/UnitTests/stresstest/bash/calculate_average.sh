source ../conf.sh
logFile=$1

totalNoOfEntries=`cat $logFile |grep real|wc|awk '{print $1}'`
#echo "total $totalNoOfEntries"
minAvg=`cat $logFile |grep real| awk '{print $2}'|awk -Fm '{sum = sum + $1} END {print sum}'| awk -v TOTAL=$totalNoOfEntries '{ avg = $1/TOTAL } END {print avg }'`
secAvg=`cat $logFile |grep real| awk '{print $2}'|awk -Fm '{print $2}'|awk -Fs '{sum = sum + $1} END {print sum}'| awk -v TOTAL=$totalNoOfEntries '{ avg = $1/TOTAL } END {print avg}'`
maxTime=`cat $logFile |grep real| awk '{print $2}'|awk '{max = $1} END {print max}'`
allTimes=`cat $logFile |grep real| awk '{print $2}'`
tmp=`echo "Average TIME took to complete test is  $minAvg MINS : $secAvg SECS. Total number of clients completed are $totalNoOfEntries . Total time taken is $maxTime . The list of times taken by each process is $allTimes"`
echo $tmp
echo $tmp | mail -s "Stress Test for $totalNoOfEntries clients" $email

