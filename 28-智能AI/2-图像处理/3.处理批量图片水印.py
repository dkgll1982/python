# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 上午11:31
# @Author  : xiaoxi
# @File    : watermark.py
import datetime
import os
from time import sleep
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont 
 
def watermark():
    dir_list,file_list=[],[]
    root_path = r'C:\Users\dkgll\Desktop\python目录\image\card_num'
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path) 
    for files in file_list: 
        font1 = ImageFont.truetype("‪C:\Windows\Fonts\simfang.ttf", size=22)
        font2 = ImageFont.truetype("‪C:\Windows\Fonts\simfang.ttf", size=22)
        im = Image.open(files)
        draw = ImageDraw.Draw(im)
        draw.text((im.size[0] / 2, im.size[1] / 2), u"这是一个测试图片", fill=(255, 0, 0), font=font1)
        draw.text((11, 11), u"等会去看电影", fill=(134, 153, 153), font=font2) 
        dir = "C:\\Users\\dkgll\\Desktop\\python目录\\syimg\\"
        name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = dir + os.path.split(files)[1]
        im.save(filename)
 
if __name__=='__main__':
    watermark()
    print("添加水印完成！")