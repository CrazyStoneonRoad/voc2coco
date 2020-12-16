#!/usr/bin/python
import os
import random
import uuid
import sys

def getFiles(dir_rt,suffix):
  res = []
  for root,directory,files in os.walk(dir_rt):
    for filename in files:
      name,suf = os.path.splitext(filename)
      if suf == suffix:
        res.append(os.path.join(root,filename))
  return(res)


def gen_lst(dir_rt_input, dtst, fold, opt, n_tiny=100, r_train=0.2, r_val=0.2):
  n_tiny = int(n_tiny)
  r_train = float(r_train)
  r_val = float(r_val)

  fils_lst = getFiles(dir_rt_input,'.xml')
  fils_lst_new = [e+'\n'for e in fils_lst]
  len_list = len(fils_lst_new)
  assert(len_list!=0)
  
  random.shuffle(fils_lst_new)
  
  r_val = r_train + r_val
  r_train = round(r_train*len_list)
  r_val = round(r_val*len_list)
  
  dtst_tiny = fils_lst_new[:n_tiny]
  dtst_train = fils_lst_new[:r_train]
  dtst_val = fils_lst_new[:r_val]
  dtst_test = fils_lst_new[r_val:]
  
  n_train = r_train
  n_val = r_val - r_train
  n_test = len_list - r_val
  
  if fold!="":
    fold = fold+'_'
  
  id_ = str(uuid.uuid1())[:4]
  
  tiny_name  ='tmp/'+ dtst+ '_tiny_' +     str(n_tiny) +'_' +id_+ '.txt'
  train_name ='tmp/'+ dtst+ '_train_'+fold+str(n_train)+'_'+ id_+ '.txt'
  val_name   ='tmp/'+ dtst+ '_val_'  +fold+str(n_val)  +'_'+ id_+ '.txt'
  test_name  ='tmp/'+ dtst+ '_test_' +fold+str(n_test) +'_'+ id_+ '.txt'
  
  opt=int(opt)
  
  if opt not in [1,2,3,4]:
    print('opt should be in [1,2,3,4]')
  elif opt==1:
    with open(tiny_name,"w") as f:
      f.writelines(dtst_tiny)
  elif opt==2:
    with open(train_name,"w") as f:
      f.writelines(dtst_train)
    with open(val_name,"w") as f:
      f.writelines(dtst_val)
  elif opt==3:
    with open(train_name,"w") as f:
      f.writelines(dtst_train)
    with open(val_name,"w") as f:
      f.writelines(dtst_val)
    with open(test_name,"w") as f:
      f.writelines(dtst_test)
  elif opt==4:
    with open(train_name,"w") as f:
      f.writelines(dtst_train)
    with open(val_name,"w") as f:
      f.writelines(dtst_val)
    with open(test_name,"w") as f:
      f.writelines(dtst_test)
    with open(tiny_name,"w") as f:
      f.writelines(dtst_tiny)
  
  s=[tiny_name,train_name,val_name,test_name]
  s=[e+'\n' for e in s]
  with open('tmp/__par__.txt',"w") as f:
    f.writelines(s)
  #return(tiny_name,train_name,val_name,test_name)
  


if __name__ == '__main__':
  len_ = len(sys.argv)
  print(sys.argv[0])
  #print(len_)
  
  if len_ <=4:
    print('4 to 7 auguments are need. Too less are given.')
    print('Usage: python gen_list.py dir_rt_input={"hrrsd/Annotations/"} dtst={hrrsd} fold={f1, f2, ..., or fn} opt={1, 2, or 3} [n_tiny=100.0] [r_train=0.2] [r_val=0.2]')
    exit(1)
  elif len_==5:
    gen_lst(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
  elif len_==6:
    gen_lst(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
  elif len_==7:
    gen_lst(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
  elif len_==8:
    gen_lst(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
  elif len_>=9:
    print('4 to 7 auguments are need. Too much are given.')
  
  
    
    
  
