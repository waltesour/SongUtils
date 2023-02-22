""" --------  脚本功能:计算指定路径中 拥有指定文字行数的txt文件数目  ------------"""
import os

def file_len(fname):
    sz = os.path.getsize(fname)
    if not sz:
        return 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

txt_list_path='C:/code/OpenLabeling-master/main/output/YOLO_darknet/'
line_num=0
count=0
for file in os.listdir(txt_list_path): #file为current_dir当前目录下图片名
    if file.endswith(".txt"): #如果file以jpg结尾
        write_name = txt_list_path+file #图片路径 + 图片名
        L=file_len(write_name)
        if (L==line_num):
            count=count+1

print("The numbers of txt files with %d lines is %d: " %(line_num,count))

