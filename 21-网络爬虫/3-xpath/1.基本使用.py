from lxml import etree
 
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item </li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item 
        """
html = etree.HTML(wb_data)          #初始化生成一个XPath解析对象
print(html)
result = etree.tostring(html)        #解析对象输出代码
print(result.decode("utf-8"))

html_data = html.xpath('/html/body/div/ul/li/a')
print(html)
for i in html_data:
    print(i.text)
 
html_data = html.xpath('/html/body/div/ul/li/a/text()')
print(html)
for i in html_data:
    print(i) 
    
html_data = html.xpath('/html/body/div/ul/li/a/@href')
for i in html_data:
    print(i)    
    