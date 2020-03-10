import lxml
from lxml import etree

html = etree.parse(r'backup/1.html')
#'//'表示获取当前节点子孙节点，'*'表示所有节点，'//*'表示获取当前节点下所有节点
html_data = html.xpath('//*')   #打印是一个列表，需要遍历

for item in html_data:
    print(item)
    
print('-'*40)
#获取当前节点的父节点。现在我要获取最后一个a节点的父节点下的class属性。
result = html.xpath('//a[@id="a2"]/../@class')
print(result)
for item in result:
    print(item)
    

print('-'*40) 
#遇到属性值有多个的情况我们需要使用contains()函数了，contains()匹配一个属性值中包含的字符串 。包含的字符串，而不是某个值。
result = html.xpath('//img[contains(@src,"https")]') 
for item in result:
    print(item)
    
print('-'*40)
result = html.xpath('//img[contains(@src,"https") and @alt = "i1"]')
print(result)
result = html.xpath('//img[contains(@src,"https") and contains(@alt,"i")]')
print(result)

print('-'*40)
result = html.xpath('//img[contains(@src,"https") or @alt="i2"]')
print(result)