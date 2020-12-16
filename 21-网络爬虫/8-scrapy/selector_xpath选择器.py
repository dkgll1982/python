from scrapy import Selector 

body= '''<html>
            <head>
                <title>我是标题</title>
            </head>
            <body>
                <b id =\'b1\'>强调</b>
                <h1 align=\'center\'>这是标题</h1>
                <div class="p">  
                    <h4>那是一条神奇的天路 </h4>    
                    <span>     段落2    </span>
                    <h4>带我们走进人间天堂 </h4>    
                    <span>     段落     </span>
                    <h4>青稞酒酥油茶会更加香甜</h4> 
                    <span>     段落4    </span>
                    <h4>幸福的歌声传遍四方  </h4>   
                    <span>     段落5    </span>
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
title = selector.xpath('//title/text() ' ).extract_first() 
print(f'标题：{title}')
href = selector.xpath('//@href | //@src' ).extract() 
print(href)
#选取所有拥有id的属性的a元素,并且class包含a，文本包含图片。
a = selector.xpath('//a[@id and contains(@class,"a") and contains(text(),"图片") ]' ).extract() 
print(a)
#匹配属性值开头、结尾，与css选择器器的^=,$=有异曲同工之妙
img = selector.xpath('//img[starts-with(@src,"https")]').extract()
print(img)
#img = selector.xpath('//img[ends-with(@src,"jpeg")]').extract()
#ends-with是xpath2.0的语法，1,0不支持，可以用下面的方式代替
img = selector.xpath('//img[substring(@src,string-length(@src)-string-length("jpeg")+1)="jpeg"]').extract()
print(img)

#text()方法变成多个分段字符串的列表
p = selector.xpath('//body//div[@class="p"]//text()').extract() 
print(p)
#string变成一个字符串的列表
p = selector.xpath('string(//body//div[@class="p"])').extract() 
print(p)