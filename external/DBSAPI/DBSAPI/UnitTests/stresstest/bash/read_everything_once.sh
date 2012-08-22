source common_init.sh
dstUrl=$1
log=$2

cp ../python/read_everything.py $dirName
cd $dirName
(time python2.4 read_everything.py $dstUrl > $outLog) 2>> $log
cd -

