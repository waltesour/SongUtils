"""-------------使用imgaug对图像和xml标注结果进行数量上的扩增------------"""
"""-------------使用labelImg虚拟环境"""
import xml.etree.ElementTree as ET
import pickle
import os
from os import getcwd
import numpy as np
from PIL import Image

import imgaug as ia
from imgaug import augmenters as iaa

ia.seed(1)

def read_xml_annotation(root, image_id):
    in_file = open(os.path.join(root, image_id),encoding='UTF-8')
    tree = ET.parse(in_file) #ET.parse 解析xml文档
    root = tree.getroot()
    bndboxlist = []

    # 读取到xml文件中所有物体的坐标信息
    for object in root.findall('object'):  # 找到root节点下的所有country节点
        bndbox = object.find('bndbox')  # 子节点下节点rank的值

        xmin = int(bndbox.find('xmin').text)
        xmax = int(bndbox.find('xmax').text)
        ymin = int(bndbox.find('ymin').text)
        ymax = int(bndbox.find('ymax').text)
        # print(xmin,ymin,xmax,ymax)
        bndboxlist.append([xmin,ymin,xmax,ymax])
        # print(bndboxlist)

    bndbox = root.find('object').find('bndbox')
    return bndboxlist
# (506.0000, 330.0000, 528.0000, 348.0000) -> (520.4747, 381.5080, 540.5596, 398.6603)
def change_xml_annotation(root, image_id, new_target):
    new_xmin = new_target[0]
    new_ymin = new_target[1]
    new_xmax = new_target[2]
    new_ymax = new_target[3]

    in_file = open(os.path.join(root, str(image_id) + '.xml'))  # 这里root分别由两个意思
    tree = ET.parse(in_file)
    xmlroot = tree.getroot()
    object = xmlroot.find('object')
    bndbox = object.find('bndbox')
    xmin = bndbox.find('xmin')
    xmin.text = str(new_xmin)
    ymin = bndbox.find('ymin')
    ymin.text = str(new_ymin)
    xmax = bndbox.find('xmax')
    xmax.text = str(new_xmax)
    ymax = bndbox.find('ymax')
    ymax.text = str(new_ymax)
    tree.write(os.path.join(root, str(image_id) + "_aug" + '.xml'))

def change_xml_list_annotation(root, image_id, new_target,saveroot,newxmlName):

    in_file = open(os.path.join(root, str(image_id) + '.xml'),encoding='UTF-8')  # 这里root分别由两个意思
    tree = ET.parse(in_file) #ET.parse函数可以对.xml文件进行解析
    xmlroot = tree.getroot()
    index = 0
    # 找到.xml文件中的object关键词
    for object in xmlroot.findall('object'):  # 找到root节点下的所有country节点
        bndbox = object.find('bndbox')  # 子节点下节点rank的值

        # xmin = int(bndbox.find('xmin').text)
        # xmax = int(bndbox.find('xmax').text)
        # ymin = int(bndbox.find('ymin').text)
        # ymax = int(bndbox.find('ymax').text)

        new_xmin = new_target[index][0]
        new_ymin = new_target[index][1]
        new_xmax = new_target[index][2]
        new_ymax = new_target[index][3]

        xmin = bndbox.find('xmin')
        xmin.text = str(new_xmin)
        ymin = bndbox.find('ymin')
        ymin.text = str(new_ymin)
        xmax = bndbox.find('xmax')
        xmax.text = str(new_xmax)
        ymax = bndbox.find('ymax')
        ymax.text = str(new_ymax)

        index = index + 1

    tree.write(os.path.join(saveroot, newxmlName))


def mkdir(path):

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

