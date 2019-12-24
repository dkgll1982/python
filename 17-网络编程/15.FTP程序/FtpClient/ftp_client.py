#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-12-07 17:24:43 
# @Last Modified by: guojun 
# @Last Modified time: 2019-12-07 17:24:43 
# @Software: vscode 
import socket
import os,json,struct
import optparse
import getpass
<<<<<<< HEAD
import hashlib
import time
import math,sys
=======
<<<<<<< HEAD
import hashlib
import time
import math,sys
=======
import  hashlib
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
>>>>>>> 5c086a7ee8903ab9f617c5e6c4e89225b9241b7c

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip_address")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username info")
        parser.add_option("-p", "--password", dest="password", help="password info")
        self.options,self.args = parser.parse_args()
        self.verify_args(self.options,self.args)
        self.make_connection()
    
    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server,self.options.port))

    def verify_args(self,options,args):
        '''校验参数合法性'''
        if (options.username and not options.password) or (not options.username and options.password):
            exit('error: username and password must be provided together!')

        if options.server or options.port:
            #print(options)
<<<<<<< HEAD
            if options.port > 0 and options.port < 65535:
=======
<<<<<<< HEAD
            if options.port > 0 and options.port < 65535:
=======
            if options.port >0 and options.port <65525:
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
>>>>>>> 5c086a7ee8903ab9f617c5e6c4e89225b9241b7c
                return True
            else:
                exit('error:host port must in 0-65535')
        
    def authentifcate(self):
        '''用户验证的功能''' 
        if self.options.username: 
            return self.get_auth_result(self.options.username,self.options.password)
        else:
            retry_count = 0
            while retry_count<3:
                username = input('username:').strip()
                password = getpass.getpass('password:').strip()  
                return self.get_auth_result(username,password)
    
    def get_auth_result(self,user,password):
        data = {'action':'auth',
                'username':user,
                'password':password}
        #encode() 方法以指定的编码格式编码字符串，默认编码为 'utf-8'。
        print(data)
        self.sock.send(json.dumps(data).encode('gbk'))
        response = self.get_response() 
        if response.get('status_code') == 254:
            print('Passed authentication！')
            self.user = user 
            return True
        else:
            print(response.get('status_msg')) 
    
    def get_response(self):
        '''得到服务器端回复结果'''
        recv = self.sock.recv(1024) 
        data = json.loads(recv.decode('gbk'))
        return data

    def interactive(self):
        if self.authentifcate():
            print('---start interactive with you...')
            #用户验证通过
            while True:
                choice = input('[%s]:'%self.user).strip()
                if len(choice) == 0:continue
                cmd_list = choice.split()
<<<<<<< HEAD
                if hasattr(self,"_%s" %cmd_list[0]):
                    func = getattr(self,"_%s"%cmd_list[0]) 
=======
<<<<<<< HEAD
                if hasattr(self,"_%s" %cmd_list[0]):
                    func = getattr(self,"_%s"%cmd_list[0]) 
=======
                if hasattr(self,"_%s"%cmd_list[0]):
                    func = getattr(self,"_%s"%cmd_list[0])
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
>>>>>>> 5c086a7ee8903ab9f617c5e6c4e89225b9241b7c
                    func(cmd_list)
                else:
                    print("Invalid cmd.")

    def _md5_required(self,cmd_list):
        '''检测命令是否需要进行MD5验证'''
        if ('--md5' in cmd_list):
            return True

    def show_process(self,total):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5c086a7ee8903ab9f617c5e6c4e89225b9241b7c
        received_size = 0
        current_percent = 0
        while received_size < total:
            if int((received_size / total) * 100) > current_percent:
                #######################################
                #模拟进度条1
                #print('#',end='',flush=True)
                #######################################

                #######################################
                #模拟进度条2
                part = total / 50  # 1%数据的大小
                count = math.ceil(received_size / part)
                sys.stdout.write('\r')
                sys.stdout.write(('[%-50s]%.2f%%' % (('>' * count), received_size / total * 100)))
                sys.stdout.flush()
                #######################################

                current_percent = int((received_size / total) * 100)
            new_size = yield
            received_size += new_size 
 
