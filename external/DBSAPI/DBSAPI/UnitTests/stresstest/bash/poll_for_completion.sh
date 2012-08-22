logFile=$2
while [ 1 ]
do
	if [ -f $logFile ]
	then

		totalNoOfEntries=`cat $logFile |grep real|wc|awk '{print $1}'`
		if [ "$totalNoOfEntries" -eq "$1" ]
		then
			#echo "All threads completed ..."
			break
		else
			#echo "Some threads still working"
			sleep 5
		fi
	fi
done
#echo "$totalNoOfEntries clients completed"
./calculate_average.sh $logFile
