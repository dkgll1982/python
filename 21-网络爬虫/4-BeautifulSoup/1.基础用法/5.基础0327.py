#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-22 11:43:08 
# @Remark: 人生苦短，我用python！

from bs4 import BeautifulSoup,NavigableString

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body><p class="title">ooooooo<b><!--Hey, buddy. Want to buy a used parser?--></b>yyyyyyyyy</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister sister2" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser')
#print(soup.prettify())
# 不同解析器的区别
print(BeautifulSoup("<a></p>", "lxml"))
print(BeautifulSoup("<a></p>", "html.parser"))
print(BeautifulSoup("<a></p>", "html5lib"))
print(soup.head)
print(soup.a)
print(soup.title.name,soup.title.string,soup.a.parent.name)
a = soup.find(id="link3")
print([x.get('href') for x in soup.find_all('a')])
print(a.name,a.attrs,a['id'],a.attrs['class'])
print(soup.a['class'])

# tag的属性可以被添加,删除或修改. 再说一次, tag的属性操作方法与字典一样
soup.a['class']=['class1','red','hot']
print(soup.a)
print(soup.p.string,type(soup.p.string))
soup.b.string.replace_with("uuuuuuu")
# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, 
# 以下.string 的输出结果是 None <class 'NoneType'>
print(soup.p.string,type(soup.p.string))
#取子节点的信息
print(list(soup.p.children)[0])

#父节点
p = soup.find('a').parent
print(p.contents)
#子节点
for c in p.children:
    print('sub:',c)
#子孙节点
for c in p.descendants:
    print('ssub:',c)
    
#所有父辈节点（从里往外）   
for parent in p.parents:
    if parent is None:
        print(parent)
    else:
        print('父辈:',parent.name)

#兄弟节点
a = soup.find(id='link2')
print(a,a.next_sibling,a.previous_sibling)
for x in a.next_siblings:
    print(x)
    
#前后节点（不分层次）
#与 .next_sibling .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次  
t = soup.p 
print(t)
print('[',t.next_element,type(t.next_element),isinstance(t.next_element, NavigableString),']')
print('[',t.previous_element,type(t.previous_element),']')

for x in t.previous_elements:
    print('>>>[',x,']')
    
print(soup.a)