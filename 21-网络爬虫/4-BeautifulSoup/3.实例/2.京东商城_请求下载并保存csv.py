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

    all_items = page.find_all('li', attrs={'class':'gl-item'})

    with open(r"backup\jd-Computer.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        fields = ('ID', '名称', '价格')
        writer.writerow(fields)

        for all in all_items:
            Computer_id = all["data-sku"]
            print(f"电脑ID为：{Computer_id}")

            Computer_name = all.find('div', attrs={'class':'p-name p-name-type-2'}).find('em').text
            print(f"电脑的名称为：{Computer_name}")

            Computer_price = all.find('div', attrs={'class':'p-price'}).find('i').text
            print(f"电脑的价格为：{Computer_price}元")

            row = []
            row.append(Computer_id)
            row.append(Computer_name)
            row.append(str(Computer_price) + "元")
            writer.writerow(row)

def main():
    headers = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "referer": "https://passport.jd.com"
    }
    URL = "https://search.jd.com/Search?keyword=macbook%20pro&enc=utf-8&suggest=5.def.0.V09&wq=mac&pvid=d3b040ed68154b06a9ff9532a10b4cac"

    find_Computer(URL, headers=headers)

if __name__ == '__main__':
    main()
