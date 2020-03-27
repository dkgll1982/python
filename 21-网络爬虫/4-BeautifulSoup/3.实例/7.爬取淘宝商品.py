# coding: utf-8

import requests
import re
import requests.exceptions

def get_html(url):
    """获取源码html"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'cookie': 'thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; cna=crnTFepEwzACAToxLRJUH5UE; miid=1428979935883017033; tracknick=dkgll; _cc_=UIHiLt3xSw%3D%3D; tg=0; enc=Gv0PWifHC8FqjD75J46hPE2W3%2BZc27XmCYmOlr5bLbQRfNgVC8r8bHlmJuJA3Wq4cMMKY%2FzEdwOVMNuL6J6iRA%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; t=718176f55972b17098d0df55b042ed14; _uab_collina=157907483098426009555682; x5sec=7b227365617263686170703b32223a226366626461336362666562366430333636336236646336653739313333326134434a574b2b2f4146454f612f692f6a6d3962325169414561436a557a4e7a597a4d446b334f7a453d227d; JSESSIONID=47382382FE152816C20DEF463A472D5F; isg=BFBQD4UlOs3D9OWbMWJ5UH22IZ6iGTRjZlV1-0ohHKt-hfAv8ikE86a3WU1lTuw7; l=cBO6XdxuqRLuiSOEBOCanurza77OSIRYYuPzaNbMi_5C96T6I5QOovJGeF96VjWd9WYB4WtSLwv9-etkZqx4rv--g3fP.'
    }
    try:
        r = requests.get(url=url,headers=headers, timeout=10)
        r.encoding = r.apparent_encoding
        return r.text 
    except requests.exceptions as e:
        print(e) 

def get_data(html, goodlist):
    """使用re库解析商品名称和价格
    tlist:商品名称列表
    plist:商品价格列表"""
    tlist = re.findall(r'\"raw_title\"\:\".*?\"', html)
    plist = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
    for i in range(len(tlist)):
        title = eval(tlist[i].split(':')[1])  # eval()函数简单说就是用于去掉字符串的引号
        price = eval(plist[i].split(':')[1])
        goodlist.append([title, price])


def write_data(list, num): 
    for i in range(num):  # num控制把爬取到的商品写进多少到文本中
        u = list[i]
        with open(r'backup\taobao.txt', 'a') as data:
            print(u, file=data)


def main():
    goods = '初中名著'
    depth = 10   # 定义爬取深度，即翻页处理
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)  # 因为淘宝显示每页44个商品，第一页i=0,一次递增
            html = get_html(url)
            get_data(html, infoList)
        except:
            continue
    write_data(infoList, len(infoList))


if __name__ == '__main__':
    main()