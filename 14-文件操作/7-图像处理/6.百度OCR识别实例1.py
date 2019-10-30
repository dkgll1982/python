# -*- coding:utf-8 -*-
#参考链接：https://blog.csdn.net/weixin_42544006/article/details/100510545

from aip import AipOcr
APP_ID = '9897191'
API_KEY = 'fZGH6al0ADgaxgabRlf8aGFX'
SECRET_KEY = 'AdGjnwvasv7pofwflH9Bf3ipGVnZ2Z7d' 
 
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
 
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
 
""" 调用通用文字识别, 图片参数为本地图片 """
image = get_file_content(r'C:\Users\dkgll\Desktop\3.jpg')
client.basicGeneral(image)
 
""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
 
""" 带参数调用通用文字识别, 图片参数为本地图片 """
# 通用文字识别 50000次/天免费
a = client.basicGeneral(image,)
# 通用文字识别（高精度版） 500次/天免费
b = client.basicAccurate(image)
print(a)
print(b)
 
 
# """ 调用通用文字识别, 图片参数为远程url图片 """
url = "http://www.xiaobaixitong.com/d/file/help/2018-08-06/f15ce5d652d8da38e9e0e384f35b39d7.png"
 
""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
 
""" 带参数调用通用文字识别, 图片参数为远程url图片 """
aa = client.basicGeneralUrl(url, options)
print(aa)