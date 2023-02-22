'''实例分割coco标注结果可视化'''
import os

from pycocotools.coco import COCO
from skimage import io
from matplotlib import pyplot as plt
import pandas as pd
# # all
json_file = r'C:/code/datasets/expressData/20221227/train.json'
dataset_dir = r'C:/code/datasets/expressData/20221227/train/'
# part
# json_file = r'C:/code/datasets/expressData/expressSeg_part1_cocolabel/annotations/instances_val2017.json'
# dataset_dir = r'C:/code/datasets/expressData/expressSeg_part1_cocolabel/val2017/'
coco = COCO(json_file)

'''只返回包含指定标签类别目标的图像名称'''
# catIds = coco.getCatIds(catNms=['zhixiang','ruanbao','madai','other']) # 按照指定类别返回图片ID
# imgIds = coco.getImgIds(catIds=catIds ) # 图片id，许多值

'''返回所有图像名称'''
imgIds = coco.getImgIds() # 所有图片id
AnnIds = coco.getAnnIds() # 所有标注目标的id(一个轮廓一个id)
'''将图片ID保存到本地xls'''
# df = pd.DataFrame(imgIds, columns=['imgID'])
# df.to_excel("C:/code/datasets/expressData/expressSeg_part1_cocolabel/cocoann.xls", index=False)
print("useful img Num:",len(imgIds))
'''将标签绘制到图像上保存'''
for i in range(len(imgIds)):
    img = coco.loadImgs(imgIds[i])[0]
    I = io.imread(dataset_dir + img['file_name'])
    plt.imshow(I) #绘制图像，显示交给plt.show()处理
    # annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None) # 返回图片中指定类别的标注信息
    annIds = coco.getAnnIds(imgIds=img['id'])
    anns = coco.loadAnns(annIds)
    coco.showAnns(anns)
    anns.clear()
    annIds.clear()
    # plt.show() #显示图像
    plt.savefig('img_new/'+str(i)+".jpg")
    plt.close()