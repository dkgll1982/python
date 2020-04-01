#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-01 09:28:02 
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
li_list = doc('ul > li.item-0.active,ul > li.item-1.active')   
print('选择节点：',str(li_list)) 
#遍历节点调用items方法
for index,li in enumerate(li_list.items(),start=1):
    print('第%d个节点'%index,li,type(li))
    print('兄弟节点：',li.siblings())
    print('*'*40)