import requests
from lxml import etree

url = "https://blog.csdn.net/qq_25343557/article/details/81912992"
headers = {
    "user_agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

request = requests.get(url,headers=headers)
html = request.text 

tree = etree.HTML(html)
result = tree.xpath("/html/body[@class='nodata ']/div[@class='main_father clearfix d-flex justify-content-center']/div[@id='mainBox']/main/div[@class='blog-content-box']/article[@class='baidu_pl']/div[@id='article_content']/div[@id='content_views']/p[34]/strong/text()")
print(result)
result = tree.xpath("/html/body[@class='nodata ']/div[@class='main_father clearfix d-flex justify-content-center']/div[@id='mainBox']/main/div[@class='blog-content-box']/article[@class='baidu_pl']/div[@id='article_content']/div[@id='content_views']/p[1]/text()")
print(result)
result = tree.xpath("/html/body[@class='nodata ']/div[@class='main_father clearfix d-flex justify-content-center']/div[@id='mainBox']/aside[@class='blog_container_aside']/div[@id='asideProfile']/div[@class='profile-intro d-flex']/div[@class='user-info d-flex flex-column profile-intro-name-box']/div[1]/span[@class='name csdn-tracking-statistics tracking-click ']/a[@id='uid']/text()")
print(result)
result = tree.xpath("/html/body[@class='nodata ']/div[@class='main_father clearfix d-flex justify-content-center']/div[@id='mainBox']/aside[@class='blog_container_aside']/div[@id='asideProfile']/div[@class='grade-box clearfix']/dl[3]/dd/text()")
print(result)
