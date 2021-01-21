from scrapy.selector import Selector
from scrapy.http import HtmlResponse 
from scrapy.linkextractors import LinkExtractor

# HtmlResponse也包含多种方法，比如css，xpath，text等方法，也可以通过jupyter notebook进行网页分析，
# 而且也可以使用linkextractor提取链接，更加方便 
html = """<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <li class="item-"><a href="link.html">first item</a></li>
    <li class="item-0"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    
    <div class="div">
        <p lang="en">单打独斗</p>
        <p lang="en-us">点点滴滴</p>
        <a id ="a0" class="hello world">图片0<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" />链接以a开头的标签链接</a>
        <a id ="a1" class="a" href='top50'>图片1<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" /></a>
        <a id ="a2" class="a" target="_blank">图片2<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3000f11f034f78f0840b9df149300a83/03087bf40ad162d9393e0d5711dfa9ec8b13cdad.jpg" /></a>
        <a class="a" href="http://www.sina.com" target="_top">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>
    </div>
</body>
</html>
"""
response = HtmlResponse(url = 'http://example.com', body = html,encoding = 'utf-8')
# response.xpath —— re:test正则匹配，starts-with匹配开头
ret = Selector(response=response).xpath('//li[re:test(@class, "item-\d+")]/a[starts-with(text(),"se")]/@href').extract()
print(ret) 

#在页面含有少量链接时，使用selector来提取信息就可以，但如果链接特别多时，就需要用LinkExtractor来提取。
#提取div区域内部的链接
le = LinkExtractor(restrict_css='div.div') 
#le = LinkExtractor() 
for link in le.extract_links(response): 
    print('区域的链接：',link.url) 
        