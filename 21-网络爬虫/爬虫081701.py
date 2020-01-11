#!/usr/bin/python
# coding:utf-8
# 实现一个简单的爬虫，爬取百度贴吧图片
import urllib.request
import re
import os

# 根据url获取网页html内容
def getHtmlContent(url):
    page = urllib.request.urlopen(url)
    return page.read()

# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):
    # 解析jpg图片url的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')  # 注：这里最后加一个'width'是为了提高匹配精确度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg, html)
    return jpgs

# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl, fileName):
    #参数url:传入的网址，网址必须得是个字符串 
    #参数filename:指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据)
    urllib.request.urlretrieve(imgUrl, fileName)

# 批量下载图片，保存到F盘zdl文件夹
def batchDownloadJPGs(imgUrls, path=r'C:\Users\dkgll\Downloads\drugs\\'):
    # 用于给图片命名
    count = 1
    for url in imgUrls:
        #downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        downloadJPG(url, ''.join([path,os.path.basename(url)]))
        print ('正在下载第'+str(count)+'张,'+ os.path.basename(url))
        count = count + 1

# 封装：从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    html=html.decode('utf-8')  
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)
 
if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)