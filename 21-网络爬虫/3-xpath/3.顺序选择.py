from lxml import etree

text = '''
<div>
    <ul>
        <li class="sp item-0" name="one"><a href="www.baidu.com">baidu</a>
        <li class="sp item-1" name="two"><a href="https://blog.csdn.net/qq_25343557">myblog</a>
        <li class="sp item-2" name="two"><a href="https://www.csdn.net/">csdn</a>
        <li class="sp item-3" name="four"><a href="https://hao.360.cn/?a1004">hao123</a>
'''

html = etree.HTML(text)
result = html.xpath('//li[2]/a/text()')#选择第二个li节点，获取a节点的文本
print(result)
result = html.xpath('//li[last()]/a/text()')#选择最后一个li节点，获取a节点的文本
print(result)
result = html.xpath('//li[last()-1]/a/text()')#选择倒数第2个li节点，获取a节点的文本
print(result)
result = html.xpath('//li[position()<=3]/a/text()')#选择前三个li节点，获取a节点的文本
print(result)
