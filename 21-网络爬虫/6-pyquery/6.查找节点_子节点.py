#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-01 09:28:06 
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
         <li class="item-2"><span>last item</span></li>
     </ul>
     <p>这是一个段落1</p>
     <p>这是一个段落2</p>
</div>
'''

doc = pq(html) 
li = doc('li')
print(li)
#所有子孙节点
print(li.find('span'))
print('*'*40)
#只查找子节点，不往下继续遍历
print(li.children())
print('-'*40)
print(li.children('span'))

