#!/bin/sh

#BSUB -q inspur
#BSUB -n 20
#BSUB -R "span[hosts=1]"
#BSUB -cwd .
#BSUB -e %J.err
#BSUB -o %J.out
#BSUB -J zhoum


#此高斯16版脚本将把缓冲放在计算节点，减少通讯和数据交换时间，提高计算速度
#同时减少用户操作步骤，只需要修改jobname和作业名，开始计算后将返回log文件
#其他文件将在计算结束后从计算节点硬盘返回存储。huawei,inspur,lenovo

jobname=TS7-d-35

#输入文件名，不加后缀名

username=`whoami`
Current_WORKDIR=`pwd`

Inputfile=${jobname}.in

export g16root=/home/soft/g16
#source $g16root/bsd/g16.profile

export GAUSS_EXEDIR=/home/soft/g16
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/soft/g16
export PATH=/home/soft/g16:$PATH
export PATH=/home/soft/nbo7/bin:$PATH
GAUSS_RUNDIR=/tmp/$username/$LSB_JOBID
if [ ! -a $GAUSS_RUNDIR ]; then
   echo "Scratch directory $GAUSS_RUNDIR created."
   mkdir -p $GAUSS_RUNDIR
fi

cp $Current_WORKDIR/$Inputfile  $GAUSS_RUNDIR
cp $Current_WORKDIR/${jobname}.chk  $GAUSS_RUNDIR
cd $GAUSS_RUNDIR

GAUSS_SCRDIR=$GAUSS_RUNDIR/${jobname}
if [ ! -a $GAUSS_SCRDIR ]; then
   echo "Scratch directory $GAUSS_SCRDIR created."
   mkdir -p $GAUSS_SCRDIR
fi
export GAUSS_SCRDIR
echo "Using $GAUSS_SCRDIR for temporary Gaussian 16 files."

echo "Starting Gaussian run at" `date`

time /home/soft/g16/g16 < $GAUSS_RUNDIR/${jobname}.in > $Current_WORKDIR/${jobname}.log

echo "Finished Gaussian run at" `date`

echo $Current_WORKDIR

mv $GAUSS_RUNDIR/*.chk $Current_WORKDIR
mv $GAUSS_RUNDIR/${jobname}.* $Current_WORKDIR
echo "$GAUSS_SCRDIR"

rm -Rf $GAUSS_SCRDIR  $GAUSS_RUNDIR



