#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-10 17:43:34 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-10 17:43:34 
# @Software: vscode 

from bs4 import BeautifulSoup
import re
#详细用法参见中文文档：https://beautifulsoup.readthedocs.io/zh_CN/latest/
#其他参考：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#beautifulsoup-new-string-new-tag

html = '<html>\
            <head>\
                <title>我是标题</title>\
            </head>\
            <body>\
                <b id =\'b1\'>强调</b>\
                <h1 align=\'center\'>这是标题</h1>\
                <p class="p"> 段落1<h4>那是一条神奇的天路 </h4>    \
                    段落2<h4>带我们走进人间天堂 </h4>    \
                    段落3<h4  align=\'left\'>青稞酒酥油茶会更加香甜</h4> \
                    段落4<h4>幸福的歌声传遍四方  </h4>   \
                    段落5<h4>幸福的歌声传遍四方 </h4>    \
                </p>  \
                <div class="div">\
                    <a id ="a1" class="a">图片1<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" /></a>\
                    <a id ="a2" class="a">图片2<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3000f11f034f78f0840b9df149300a83/03087bf40ad162d9393e0d5711dfa9ec8b13cdad.jpg" /></a>\
                    <a class="a">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>\
                </div>\
            </body>\
        </html>'        
soup = BeautifulSoup(html,'lxml')
# recursive 参数 
print(soup.div("img")) 
# <img>标签在 <div> 标签下, 但并不是直接子节点, <a> 标签才是直接子节点. 
# 在允许查询所有后代节点时 Beautiful Soup 能够查找到 <img> 标签. 
# 但是使用了 recursive=False 参数之后,只能查找直接子节点,这样就查不到 <img> 标签了.
# 只有 find_all() 和 find() 支持 recursive 参数.
print(soup.div("img", recursive=False))
#soup.find_all('title', limit=1) 等价于 soup.find('title')
print('----',soup.p.find_next_sibling())
for x in soup.p.find_next_siblings():print('=>',x)
for x in soup.p.find_previous_siblings():print('-->',x)

for x in soup.body.find_all_next(string=True):
    if x.strip() is not None and x !=' ':
        print('++>%s'%(x.strip()))
        
for x in soup.div.find_all_previous(string=True):
    if x.strip() is not None and x !=' ':
        print('=>%s'%(x.strip()))
#CSS选择器
#通过tag标签逐层查找:
print(soup.select("div a img"))
#找到某个tag标签下的直接子标签
print(soup.select("div >a"))
#通过tag的id查找:
print(soup.select("#a1"))
#通过CSS的类名查找:
print(soup.select(".p"))
#同时用多种CSS选择器查询元素:
print(soup.select(".div,#b1"))
#通过是否存在某个属性来查找:
print(soup.select("[align]"))
#通过属性的值来查找:
print(soup.select("[align=left]"))
#返回查找到的元素的第一个
print(soup.select_one("div >a"))

#修改文档树
tag = soup.b
tag.name = "blockquote"
tag['class'] = 'verybold'
tag['id'] = 1
#修改 .string
tag.string='文本也改了吧'
print(tag)
print("body的下一个标签:",soup.body.find_next())
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

del tag['class']
del tag['id']
print(tag)
#append()
#创建一个tag最好的方法是调用工厂方法 BeautifulSoup.new_tag() :
new_tag = soup.new_tag("a",href='/')
new_tag['class']='Foo'
new_tag.string = "Link text."
soup.div.append(new_tag)
soup.find_all('a')[3].append('Bar')
print(soup.find_all('div'))