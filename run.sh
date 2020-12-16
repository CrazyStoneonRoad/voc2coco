#!/bin/bash
VocAnn_path=$1
#"/data/yuanlin/DATA/detection/Old_Dtsts/MY_VOC_dataset/OPTIMAL_Z_FINAL/Annotations/"
dataset=$2
#"hrrsd"
fold_type="m-fld"
option_type=4


python check.py $VocAnn_path $dataset $fold_type $option_type
check=$?
#echo $check
if [ $check -eq 0 ]; then
  exit
fi
#if $#<=3
#then
#  python gen_lst.py "/data/yuanlin/DATA/detection/Old_Dtsts/MY_VOC_dataset/OPTIMAL_Z_FINAL/Annotations/" "hrrsd" "m-fld" 4
#elif [$#<=7]
#  VocAnn_path=$1
#  COCOAnn_path=$2
#  prfx=$3
#  opt=$4
#  python gen_lst.py $VocAnn_path $dataset $fold_type $option_type #$5 $6 $7
#fi
python gen_lst.py $VocAnn_path $dataset $fold_type $option_type
for line in `cat ./tmp/__par__.txt`
do 
  name=$line
  #echo $name
  name=${name%%.*}.json
  echo $name
  python voc2coco.py $line '' $name
done
