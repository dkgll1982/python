import socketserver
import json
import os,sys
import configparser
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
import hashlib

STATUS_CODE = {
    250:'Invalid cmd',
    251:"Invalid cmd format,e.g:{'action':'get','fimename':'test.py','size':1223}",
    252:"Invalid auth data",
    253:"Worng username or password",
    254:"Passed authentication",
    255:"Filename doesn't provided",
    256:"Filename does't exists on server",
    257:"read to send file",
    258:"md5 verification"
}

class FtpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address),end='')
                if self.data:
                    print(self.data.decode('gbk'))
                else:
                    print('client closde...')
                    break
                data = json.loads(self.data.decode('gbk'))
                if data.get('action') is not None:
                    if hasattr(self, "_%s" % data.get('action')):
                        func = getattr(self, "_%s" % data.get('action')) 
                        func(data)
                    else:
                        print('invalid cmd') 
                        self.send_response(250)
                else:
                    print('invalid cmd format')
                    self.send_response(251)
        except Exception as e:
            print(self.client_address, "连接断开")
        finally:
            self.request.close()
    
    def send_response(self,status_code,data=None):
        '''向客户端返回数据'''
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode('gbk'))

    def _auth(self, *args, **kwargs):
        data = args[0]
        print(data.get("username"),data.get("password"))
        if data.get("username") is None or data.get("password") is None:
            self.send_response(252)
            
        user = self.authenticate(data.get("username"),data.get("password"))
        if user is None:
            self.send_response(253)
        else:
            print('passed authentication',user)  
            self.user = user
            self.send_response(254)

    def authenticate(self,username,password):
        '''验证用户合法性,合法就返回用户数据'''
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print('pass auth..',username)
                config[username]['Username'] =username
                return config[username] 

    def setup(self):
        print("before handle,连接建立：", self.client_address)

    def finish(self):
        print("finish run after handle")

    def _put(self, *args, **kwargs):
        pass

    def _get(self, *args, **kwargs): 
        data = args[0]
        if (data.get('filename')) is None:
            self.send_response(255) 
            
        user_home_dir = "%s/%s" %(settings.USER_HOME,self.user["username"]) 
        file_abs_path = "%s/%s" %(user_home_dir,data.get('filename')) 
        print('file abs path:',file_abs_path)

        if os.path.isfile(file_abs_path):
            file_obj = open(file_abs_path,"rb")
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257,data={'file_size':file_size}) 

            if data.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    ######################################################################################
                    # 2019-12-11:花了三天时间才定位到粘包的问题,在此处sleep一下,可以解决发送粘包的问题.....   #
                    # 标记：需要想别的办法                                                                 #
                    # import time                                                                        #
                    # time.sleep(1)                                                                      #
                    ######################################################################################

                    #######################################################################################
                    #2019-12-11:（解决粘包的问题）接收客户端确认消息
                    self.request.recv(1)
                    #######################################################################################
                    self.send_response(258,data={'md5':md5_val})
                    print({'md5':md5_val})
                print('send file done!...')
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print('send file done。...')
        else:
            self.send_response(256)

    def _ls(self, *args, **kwargs):
        pass

    def _cd(self, *args, **kwargs):
        pass

    def _mv(self, *args, **kwargs):
        pass
