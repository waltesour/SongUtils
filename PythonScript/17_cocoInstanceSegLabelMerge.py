import json
import os
from pycocotools.coco import COCO
import copy
'''
脚本功能:只能将两个coco类型的json标注结果合并到一起
'''
# 需要合并的json文件路径
path = 'C:/code/datasets/expressData/20221227/ann/'
# 合并后的json文件名
new_json2 = 'C:/code/datasets/expressData/20221227/all.json'
# ID重拍后的json文件名
final_json2 = 'C:/code/datasets/expressData/instanceSegCOCO/COCO.json'
entries = os.listdir(path)
entries.sort()
coco = COCO(path + entries[0])
main = open(path + entries[0])
main = json.load(main)

# 第一个json文件 image的数量
main_image_number = len(main['images'])
# 第一个json文件 annotation的数量
main_annotation_number = len(main['annotations'])
# 第一个json文件图片ID的最大值(如果拆分过标注文件,该最大值和图像数目不同)
main_imageID_maxIndex = max(coco.getImgIds())
# 第一个json文件标注轮廓数目ID的最大值(如果拆分过标注文件,该最大值和总轮廓数目也不同)
main_AnnID_maxIndex = max(coco.getAnnIds())


# 这里获得所有的图像信息和标注ann信息
for entry in entries[1:]:
    file = open(path + entry)
    file = json.load(file)
    # newjsonAddIndex=1
    for i in file['images']:
        i['id']=main_imageID_maxIndex + i['id']
        main['images'].append(i)

    for i in file['annotations']:
        i['image_id']=i['image_id']+main_imageID_maxIndex
        i['id']=i['id']+main_AnnID_maxIndex
        main['annotations'].append(i)
print(len(main['images']))
imgNameStartIndex=0
# pre_name="youzheng_part3_hangye/youzheng_part3_hangye/part3/part3"
# imgNameStartIndex = len(pre_name)+2
for i in range(0,len(main['images'])):
    main['images'][i]['file_name']=main['images'][i]['file_name'][imgNameStartIndex:] #AI平台标注出来的图片路径多了很多前缀
with open(new_json2, 'w') as outfile:
    json.dump(main, outfile)

#对新的json文件的id(ann的id和图像id)进行从0开始的重新排序
temp = copy.deepcopy(main) #深拷贝
annnewId=1
for i in range(len(main['images'])):
    main['images'][i]['id'] = i 
    #这里对标注信息的id和对应图像id进行修改
    for j in range(len(main['annotations'])):
        if(temp['annotations'][j]['image_id']==temp['images'][i]['id']):#标注文件中找到对应图像索引
            main['annotations'][j]['image_id']=i
            main['annotations'][j]['id'] = annnewId
            annnewId=annnewId+1

# 保存到新的json
json.dump(main,open(final_json2,'w'),indent=4)
