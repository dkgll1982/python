#参考链接（获取360图片站图片自联系）：https://www.jianshu.com/p/1dddcbe8e312

import scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
import re
from images360.items import Images360Item

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com'] 

    def start_requests(self):
        data = {'ch': 'photography', 'listtype': 'new'}
        base_url = 'https://image.so.com/z?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)
        
    def parse(self, response):                
        json_str = re.findall(r'.*?<script.*id="initData">(.*?)</script>',response.text)
        result = json.loads(json_str[0])['data']  
        for image in result.get('list'):
            item = Images360Item()
            item['id'] = image.get('id')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('site')
            item['thumb'] = image.get('qhimg_thumb')
            yield item
