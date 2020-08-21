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

#查询具有某个属性的节点
result = html.xpath('//li[@data_attention]/@data_attention') 
print(result)

#查询具有一个或多个属性的节点
result = html.xpath('//li[@data_attention or @data_aclss]/a/text()') 
print(result)

#查询具有多个属性的节点
result = html.xpath('//li[@data_attention and @class]/a/text()') 
print(result)

#查询不具有某个属性的节点
result = html.xpath('//li[not(@data_aclss)]/a/text()') 
print(result)

#查询不具有一个或多个属性的节点
result = html.xpath('//li[not(@data_aclss or @data_attention)]/a/text()') 
print(result)

#查询不具有多个属性的节点
result = html.xpath('//li[not(@class and @name)]/a/text()') 
print(result)