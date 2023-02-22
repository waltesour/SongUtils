# 将txt内的文件行数随机打乱顺序
import random
out = open("trainNew.txt",'w')  #打乱顺序后的新txt
lines=[]
with open("train.txt", 'r') as infile:  #打乱顺序前的txt
    for line in infile:
        lines.append(line)
    random.shuffle(lines)
    for line in lines:
        out.write(line)