source ../conf.sh
uuid=`uuidgen`
if [ -f $timeReadLog ]
then
	mkdir -p logs
	mv $timeReadLog "${timeReadLog}_${uuid}"
	mv "${timeReadLog}_${uuid}" logs
	touch $timeReadLog
fi

readEverything()
{
	start=0
	while [ "$start" -lt "$1" ] 
	do 
		((++start))
		./read_everything_once.sh $dstUrl $timeReadLog &
	done
}
readEverything $1
./poll_for_completion.sh $1 $timeReadLog
