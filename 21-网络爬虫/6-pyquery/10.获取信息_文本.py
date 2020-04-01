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
a_list = doc('ul a')   
print('选择节点：',str(a_list)) 
#遍历节点调用items方法
for index,a in enumerate(a_list.items(),start=1):
    #获取文本，此时会忽略掉节点内部所包含的所有HTML，只返回纯文字内容
    print('①：第{}个节点[{}]的内容="{}"'.format(index,a,a.text()))  
    #如果要获取这个节点内部的HTML文本，用html()方法
    print('②：第{}个节点[{}]的代码="{}"'.format(index,a,a.html()))  
    