import json
import time
import requests 
# 验证码类型：http://www.yundama.com/price.html

#2020-08-03测试已跑路
class YDMHttp:
    apiurl = 'http://api.yundama.com/api.php'
    # 使用你自己的云打码账户：
    username = 'dkgll'                          # 你充钱的那个用户名
    password = 'tggcTGGC!@#$1234'               # 密码
    appid = '10457'                             # 软件代码，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '40359b8c431f5ba11ae1c358ab6cbac3' # 通讯秘钥，开发者分成必要参数。登录开发者后台【我的软件】获得！

    def __init__(self,  filename, codetype, timeout, username=None, password=None, appid=None, appkey=None):
        """
        :param filename: 图片路径
        :param codetype: 验证码类型，你一定要请参考：http://www.yundama.com/price.html
        :param timeout: 识别验证码时的超时时间（秒）
        """
        self.filename = filename
        self.codetype = codetype
        self.timeout = timeout
        # 登录云打码
        uid = self.login()
        # print(f'uid: {uid}')
        # 查询余额
        balance = self.balance()
        # print(f'余额：{balance}')

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password,
                'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password,
                'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password,
                'appid': self.appid, 'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password,
                'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self):
        cid = self.upload(self.filename, self.codetype, self.timeout)
        if (cid > 0):
            for i in range(0, self.timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password,
                'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb')
        res = requests.post(url, files=files, data=fields)
        return res.text


if __name__ == '__main__':
    # 初始化
    ydm = YDMHttp(filename=r'backup\爬虫\验证码\code1.jpeg', codetype = '1004', timeout = 60)

    # 开始识别图片验证码
    cid, result = ydm.decode()
    print(f'cid: {cid}', )
    print(f'识别结果：{result}')