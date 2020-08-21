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

#计算两个节点集
result = html.xpath('//li[@data_attention]/@data_attention | //a[not(contains(@href,"https"))]/@href') 
print(result)

#或(注意节点属性名称需要小写)
result = html.xpath('//li[@data_attention or @data_aclss]') 
print(result)

#与(注意节点属性名称需要小写)
result = html.xpath('//li[@data_aclss and @name]') 
print(result)

#元素等于
result = html.xpath("//li[@name='two']//text()") 
print(result)

#位置计算
result = html.xpath('//li[position()>=3 and position()<=5]') 
print(result)

text = '''
<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>
<book>
  <title lang="eng">Harry Potter</title>
  <price>33.99</price>
</book>
<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>'''

html = etree.HTML(text)

#元素值计算
result = html.xpath('//book[price>=30 and position()>2]/price/text()') 
print(result)