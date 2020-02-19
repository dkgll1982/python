import urllib.request
import urllib.parse

class NeiHanSpider():
    def __init__(self):
        self.url = "https://www.neihanba.com/dz/{}.html"
        self.page = 0
    
    def send_request(self,url,page):
        print('正在爬取第{}页：地址：{}'.format(page,url)) 
        header = {'Referer':'jczl.com'}         #防盗链
        response = urllib.request.urlopen(url, data=None, cafile=None, capath=None, cadefault=False, context=None) 
        if response.status == 200:
            self.write_content(response.read(),page)
        else:
            print('爬取第{}页出错'.format(page))
            
    def write_content(self,content,page):
        with open(r'backup\爬虫\neihan8_%d.html'%page,'wb') as f:
            f.write(content)
            print('爬取第{}页成功！'.format(page))
    
    def start(self):
        while True:
            self.page +=1
            if self.page == 1: 
                self.send_request(self.url.format("index"),self.page)
            else: 
                self.send_request(self.url.format("list_{}".format(self.page)),self.page)
            inp = input('继续按任意键，退出按q键：')
            if inp =='q':
                break
                

if __name__ == "__main__":
    nhs = NeiHanSpider()
    nhs.start()