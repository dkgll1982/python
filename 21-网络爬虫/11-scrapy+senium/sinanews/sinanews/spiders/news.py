import scrapy
from ..items import SinanewsItem
from selenium import webdriver
 
class NewsSpider(scrapy.Spider):
  name = 'news'
  # allowed_domains = ['www.xxx.con']
  start_urls = ['https://news.163.com/']
  # 浏览器实例化的操作只会被执行一次
  bro = webdriver.Chrome(executable_path='chromedriver.exe')
  
  # 最终存放的就是5个板块对应的url
  urls = []                 
 
  def parse(self, response):
    li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
    for index in [3,4,6,7,8]:
      li = li_list[index]
      new_url = li.xpath('./a/@href').extract_first()
      self.urls.append(new_url)
 
      # 对5大板块对应的url进行请求发送
      yield scrapy.Request(url=new_url,callback=self.parse_news)
 
  # 用来解析每一个板块对应的新闻数据【只能解析到新闻的标题】
  def parse_news(self,response):
    div_list = response.xpath('//div[@class="ndi_main"]/div')
    for div in div_list:
      title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
      news_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
      # 实例化item对象，将解析到的标题和内容存储到item对象中
      item = SinanewsItem()
      item['title'] = title
      # 对详情页的url进行手动请求发送获得新闻内容
      yield scrapy.Request(url=news_detail_url,callback=self.parse_detail,meta={'item':item})
 
  def parse_detail(self,response):
    item = response.meta['item']
    # 通过response解析出新闻内容
    content = response.xpath('//div[@id="endText"]//text()').extract()
    content = ''.join(content)
 
    item['content'] = content
    yield item
 
  def close(self,spider):
    # 当爬虫结束之后，调用关闭浏览器方法
    print('爬虫整体结束~~~~~~~~~~~~~~~~~~~')
    self.bro.quit()  