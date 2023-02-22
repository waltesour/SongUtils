"""------------根据图像大小和图像尺寸，去掉爬取的无效图片----------------"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
from PIL import Image
 
path = 'C:/code/pythonScript/images/'
dirs = os.listdir(path)
for file in dirs:
	temp = path + file
	file_stats = os.stat(temp)
	if file_stats.st_size==0: #判断文件占多少字节
		os.remove(temp)
		continue
	img = Image.open(temp)
 
	#print os.path.isfile(temp),将图像尺寸太小的删除
	if(img.size[0] < 20 or img.size[1] < 20):
		if os.path.isfile(temp):
			img = 1
			os.remove(temp)