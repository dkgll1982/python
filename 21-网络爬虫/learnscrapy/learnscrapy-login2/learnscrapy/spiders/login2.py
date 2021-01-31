import scrapy
from scrapy import Request
from ..items import Login2ScrapyItem

class SSR1(scrapy.Spider):
    name = 'login2'

    #在 start_requests 中进行登录动作，scrapy 会自动处理 cookie，所以在回调函数中进行正常的翻页爬取就可以了
    def start_requests(self):
        urls = ['https://login2.scrape.center/login']
        for url in urls:
            # 添加需要提交的表单参数
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata={'username': 'admin', 'password': 'admin'})

    def parse(self, response, **kwargs):
        for a in range(1, 11):
            yield Request(url=response.urljoin(f'/page/{a}'), callback=self.parse_page)

    def parse_page(self, response):
        result = response.xpath('//div[@class="el-card item m-t is-hover-shadow"]')
        for a in result:
            item = Login2ScrapyItem()
            item['title'] = a.xpath('.//h2[@class="m-b-sm"]/text()').get()
            item['fraction'] = a.xpath('.//p[@class="score m-t-md m-b-n-sm"]/text()').get().strip()
            item['country'] = a.xpath('.//div[@class="m-v-sm info"]/span[1]/text()').get()
            item['time'] = a.xpath('.//div[@class="m-v-sm info"]/span[3]/text()').get()
            item['date'] = a.xpath('.//div[@class="m-v-sm info"][2]/span/text()').get()
            url = a.xpath('.//a[@class="name"]/@href').get()
            yield Request(url=response.urljoin(url), callback=self.parse_person, meta={'item': item})

    def parse_person(self, response):
        item = response.meta['item']
        item['director'] = response.xpath('//div[@class="directors el-row"]//p[@class="name text-center m-b-none m-t-xs"]/text()').get()
        yield item