<<<<<<< HEAD
=======
=======
        recive_size = 0
        current_percent = 0
        while recive_size < total:
            if (recive_size / total) * 100 > current_percent:
                print('#',end='',flush=True)
                current_percent =  (recive_size / total) * 100
            new_size = yield
            recive_size += new_size 

            new_size 
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
>>>>>>> 5c086a7ee8903ab9f617c5e6c4e89225b9241b7c
    def _get(self,cmd_list):
        print('get--',cmd_list)
        if len(cmd_list) == 1:
            print('no filename follows...')
            return  
        data_header = {
            'action':'get',
            'filename':cmd_list[1] 
        }
        if self._md5_required(cmd_list):
            data_header['md5'] = True

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5c086a7ee8903ab9f617c5e6c4e89225b9241b7c
        self.sock.send(json.dumps(data_header).encode('gbk'))
        response = self.get_response()
        print(response)
        if response['status_code'] == 257:  #ready to revice  
            base_file_name = cmd_list[1].split('/')[-1]            
            received_size = 0
            file_obj = open(BASE_DIR+'/'+base_file_name,'wb') 
            
            start = time.time()

            if self._md5_required(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_process(response['file_size']) #generator
                progress.__next__()
 
                while received_size < response['file_size']: 
                    data = self.sock.recv(4096) 
                    received_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        #######################################
                        #print('100%') 
                        #######################################

                        #######################################
                        sys.stdout.write('\r')
                        sys.stdout.write(('[%-50s]%.2f%%' % (('>' * 50), 100)))
                        sys.stdout.flush()
                        #######################################
                    file_obj.write(data)
                    md5_obj.update(data)
                else: 
                    print("\n--->file recive done!---")
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()  
                    print("md5_obj:",md5_val)

                    #######################################################################################
                    #2019-12-11:（解决粘包的问题）先发送消息到服务端
                    self.sock.send(b'1')            #send confirmation to server
                    #######################################################################################

                    md5_from_server = self.get_response() 
                    print('服务端文件信息—',md5_from_server)
                    if md5_from_server['status_code'] == 258:
                        if md5_from_server['md5'] == md5_val:
                            print('下载本地文件"%s"—md5值：%s,一致性校验成功!'%(base_file_name,md5_val))
            else:
                progress = self.show_process(response['file_size']) #generator
                progress.__next__()
                while received_size < response['file_size']: 
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        #######################################
                        #print('100%') 
                        #######################################

                        #######################################
                        sys.stdout.write('\r')
                        sys.stdout.write(('[%-50s]%.2f%%' % (('>' * 50), 100)))
                        sys.stdout.flush()
                        #######################################
                    file_obj.write(data) 
                else:
                    print("\n--->file recive done---")
                    file_obj.close()
            
            end = time.time()
            print("下载文件完成！！！""总耗时：%0.6fs"%(end -start)); 

<<<<<<< HEAD
=======
=======

        self.sock.send(json.dumps(data_header).encode('gbk'))
        response = self.get_response()
        print(response)
        if response['status_code'] == 257:  #ready to revice
            base_file_name = cmd_list[1].split('/')[-1]            
            recived_size = 0
            file_obj = open(BASE_DIR+'/'+base_file_name,'wb')
            if self._md5_required(cmd_list):
                md5_obj = hashlib.md5()

                progress = self.show_process(response['file_size']) #generator
                progress.__next__()
                
                while recived_size < response['file_size']:
                    data = self.sock.recv(4096)
                    recived_size += len(data)
                    try:
                        progress.send(len(data))
                    except  StopIteration as e:
                        print('100%')
                    
                    file_obj.write(data)
                    md5_obj.update(data)
                else:
                    print("--->file recive done---")
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    md5_from_server = self.get_response()
                    if md5_from_server['status_code'] == 258:
                        if md5_from_server['md5'] == md5_val:
                            print('%s 文件一致性校验成功'%base_file_name)
            else:
                while recived_size < response['file_size']:
                    data = self.sock.recv(4096)
                    recived_size += len(data)
                    file_obj.write(data) 
                else:
                    print("--->file recive done---")
                    file_obj.close()
>>>>>>> 8c71f90a755f435117c304b5b10d4370e123be32
>>>>>>> 5c086a7ee8903ab9f617c5e6c4e89225b9241b7c
if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()   #交互
