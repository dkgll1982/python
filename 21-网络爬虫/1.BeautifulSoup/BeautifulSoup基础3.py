#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-01-10 17:43:34 
# @Last Modified by: guojun 
# @Last Modified time: 2020-01-10 17:43:34 
# @Software: vscode 

from bs4 import BeautifulSoup,NavigableString,Comment,UnicodeDammit
import re
#详细用法参见中文文档：https://beautifulsoup.readthedocs.io/zh_CN/latest/
#其他参考：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#beautifulsoup-new-string-new-tag

html = '<html>\
            <head>\
                <title>我是标题</title>\
            </head>\
            <body>\
                <b id =\'b1\'>强调</b>\
                <h1 align=\'center\'>这是标题</h1>\
                <p class="p"> 段落1<h4>那是一条神奇的天路 </h4>    \
                    段落2<h4>带我们走进人间天堂 </h4>    \
                    段落3<h4  align=\'left\'>青稞酒酥油茶会更加香甜</h4> \
                    段落4<h4>幸福的歌声传遍四方  </h4>   \
                    段落5<h4>幸福的歌声传遍四方 </h4>    \
                </p>  \
                <div class="div">\
                    <a id ="a1" class="a">图片1<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" /></a>\
                    <a id ="a2" class="a">图片2<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3000f11f034f78f0840b9df149300a83/03087bf40ad162d9393e0d5711dfa9ec8b13cdad.jpg" /></a>\
                    <a class="a">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>\
                </div>\
            </body>\
        </html>'        
soup = BeautifulSoup(html,'lxml')

tag = soup.b
tag.append(" Hello")
new_string = NavigableString(" there")
tag.append(new_string)
print(tag)
# <b>Hello there.</b>
print(tag.contents)
# [u'Hello', u' there']

#如果想要创建一段注释,或 NavigableString 的任何子类, 只要调用 NavigableString 的构造方法: 
new_comment = soup.new_string("Nice to see you.", Comment)
tag.append(new_comment)
print(tag)
# <b>Hello there<!--Nice to see you.--></b>
print(tag.contents)

#如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
#如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:
#如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :
for x in tag.strings:print(x)
# [u'Hello', u' there', u'Nice to see you.']

#Tag.insert() 方法与 Tag.append() 方法类似,区别是不会把新元素添加到父节点 .contents 属性的最后,
#而是把元素插入到指定的位置.与Python列表总的 .insert() 方法的用法下同: 
tag = soup.a

tag.insert(1, " but did not endorse ")
print(tag) 
print(tag.contents)

#insert_before() 方法在当前tag或文本节点前插入内容:
tag = soup.new_tag("i")
tag.string = "insert_before"
soup.b.insert_before(tag) 

tag = soup.new_tag("i")
tag.string = "insert_after"
soup.b.insert_after(tag) 
print('==>',soup.body.prettify())

#Tag.clear() 方法移除当前tag的内容:
tag = soup.i 
print(tag) 
tag.clear() 
print(tag) 

#PageElement.extract() 方法将当前tag移除文档树,并作为方法结果返回: 
a_tag = soup.a 
print('a移除img前:',a_tag) 
img_tag = soup.a.img.extract() 
print('a移除img后:',a_tag) 
print('img:',img_tag)   
#这个方法实际上产生了2个文档树: 一个是用来解析原始文档的 BeautifulSoup 对象,
#另一个是被移除并且返回的tag.被移除并返回的tag可以继续调用 extract 方法:
title_string = soup.head.title.string.extract()
print(title_string) 
print(title_string.parent) 
print(soup.head) 

#Tag.decompose() 方法将当前节点移除文档树并完全销毁:
soup.head.title.decompose()
print(soup.head)

#PageElement.replace_with() 方法移除文档树中的某段内容,并用新tag或文本节点替代它:
new_tag = soup.new_tag("b")
new_tag.string = "example.net"
soup.b.replace_with(new_tag)
print(soup.b)

#PageElement.wrap() 方法可以对指定的tag元素进行包装 [8] ,并返回包装后的结果:
soup.b.string.wrap(soup.new_tag("b"))
print(soup.b)
soup.b.wrap(soup.new_tag("div"))
print(soup.div)

print('')

#Tag.unwrap() 方法与 wrap() 方法相反.将移除tag内的所有tag标签,该方法常被用来进行标记的解包:
soup.div.unwrap()
print(soup)

#压缩输出
#如果只想得到结果字符串,不重视格式,那么可以对一个BeautifulSoup对象或Tag对象使用Python的unicode()或str()方法:
#str() 方法返回UTF-8编码的字符串,可以指定 编码 的设置.
#还可以调用 encode() 方法获得字节码或调用 decode() 方法获得Unicode.
print(str(soup))
print(soup.div.decode())

#Beautiful Soup输出是会将HTML中的特殊字符转换成Unicode,比如“&lquot;”:

soup = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.")
print(str(soup))

#如果只想得到tag中包含的文本内容,那么可以调用 get_text() 方法,
#这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回:
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

print(soup.i.get_text())
#可以通过参数指定tag的文本内容的分隔符:
#还可以去除获得文本内容的前后空白:
print(soup.get_text("|", strip=True))
#或者使用 .stripped_strings 生成器,获得文本列表后手动处理列表:
print([text for text in soup.stripped_strings])

markup = "<h1>df否</h1>"
soup = BeautifulSoup(markup, from_encoding="utf-8")
print(soup.h1,soup.original_encoding)