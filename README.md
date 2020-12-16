# Get started
## run.sh ##
Main file is `run.sh`

- Input parameters: 
	- `/.../AnnotationXMLs_path/` which contains xmls,
	- `DatasetName` defined by yourself. 
- Function: several `*.json` files.

Run under `/.../voc2coco/`:

```
run "/.../AnnotationXMLs_path/" "DatasetName"
```
This file would call the follwing files. 

You can change the run.sh file to change parameters to be used.

## check.py ##

Check if the dataset contains some error labels:

```
xmin>xmax    
ymin>ymax
```

## gen_lst.py ##

Usage: 

```
python gen_list.py dir_rt_input={"hrrsd/Annotations/"} dtst={hrrsd} fold={f1, f2, ..., or fn} opt={1, 2, or 3} [n_tiny=100.0] [r_train=0.2] [r_val=0.2]
```
## voc2coco.py ##

Convert pascol voc annotation xml to COCO json format.

1. pip install lxml
2. python voc2coco.py xmllist.txt ../Annotations output.json

The xmllist.txt is the list of xml file names to convert.

- 000005.xml
- 000007.xml
- 000009.xml

The "../Annotations" is the place where all xmls located.

The "output.json" is the output json file.
