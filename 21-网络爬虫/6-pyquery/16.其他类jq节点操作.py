#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-01 09:28:02 
# @Remark: 人生苦短，我用python！
# 参考链接：https://pyquery.readthedocs.io/en/latest/manipulating.html

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
     <p>这是一个段落2<input type="button"/></p>
     <div><input type="file"/></div>
</div>
'''

d = pq(html)   
d('p:eq(0)').append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>') 
print(d('p:eq(0)'))
print('-'*40)
d('p:eq(0)').prepend(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>') 
print(d('p:eq(0)'))
span = d('li:eq(2) .bold')
print(span)  
#Prepend or append an element into an other:
d('p:eq(0)').prependTo(span)
print(span)