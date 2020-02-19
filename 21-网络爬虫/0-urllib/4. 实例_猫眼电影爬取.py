#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-02-19 10:32:53 
# @Last Modified by: guojun 
# @Last Modified time: 2020-02-19 10:32:53 
# @Software: vscode 

#如果返回结果为[]，可以修改cookie参数

import urllib.request
import ssl
import re
import time
import random
import csv

ssl._create_default_https_context = ssl._create_unverified_context


class MaoYanSpider():
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset='
        self.headers = {
            'Cookie': '__mta=217864489.1581919450112.1582012903861.1582014666675.19; uuid_n_v=v1; uuid=4F816AA0514B11EA9AAB559E646C46DFEF08A7095E3A47109591C9E98B8EAB10; _lxsdk_cuid=17051bf33091a-063ccd137f1eec-6313f69-144000-17051bf330ac8; _lxsdk=4F816AA0514B11EA9AAB559E646C46DFEF08A7095E3A47109591C9E98B8EAB10; mojo-uuid=96237b04f540635c674fe6c5ba96e608; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=247346e5fb08ada76e66e3d60764d819a373abb488ab07e08a06c51abd6e3420; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1581919450,1581991474,1582005929; __mta=217864489.1581919450112.1581992041956.1582008769102.12; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1582014667; _lxsdk_s=17057ccbb56-b81-a5-fd4%7C%7C1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
        }

        # 写入csv
        csv_f = open(r'backup\爬虫\movies.csv', 'a', encoding='utf-8-sig')
        fieldnames = ['rank', 'pic', 'name', 'actor', 'time', 'grade']
        self.wirter = csv.DictWriter(csv_f, fieldnames)
        self.wirter.writeheader()  # 写头部

    def send_request(self, url):
        request = urllib.request.Request(url=url, headers=self.headers)

        response = urllib.request.urlopen(request)
        if response.status == 200:
            return response

    def parse(self, response):
        content = response.read().decode()
        pattern = re.compile(
            r'<dd>.*?>(.*?)<.*?data-src="(.*?)".*?<p.*?class="name">.*?>(.*?)<.*?<p.*?class="star">(.*?)<.*?<p.*?class="releasetime">(.*?)<.*?<i.*?>(.*?)</i>.*?<i.*?>(.*?)</i>.*?</dd>',
            re.S)

        # 2020-02-18页面解析正则模式
        # pattern = re.compile(
        #    r'<dd>.*?>(.*?)<.*?data-src="(.*?)".*?<p.*?class="name">.*?>(.*?)<.*?<p.*?class="star">(.*?)<.*?<p.*?class="releasetime">(.*?)<.*?<i.*?>(.*?)</i>.*?<i.*?>(.*?)<.*?</dd>',
        #    re.S)
        result = re.findall(pattern, content)
        print(result)
        for movie in result:
            dict_movie = {}
            dict_movie['rank'] = movie[0]
            dict_movie['pic'] = movie[1]
            dict_movie['name'] = movie[2]
            dict_movie['actor'] = movie[3]
            dict_movie['time'] = movie[4]
            dict_movie['grade'] = movie[5] + movie[6]
            if movie[0] is not None:
                self.write_csv(dict_movie)

    def write_csv(self, dict_movie):
        self.wirter.writerow(dict_movie,)

    def start(self):
        for i in range(1, 4):
            offset = (i - 1) * 10
            full_url = self.url + str(offset)
            print(full_url)
            response = self.send_request(full_url)
            self.parse(response)
            time.sleep(random.randint(1, 10))


if __name__ == '__main__':
    mys = MaoYanSpider()
    mys.start()
