# 批量分割二值化图像
import os  #通过os模块调用系统命令
import cv2
import numpy as np

file_path = "C:/code/datasets/book/masks/"  #文件路径
path_list = os.listdir(file_path) #遍历整个文件夹下的文件name并返回一个列表

path_name = []#定义一个空列表

for i in path_list:
    # path_name.append(i.split(".")[0]) #若带有后缀名，利用循环遍历path_list列表，split去掉后缀名
    path_name.append(i)

#path_name.sort() #排序


kernel = np.ones((5,5),np.uint8)
for file_name in path_name:
    name=file_path+file_name
    read_img = cv2.imread(name)
    # foreground = (read_img > 0.99).astype(int)
    # background = (read_img < 0.01).astype(int)
    foreground=read_img
    erosion = cv2.erode(foreground,kernel,iterations = 15)
    dilation = cv2.dilate(foreground,kernel,iterations = 15)
    mid=dilation-erosion
    trimap=erosion*255+mid*150
    cv2.imwrite(name[:-4]+"_obj.jpg",foreground*255)
    # cv2.imwrite(name[:-4]+"_ero.jpg",erosion*255)
    # cv2.imwrite(name[:-4]+"_dil.jpg",dilation*255)
    cv2.imwrite(name[:-4]+"_trimap.jpg",trimap)
    