#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-21 09:52:34 
# @Remark: 人生苦短，我用python！
# 参考链接：https://www.cnblogs.com/zhangxinqi/p/9210211.html

from lxml import etree
 
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1" id="t1" dataar-Tidanchor="981451" ><a href="link2.html">second item </li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item 
        """
html = etree.HTML(wb_data)                      #初始化生成一个XPath解析对象并对HTML文本进行自动修正。
print(html)
result = etree.tostring(html,encoding='utf-8')  #解析对象输出代码，输出修正后的结果，类型是bytes
print(type(html))
print(type(result))
print(result.decode("utf-8"))                   #利用decode()方法将其转成str类型

#发现属性要改成小写，才能识别，不清楚是否是bug
data = html.xpath('//li[2]/attribute::dataar-tidanchor')
print('====>',data)

html_data = html.xpath('/html/body/div/ul/li/a')
print(html)
for i in html_data:
    print(i.text)
 
html_data = html.xpath('/html/body/div/ul/li/a/text()')
print(html)
for i in html_data:
    print(i) 
    
html_data = html.xpath('/html/body/div/ul/li/a/@href')
for i in html_data:
    print(i)    
    