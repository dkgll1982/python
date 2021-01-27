#!/usr/bin/env python 
# -*- coding:utf-8 -*-  
# @Author: suixin 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd  
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2021-01-22 22:46:10 
# @Remark: Life is short, I use python！ 
# @Software: vscode 
# 备注：页面为本地测试页面，可以本地启动web服务（tomcat、ngix、iis等）运行

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule,logging
import re
import copy

class Local1Spider(CrawlSpider):
    name = 'local1'
    #allowed_domains = ['localhost:8080']
    
    #本地测试tomat启动的页面
    #页面的源码如下：
    """<!DOCTYPE html>
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
            <p lang="en" style="width:100px;background:pink;cursor:pointer" onclick="window.open('http://www.taobao.com', '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');">单打独斗</p>
            <p lang="en-us" onclick="window.open('localhost:8080/openVone/2.html', '_blank')">点点滴滴</p>
            <p lang="en-us" onclick="http://www.163.com/">163</p>
            <p lang="en-us" onclick="http://localhost:8080/openVone/3.html">点点滴滴2</p>
            <p lang="en-us" onclick="http://www.baidu.com">点点滴滴3</p>
            <a id ="a0" class="hello world">图片0<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" />链接以a开头的标签链接</a>
            <a id ="a1" class="a" href='top50'>图片1<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" /></a>
            <a id ="a2" class="a" target="_blank">图片2<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3000f11f034f78f0840b9df149300a83/03087bf40ad162d9393e0d5711dfa9ec8b13cdad.jpg" /></a>
            <a class="a" href="http://www.sina.com" target="_top">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>
        </div>
    </body>
    </html>
    """
    start_urls = ['http://localhost:8080/openVone/1.html']
    
    rules = ( 
        # allow参数没有必要写出要提取的url完整的正则表达式,部分即可,只要能够区别开来。
        # 且最重要的是,即使原网页中写的是相对url,通过LinkExtractor这个类也可以提取中绝对的url,这个类太厉害了。 
        
        # 提取css、jpg、png、js等有些链接的时候,process_value函数收到后给过滤了！所有link提取的值都会经过process_value这个函数,如果这个函数没指定,默认为lambda x: x
        # LinkExtractor中allow正则表达式必须是没有被过滤的链接，否则返回来会是空（css、jpg、png、js文件类链接process_value函数过滤之后，返回来都是空列表）
        # allow=["[\w\W]+?\.css"],tags=["img","script","link","a","area"],
        #                         attrs=["href","src"]
        
        # 默认的tags：接收一个标签（字符串）或一个标签列表，提取指定标签内的链接，默认为tags=（‘a’，‘area’）
        # attrs：接收一个属性（字符串）或者一个属性列表，提取指定的属性内的链接，默认为attrs=（‘href’，）
        # 下边演示的链接地址是在p(tags=["p"])标签的onlick方法(attrs=["onclick"])里，通过process_links方法正则处理返回link再次请求，正常情况该链接是无法获取到的
        Rule(LinkExtractor( 
                            #allow参数设置正则匹配，只爬取按照规则能匹配到的链接，不写则爬取所有，下边爬取的是以window.open开头的链接
                            #allow=r"window.open\('.+'",
                            tags=["p"],
                            attrs=["onclick"],
                           ), process_links='check_links', callback = "parse_item", follow = False),
        
        Rule(LinkExtractor(), callback = "parse_detail", follow = False),
    )
     
    def check_links(self,link): 
        print('处理前的link：',link)
        
        # bug记录：2021/01/23:一个bug处理了3个小时左右，已解决
        # bug跟踪：传递过来的link被转义，本来是http://www.qq.com的形式，结果一看是http:/www.qq.com,双斜杠变成了单斜杠
        # 因此在下边方法里做处理：过滤掉非链接的字符，将单斜杠改为双斜杠
        for i,l in enumerate(link,start=1):
            if 'window' in l.url:                 
                url = re.findall(r"window.open\('(.*?)'," , l.url ,re.M|re.S)[0] 
                # 如果链接地址是http:/的形式就替换成http://的形式
                rep = re.compile("http:/(\w.*)")
                l.url = rep.sub(r'http://\1',url)  
                
            #链接开头要包含'http'，否则会报ValueError: Missing scheme in request url:
            if not l.url.startswith('http:'):
                l.url = f"http://{l.url}"
            
            print(f'区域的链接{i}：',l.url) 
        
        #传递过来的link是list，可以进行添加、修改、删除操作，下边测试添加一条链接地址
        new_link = copy.deepcopy(link[-1])
        new_link.url = 'http://www.jd.com'
        new_link.text = 'jd'
        link.append(new_link)
        
        print('处理后的link：',link)
        return link
    
    def parse_item(self,response):
        print('请求的url地址：',response.url)
        
    def parse_item(self,response):
        print('url:',response.url,',title:',response.css("title::text").extract_first())