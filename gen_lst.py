#!/usr/bin/python
import os

def getFiles(dir_rt,suffix):
  res = []
  for root,directory,files in os.walk(dir_rt):
    for filename in files:
      name,suf = os.path.splitext(filename)
      if suf == suffix:
        res.append(os.path.join(root,filename))
  return(res) 

dir_rt = "/data/yuanlin/DATA/detection/MY_VOC_dataset/OPTIMAL_Z_FINAL/Annotations/"
dir_rt2 = "/home/yuanlin/CODE/TGRS-HRRSD-Dataset/OPT2017/Annotations/"
fils_lst = getFiles(dir_rt2,'.xml')
len_list = len(fils_lst)

if len_list!=0:
  f=open("xml_list.txt","w")
  f.writelines([e+'\n'for e in fils_lst])
  f.close()
  