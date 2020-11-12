import requests
import scrapy

# 这是百度新闻主页
url = 'https://pianoadventures.cn/?product=%E5%9C%A8%E7%BA%BF%E9%9F%B3%E9%A2%91%E8%B5%84%E6%BA%90%C2%B7%E6%88%91%E7%9A%84%E9%92%A2%E7%90%B4%E7%AC%AC%E4%B8%80%E8%AF%BE%C2%B7c%E7%BA%A7'
res = requests.get(url=url)
html = res.text
with open(r'backup/test2.html','w') as f:
    f.write(html)

sel = scrapy.Selector(text=html)
    
# 解析抓取“热点要闻”
words = sel.css('div.wp-playlist-item').extract()
    
for word in words:
    print(word)