source common_init.sh
srcUrl=$1
dstUrl=$2
dataset=$3
log=$4

cp ../python/dbsMigrateWithParents.py $dirName
cd $dirName
(time python2.4 dbsMigrateWithParents.py $srcUrl $dstUrl $dataset > $outLog) 2>> $log
cd -
