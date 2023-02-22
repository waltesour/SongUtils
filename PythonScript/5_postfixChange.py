# python批量更换后缀名
import os
import shutil
foldName='C:/code/datasets/crossRoad/IMG_3510_Img'
os.chdir(foldName)
# 列出当前目录下所有的文件
files = os.listdir('.')
for filename in files:
	portion = os.path.splitext(filename)
	# 如果后缀是.jpg
	if (portion[1] == ".jpg") & (int(portion[0])>414) & (int(portion[0])<626):
		new_name=portion[0]+'.xml' #为文件赋予新名字
		shutil.copyfile('C:/code/datasets/crossRoad/IMG_3510_Img/410.xml',os.path.join(foldName,new_name)) #复制并重命名文件
		# # 重新组合文件名和后缀名
		# newname = portion[0] + ".txt" 
		# os.rename(filename,newname)  

		