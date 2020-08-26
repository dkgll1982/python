import scrapy
from lianjia.items import LianjiaItem

# 为方便更改，设置全局变量，爬取页数
page = 10 

class NewhouseSpider(scrapy.Spider):
    name = 'newhouse' 
    # 允许域名
    allowed_domains = ["bj.fang.lianjia.com"] 
    # 新建爬取链接为空列表 
    start_urls = [] 
    if page >= 1: 
        for i in range(1 , page + 1): 
            # 依次将第1页到第page页放入开始连接队列 
            start_urls.append("https://bj.fang.lianjia.com/loupan/nhs1pg{}".format(i)) 
    else: 
        print("page must >= 1") 
    
    def parse(self, response): 
        item = LianjiaItem()
        # 迭代爬取每个li区块
        for each in response.xpath("/html/body/div[4]/ul[2]/*"): 
            item['name'] = each.xpath("div/div[1]/a/text()").extract() 
            item['resblock_type'] = each.xpath('div/div[1]/span[@class="resblock-type"]/text()').extract() 
            # span[@class="resblock-type"]为限定属性class值为"resblock-type"的区块 
            item['sale_status'] = each.xpath('div/div[1]/span[@class="sale-status"]/text()').extract() 
            item['location0'] = each.xpath('div/div[2]/span[1]/text()').extract() 
            item['location1'] = each.xpath('div/div[2]/span[2]/text()').extract() 
            item['location2'] = each.xpath('div/div[2]/a/text()').extract() 
            item['num_room'] = [] 
        for room in each.xpath('div/a/*'): 
            item['num_room'] += room.xpath('text()').extract() 
            # 去除掉列表中为'/'的元素 
            if item['num_room'][-1] == '/': 
                del item['num_room'][-1] 
        item['area'] = each.xpath('div/div[3]/span/text()').extract() 
        item['price_pre_spm'] = ['均价{}元/平方米'.format(each.xpath('div/div[6]/div[1]/span[1]/text()').extract()[0])] 
        item['price_pre_suite'] = each.xpath('div/div[6]/div[2]/text()').extract() 
        # 传递数据 
        yield item

# 来源: BoyInTheSun
# 文章作者: BoyInTheSun
# 文章链接: https://boyinthesun.cn/post/python-scrapy/
# 本文章著作权归作者所有，任何形式的转载都请注明出处。来自阳光男孩的博客www.boyinthesun.cn
