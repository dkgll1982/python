#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-09 16:04
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : HTMLParse1.html
# @Software: PyCharm

import html.parser as h

class MyHTMLParser(h.HTMLParser):
    a_t=False
    #处理开始标签，比如<xx>
    def handle_starttag(self, tag, attrs):
        print("开始一个标签:",tag)
        if str(tag).startswith("title"):
            self.a_t=True
        for attr in attrs:
            print("属性值：",attr)
       # print()
    #处理<xx>data</xx>中间的那些数据
    def handle_data(self, data):
        if self.a_t is True:
            print("得到的数据: ",data)
    #处理结束标签，比如</xx>或者<……/>
    def handle_endtag(self, tag):
        self.a_t=False
        print("结束一个标签:",tag)
        print()

p=MyHTMLParser()
mystr = '''<head>
<meta charset="utf-8"/>
    <title>找找看 - 博客园</title>
    <link rel="shortcut icon" href="/Content/Images/favicon.ico" type="image/x-icon"/>
    <meta content="技术搜索,IT搜索,程序搜索,代码搜索,程序员搜索引擎" name="keywords" />
    <meta content="面向程序员的专业搜索引擎。遇到技术问题怎么办，到博客园找找看..." name="description" />
    <link type="text/css" href="/Content/Style.css" rel="stylesheet" />
    <script src="http://common.cnblogs.com/script/jquery.js" type="text/javascript"></script>
    <script src="/Scripts/Common.js" type="text/javascript"></script>
    <script src="/Scripts/Home.js" type="text/javascript"></script>
</head>'''
p.feed(mystr)
p.close()