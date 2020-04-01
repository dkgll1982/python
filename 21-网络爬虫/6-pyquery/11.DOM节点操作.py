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
        <ul class="s_from">
            asdasd
            <link class='active1 a123' href="http://asda.com"><a>asdadasdad12312</a></link>
            <link class='active2' href="http://asda1.com">asdadasdad12312</link>
            <link class='movie1' href="http://asda2.com">asdadasdad12312</link>
            <link  href="http://asda3.com">aas</link>
        </ul>
    </div>
'''

doc = pq(html)
its = doc("link").items()
for it in its:
    # addClass removeClass 添加，移除class标签
    print("添加:%s" % it.addClass('active1'))
    print("移除:%s" % it.removeClass('active1'))

print('='*40)

its = doc("link").items()
for it in its:
    # attr 为获取/修改属性 css 添加style属性
    print("修改:%s" % it.attr('class', 'active'))
    print("添加:%s" % it.css('font-size', '14px'))
    
print('*'*40)

its = doc("div")
print('移除前获取文本结果:\n%s' % its.text())
it = its.remove('ul')
print('移除后获取文本结果:\n%s' % it.text())
