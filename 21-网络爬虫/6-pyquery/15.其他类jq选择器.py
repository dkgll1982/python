#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-01 09:28:02 
# @Remark: 人生苦短，我用python！
# 参考链接：https://pyquery.readthedocs.io/en/latest/

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

doc = pq(html)  
# You can use some of the pseudo classes that are available in jQuery but that are not standard in css 
# such as :first :last :even :odd :eq :lt :gt :checked :selected :file:  
print(doc('li:eq(1)'),doc('li:eq(3)'))
print('*'*40)
print(doc('li:first'),doc('li:last'))
print('*'*40)
print(doc('li:odd'))
print('='*40)
print(doc('li:even'))
print('-'*40)
print(doc('li:lt(4)'))
print('+'*40)
print(doc('li:gt(4)'))
print('*'*40)
d = doc("li[class*='item']")
print(d)
print('#'*40)
li = doc('li:nth-child(4)')
print(li)

#更改属性
li.attr('id','aid')
print(li)
li.attr(id='adi2',class_='class2')
print(li) 

print('#'*40)
#该方法检查每个元素中指定的类。如果不存在则添加类，如果已设置则删除之。这就是所谓的切换效果。
print(doc('li:nth-child(3)').toggle_class('active'))
print(doc('li:nth-child(5)').toggle_class('active'))
print('#'*40)
print(doc('input:file'))
print('#'*40)
print(doc(':input'))
print('#'*40)
print(doc(':button'))