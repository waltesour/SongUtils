import os
import pandas as pd
import cv2
import numpy as np
from skimage.measure import label
import random
from random import choice
from goto import with_goto

def calculate(image1, image2):
    # 灰度直方图算法
    # 计算单通道的直方图的相似值
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + \
                (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree
 
 
def classify_hist_with_split(image1, image2, size=(256, 256)):
    # RGB每个通道的直方图相似度
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    # image1 = cv2.resize(image1, size)
    # image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data

def intensitySame(img1,img2):
    (mean1 , stddv1) = cv2.meanStdDev(img1) 
    (mean2 , stddv2) = cv2.meanStdDev(img2)

    return abs(mean1.mean()-mean2.mean())

mask_list_path='C:/code/datasets/carDefect/img_blue_mask/'
rgb_list_path='C:/code/datasets/carDefect/img_blue/'
new_mask_list_path='C:/code/datasets/carDefect/img_blue_mask_new/'
new_rgb_list_path='C:/code/datasets/carDefect/img_blue_new/'
rotatelist=[0,1,2]
# AreaRange=[[0,37],[38,55],[56,100]] #约束的缺陷大小范围
# augTimes=[5,10,21] #每个特定范围的缺陷应该扩增原图像数目的多少倍
# [40,50][70,80]
AreaRange=[[37,70]] #约束的缺陷大小范围
augTimes=[1] #每个特定范围的缺陷应该扩增原图像数目的多少倍
aug=7
arealist=[]
imgNuminFile=1351  # 目标路径中已有的图像数目
# angleList=[90,180,270]
# ----------------step0:不同尺寸缺陷及扩增倍数遍历------------------
for num in range(0,len(augTimes)):
    hopeNum= augTimes[num] * len(os.listdir(rgb_list_path))+ imgNuminFile# 本组约束内的缺陷期望扩增到的图像数目
    
    while(len(os.listdir(new_rgb_list_path))<hopeNum):
        # aug=aug+1
        # ----------------step1:缺陷的遍历扣取------------------
        for file in os.listdir(rgb_list_path): #缺陷从file里扣取
            if file.endswith(".png"): #如果file以png结尾
                mask_img = cv2.imread(mask_list_path+file)
                rgb_img = cv2.imread(rgb_list_path+file)
                mask_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)#灰度
                ret, binary = cv2.threshold(mask_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                # 缺陷面积统计
                # cv2.imwrite("binary.jpg",binary)
                num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
                for i in range(0,stats.shape[0]): # 当前图像中的缺陷遍历,stats存储每个连通域的(x,y,width,height,area)
                    if(AreaRange[num][0]<=stats[i][4]<=AreaRange[num][1]): # 将落在限定范围内的缺陷提取出来
                        if(len(mask_img.shape)!=3):
                            mask_img = cv2.cvtColor(mask_img, cv2.COLOR_GRAY2BGR)#灰度
                        roiMask = mask_img[stats[i][1]:stats[i][1]+stats[i][3],stats[i][0]:stats[i][0]+stats[i][2],:]
                        coeff= np.zeros((mask_img.shape[0],mask_img.shape[1],3))
                        coeff[stats[i][1]:stats[i][1]+stats[i][3],stats[i][0]:stats[i][0]+stats[i][2],:]=roiMask
                        roi_rgb_all = rgb_img*(coeff/255) #缺陷roi区域扣取,非缺陷区域灰度值为0
                        roi_rgb = roi_rgb_all[stats[i][1]:stats[i][1]+stats[i][3],stats[i][0]:stats[i][0]+stats[i][2],:]
                        rorateFlag=choice(rotatelist)
                        if(rorateFlag==1):
                            roi_rgb = cv2.flip(roi_rgb, 1)
                        if(rorateFlag==2):
                            roi_rgb = cv2.flip(roi_rgb, 0)
                        # cv2.imwrite("roi.png",roi_rgb)


                        # cv2.imwrite("roi_rotate.png",roi_rgb)
                        # 往新mask上贴缺陷
                        skip=0
                        # ----------------step2:接收缺陷的图像遍历------------------
                        for newfile in os.listdir(rgb_list_path):
                            new_mask_img = cv2.imread(mask_list_path+newfile)
                            new_rgb_img = cv2.imread(rgb_list_path+newfile)
                            skip=0
                            for times in  range(0,5):#往一个图上粘多少次
                                while(skip<10):
                                    yIndex=random.randint(40,mask_img.shape[1]-40)
                                    xIndex=random.randint(40,mask_img.shape[0]-40)
                                    #对xIndex 和 yIndex 所示位置处的信息添加一些判断,保证贴图的自然
                                    patchSize=10
                                    roi_rgb_patch=rgb_img[stats[i][1]-patchSize:stats[i][1]+patchSize,stats[i][0]-patchSize:stats[i][0]+patchSize,:]
                                    new_rgb_img_patch=new_rgb_img[yIndex-patchSize:yIndex+patchSize,xIndex-patchSize:xIndex+patchSize,:]
                                    if(roi_rgb_patch.shape[0]==0 or roi_rgb_patch.shape[1]==0 or new_rgb_img_patch.shape[0]==0 or new_rgb_img_patch.shape[1]==0):
                                        continue
                                    # cv2.imwrite("patch1.jpg",roi_rgb_patch)
                                    # cv2.imwrite("patch2.jpg",new_rgb_img_patch)
                                    # if(classify_hist_with_split(rgb_img_patch,new_rgb_img_patch)<0.95):
                                    if(intensitySame(roi_rgb_patch,new_rgb_img_patch)>14):
                                        skip=skip+1
                                        
                                    else:
                                        # cv2.imwrite("img1.jpg",rgb_img)
                                        # cv2.imwrite("img2.jpg",new_rgb_img)
                                        break
                                        
                                if(new_mask_img[yIndex:yIndex+stats[i][3],xIndex:xIndex+stats[i][2],:].shape!=roiMask.shape):
                                    continue
                                if(skip<10):
                                    new_mask_img[yIndex:yIndex+stats[i][3],xIndex:xIndex+stats[i][2],:]=roiMask
                                    cv2.imwrite(new_mask_list_path+file[:-4]+"_"+newfile[:-4]+"_epoch"+str(num)+"_aug"+str(aug)+".png",new_mask_img)
                                    coeff= np.zeros((mask_img.shape[0],mask_img.shape[1],3))
                                    roi_rgb_allImg=  np.zeros((mask_img.shape[0],mask_img.shape[1],3))
                                    roi_rgb_allImg[yIndex:yIndex+stats[i][3],xIndex:xIndex+stats[i][2],:] = roi_rgb
                                    coeff[yIndex:yIndex+stats[i][3],xIndex:xIndex+stats[i][2],:] = roiMask
                                    coeff= 1- coeff/255
                                    new_rgb_img= new_rgb_img * coeff + roi_rgb_allImg
                                    cv2.imwrite(new_rgb_list_path+file[:-4]+"_"+newfile[:-4]+"_epoch"+str(num)+"_aug"+str(aug)+".png",new_rgb_img)
                                    
                                    if(len(os.listdir(new_rgb_list_path))>hopeNum): #扩增到指定数量就结束程序
                                        os._exit(0)           
                    


