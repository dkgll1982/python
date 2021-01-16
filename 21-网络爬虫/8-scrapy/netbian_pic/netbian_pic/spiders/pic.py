import scrapy
from ..items import NetbianPicItem

class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kdongman/']      #爬取起始页：彼岸4K动漫  

    def parse(self, response):
        # 当前页的所有图片链接
        link_list = response.xpath('//ul[@class="clearfix"]/li/a/@href').extract()
        for link in link_list: 
            url = response.urljoin(link)
            # 转到图片详细页
            yield scrapy.Request(url = url, callback = self.parse_detail)

        # 下一页的链接
        next_link = response.xpath("//div[@class='page']/a[contains(text(),'下一页')]")
        if next_link:
            next_url = response.urljoin(next_link.xpath("@href").get()) 
            yield scrapy.Request(url = next_url, callback = self.parse)
    
    #图片详情页        
    #python中get和getall_Scrapy框架get() 、getall() 、extract() 、extract_first()的区别:https://blog.csdn.net/weixin_39720181/article/details/110703512    
    def parse_detail(self,response):
        item = NetbianPicItem() 
        item['title'] = response.xpath('//div[@class="photo-hd"]/h1/text()').get()
        item['link'] = response.urljoin(response.xpath('//div[@class="photo-pic"]/a/img/@src').get()) 
        yield item