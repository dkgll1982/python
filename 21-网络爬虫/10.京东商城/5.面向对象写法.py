#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 完善爬虫安全措施（headers，proxies，retries，delay, timeout）
# 参考链接：https://blog.csdn.net/qq_39591494/article/details/85922317

import json
import re
import time
import csv
from urllib.parse import urlparse
from datetime import datetime, timedelta
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


class Throttle:
    """阀门类，对相同域名的访问添加延迟时间，避免访问过快
    """
    def __init__(self, delay):
        # 延迟时间，避免访问过快
        self.delay = delay
        # 用字典保存访问某域名的时间
        self.domains = {}
        
    def wait(self, url):
        """对访问过的域名添加延迟时间
        """
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()


class Phone:
    def __init__(self, headers=None, num_retries=3, proxies=None, delay=5, timeout=30):
        self.headers = headers
        self.num_retries = num_retries
        self.throttle = Throttle(delay)
        self.timeout = timeout
        self.proxies = proxies

    def download(self, url, is_json=False):
        print('下载页面:', url)
        self.throttle.wait(url)
        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=self.timeout)
            print(response.status_code)
            if response.status_code == 200:
                if is_json:
                    return response.json()
                else:
                    return response.content
            return None
        except RequestException as e:
            print('error:', e.response)
            html = ''
            if hasattr(e.response, 'status_code'):
                code = e.response.status_code
                print('error code:', code)
                if self.num_retries > 0 and 500 <= code < 600:
                    # 遇到5XX 的错误就重试
                    html = self.download(url)
                    self.num_retries -= 1
            else:
                code = None
        return html

    def write_csv(self, all_list):
        """"""
        with open(r"backup\yk.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            fields = ('phone_ID', '名称', '价格', '累计评价', '好评率')
            writer.writerow(fields)
            for row in all_list:
                writer.writerow(row)

    def find_all(self, url):
        r = self.download(url)
        soup_all = BeautifulSoup(r, 'lxml')
        sp_all_items = soup_all.find_all('li', attrs={'class': 'gl-item'})
        print(f"共找到{len(sp_all_items)}件商品....".center(50, "-"))
        data_list = []
        for soup in sp_all_items:
            # 取手机名称
            phone_name = soup.find('div', attrs={'class': 'p-name p-name-type-2'}).find('em').text
            print(phone_name)

            # 取手机价格
            phone_price = soup.find('div', attrs={'class': 'p-price'}).find('i').text
            print(phone_price)

            # 取手机ID
            item_id = soup['data-sku']
            print('item-id', item_id)

            ID_URL = f"https://club.jd.com/comment/productCommentSummaries.action?referenceIds={item_id}"
            comment_count, good_rate = self.get_json(ID_URL)
            print('评价人数：', comment_count)
            print('好评率：', good_rate)

            row = []
            row.append(item_id)
            row.append(phone_name)
            row.append(str(phone_price) + "￥")
            row.append(comment_count)
            row.append(str(good_rate) + "%")
            data_list.append(row)

        return data_list

    def get_json(self, id_url):
        data = self.download(id_url, is_json=True)
        result = data['CommentsCount']
        for i in result:
            return i["CommentCountStr"], i["GoodRateShow"]

    def fetch_data(self, jd_url, page_start, page_end, page_offset):
        all_list = []
        for page in range(page_start, page_end, page_offset):
            data_list = self.find_all(jd_url.format(page))
            all_list += data_list   
        self.write_csv(all_list)


def main():
    headers = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "referer": "https://www.jd.com"
    }

    jd_html = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.def.0.V06&wq=sho&cid2=653&cid3=655&page={}&s=113&click=0'"

    # start = time.time()
    spider = Phone(headers=headers)
    spider.fetch_data(jd_html, 1, 5, 2)
    # stop = time.time()
    # print(f'抓取结束，一共用时时间为：{(start - stop)}秒......')


if __name__ == "__main__":
    main()
