#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-08-26 09:37:36 
# @Remark: 人生苦短，我用python！
# 参考链接：https://blog.csdn.net/weixin_45335208/article/details/103351806

import scrapy
from ..items import Wangzherongyao2Item

class PfSpider(scrapy.Spider):
    name = 'pf'
    allowed_domains = ['pvp.qq.com']
    start_urls = ['https://pvp.qq.com/web201605/herolist.shtml']

    def parse(self, response):
        pf_urls = response.xpath('//ul[@class="herolist clearfix"]/li/a/@href').extract()
        for pf_url in pf_urls:
            yield scrapy.Request(url='https://pvp.qq.com/web201605/%s' % pf_url, callback=self.pf_parse)

    def pf_parse(self, response):
        item = Wangzherongyao2Item()
        item['hero_name'] = response.xpath('//h2[@class="cover-name"]/text()').extract_first()
        # '圣骑之力&0|死亡骑士&1|狮心王&13|心灵战警&12' ==》 ['圣骑之力', '死亡骑士', '狮心王', '心灵战警']
        item['pf_names'] = response.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname').re('(.*?)\&\\d+\|?')
        item['image_urls'] = []
        for num in range(1, len(item['pf_names'])+1):
            # //game.gtimg.cn/imgs/yxzj/img201606/heroimg/166/166-mobileskin-1.jpg
            # 去除-后面的字符，再重新进行拼接
            image_url_head = response.xpath('//a[@class="hero-video"]/img/@src').extract_first()[:-5]
            image_url = "https:{}{}.jpg".format(image_url_head, num)
            item['image_urls'].append(image_url)
        yield item