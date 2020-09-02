# W3Cschool-CSS 选择器 https://www.w3cschool.cn/cssref/css-selectors.html
from scrapy import Selector 

body= '''<html>
            <head>
                <title>我是标题</title>
            </head>
            <body>
                <b id =\'b1\'>强调</b>
                <h1 align=\'center\'>这是标题</h1>
                <div class="p"><h4>那是一条神奇的天路</h4>    
                    <span>     段落2    </span>
                    <h4>带我们走进人间天堂 </h4>    
                    <span>     段落     </span>
                    <h4>青稞酒酥油茶会更加香甜</h4> 
                    <span>     段落4    </span>
                    <h4>幸福的歌声传遍四方  </h4>   
                    <span>     段落5 <h4>内部  </h4>   </span>
                    <h4>幸福的歌声传遍四方 </h4>    
                </div>  
                <div class="div">
                    <a id ="a1" class="a">图片1<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" /></a>
                    <a id ="a2" class="a">图片2<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3000f11f034f78f0840b9df149300a83/03087bf40ad162d9393e0d5711dfa9ec8b13cdad.jpg" /></a>
                    <a class="a" href="/">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>
                </div>
            </body>
        </html>'''
selector = Selector(text=body) 

# 标签内容的提取“::text”
title = selector.css('title::text' ).extract_first() 
print(f'标题：{title}')

a = selector.css('a' ).extract() 
print(f'所有的a标签：{a}')

# 提取属性我们是用：“标签名::attr(属性名)”，
# 比如我们要提取url表达式就是：a::attr(href)，要提取图片地址的表达式就是：img::attr(src)
a = selector.css('a::text').extract() 
print(f'所有的a标签文本：{a}')

img = selector.css('img::attr(src)').extract() 
print(f'所有的img标签链接：{img}')

img = selector.css('a[id^="a"] img::attr(src)').extract() 
print(f'所有的img标签链接：{img}')

img = selector.css('img[src$=".jpeg"]').extract() 
print(f'所有的img标签链接：{img}')

#contains()匹配包含指定文本的元素
txt = selector.css('h4:contains("天")').extract() 
print(f'所有的h标签文本：{txt}')

# 第一个h4节点
h = selector.css("h4:first-child").extract() 
print(f'第一个h4节点：{h}')

# 最后一个h4节点
h = selector.css("h4:last-child").extract() 
print(f'最后一个h4节点{h}')

its = selector.css("div h4:nth-child(5)").extract()    
print("获取2以前的h4标签:%s" % its)

#提取所有文字，用*
its = selector.css("div *::text").extract()      
print("div的文本:%s" % its)

#:not(p)	选择每个并非p元素的元素
its = selector.css("div.p :not(span)").extract()      
print("div的文本:%s" % its)
its = selector.css("div.p :not(h4)").extract()      
print("div的文本:%s" % its)

#选择<div>元素内的所有<h4>元素
h4 = selector.css("div.p h4").extract()      
print("h4的文本:%s" % h4)

#选择所有父级是 <div> 元素的 <H4> 元素 ,直接子节点
h4 = selector.css("div.p>h4").extract()      
print("h4的文本:%s" % h4)

#选择所有紧接着<div>元素之后的<h4>元素
h4 = selector.css("div.p+h4").extract()      
print("h4的文本:%s" % h4)