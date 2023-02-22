"""-------------------使用imgaug对图像进行数量上的扩增--------------------"""
"""-----------------------使用 labelImg 虚拟环境 ------------------------"""
import cv2
import imgaug.augmenters as iaa
import os

"""输入原图像所在文件夹，生成图像存储文件夹，给扩增图像名称添加的后缀"""
dirPath='C:/code/datasets/wellCoverROI2/val/bad'
dstPath='C:/code/datasets/wellCoverROI2/val/badAug'
augSuffix='aug2'

"""定义扩增操作"""
seq = iaa.Sequential([
    # iaa.Crop(px=(1, 16), keep_size=False),
    # iaa.CoarseDropout(0.02, size_percent=0.5),
    # iaa.AllChannelsHistogramEqualization(),
    # iaa.Rain(speed=(0.1, 0.3)),
    # iaa.Snowflakes(flake_size=(0.1, 0.4), speed=(0.01, 0.05)),
    # iaa.Rot90(1),
    # iaa.Affine(scale=(0.8, 1.0)),
    # iaa.CropAndPad(percent=(-0.25, 0.25)),
    iaa.CropAndPad(percent=(0, 0.2),pad_mode=["constant", "edge"],pad_cval=(0, 128)),
    # iaa.LogContrast(gain=(0.6, 1.4)),
    iaa.Affine(rotate=(-15, 15)),
    iaa.Fliplr(0.5),
    # iaa.GaussianBlur(sigma=(0, 2.0))
])

imglist=[]
for file in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath, file)) == True:
        c= os.path.basename(file) #basename返回文件名
        name = dirPath + '/' + c
        img = cv2.imread(name)
        imglist.append(img)
images_aug = seq.augment_images(imglist)
i=0
for file in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath, file)) == True:
        c= os.path.basename(file) #basename返回文件名
        name = dstPath + '/' + c[:-4] +augSuffix+'.jpg'
    cv2.imwrite(name,images_aug[i])
    i=i+1