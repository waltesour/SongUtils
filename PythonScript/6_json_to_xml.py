# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 17:24:21 2021

@author: admin
"""

import os
from typing import List, Any
import numpy as np
import codecs
import json
from glob import glob
import cv2
import shutil
from sklearn.model_selection import train_test_split
 

labelme_path = "C:/code/datasets/wellCover/井盖江西/敬涛_井盖/"

saved_path = "C:/code/datasets/wellCover/井盖江西/敬涛_井盖/"

isUseTest = False    #是否创建test集

if not os.path.exists(saved_path + "Annotations"):
    os.makedirs(saved_path + "Annotations")
if not os.path.exists(saved_path + "JPEGImages/"):
    os.makedirs(saved_path + "JPEGImages/")
if not os.path.exists(saved_path + "ImageSets/Main/"):
    os.makedirs(saved_path + "ImageSets/Main/")
# 3.获取待处理文件
files = glob(labelme_path + "*.json")
files = [i.replace("\\","/").split("/")[-1].split(".json")[0] for i in files]
# print(files)
# 4.读取标注信息并写入 xml
for json_file_ in files:
    json_filename = labelme_path + json_file_ + ".json"
    print(json_filename)
    json_file = json.load(open(json_filename, "r", encoding="utf-8"))
    # 使用imdecode替换imread,应该是与图片的格式有关
    # height, width, channels =cv2.imdecode(np.fromfile(labelme_path + json_file_ + ".jpg",dtype=np.uint8),cv2.IMREAD_COLOR).shape
    height, width, channels = cv2.imread(labelme_path + json_file_ + ".jpg").shape
    with codecs.open(saved_path + "Annotations/" + json_file_ + ".xml", "w", "utf-8") as xml:
        xml.write('<?xml version="1.0" ?>\n')
        xml.write('<annotation>\n')
        xml.write('<folder>' + 'WH_data' + '</folder>\n')
        xml.write('<filename>' + json_file_ + ".jpg" + '</filename>\n')
        xml.write('<source>\n')
        xml.write('    <database>chefhat</database>\n')
        xml.write('    <annotation>chefhat</annotation>\n')
        xml.write('    <image>flickr</image>\n')
        xml.write('    <flickrid>NULL</flickrid>\n')
        xml.write('</source>\n')
        xml.write('<owner>\n')
        xml.write('    <flickrid>NULL</flickrid>\n')
        xml.write('    <name>chefhat</name>\n')
        xml.write('</owner>\n')
        xml.write('<size>\n')
        xml.write('    <width>' + str(width) + '</width>\n')
        xml.write('    <height>' + str(height) + '</height>\n')
        xml.write('    <depth>' + str(channels) + '</depth>\n')
        xml.write('</size>\n')
        xml.write('<segmented>0</segmented>\n')
        for multi in json_file["shapes"]:
            points = np.array(multi["points"])
            labelName=multi["label"]
            xmin = min(points[:, 0])
            xmax = max(points[:, 0])
            ymin = min(points[:, 1])
            ymax = max(points[:, 1])
            label = multi["label"]
            if xmax <= xmin:
                pass
            elif ymax <= ymin:
                pass
            else:
                xml.write('<object>\n')
                xml.write('    <name>' + labelName+ '</name>\n')
                xml.write('    <pose>Unspecified</pose>\n')
                xml.write('    <truncated>1</truncated>\n')
                xml.write('    <difficult>0</difficult>\n')
                xml.write('    <bndbox>\n')
                xml.write('      <xmin>' + str(int(xmin)) + '</xmin>\n')
                xml.write('      <ymin>' + str(int(ymin)) + '</ymin>\n')
                xml.write('      <xmax>' + str(int(xmax)) + '</xmax>\n')
                xml.write('      <ymax>' + str(int(ymax)) + '</ymax>\n')
                xml.write('    </bndbox>\n')
                xml.write('</object>\n')
                # print(json_filename, xmin, ymin, xmax, ymax, label)
        xml.write('</annotation>')
    
# 5.复制图片到 VOC2007/JPEGImages/下
image_files = glob(labelme_path + "*.jpg")
# print("copy image files to VOC007/JPEGImages/")
for image in image_files:
    shutil.copy(image, saved_path + "JPEGImages/")

#6.生成没有物体的图片的xml文件
xml_files=glob(saved_path+"Annotations/"+"*.xml")
img_names=[]
xml_names=[]

for xml in xml_files:
    xml_name=xml[xml.find("\\")+1:-4]
    xml_names.append(xml_name)
    #print(xml_name)

for image in image_files:
    image_name=image[image.find('\\')+1:-4]
    #img_names.append(image_name)
    #print(image_name)
    if image_name not in xml_names:
        print(image_name)




# # 6.split files for txt
# txtsavepath = saved_path + "ImageSets/Main/"
# ftrainval = open(txtsavepath + '/trainval.txt', 'w')
# ftest = open(txtsavepath + '/test.txt', 'w')
# ftrain = open(txtsavepath + '/train.txt', 'w')
# fval = open(txtsavepath + '/val.txt', 'w')
# total_files = glob("./VOC2007/Annotations/*.xml")
# total_files = [i.replace("\\","/").split("/")[-1].split(".xml")[0] for i in total_files]
# trainval_files=[]
# test_files=[] 
# if isUseTest:
#     trainval_files, test_files = train_test_split(total_files, test_size=0.15, random_state=55) 
# else: 
#     trainval_files=total_files 
# for file in trainval_files: 
#     ftrainval.write(file + "\n") 
# # split 
# train_files, val_files = train_test_split(trainval_files, test_size=0.15, random_state=55) 
# # train
# for file in train_files: 
#     ftrain.write(file + "\n") 
# # val 
# for file in val_files: 
#     fval.write(file + "\n")
# for file in test_files:
#     print(file)
#     ftest.write(file + "\n")
# ftrainval.close()
# ftrain.close()
# fval.close()
# ftest.close()