if __name__ == "__main__":

    IMG_DIR = "C:/code/datasets/crossRoad/img" # 输入的影像文件夹路径
    XML_DIR = "C:/code/datasets/crossRoad/xml" # 输入的XML文件夹路径

    AUG_IMG_DIR = "C:/code/datasets/crossRoad/imgAug"  # 存储增强后的影像文件夹路径
    mkdir(AUG_IMG_DIR)

    AUG_XML_DIR = "C:/code/datasets/crossRoad/xmlAug" # 存储增强后的XML文件夹路径
    mkdir(AUG_XML_DIR)

    AUGLOOP = 1 # 每张影像增强的数量

    boxes_img_aug_list = []
    new_bndbox = []
    new_bndbox_list = []


    # 影像增强
    seq = iaa.Sequential([
        # iaa.Flipud(0.5),  #1 -- 50%的概率垂直翻转
        iaa.Fliplr(0.5),  #2 -- 50%的概率水平翻转
        # iaa.Multiply((0.5, 1.5)),  #3 -- change brightness, doesn't affect BBs（boundingBox?）
        # iaa.GaussianBlur(sigma=(0, 1.0)), #4 --  高斯模糊,使用高斯核的sigma取值范围在(0,3)之间
        # iaa.AdditiveGaussianNoise(scale=(10, 20)), #5 -- 加入额外的高斯噪声
        # 从图片边随机裁剪50~100个像素,裁剪后图片的尺寸和之前不一致
        # 通过设置keep_size为True可以保证裁剪后的图片和之前的一致
        # iaa.Crop(px=(50,100),keep_size=True),
        # iaa.LogContrast(gain=(0.6, 1.4)),
        # iaa.AllChannelsHistogramEqualization(),
        # iaa.CoarseDropout(0.08, size_percent=0.5),
        # iaa.AddToHueAndSaturation((-30, 30)),  # change their color
        # iaa.Cutout(),  # replace one squared area within the image by a constant intensity value
        iaa.Affine(scale=(0.5, 1.5)),
        iaa.Affine(
            translate_px={"x": 15, "y": 15},#偏移0-15个像素，新图片仍然和原尺寸相同，新出现的部分补黑边
            scale=(0.8, 1.2), #尺度在0.8-0.95倍之间进行缩小，新图片仍然和原尺寸相同，空白部分补黑边
            rotate=(-3, 3)  #角度在[-15，15]之间旋转
        ) # affects BBs
    ])
# os.walk返回三个信息：
# 1是正在遍历的文件夹本身
# 2是该文件夹中所有目录(子文件夹)的名字
# 3是该文件夹内所有文件的名字
    for root, sub_folders, files in os.walk(XML_DIR):

        for name in files:
            #读取该xml文件中所有目标的坐标信息
            bndbox = read_xml_annotation(XML_DIR, name)

            for epoch in range(AUGLOOP):
                seq_det = seq.to_deterministic()  # 保持坐标和图像同步改变，而不是随机

                # 读取图片
                img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.jpg'))
                img = np.array(img)

                # bndbox 坐标增强
                for i in range(len(bndbox)):
                    bbs = ia.BoundingBoxesOnImage([
                        ia.BoundingBox(x1=bndbox[i][0], y1=bndbox[i][1], x2=bndbox[i][2], y2=bndbox[i][3]),
                    ], shape=img.shape)

                    bbs_aug = seq_det.augment_bounding_boxes([bbs])[0] #这个函数应该是对坐标进行变换
                    boxes_img_aug_list.append(bbs_aug)

                    # new_bndbox_list:[[x1,y1,x2,y2],...[],[]]
                    new_bndbox_list.append([int(bbs_aug.bounding_boxes[0].x1),
                                            int(bbs_aug.bounding_boxes[0].y1),
                                            int(bbs_aug.bounding_boxes[0].x2),
                                            int(bbs_aug.bounding_boxes[0].y2)])
                # 存储变化后的图片
                image_aug = seq_det.augment_images([img])[0]
                newimgName=str(name[:-4]) + "_aug_" + str(epoch) + '.jpg'
                path = os.path.join(AUG_IMG_DIR, newimgName)
                # image_auged = bbs.draw_on_image(image_aug, thickness=0)
                Image.fromarray(image_aug).save(path)

                # 存储变化后的XML
                newxmlName=str(name[:-4] + "_aug_" + str(epoch) + '.xml')
                change_xml_list_annotation(XML_DIR, name[:-4], new_bndbox_list,AUG_XML_DIR,newxmlName)
                print('get new image: ',newxmlName)
                new_bndbox_list = []