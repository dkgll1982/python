import base64
import json
import ssl
import requests

# Python网络爬虫报错“SSL: CERTIFICATE_VERIFY_FAILED”的解决方案
#参考链接：https://blog.csdn.net/Hudeyu777/article/details/76021573
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    # execute(['scrapy', 'crawl', 'spa1'])

    data = {
        'username': 'admin',
        'password': 'admin'
    }
    url = 'https://login1.scrape.center/'
    # 注意这里是 get 请求，如果是 post 请求的话会报405错误代码。
    r = requests.get(url=url, data={'token': base64.b64encode(json.dumps(data).encode())},verify=False)
    print(r.text)
    print(r.status_code)
    print(r.headers)
