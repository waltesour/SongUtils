"""------------将文件内图像拼接成视频----------------"""
"""------------图像尺寸必须相同，否则该图片将不参与拼接----------------"""

import cv2
import glob

#根据自己的实际情况更改目录。
#要转换的图片的保存地址，按顺序排好，后面会一张一张按顺序读取。
convert_image_path = 'C:/code/yolov5-master/runs/detect/exp-wellCover'

#帧率(fps)，尺寸(size)，此处设置的fps为24，size为图片的大小，本文转换的图片大小为400×1080，
#即宽为400，高为1080，要根据自己的情况修改图片大小。
fps = 0.5
size = (2560,1440)

videoWriter = cv2.VideoWriter('C:/code/datasets/1.mp4',cv2.VideoWriter_fourcc('I','4','2','0'),
                              fps,size)

for img in glob.glob(convert_image_path + "/*.png"):
    print(img)
    read_img = cv2.imread(img)
    # read_img = dst = cv2.resize(read_img,None,fx=size[1]/read_img.shape[0],fy=size[0]/read_img.shape[1],interpolation=cv2.INTER_LINEAR)
    print(read_img.shape)
    videoWriter.write(read_img)
videoWriter.release()