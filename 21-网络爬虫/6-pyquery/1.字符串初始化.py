#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-29 21:48:30 
# @Remark: 人生苦短，我用python！
from pyquery import PyQuery as pq

html = '''
<div id="wrap">
    <ul class="s_from">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
     <p>这是一个段落1</p>
     <p>这是一个段落2</p>
</div>
'''

doc = pq(html)
print(doc)
print(type(doc))
print(doc('li'))

print('*'*40)
print(doc("#wrap .s_from li.item-1"))
item = doc('#wrap')
li = item.find('li.item-0')
print(li)
print('-'*40)
child = item.children('p')
print(child)
for item in child.items():  
    print(item.html())
     