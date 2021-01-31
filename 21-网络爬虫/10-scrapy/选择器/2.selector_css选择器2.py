#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-22 11:16:38 
# @Remark: Life is short, I use python！ 
# @Software: vscode #!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-22 11:15:04 
# @Remark: Life is short, I use python！ 
# @Software: vscode 

# W3Cschool-CSS 选择器： https://www.w3cschool.cn/cssref/css-selectors.html
# 测试css选择器地址：https://www.w3school.com.cn/tiy/t.asp?f=css_sel_class

from scrapy import Selector 
import sys

body= '''<html>
            <head>
                <title>我是标题</title>
            </head>
            <body>
                <b id =\'b1\'>强调段落</b>
                <h1 align=\'center\'>这是标题</h1>
                <div class="p">
                    <p>段落1
                        <a id ="ff1" class="a item-d31" href='www.sohu.com'>图片21</a>    
                    </p>             
                    <h4>那是一条神奇的天路</h4>    
                    <p>段落2
                        <a id ="ff2" class="a item-d2d" href='www.163.com'>中间段落</a>    
                    </p>             
                    <span>     段落2    </span>
                    <h4>带我们走进人间天堂 </h4>    
                    <span>     段落     </span>
                    <h4>青稞酒酥油茶会更加香甜</h4> 
                    <p>段落3
                        <a id ="ff3" class="a item-d3d" href='www.sina.com'>图片22</a>    
                    </p>             
                    <span>     段落4    </span>
                    <h4>幸福的歌声传遍四方  </h4>   
                    <span>     段落5 <h4>内部  </h4>   </span>
                    <h4>幸福的歌声传遍四方 </h4>    
                </div>  
                <p class='text'>这个是紧挨这div的p元素</p>
                <div class="div">
                    <p lang="en">单打独斗</p>
                    <p lang="en-us">点点滴滴</p>
                    <a id ="a0" class="hello world item-t">图片0<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" />链接以a开头的标签链接</a>
                    <a id ="a22" class="a item-2d" href='www.baidu.com'>图片22</a>                   
                    <a id ="a1" class="a item-1">图片1<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" /></a>
                    <a id ="a2" class="item-12" target="_blank">图片2<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3000f11f034f78f0840b9df149300a83/03087bf40ad162d9393e0d5711dfa9ec8b13cdad.jpg" /></a>
                    <a class="a" href="/" target="_top">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>
                </div>
            </body>
        </html>'''
selector = Selector(text=body) 

print(f'第{str(sys._getframe().f_lineno)}行返回结果：',
      selector.css('title::text').extract_first(), 
      selector.css('title::text').get(),
      selector.css('title::text').extract(),
      selector.css('title').extract_first(),
      selector.css('title').extract())

#标签属性值的提取 
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('a::attr(href)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div a::attr(href)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div p a::attr(href)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div :last-child::attr(href)').extract())

print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div p:first-of-type a::attr(href)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div p:nth-of-type(2) a::attr(href)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div p:last-of-type a::attr(href)').extract())


print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div p').extract())
#:nth-child(n) 选择器匹配属于其父元素的第 N 个子元素，不论元素的类型。n 可以是数字、关键词或公式。
# 这里div.p下边的子元素：1-p，2-h4,3-p,4-span,5-h4,6-span,7-h4,8-p....
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(1)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(2)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(3)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(4)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(5)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(6)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(7)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(8)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(odd)').extract())     #奇数行
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(even)').extract())    #偶数行
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p :nth-child(2n+1)').extract())    #使用公式 (an + b)。描述：表示周期的长度，n 是计数器（从 0 开始），b 是偏移值。
#nth-child前边带上元素类型，如果位置和元素类型不一致，返回结果为空
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p p:nth-child(3)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.p p:nth-child(2)').extract())

print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.div :last-child').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.div :nth-last-child(1)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.div :nth-last-child(2)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div.div :nth-last-child(3)').extract())


print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div p:nth-child(2)').extract())
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div>a::attr(href)').extract())

print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('p a').extract())
#选择<div>元素内的所有<p>元素
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div p').extract())
#选择所有紧接着<div>元素之后的<p>元素
print(f'第{str(sys._getframe().f_lineno)}行返回结果：',selector.css('div+p').extract())
