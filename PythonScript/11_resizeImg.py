"""------------将path1内的图像尺寸批量修改为指定尺寸，存到path2中----------------"""
import os
from PIL import Image

path1='C:/Users/SONGSHUXIANG/Desktop/test'
path2='C:/Users/SONGSHUXIANG/Desktop/test1'
fileName = os.listdir(path1)
width = 1920
height = 1080

for img in fileName:
    pic = Image.open(path1+'/'+img)
    newpic = pic.resize((width,height),Image.ANTIALIAS)
    print(newpic)
    newpic.save(path2+'/'+img)