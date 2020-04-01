#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: guojun
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd
# @Site: https://user.qzone.qq.com/350606539/main
# @Date: 2020-03-31 12:47:02
# @Remark: 人生苦短，我用python！

from pyquery import PyQuery as pq
html = '''
    <div href="wrap">
        hello nihao
        <p>单独</p>
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com"><a>asdadasdad12312</a></link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
            <link  href="http://asda3.com">aas</link>
        </ul>
        <b>全部</b>
        <p><a href='#'>链接</a></p>
        <p><div><a href='#'>链接2</a></div></p>
    </div>
'''

doc = pq(html)

#E[attr ^="val"]  以 val 开头的,E[attr $="val"]  以 val 结尾的
its = doc("link[class^='active']")
print(its)

# E[attr *="val"],里面只要包含着 val 就可以选中
its = doc("link[class*='v']")
print(its)

#E + F 下一个满足条件的兄弟元素节点。也就是说 可以选择下一个兄弟元素节点，但是呢，必须是满足条件的，条件就是+后面的
#div + .box 意思就是 我要选择 div 的兄弟节点，而且必须是 类名是box 的。
its = doc("link + .movie1")
print(its)

its = doc("link ~ link[class*='v']")
print(its)

#分组选择
its = doc("p,b")
print(its)

#后代选择器
its = doc("p a")
print(its)

#后代选择器
its = doc("p>a")
print(its)