import scrapy
from ..items import QiushibaikeItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # 允许爬取的域名（如果遇到非该域名的url则爬取不到数据）
    allowed_domains = ['https://www.qiushibaike.com/']
    # 起始爬取的url
    start_urls = ['https://www.qiushibaike.com/text']

    # 爬取多页
    pageNum = 1  # 起始页码
    # 统用的url模板（不可变）
    url = 'https://www.qiushibaike.com/text/page/%s/'  # 每页的url

    # 访问起始URL并获取结果后的回调函数，该函数的response参数就是向起始的url发送请求后，获取的响应对象.该函数返回值必须为可迭代对象或者NUll
    def parse(self, response):
        # print(response.text)  # 获取字符串类型的响应内容
        # 获取作者名称和内容
        # print(response.body)  # 获取字节类型的相应内容
        # xpath为response中的方法，可以将xpath表达式直接作用于该函数中
        odiv = response.xpath('//div[@class="col1 old-style-col1"]/div')
        # print(len(odiv))
        content_list = []  # 用于存储解析到的数据
        for div_item in odiv:
            # xpath函数返回的为列表，列表中存放的数据为Selector类型的数据。
            # 我们解析到的内容被封装在了Selector对象中，需要调用extract()函数将解析的内容从Selecor中取出。
            author = div_item.xpath('.//div[1]/a[2]/h2/text() | .//div[1]/span/h2/text()')[0].extract()
            content = div_item.xpath('.//div[@class="content"]/span/text()').extract()
            content = ''.join(content)  # 列表转换为字符串
            # 打印展示爬取到的数据
            # print(author, content)
            # print(content)
            author = author.strip('\n')  # 过滤空行
            content = content.strip('\n')
            # 将解析到的数据封装至items对象中
            item = QiushibaikeItem()
            item['author'] = author
            item['content'] = content
            print(author)

            yield item  # 提交item到管道文件（pipelines.py）

        # 爬取所有页码数据
        print('pageNum={}'.format(self.pageNum))
        if self.pageNum < 13:  # 一共爬取13页（共13页）
            self.pageNum += 1
            new_url = format(self.url % self.pageNum)
            print(new_url)
            # 递归爬取数据：callback参数的值为回调函数（将url请求后，得到的相应数据继续进行parse解析），递归调用parse函数
            # 在 scrapy.Request() 函数中将参数 dont_filter=True 设置为 True,使 requests 不被过滤:
            yield scrapy.http.Request(url=new_url, callback=self.parse, dont_filter=True)