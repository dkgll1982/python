# coding:utf-8
import requests
import bs4
from bs4 import BeautifulSoup


#定义获取网页源码函数
def get_html(url):
    try:
        r = requests.get(url, timeout=20)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


#定义从网页源码获取数据并处理数据函数
def get_data(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            td = tr('td')
            t = [td[0].string, td[1].string, td[2].string,td[3].string]  # 把每个学校解析处的数据各自装到一个列表中
            list.append(t)   # 把每个学校信息列表都追加到一个大列表中，方便后面写入文件
                # return list  # 不能加return,造成的后果就是第一次循环时就把结果返回出去了，只取到了第一条数据


#定义把数据写入文件函数"""
def write_data(ulist, num):   # num参数，控制提取多少组数据写入文件
    for i in range(num):
        u = ulist[i]
        with open(r'backup\test.txt', 'a') as data:
            print(u, file=data)


if __name__ == '__main__':
    list = []  # 我之前是把list=[]放到get_data()函数的for循环里面了，导致每次循环都会先清空列表，然后再追加数据，结果最后遍历完只剩最后一组数据。。。
    url = 'http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2018.html'
    html = get_html(url)
    get_data(html, list)
    write_data(list, 50)
