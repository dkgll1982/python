import urllib.request
import urllib.response
import urllib.parse
import urllib.error 

class TieBaSpider():
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?'

    def send_request(self, url, page):
        print('正在发送第{}页'.format(page))
        response = urllib.request.urlopen(url)
        self.write_file(response.read(),page)

    def write_file(self, content, page):
        print('正在保存第{}页'.format(page))
        with open(r'backup/tieba_{}.html'.format(page), 'wb') as f:
            f.write(content)

    def start(self):
        page = int(input('请输入要爬取的页码：'))
        for i in range(1, page+1):
            pn = (i-1)*50
            kw = {'kw': '美女', 'pn': pn}
            result = urllib.parse.urlencode(kw)
            full_url = self.url + result
            self.send_request(full_url,i)


if __name__ == '__main__':
    tbs = TieBaSpider()
    tbs.start()
