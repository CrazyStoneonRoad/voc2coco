#!/usr/bin/python

# pip install lxml

import sys
import os
import json
import xml.etree.ElementTree as ET
from time import sleep
from tqdm import tqdm


def getFiles(dir_rt,suffix):
  res = []
  for root,directory,files in os.walk(dir_rt):
    for filename in files:
      name,suf = os.path.splitext(filename)
      if suf == suffix:
        res.append(filename)
  return(res)
  
def get(root, name):
    vars = root.findall(name)
    return vars

def get_and_check(root, name, length):
    vars = root.findall(name)
    if len(vars) == 0:
        raise NotImplementedError('Can not find %s in %s.'%(name, root.tag))
    if length > 0 and len(vars) != length:
        raise NotImplementedError('The size of %s is supposed to be %d, but is %d.'%(name, length, len(vars)))
    if length == 1:
        vars = vars[0]
    return vars



def get_filename_as_int(filename):
    try:
        filename = os.path.splitext(filename)[0]
        return int(filename)
    except:
        raise NotImplementedError('Filename %s is supposed to be an integer.'%(filename))


def loc_check(x,xx,y,yy):
    if (xx>x) and (yy>y):
        return True
    else:
        return False


def _check_(xml_dir):
    result=[]
    
    fils = getFiles(xml_dir,'.xml')
    
    for fil_ in tqdm(fils):
        fil_ = fil_.strip()
        xml_f = os.path.join(xml_dir, fil_)
        tree = ET.parse(xml_f)
        root = tree.getroot()
        path = get(root, 'path')
        if len(path) == 1:
            filename = os.path.basename(path[0].text)
        elif len(path) == 0:
            filename = get_and_check(root, 'filename', 1).text
        else:
            raise NotImplementedError('%d paths found in %s'%(len(path), fil_))
        ## The filename must be a number
        image_id = get_filename_as_int(filename)
        
        
        cunt_obj = 0
        for obj in get(root, 'object'):
            cunt_obj = cunt_obj + 1
            
            bndbox = get_and_check(obj, 'bndbox', 1)
            xmin = int(get_and_check(bndbox, 'xmin', 1).text) - 1
            ymin = int(get_and_check(bndbox, 'ymin', 1).text) - 1
            xmax = int(get_and_check(bndbox, 'xmax', 1).text)
            ymax = int(get_and_check(bndbox, 'ymax', 1).text)
            if not loc_check(xmin,xmax,ymin,ymax):
                result.append( ['img_id:\t'+str(image_id),'obj_id:\t'+str(cunt_obj)] )
        pass
    return(result)



if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('1 augument is needed.')
        print('Usage: %s XML_DIR'%(sys.argv[0]))
        exit(1)
    print(sys.argv[0])
    res = _check_(sys.argv[1])
    if (res):
        print("Failed files are:",res)
        #[[print('\t'+e) for e in part] for part in res]
        [print(part) for part in res]
        sys.exit(0)
    else:
        print("well done!")
        sys.exit(1)
