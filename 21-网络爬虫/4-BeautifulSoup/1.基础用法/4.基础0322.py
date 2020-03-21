#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-22 11:43:08 
# @Remark: 人生苦短，我用python！

from bs4 import BeautifulSoup,NavigableString
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body><h1></h1>标题<p class="title">ooooooo<b><!--Hey, buddy. Want to buy a used parser?--></b>yyyyyyyyy</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a data-foo='d1' data_hub='df1d' href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a data-foo='d2' data_hub='df2' href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a data-foo='d3' data_hub='df3d' href="http://example.com/tillie" class="sister sister2" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
<div>底部</div>
""" 

soup = BeautifulSoup(html_doc,'html.parser') 
tag = soup.b

tag.name = "blockquote"
tag['class'] = 'verybold'
tag['id'] = 1
print(tag)
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

del tag['class']
del tag['id']
print(tag)
# <blockquote>Extremely bold</blockquote>   
print(soup)

print(soup.a,soup.a.contents)
soup.a.append("Bar")
soup.a.append("loo")
print(soup.a,soup.a.contents)

# 如果想添加一段文本内容到文档中也没问题,可以调用Python的 append()方法或调用 NavigableString的构造方法:
tag = soup.blockquote
tag.append("Hello")
new_string = NavigableString(" there")
tag.append(new_string)
print(tag,tag.contents) 

print('-'*60)
# 创建一个tag最好的方法是调用工厂方法 BeautifulSoup.new_tag() :
# 第一个参数作为tag的name,是必填,其它参数选填
new_tag = soup.new_tag("a", href="http://www.example.com")
p = soup('p')[1]
p.append(new_tag)
print(p) 

new_tag.string = "Link text."
print(p) 

print('>'*60)
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,'lxml')
tag = soup.a

# Tag.insert()方法与Tag.append()方法类似,区别是不会把新元素添加到父节点.contents属性的最后,
# 而是把元素插入到指定的位置.与Python列表总的.insert()方法的用法下同:
tag.insert(2, "but did not endorse ")
print(tag)
# <a href="http://example.com/">I linked to but did not endorse <i>example.com</i></a>
print(tag.contents) 

print('<'*60)
# insert_before() 方法在当前tag或文本节点前插入内容:
soup = BeautifulSoup("<b>stop</b>",'lxml')
tag = soup.new_tag("i")
tag.string = "Don't"
soup.b.string.insert_after(tag) 
print(soup) 

tag = soup.new_tag("i")
tag.string = "后边"
soup.b.insert_after(tag) 
print(soup) 

tag = soup.new_tag("i")
tag.string = "前边"
soup.b.insert_before(tag) 
print(soup) 

print('='*40+'>')
# PageElement.wrap() 方法可以对指定的tag元素进行包装 [8] ,并返回包装后的结果:
soup = BeautifulSoup("<p>I wish I was bold.</p>",'lxml')
soup.p.string.wrap(soup.new_tag("b"))
# <b>I wish I was bold.</b>
print(soup)
soup.p.wrap(soup.new_tag("div"))
# <div><p><b>I wish I was bold.</b></p></div>
print(soup)

# Tag.unwrap() 方法与 wrap() 方法相反.将移除tag内的所有tag标签,该方法常被用来进行标记的解包:
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,'lxml')
# 如果只想得到tag中包含的文本内容,那么可以调用 get_text()方法
# 这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回:
print(soup.get_text())
# 可以通过参数指定tag的文本内容的分隔符:
print(soup.get_text(' | '))
# 还可以去除获得文本内容的前后空白:
print(soup.get_text(' | ',strip=True))

a_tag = soup.a

a_tag.i.unwrap()
print(a_tag)