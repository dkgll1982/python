from concurrent.futures import ThreadPoolExecutor
import requests
import time

def get(url):
    print('GET %s'%url)
    res = requests.get(url)
    time.sleep(3)
    return {"url":url,"content":res.text}

def parse(res):
    res =res.result()
    print('%s parse res is %d'%(res["url"],len(res["content"])))

if __name__ == "__main__":
    urls=[
        "http://c.biancheng.net/view/2627.html",
        "https://blog.csdn.net/weixin_33851429/article/details/94067841",
        "https://blog.51cto.com/ruifar/2445384",
        "https://blog.csdn.net/qq_37174887/article/details/98876216",
        "http://www.sina.com/"
    ]

    pool = ThreadPoolExecutor(2)

    for url in urls:
        pool.submit(get,url).add_done_callback(parse)