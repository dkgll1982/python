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
#语法格式：
#轴名称：节点测试[谓语]
#  -----------------------------------------------------------------
#  轴名称                  结果                                    
#  ancestor：          选取当前节点的所有先辈(包括父，祖父，祖祖父等) 
#  ancestor-or-self：  选取当前节点的所有先辈以及当前节点本身         
#  attribute：         选取当前节点的所有属性                       
#  child：             选取当前节点的所有子元素                     
#  descendant：        选取当前节点的所有后代元素（包括子，孙等）     
#  descendant-or-self：选取当前节点的所有后代元素及当前节点本身       
#  following：         选择文本中当前节点结束标签后的所有节点         
#  namespace：         选取当前节点的所有命名空间节点                       
#  parent：            选取当前节点的父节点                         
#  preceding：         选取文档中当前节点的开始标签之前的所有节点     
#  preceding-sibling： 选取当前节点之前的所有同级节点                
#  self：              选取当前节点                                
#  -----------------------------------------------------------------

result = html.xpath('//li[1]/ancestor::*')           #ancestor表示选取当前节点祖先节点，*表示所有节点。合：选择当前节点的所有祖先节点。
print(result)
result = html.xpath('//li[1]/ancestor::div')         #ancestor表示选取当前节点祖先节点，div表示div节点。合：选择当前节点的div祖先节点。
print(result)
result =  html.xpath('//li[1]/ancestor-or-self::*')  #ancestor-or-self表示选取当前节点及祖先节点，*表示所有节点。合：选择当前节点的所有祖先节点及本及本身。
print(result)
result =  html.xpath('//li[1]/attribute::*')         #attribute表示选取当前节点的所有属性，*表示所有节点。合：选择当前节点的所有属性。
print(result)
result =  html.xpath('//li[1]/attribute::name')      #attribute表示选取当前节点的所有属性，name表示name属性。合：选择当前节点的name属性值。
print(result)
result =  html.xpath('//ul/child::*')                #child表示选取当前节点的所有直接子元素，*表示所有节点。合：选择ul节点的所有直接子节点。
print(result)
result =  html.xpath('//ul/child::li[@name="two"]')  #child表示选取当前节点的所有直接子元素，li[@name="two"]表示name属性值为two的li节点。合：选择ul节点的所有name属性值为two的li节点。
print(result)
result =  html.xpath('//ul/descendant::*')           #descendant表示选取当前节点的所有后代元素（子、孙等），*表示所有节点。合：选择ul节点的所有子节点。
print(result)
result =  html.xpath('//ul/descendant::a/text()')    #descendant表示选取当前节点的所有后代元素（子、孙等），a/test()表示a节点的文本内容。合：选择ul节点的所有a节点的文本内容。
print('-',result)
result =  html.xpath('//li[1]/following::*')         #following表示选取文档中当前节点的结束标签之后的所有节点。，*表示所有节点。合：选择第一个li节点后的所有节点。
print(result)
result =  html.xpath('//li[1]/following-sibling::*') #following-sibling表示选取当前节点之后的所有同级节点。，*表示所有节点。合：选择第一个li节点后的所有同级节点。
print(result)
result =  html.xpath('//li[1]/parent::*')            #选取当前节点的父节点。父节点只有一个，祖先节点可能多个。
print(result)
result =  html.xpath('//li[3]/preceding::*')         #preceding表示选取文档中当前节点的开始标签之前的所有同级节点及同级节点下的节点。，*表示所有节点。合：选择第三个li节点前的所有同级节点及同级节点下的子节点。
print(result)
result =  html.xpath('//li[3]/preceding-sibling::*') #preceding-sibling表示选取当前节点之前的所有同级节点。，*表示所有节点。合：选择第三个li节点前的所有同级节点。
print(result)
result =  html.xpath('//li[3]/self::*')              #选取当前节点。
print(result)
result =  html.xpath('//li[3]')                      #选取当前节点。
print(result)
result =  html.xpath('//li[position()=2 or position()=4]/a/text()') #选取某个指定的或者某个区间的节点。
for r in result:
    print('---->',r)

