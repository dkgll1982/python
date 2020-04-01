#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-03-31 12:47:02
# @Remark: 人生苦短，我用python！

from pyquery import PyQuery as pq
html = '''
   <ul>
    <li>List item 1
        <ol>
        <li>List item 1-1</li>
        <li>List item 1-2</li>
        <li>List item 1-3
            <ol>
            <li>List item 1-3-1</li>
            <li>List item <em>1-3-2</em></li>
            <li>List item 1-3-3</li>
            </ol>
        </li>
        <li>List item 1-4</li>
        </ol>
    </li>
    <li>List item 2</li>
    <li>List item 3</li>
  </ul>
'''

pq = pq(html)
#有关后代选择器有一个易被忽视的方面，即两个元素之间的层次间隔可以是无限的。
#例如，如果写作 ul em，这个语法就会选择从 ul 元素继承的所有 em 元素，而不论 em 的嵌套层次多深。
print(pq('ul em')) 

#后代结合子元素选择器
print(pq('ul ol>li'))