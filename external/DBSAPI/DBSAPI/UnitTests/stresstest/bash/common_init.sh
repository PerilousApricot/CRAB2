timestamp=`date +%m%y%d%M%S`
uuid=`uuidgen`
dirName="tmp/${timestamp}_${uuid}"
#echo $dirName 
mkdir -p $dirName
outLog="OUTPUT_LOG.txt"

