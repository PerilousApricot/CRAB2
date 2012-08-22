source common_init.sh
dstUrl=$1
log=$2

cp ../python/insert_everything.py $dirName
cd $dirName
(time python2.4 insert_everything.py $dstUrl > $outLog) 2>> $log
cd -

