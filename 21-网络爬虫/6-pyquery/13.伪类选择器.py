#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-03-31 12:54:00
# @Remark: 人生苦短，我用python！

from pyquery import PyQuery as pq
html = '''
    <div href="wrap">
        hello nihao
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com"><a>helloasdadasdad12312</a></link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com" disabled></link>
        </ul>
    </div>
    <div> 
        <li>发发发</li>
    </div>
    <ul>
        <li>单独的</li>
    </ul>
    <ul>
        <li>历史上是</li>
    </ul>
'''

doc = pq(html)
its = doc("link:first-child")
print('第一个标签:%s' % its)
its = doc("link:last-child")
print('最后一个标签:%s' % its)
its = doc("link:nth-child(2)")
print('第二个标签:%s' % its)
its = doc("link:gt(0)")  # 从零开始
print("获取0以后的标签:%s" % its)
its = doc("link:lt(2)")  # 从零开始
print("获取2以前的标签:%s" % its)
its = doc("link:nth-child(2n-1)")
print("获取奇数标签:%s" % its)
its = doc("link:nth-last-child(2)")
print("获取倒数的第二个标签:%s" % its)
its = doc("link:contains('hello')")
print("获取文本包含hello的标签:%s" % its)
#选择所有没有子元素的p元素
its = doc("link:empty")
print("选择所有没有子元素的link元素:%s" % its) 
#选择所有ul以外的标签
its = doc(":not(ul)")
print("选择所有ul以外的标签:%s" % its) 
#选择，父元素下的 独生子，也就是说，看父元素下面的子元素，是不是仅有一个。是的话，那就选中这个独生子
its = doc('li:only-child')
print("选择仅有一个子元素的标签:%s" % its) 
#在父元素下面寻找 第一个所匹配的子元素
#与first_child的区别：
its = doc('link:first-of-type')
print("选择仅有一个子元素的标签:%s" % its) 