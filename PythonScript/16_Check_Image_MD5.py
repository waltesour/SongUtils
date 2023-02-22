# 将一个文件夹中完全相同的图片挑出来
import os
import shutil
from tqdm import tqdm
import hashlib

def getmd5(file):
    if not os.path.isfile(file):
        return
    fd = open(file,'rb')
    md5 = hashlib.md5()
    md5.update(fd.read())
    fd.close()
    return md5.hexdigest()
#定义文件夹路径
original_path = r'E:\telecom\data\4_14\head'
move_path = r'E:\telecom\data\4_14\head_move'
copy_path = r'E:\telecom\data\4_14\head_copy'

#创建移动与复制的文件夹
os.makedirs(move_path,exist_ok=True)
os.makedirs(copy_path,exist_ok=True)
dirc = {}
images = os.listdir(original_path)


for image in tqdm(images):
    image_md5 = getmd5(os.path.join(original_path,image))

    if(dirc.__contains__(image_md5)):
        shutil.copy(os.path.join(original_path, image), os.path.join(copy_path, image))
        shutil.copy(os.path.join(original_path, dirc[image_md5]), os.path.join(copy_path,dirc[image_md5] ))
        shutil.move(os.path.join(original_path, image), os.path.join(move_path, image))
    else:
        dirc[image_md5] = image

