# Getting started

@[toc]

## 中文版本 ##
### run.sh ###
主文件为 `run.sh`

确保运行前，项目下存在目录`run.sh`

- 输入参数：
	- `/.../AnnotationXMLs_path/`：该目录下须包含所有VOC格式的`xml`文件
	- `DtasetName`：数据库名称，由用户自己定义
- 功能：输出若干COCO数据集格式的`*.json`文件

在`/.../voc2coco/`目录下运行：

```
run "/.../AnnotationXMLs_path/" "DatasetName"
```

`run.sh`会调用如下文件：`check.py gen_lst.py voc2coco.py`

如需修改参数、参数输入方式，可以更改`run.sh`中前面几行的变量值


### check.py ###

检查数据集是否包含一些错误标签，例如：

```
xmin>xmax    
ymin>ymax
```

### gen_lst.py ###

生成文件列表，为`voc2coco.py`做准备

用法：

```
python gen_list.py dir_rt_input={"hrrsd/Annotations/"} dtst={hrrsd} fold={f1, f2, ..., or fn} opt={1, 2, or 3} [n_tiny=100.0] [r_train=0.2] [r_val=0.2]
```

[参数] 可选参数.

### voc2coco.py ###

将pascol voc格式xml标注文件，转换成coco格式标注文件

> pip install lxml
> 
> python voc2coco.py xml_list.txt ../Annotations output.json

`xml_list.txt` 是待转换格式的 `xml` 文件：

```
000005.xml 000007.xml 000009.xml ...
```

`"../Annotations"` 是存放所有 `xml` 的目录.

`"output.json"`为输出的`json`文件

## English Version ##
### run.sh ###
Main file is `run.sh` 

Better make sure the existence of the path `./tmp/`

- Input parameters: 
	- `/.../AnnotationXMLs_path/` which contains `xmls`,
	- `DatasetName` defined by yourself. 
- Function: Output several `*.json` files of COCO format.

Run under `/.../voc2coco/`:

```
run "/.../AnnotationXMLs_path/" "DatasetName"
```

This file would call the follwing files. 

You can change the run.sh file to change parameters to be used.

### check.py ###

Check if the dataset contains some error labels:

```
xmin>xmax    
ymin>ymax
```

### gen_lst.py ###

Generate file list to get prepared for `voc2coco.py`

Usage: 

```
python gen_list.py dir_rt_input={"hrrsd/Annotations/"} dtst={hrrsd} fold={f1, f2, ..., or fn} opt={1, 2, or 3} [n_tiny=100.0] [r_train=0.2] [r_val=0.2]
```

[parameter] optional parameters.

### voc2coco.py ###

Convert pascol voc annotation xml to COCO json format.

1. pip install lxml
2. python voc2coco.py xmllist.txt ../Annotations output.json

The xmllist.txt is the list of xml file names to convert.

```
000005.xml 000007.xml 000009.xml ...
```

The "../Annotations" is the place where all xmls located.

The "output.json" is the output json file.
