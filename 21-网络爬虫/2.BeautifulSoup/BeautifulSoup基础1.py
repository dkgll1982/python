from bs4 import BeautifulSoup
import re
#详细用法参见中文文档：https://beautifulsoup.readthedocs.io/zh_CN/latest/

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
                    <a class="a">图片3<img src="http://5b0988e595225.cdn.sohucs.com/q_70,c_lfill,w_300,h_200,g_faces/images/20200105/8cd5207bdd4d426d9167912559c69063.jpeg" /></a>\
                </div>\
            </body>\
        </html>'        
beau = BeautifulSoup(html,'lxml')
tag1 = beau.img
tag2 = beau.findAll('a') 
print(type(tag1))
print(type(tag2))
print(tag1.name)
print(tag1['src'])
print(tag2[0].name)
print(tag2[0].contents)
print('父节点:',tag2[0].parent)
for x in tag2[0].parents:print('所有父节点:',x)
print(tag2[0].parent.name)
print(beau.title)
print(beau.title.name)
print(beau.title.string,type(beau.title.string))
#tag的 .contents 属性可以将tag的子节点以列表的方式输出:
print(beau.head,beau.head.contents)
#遍历子节点（直到子级，不进行多级遍历）
for x in beau.head.children:print('head-children:',x) 
#.descendants 属性可以对所有tag的子孙节点进行递归循环 [5] :
for x in beau.head.descendants:print('head-sub:',x) 
#for string in beau.strings:
#输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:
for string in beau.stripped_strings:
    print('段落文字：',repr(string))
#实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
#因为解析的很有可能是标签之间的顿号和换行符    
print('p下级节点:',beau.p.next_sibling.next_sibling.next_sibling )    
print('p上级节点:',beau.p.previous_sibling.previous_sibling)   
print('')
beau = BeautifulSoup(open(r'backup\1.html',encoding='utf-8'),'lxml')
print(beau.title,beau.find_all('a'))

print('')

#正则搜索 
for tag in beau.find_all(re.compile('b|a')):
    print(tag.name)
    
print('') 

#True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
for tag in beau.find_all(True):
    print(tag.name)
    
print('') 

#校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

for x in beau.find_all(has_class_but_no_id):
    print('=>:',x)
#find_all( name , attrs , recursive , string , **kwargs )

#有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:
#可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
print(beau.find_all(id=True,attrs={'class':'a'}))

#按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字class在Python中是保留字,使用class做参数会导致语法错误.
#从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag:
#class_ 参数同样接受不同类型的 过滤器 ,字符串,正则表达式,方法或 True :
print(beau.find_all(class_=re.compile("a|p")))

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 3
#此例中div class的长度为3
print(beau.find_all(class_=has_six_characters))
#string 参数
print(beau.find_all(string=re.compile('段落|图')))
#使用 limit 参数限制返回结果的数量
print(beau.find_all('h4',string=re.compile('幸福|天堂'),limit=4))