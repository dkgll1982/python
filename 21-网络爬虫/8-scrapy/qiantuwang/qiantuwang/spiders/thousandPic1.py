# -*- coding: utf-8 -*-
import scrapy
# 这里使用import或是from的方式都行，关键要看当前项目在pycharm的打开方式，是否是作为一个项目打开的，建议使用这一种方式。
import qiantuwang.items as items
# 使用from 这种方式，qiantuwang 需要作为一个项目打开。
# from qiantuwang.items import qiantuwangItem

class thousandpic1Spider(scrapy.Spider):
    name = 'thousandPic1'                         #爬虫名称
    allowed_domains = ['58pic.com']               #爬虫作用范围
    start_urls = ['https://www.58pic.com/c/'] 

    def parse(self, response): 
        '''
        查看页面元素
         /html/body/div[4]/div[3]/div/a/p[2]/span/span[2]/text()
          因为页面中 有多张图，而图是以 /html/body/div[4]/div[3]/div[i]  其中i  为变量 作为区分的 ，所以为了获取当前页面所有的图
          这里 不写 i 程序会遍历 该 路径下的所有 图片。
        '''

        item = items.qiantuwangItem()
        
        # author作者
        author = response.xpath("//span[@class='usernameColor']/text()").extract()
        # theme主题
        theme = response.xpath("//span[@class='fl info-h1']/text()").extract()
        # 使用爬虫的log方法在控制台输出爬取的内容。
        self.log(author)
        self.log(theme)
        
        # 使用遍历的方式 打印出 爬取的内容，因为当前一页有20张图片。
        for i in range(1, len(author)):
            print(i,' **** ',theme[i - 1], ': ',author[i - 1] )

        item['author'] = author
        item['theme']  = theme

        yield item