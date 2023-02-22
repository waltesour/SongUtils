""" --------  脚本功能:将指定路径中图片的路径和名称存储到指定txt文件  ------------"""

# 将以下内容添加到launch.json后，即可以调试该脚本
# "args":
# [
#     "-i","C:\\code\\OpenLabeling-master\\main\\input",
#     "-o","C:\\code\\OpenLabeling-master\\main\\input\\dir.txt"
# ]

import sys
# sys.path.append('虚拟环境的地址/引用模块的地址')
import os #os：操作系统相关的信息模块
import random #导入随机函数
import argparse

# metavar用来生成帮助信息,required表明这个参数是必须有的(不提供就报错),type表示该参数类型
def parse_args():
    parser = argparse.ArgumentParser('ImgNameListGen')
    parser.add_argument("--image_path","-i", metavar=': image file', required=True, type=str, default="image",help='input')
    parser.add_argument("--out_txt_path","-o", metavar=':txt file', required=False, type=str, default="lib.txt")
    # parser.add_argument("--label","-l", metavar=':space + label,0 or 1', required=True, type=str)
    return parser.parse_args()

def main():
  args = parse_args()
  #存放原始图片地址
  # image_path = 'C:\code\OpenLabeling-master\main\input'
  #读取图片文件，并将图片地址、图片名和标签写到txt文件中
  # out_txt_path= 'C:\code\OpenLabeling-master\main\input\dir.txt'
  file_list = [] #建立列表，用于保存图片信息
  write_file = open(args.out_txt_path, "a") #以只写方式打开write_file_name文件
  for file in os.listdir(args.image_path): #file为current_dir当前目录下图片名
      if file.endswith(".lib"): #如果file以jpg结尾
          write_name = file #文件名
          # """ 代码片段功能：指定路径下创建同图片同名的空txt文件 """
          # txtsavedPath="../datasets/wellCover_new/txt/"
          # file_name = write_name[:-4]+'.txt'
          # open(txtsavedPath+file_name, "w")
          # """ --------------------------------------------- """
          file_list.append(write_name) #将write_name添加到file_list列表最后
          sorted(file_list) #将列表中所有元素随机排列
          number_of_lines = len(file_list) #列表中元素个数.
  
  #将文件名称写入txt文件中，逐行写入
  for current_line in range(number_of_lines):
        write_file.write(file_list[current_line]+'\n') #写入的名称不包含后缀
      # write_file.write(args.image_path+'/'+file_list[current_line] + args.label + '\n') #生成resnet18二分类所需标签
  
  #关闭文件
  write_file.close()

if __name__ == '__main__':
    main()