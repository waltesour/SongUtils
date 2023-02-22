import os
import cv2
import imageio
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def augment_hsv(img, h_gain=0.5, s_gain=0.5, v_gain=0.5):
    # 从-1~1之间随机生成3随机数与三个变量进行相乘
    r = [h_gain+ 1, s_gain+ 1, v_gain+ 1]   # random gains
    hue, sat, val = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    dtype = img.dtype  # uint8

    # 分别针对hue, sat以及val生成对应的Look-Up Table（LUT）查找表
    x = np.arange(0, 256, dtype=np.int16)
    lut_hue = ((x * r[0]) % 180).astype(dtype)
    lut_sat = np.clip(x * r[1], 0, 255).astype(dtype)
    lut_val = np.clip(x * r[2], 0, 255).astype(dtype)

    # 使用cv2.LUT方法利用刚刚针对hue, sat以及val生成的Look-Up Table进行变换
    img_hsv = cv2.merge((cv2.LUT(hue, lut_hue), cv2.LUT(sat, lut_sat), cv2.LUT(val, lut_val))).astype(dtype)
    aug_img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR, dst=img)  # no return needed

    # 这里源码是没有进行return的，不过我还是觉得return一下比较直观了解
    return aug_img

if __name__ == '__main__':
    #获取图像列表，此处为原始图像所在路径
    input_list = "C:/code/datasets/carDefect/img_BGR/"
    output_list = "C:/code/datasets/carDefect/img_BGR_all/"
    
    mask_list = "C:/code/datasets/carDefect/img_BGR_mask/"
    mask_hsv_list = "C:/code/datasets/carDefect/img_BGR_all_mask/"
    files = os.listdir(input_list)
    s=0
    h_gain=[-0.3, 0.3,1]
    s_gain=[-0.5, -0.3,0.3]
    for file in files:
        #按照获取的列表依次读取列表，路径同上
        for h in range(0,3):
            img = io.imread(input_list+file)
            mask = io.imread(mask_list+file)
            img_out = augment_hsv(img,h_gain[h],0,0) # H -0.5 0.5 1 
            #s = s + 1
            #路径为结果保存路径
            imageio.imwrite(output_list + file[:-4] + "_{}.png".format(h), img_out)
            imageio.imwrite(mask_hsv_list + file[:-4] + "_{}.png".format(h), mask)

        for s in range(0,3):
            img = io.imread(input_list+file)
            mask = io.imread(mask_list+file)
            img_out = augment_hsv(img,0,s_gain[s],0) #v:  -0.3  0.3  0.5
            #s = s + 1
            #路径为结果保存路径
            imageio.imwrite(output_list + file[:-4] + "_{}.png".format(3+s), img_out)
            imageio.imwrite(mask_hsv_list + file[:-4] + "_{}.png".format(3+s), mask)

    #print('已处理完{}张照片'.format(s))

