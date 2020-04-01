#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-03-31 12:54:00
# @Remark: 人生苦短，我用python！
# 参考链接：https://www.cnblogs.com/xuan52rock/p/4416228.html
# CSS3选择器；https://www.cnblogs.com/yanggeng/p/11188285.html

from pyquery import PyQuery as pq
html = '''
    <div href="wrap"> 
        <p>第一个子元素</p>
        <h1>第二个子元素</h1>
        <span>第三个子元素</span>
        <span>第四个子元素</span>
    </div>
'''

doc = pq(html) 
#字面意思：选择是第一个子元素的标签
print(doc("p:first-child"))
print(doc("h1:first-child"))
#同理，last-chlid是选择最后一个子元素的标签
print(doc("span:last-child"))
print(doc("p:last-child"))

print(doc('p:first-of-type'))
print(doc('span:first-of-type'))
print(doc('span:last-of-type'))
print('*'*40)

#匹配父元素的所有子元素中唯一的那个子元素
print(doc('span:only-of-type'))
print(doc('p:only-of-type'))

#:first-child 匹配的是某父元素的第一个子元素，可以说是结构上的第一个子元素。
#:first-of-type 匹配的是该类型的第一个，类型是指什么呢，就是冒号前面匹配到的东西，
# 比如 p:first-of-type，就是指所有p元素中的第一个。这里不再限制是第一个子元素了，只要是该类型元素的第一个就行了，
# 当然这些元素的范围都是属于同一级的，也就是同辈的。
#同样类型的选择器 :last-child  和 :last-of-type、:nth-child(n)  和  :nth-of-type(n) 也可以这样去理解。