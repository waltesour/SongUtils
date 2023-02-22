# 基于文件名,将文件夹A中已有的图片从文件夹B中移动到文件夹C中
import os
import shutil
from tqdm import tqdm
fileA = r'C:\code\datasets\expressData\instanceSegCOCO\train2017'
fileB = r'C:\code\datasets\expressData\20221124\img1'
fileC = r'C:\code\datasets\expressData\20221124\sameImg'
path_list_A = os.listdir(fileA) #遍历整个文件夹下的文件name并返回一个列表
path_list_B = os.listdir(fileB)
for i in path_list_B:
    if(i in path_list_A):
        print("yes")
        shutil.move(os.path.join(fileB, i), os.path.join(fileC, i))
print()