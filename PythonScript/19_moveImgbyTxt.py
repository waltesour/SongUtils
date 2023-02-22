# -*- coding: utf-8 -*-
import os 

# 1、将指定路径下的图像名存入txt
'''
mask_list_path='C:/code/datasets/carDefect/img_gray/'
f = open('img_gray.txt', 'a')            # 创建标签文件存放图片文件名
for file in os.listdir(mask_list_path):
    f.write(file + '\n')                 # 将图片文件名逐行写入txt      
f.close() 
print('save name OK')
'''

# 2、将txt中指定的图像从A文件夹移动到B文件夹
import shutil
# 读取图片的路径
read_path = "C:/code/datasets/carDefect/mask/"
# 存放图片的路径
save_path = "C:/code/datasets/carDefect/img_gray_mask/"
txtPath='img_gray.txt'
if not os.path.exists(save_path):
    os.mkdir(save_path)
num = 0
# 读取并遍历读取txt中的每行
with open(txtPath,'r') as f:
    for name in f:
        fileName = name.strip() # 去除末尾的换行
        # 读取并遍历文件夹中的图片
        for file in os.listdir(read_path):
            if fileName == file:
                num+=1
                shutil.copy(os.path.join(read_path,fileName),save_path)
                print("%s Copy successfully"%(fileName))
    print("Copy complete!")
    print("Total pictures copied:",num)
