# 统计缺陷面积分布情况统计
import os
import pandas as pd
import cv2
import numpy as np
from skimage.measure import label
from collections import Counter

mask_list_path='C:/code/datasets/carDefect/imgMaskAug/'
arealist=[]
for file in os.listdir(mask_list_path): #file为current_dir当前目录下图片名
    if file.endswith(".png"): #如果file以png结尾
        read_img = cv2.imread(mask_list_path+file)
        read_img = cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY)#灰度
        ret, binary = cv2.threshold(read_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # 缺陷面积统计
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
        for i in range(0,stats.shape[0]): # stats存储每个连通域的(x,y,width,height,area)
            if(binary[int(centroids[i][1]),int(centroids[i][0])]==255): # centroids存储每个连通域的中心点坐标
                arealist.append(stats[i][4])
                # if(len(binary.shape)!=3):
                #     binary = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
                #     cv2.circle(binary,(int(centroids[i][0]),int(centroids[i][1])),1,(0,0,255),3)
                #     cv2.imwrite("binary.jpg",binary)
arealist.sort()
result = Counter(arealist)
file0 = open('defectNum.txt','w')
file0.write(str(result))
file0.close()
file = open('defectArea.txt','w')
file.write(str(arealist))
file.close()

import matplotlib.pyplot as plt
def draw_hist(myList,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax):
    plt.hist(myList,20)
    plt.xlabel(Xlabel)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin,Ymax)
    plt.title(Title)
    # plt.show()
    plt.savefig('blueAnasys.jpg')
draw_hist(arealist,'AreasList','Area','number',min(arealist),max(arealist),0,20000)