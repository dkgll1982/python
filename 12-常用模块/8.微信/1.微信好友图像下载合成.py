#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-04-05 20:15:40
# @Remark: 人生苦短，我用python！
# 源码：https://github.com/gzm1997/wxImage

from numpy import *
import itchat
import urllib
import requests
import os
import PIL.Image as Image
from os import listdir
import math
import time

itchat.auto_login()
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]
nickname = friends[0]['NickName'] 
path = r'backup/微信/' + user
os.mkdir(path)

num = 0 
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(path + "/" + str(num) + ".jpg", 'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1
    # if(num == 200):              #设置读取的好友数量上限
    #     break

pics = listdir(path)
numPic = len(pics) 
eachsize = int(math.sqrt(float(640 * 640) / numPic)) 
numline = int(640 / eachsize)

toImage = Image.new('RGBA', (640, 640))  

x = 0
y = 0

# 缩小并拼接图片：
for i in pics:
    try:
        f_path = path + "/" + i 
		# 打开图片
        img = Image.open(path + "/" + i)
    except IOError:
        print("Error: {}没有找到或读取失败!".format(f_path))
    else:
		# 缩小图片
        img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
		# 拼接图片
        toImage.paste(img, (x * eachsize, y * eachsize))
        x += 1
        if x == numline:
            x = 0
            y += 1

new_path = r'backup\微信\{}_{}.png'.format(nickname,time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))) 
toImage.save(new_path)
# 发送给文件助手
itchat.send_image(new_path, 'filehelper')

print("{}的好友图像已合成并发送完毕！")
