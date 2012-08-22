source ../conf.sh
uuid=`uuidgen`
if [ -f $timeInsertLog ]
then
	mkdir -p logs
	mv $timeInsertLog "${timeInsertLog}_${uuid}"
	mv "${timeInsertLog}_${uuid}" logs
	touch $timeInsertLog
fi

insertEverything()
{
	start=0
	while [ "$start" -lt "$1" ] 
	do 
		((++start))
		./insert_everything_once.sh $dstUrl $timeInsertLog &
	done
}
insertEverything $1
./poll_for_completion.sh $1 $timeInsertLog
