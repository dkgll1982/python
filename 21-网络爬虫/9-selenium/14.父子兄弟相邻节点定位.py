#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-28 14:31:46 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 备注：节点定位

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#请求本地页面的源码如下：
"""
<!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <li class="item-"><a href="link.html">first item</a></li>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        
        <div class="div">
            <p lang="en" style="width:100px;background:pink;cursor:pointer" onclick="window.open('http://www.taobao.com', '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');">单打独斗</p>
            <p lang="en-us" onclick="window.open('localhost:8080/openVone/2.html', '_blank')">点点滴滴</p>
            <p lang="en-us" onclick="http://www.163.com/">163</p>
            <p lang="en-us" onclick="http://localhost:8080/openVone/3.html">点点滴滴2</p>
            <p lang="en-us" onclick="http://www.baidu.com">点点滴滴3</p>
            <a id ="a0" class="hello world">图片0<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" />链接以a开头的标签链接</a>
            <a id ="a1" class="a" href='top50'>图片1<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" /></a>
            <a id ="a2" class="a" target="_blank">图片2<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3000f11f034f78f0840b9df149300a83/03087bf40ad162d9393e0d5711dfa9ec8b13cdad.jpg" /></a>
            <a class="a" href="http://www.sina.com" target="_top">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>
        </div>
    </body>
    </html>
"""

#本地服务调试页面
url = 'http://127.0.0.1:8080/openVone/1.html'
chrome = webdriver.Chrome()
chrome.get(url)

#与xpath轴的用法相同
result = chrome.find_element_by_xpath("//a[@class='hello world']/parent::div")
tag_name = result.tag_name
class_name = result.get_attribute('class')
print(tag_name,' ',class_name)     
              
body = result.find_element_by_xpath('parent::*')
print(body.tag_name)

#继续以上一个查询的部分进行查询
link_list = result.find_elements_by_xpath('./a[(@href)]')
for link in link_list:
    href= link.get_attribute('href')
    print(link.text,'',href)


