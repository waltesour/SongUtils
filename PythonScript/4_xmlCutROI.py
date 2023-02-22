from __future__ import division
""" --------  脚本功能:根据xml标注结果,裁剪出被框选的子图区域  ------------"""
"""
ImgPath:图像路径
AnnoPath:xml文件的路径
ProcessedPath:子图区域的保存路径
"""
import os
from PIL import Image
import xml.dom.minidom
import numpy as np
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
ImgPath = r'C:/code/datasets/wellCover/每张图片都至少一个井盖的图片/images/'
AnnoPath = r'C:/code/datasets/wellCover/每张图片都至少一个井盖的图片/xml/'
ProcessedPath = r'C:/code/datasets/wellCover/每张图片都至少一个井盖的图片/cutROI/'
 
imagelist = os.listdir(ImgPath)
 
for image in imagelist:
  image_pre, ext = os.path.splitext(image) #将名称和后缀拆分开来
  imgfile = ImgPath + image
  print(imgfile)
  if not os.path.exists(AnnoPath + image_pre + '.xml' ): #若某图像无对应xml,就跳过
    continue
  xmlfile = AnnoPath + image_pre + '.xml'
  DomTree = xml.dom.minidom.parse(xmlfile)
  annotation = DomTree.documentElement
  filenamelist = annotation.getElementsByTagName('filename')
  filename = filenamelist[0].childNodes[0].data
  objectlist = annotation.getElementsByTagName('object')
  i = 1
  for objects in objectlist:
    namelist = objects.getElementsByTagName('name')
    objectname = namelist[0].childNodes[0].data
    savepath = ProcessedPath + objectname
    if not os.path.exists(savepath):
      os.makedirs(savepath)
    bndbox = objects.getElementsByTagName('bndbox')
    cropboxes = []
    for box in bndbox:
      x1_list = box.getElementsByTagName('xmin')
      x1 = int(x1_list[0].childNodes[0].data)
      y1_list = box.getElementsByTagName('ymin')
      y1 = int(y1_list[0].childNodes[0].data)
      x2_list = box.getElementsByTagName('xmax')
      x2 = int(x2_list[0].childNodes[0].data)
      y2_list = box.getElementsByTagName('ymax')
      y2 = int(y2_list[0].childNodes[0].data)
      w = x2 - x1
      h = y2 - y1
      obj = np.array([x1,y1,x2,y2])
      shift = np.array([[1,1,1,1]])
      XYmatrix = np.tile(obj,(1,1))
      cropboxes = XYmatrix * shift
      img = Image.open(imgfile)
      for cropbox in cropboxes:
        cropedimg = img.crop(cropbox)
        cropedimg.save(savepath + '/' + image_pre + '_' + str(i) + '.jpg')
        i += 1