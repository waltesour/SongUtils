
# coding=utf-8
import os, random, shutil
"""------------脚本功能:从路径A中随机选取一定比例的图片移动到路径B中----------------"""
# if __name__ == '__main__':
#     ori_path  = 'C:/code/datasets/expressCount/images/train'  # 所有图片原始的路径
#     split_Dir = 'C:/code/datasets/expressCount/images/val'  # 划出的图片要新存储的路径
#     ratio = 0.2  # 抽取比例
#     pathDir = os.listdir(ori_path)
#     filenumber = len(pathDir)
#     picknumber = int(filenumber * ratio)  # 按照rate比例从文件夹中取一定数量图片
#     sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
#     for name in sample:
#         shutil.move(os.path.join(ori_path, name), os.path.join(split_Dir, name))

# """------------脚本功能:基于上一个脚本的划分结果，对label再进行划分----------------"""
if __name__ == '__main__':
    ori_path = 'C:/code/datasets/expressCount/images/val'  # 划出的 “图片” 所在的路径
    ori_label_path = 'C:/code/datasets/expressCount/labels/train'  # 所有 “图片标签” 原始的路径
    split_label_Dir = 'C:/code/datasets/expressCount/labels/val'  # 划出的 “图片标签” 要新存储的路径
    pathDir = os.listdir(ori_path)
    for name in pathDir:
        shutil.move(os.path.join(ori_label_path, name[:-4]+'.txt'), os.path.join(split_label_Dir, name[:-4]+'.txt'))