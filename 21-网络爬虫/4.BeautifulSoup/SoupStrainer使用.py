from bs4 import BeautifulSoup, NavigableString
from bs4 import SoupStrainer

html = '<html>\
            <head>\
                <title>我是标题</title>\
            </head>\
            <body>\
                <b id =\'b1\'>强调</b>\
                <h1 align=\'center\'>这是标题</h1>\
                <p class="p"> 段落1<h4>那是一条神奇的天路 </h4>    \
                    段落2<h4>带我们走进人间天堂 </h4>    \
                    段落3<h4>青稞酒酥油茶会更加香甜</h4> \
                    段落4<h4>幸福的歌声传遍四方  </h4>   \
                    段落5<h4>幸福的歌声传遍四方 </h4>    \
                </p>  \
                <div class="div">\
                    <a id ="a1" class="a">图片1<img src="https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=5ed1e4838eb1cb133e693b15e56f3173/0bd162d9f2d3572c7ba613b08913632762d0c312.jpg" /></a>\
                    <a id ="a2" class="a">图片2<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=3000f11f034f78f0840b9df149300a83/03087bf40ad162d9393e0d5711dfa9ec8b13cdad.jpg" /></a>\
                    <a class="a" id="link2" href="/">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>\
                </div>\
            </body>\
        </html>'        
        
only_a_tags = SoupStrainer("a")
only_tags_with_id_link2 = SoupStrainer(id="link2")

def is_short_string(string):
    return len(string) < 6 

only_short_strings = SoupStrainer(text=is_short_string)

soup = BeautifulSoup(html, "lxml")
print('1------------找到所有a元素')
print(BeautifulSoup(html, "html.parser", parse_only=only_a_tags).prettify())
print('2------------找到id=link2的元素')
print(BeautifulSoup(html, "html.parser", parse_only=only_tags_with_id_link2).prettify())
print('3------------找到元素长度小于10的元素')
print(BeautifulSoup(html, "html.parser", parse_only=only_short_strings).prettify()) 