import scrapy
from urllib import parse
from meituba.items import MeitubaItem

class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['meituba.com']
    start_urls = ['http://www.meituba.com/meinv/']

    #解析起始页
    def parse(self, response):
        #选择具有href属性的a标签
        a_list = response.css('div.span2>a::attr(href)').extract()
        for url in a_list:
            if url:           #链接不为空
                yield scrapy.Request(url = url,callback = self.parse_detail)
                
    #跳转到详情页
    def parse_detail(self, response):
        item = MeitubaItem()
        #图片分类
        item["category"] = response.css('div.tit_top+a>img::attr(alt)').extract_first().replace('/','_')        
        #图片名称
        item["name"] = item["category"] + '_' + response.css('div.tit_top+a::attr(href)').extract_first().replace('.html','').replace('/','_')            
        #图片链接
        item["image_urls"] = response.css('div.tit_top+a>img::attr(src)').extract_first()  
        
        yield item
        
        #下一页
        next_page = response.css("div.pages ul li:last-child a::attr(href)").extract_first()        
        if next_page and next_page != '#':          #链接为有效链接地址
            next_page = parse.urljoin(response.url,next_page) 
            yield scrapy.Request(url = next_page,callback = self.parse_detail)
         
    
