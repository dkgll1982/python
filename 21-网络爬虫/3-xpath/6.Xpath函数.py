# 字符串函数：https://blog.csdn.net/weixin_30929295/article/details/95697646
# 字符串函数主要用来处理字符串。字符串函数主要包括以下：
# concat(),contains(),normalize-space(),starts-with(),substing(),substring-before(),subsring-after(),translate()
# concat()函数用于串连多个字符串。

from lxml import etree

text = '''
<div>
    <ul>
        <li class="sp item-0" name="one"><a href="www.baidu.com">baidu</a>
        <li class="sp item-0" data_Attention="96551"><a href="www.sougou.com">sogou</a>
        <li class="sp item-0" name="one"><a href="www.tencent.com">tencent web</a>
        <li class="sp item-1" name="two"><a href="https://blog.csdn.net/qq_25343557">myblog</a>
        <li class="sp item-2" data_Aclss='li tclass1' name="two"><a href="https://www.csdn.net/">csdn</a>
        <li class="sp item-3" name="four"><a href="https://hao.360.cn/?a1004">hao123</a>
        <li class="sp item-3" name="four"><a data_Attention="2149" href="https://daojian.360.cn/?a1004">刀剑 online</a>
'''
html = etree.HTML(text)

#starts-with函数:选取name值以'o'开头的节点
result = html.xpath('//li[starts-with(@name,"o")]/a/text()') 
print(result)

#ends-with是xpath2.0的语法,可能你的浏览器还只支持1.0的语法
#result = html.xpath('//li[ends-with(@name,"e")]/a/text()') 
#等价于
result = html.xpath('//li[concat(substring(@name,string-length(@name)-string-length("o")+1),"i")="oi"]/a/text()') 
#string-length(string)函数用来返回参数string的长度，如果参数string为缺省，将返回上下文节点的字符串长度。
print(result)

#text()函数:选取节点文本包含s或b的a节点
result = html.xpath('//a[contains(text(),"s") or contains(text(),"b")]/text()') 
print(result)