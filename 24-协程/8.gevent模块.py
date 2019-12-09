# coding:utf8
import requests
import gevent
from gevent import monkey
monkey.patch_all()      # 用于将标准库中大部分阻塞式调用修改为协作式运行


def fetch(url):
    print("get: {}".format(url))
    response = requests.get(url).content
    print("{}: {}".format(url, len(response)))


if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(fetch, "https://stackoverflow.com/"),
        gevent.spawn(fetch, "https://www.douban.com"),
        gevent.spawn(fetch, "https://www.github.com")
    ])