#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import csv
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def download(url, headers, num_retries=3):
    print("download", url)
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.content
        return None

    except RequestException as e:
        print(e.response)
        html = ""
        if hasattr(e.response, 'status_code'):
            code = e.response.status_code
            print('error code', code)
            if num_retries > 0 and 500 <= code < 600:
                html = download(url, headers, num_retries - 1)
        else:
            code = None
    return html


def find_Computer(url, headers):
    r = download(url, headers=headers)
    page = BeautifulSoup(r, "lxml")
    all_items = page.find_all('li', attrs={'class' : 'gl-item'})

    with open(r"backup\Computer2.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        fields = ('ID', '名称', '价格', '评论数', '好评率')
        writer.writerow(fields)

        for all in all_items:
            # 取每台电脑的ID
            Computer_id = all["data-sku"]
            print(f"电脑ID为：{Computer_id}")

            # 取每台电脑的名称
            Computer_name = all.find('div', attrs={'class':'p-name p-name-type-2'}).find('em').text
            print(f"电脑的名称为：{Computer_name}")

            # 取每台电脑的价格
            Computer_price = all.find('div', attrs={'class':'p-price'}).find('i').text
            print(f"电脑的价格为：{Computer_price}元")

            # 取每台电脑的Json数据(包含 评价等等信息)
            Comment = f"https://club.jd.com/comment/productCommentSummaries.action?referenceIds={Computer_id}"
            comment_count, good_rate = get_json(Comment)
            print('评价人数：', comment_count)
            print('好评率：', good_rate)

            row = []
            row.append(Computer_id)
            row.append(Computer_name)
            row.append(str(Computer_price) + "元")
            row.append(comment_count)
            row.append(good_rate)
            writer.writerow(row)


def get_json(url):
    data = requests.get(url).json()
    result = data['CommentsCount']
    for i in result:
        return i["CommentCountStr"], i["GoodRateShow"]


def main():
    headers = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "referer": "https://passport.jd.com"
    }
    URL = "https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&wq=%E7%94%B5%E8%84%91&pvid=1ff18312e8ef48febe71a66631674848"

    find_Computer(URL, headers=headers)

if __name__ == '__main__':
    main()
