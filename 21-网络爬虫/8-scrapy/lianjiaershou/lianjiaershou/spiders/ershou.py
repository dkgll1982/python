#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : guojun
# @Company : 航天神舟智慧系统技术有限公司
# @Site    : https://user.qzone.qq.com/350606539/main
# @Date    : 2020-08-26 16:05
# @File    : main
# @Software: PyCharm
# 参考链接：https://boyinthesun.cn/post/python-scrapy2/

import scrapy
from ..items import LianjiaershouItem

# 为了方便更改，设置全局变量
page = 100          # 爬取页数
area = "haidian"    # 爬取城区

class ErshouSpider(scrapy.Spider):
    name = 'ershou'
    allowed_domains = ['bj.lianjia.com']
    start_urls = []
    # 依次将第1页到第page页放入开始连接队列
    for i in range(1, page + 1):
        start_urls.append("https://bj.lianjia.com/ershoufang/{}/pg{}/".format(area, i))
    # 如果你希望一次爬取多个城区，可以使用如下语句
    '''
    areas = ['dongcheng', 'xicheng', 'haidian', 'chaoyang']
    for each in areas:
        for i in range(1, page+1):
            start_urls.append("https://bj.lianjia.com/ershoufang/{}/pg{}/".format(each, i))
    '''

    def parse(self, response):
        item = LianjiaershouItem()
        for each in response.xpath("/html/body/div[4]/div[1]/ul/*"):
            # 如果你一次性爬取了多个城区，可以使用该语句
            # item['城区'] = response.url.split('/')[-3]
            item['标题'] = each.xpath("div/div[1]/a/text()").extract()[0]
            item['小区'] = each.xpath("div/div[2]/div/a[1]/text()").extract()[0]
            item['区域'] = each.xpath("div/div[2]/div/a[2]/text()").extract()[0]
            # 由于信息以字符串形式存在，并以' | '分隔，故创建临时变量，分割字符串，存为列表
            temp = each.xpath("div/div[3]/div/text()").extract()[0].split(' | ')
            # temp[0]的格式是n室m厅
            item['户型_室'] = temp[0][0]
            item['户型_厅'] = temp[0][-2]
            item['面积'] = temp[1][:-2]         # 去除汉字'平米'
            item['朝向'] = temp[2]
            item['装修'] = temp[3]
            item['楼层'] = temp[4]
            item['建成年份'] = temp[5][:-2]     # 去除汉字'年建'
            if len(temp) <= 6 or temp[6] == '暂无数据':
                item['建筑结构'] = 'N/A'
            else:
                item['建筑结构'] = temp[6]
            temp = each.xpath("div/div[4]/text()").extract()[0].split(' / ')
            item['关注人数'] = temp[0][:-3]
            # 日期格式可分为 n天以前前 n个月以前 一年前
            if temp[1][1] == '天':
                item['已发布日'] = int(temp[1][0])
            elif temp[1][1] == '个':
                item['已发布日'] = int(temp[1][0]) * 30
            else:
                item['已发布日'] = 360
            if each.xpath("div/div[5]/span[@class='taxfree']/text()").extract():
                item['满五'] = True
            else:
                item['满五'] = False
            if each.xpath("div/div[5]/span[@class='five']/text()").extract():
                item['满二'] = True
            else: item['满二'] = False
            if each.xpath("div/div[5]/span[@class='subway']/text()").extract():
                item['近地铁'] = True
            else:
                item['近地铁'] = False
            item['总价'] = each.xpath("div/div[6]/div[1]/span/text()").extract()[0]
            item['单价'] = each.xpath("div/div[6]/div[2]/span/text()").extract()[0][2:-4] # 去除汉字'单价*元/平米'
            yield item

            # 来源: BoyInTheSun
            # 文章作者: BoyInTheSun
            # 文章链接: https: // boyinthesun.cn / post / python - scrapy2 /
            # 本文章著作权归作者所有，任何形式的转载都请注明出处。来自阳光男孩的博客www.boyinthesun.cn
