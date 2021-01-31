import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..items import Antispider1ScrapyItem
import os

# scrapy_selenium用法：https://pypi.org/project/scrapy-selenium/


class AntiSpider(scrapy.Spider):
    name = 'antispider1'

    def start_requests(self):
        urls = ['https://antispider1.scrape.center/']
        for a in urls:
            ''' 
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support import expected_conditions as EC

            yield SeleniumRequest(
                url=url,
                callback=self.parse_result,
                wait_time=10,
                wait_until=EC.element_to_be_clickable((By.ID, 'someid'))
            )
            '''
            '''screenshot
            When used, selenium will take a screenshot of the page and the binary data of the .png captured will be added to the response `meta`:
            ```python
            yield SeleniumRequest(
                url=url,
                callback=self.parse_result,
                screenshot=True
            )
            '''
            '''script
            When used, selenium will execute custom JavaScript code.
            ```python
            yield SeleniumRequest(
                url,
                self.parse_result,
                script='window.scrollTo(0, document.body.scrollHeight);',
            )
            '''
            yield SeleniumRequest(url=a,
                                  callback=self.parse,
                                  wait_time=3,
                                  wait_until=EC.presence_of_element_located((By.CLASS_NAME, 'm-b-sm'))
                                  )

    def parse(self, response, **kwargs):
        file_path = r'data'
        if not os.path.exists(file_path):   # 判断是否存在该文件夹
            os.mkdir(file_path)             # 不存在的话就创建一个
        with open(r'data\html.txt','w') as f:
            f.write(response.text)
            
        result = response.xpath('//div[@class="el-card item m-t is-hover-shadow"]')
        for a in result:
            item = Antispider1ScrapyItem()
            item['title'] = a.xpath('.//h2[@class="m-b-sm"]/text()').get()
            item['fraction'] = a.xpath('.//p[@class="score m-t-md m-b-n-sm"]/text()').get().strip()
            item['country'] = a.xpath('.//div[@class="m-v-sm info"]/span[1]/text()').get()
            item['time'] = a.xpath('.//div[@class="m-v-sm info"]/span[3]/text()').get()
            item['date'] = a.xpath('.//div[@class="m-v-sm info"][2]/span/text()').get()
            url = a.xpath('.//a[@class="name"]/@href').get()
            print(response.urljoin(url))
            '''
            The request will be handled by selenium, and the request will have an additional `meta` key, 
            named `driver` containing the selenium driver with the request processed.
            ```python
            def parse_result(self, response):
            print(response.request.meta['driver'].title)
            '''
            yield SeleniumRequest(url=response.urljoin(url),
                                  callback=self.parse_person,
                                  meta={'item': item},
                                  wait_time=3,
                                  wait_until=EC.presence_of_element_located((By.CLASS_NAME, 'm-b-sm'))
                                  )

    def parse_person(self, response):
        item = response.meta['item']
        item['director'] = response.xpath('//div[@class="directors el-row"]//p[@class="name text-center m-b-none m-t-xs"]/text()').get()
        yield item
