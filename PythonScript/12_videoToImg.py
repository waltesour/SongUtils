"""------------从视频读取帧保存为图片----------------"""
import cv2
import os

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

videoPath='C:/code/datasets/expressCount/6.mp4'
# imgPath=videoPath[:-4]+'_Img/'
# mkdir(imgPath)
imgPath = 'C:/code/datasets/expressCount/1_Img/'
cap = cv2.VideoCapture(videoPath)
print("frame rate is: ",cap.get(5))# 获取帧速度
print("frame sum is: ",cap.get(7))# 获取总帧数
c=2649                              #文件名从0开始
while(1):
    # get a frame
    count=0
    while(count!=100):
        count=count+1
        ret, frame = cap.read()
    if ret==False:
        break
    # show a frame
    # cv2.imshow("capture", frame)
    cv2.imwrite(imgPath + str(c) + '.jpg',frame) #存储为图像
    c=c+1
    # if cv2.waitKey(100) & 0xFF == ord('q'):
    #     break
cap.release()
cv2.destroyAllWindows()
