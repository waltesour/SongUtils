# -*- coding: utf-8 -*-
from __future__ import print_function
import copy

'''
脚本功能:从coco的完整标注文件里提取某些图片对应的json信息,并保存成新的子json文件
'''
import matplotlib.pyplot as plt
import os, sys, zipfile
import urllib.request
import shutil
import numpy as np
# import skimage.io as io
import pylab
import json
from pycocotools.coco import COCO

pylab.rcParams['figure.figsize'] = (8.0, 10.0)
image_path = 'C:/code/datasets/expressData/20221227/train' #子图路径
json_file='C:/code/datasets/expressData/20221227/all.json' # # 所有图像的json源文件
new_json = 'C:/code/datasets/expressData/20221227/train.json'
imgNameStartIndex=0
# imgNameStartIndex= len('/youzheng_part1_hangye/youzheng_part1_hangye/part1/part1')+1   #根据AI平台导出json文件的实际路径选取,[imgNameStartIndex:]
label=['zhixiang','ruanbao','madai','other']
coco=COCO(json_file)
data=json.load(open(json_file,'r')) 

data_2={}   #新json文件

data_2['info']=data['info']
data_2['licenses']=data['licenses']
data_2['categories']=data['categories']


annotation=[]
images = []
# print(data_img['images'])

imagename = [f for f in os.listdir( image_path)] #读取文件夹下图片名字
print(len(data['images'])) 

#根据图片数量找到每张图片对应的annotation，即每个‘images’可能有多个annotation（一张图片有多个可识别的目标）
for name_index in range(0,len(imagename)):
    # 通过imgID 找到其所有instance
    print("recent Index: ",name_index)
    imgID = 0
    for i in range(0,len(data['images'])):
        if data['images'][i]['file_name'][imgNameStartIndex:] == imagename[name_index]:  #根据图片名找到对应的json中的'images'
            data['images'][i]['file_name']=data['images'][i]['file_name'][imgNameStartIndex:] #AI平台标注出来的图片路径多了很多前缀
            imgID=data['images'][i]['id']
            # print(name_index, imgID)
            recentIDTimes=0     
            for img in data['images']:    #根据image_id找到对应的img
                if img['id']==imgID:
                    recentIDTimes=recentIDTimes+1 # 累计当前imgID出现的次数,正常每个imgID应该是唯一的
                    objImg=img
            if recentIDTimes==1:#如果当前imgID唯一,就保留当前img和对应ann,否则该imgID对应的img和ann全部抛弃
                images.append(objImg)
                for ann in data['annotations']:    #根据image_id找到对应的annotation
                    if ann['image_id']==imgID:  
                        if('package' in ann['attributes'] and ann['attributes']['package']!=''):
                            ann['category_id']=label.index(ann['attributes']['package']) #根据package 指定的标签类型返回对应标签序号
                        annotation.append(ann)
data_2['images'] = images
data_2['annotations']=annotation
print(len(data_2['images']))
json.dump(data_2,open(new_json,'w'),indent=4)

#对子json文件的id(ann的id和图像id)进行从0开始的重新排序
temp = copy.deepcopy(data_2) #深拷贝
annnewId=1
for i in range(len(data_2['images'])):
    data_2['images'][i]['id'] = i 
    #这里对标注信息的id和对应图像id进行修改
    for j in range(len(data_2['annotations'])):
        if(temp['annotations'][j]['image_id']==temp['images'][i]['id']):#标注文件中找到对应图像索引
            data_2['annotations'][j]['image_id']=i
            data_2['annotations'][j]['id'] = annnewId
            annnewId=annnewId+1
new_json2 = 'C:/code/datasets/expressData/test/divide/img2.json'
# 保存到新的json
json.dump(data_2,open(new_json2,'w'),indent=4)
