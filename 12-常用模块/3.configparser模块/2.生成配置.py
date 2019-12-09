import os
import configparser #引入模块 
curpath = os.path.dirname(os.path.realpath(__file__))
path1 = os.path.join(curpath, "setting.ini")
path2 = os.path.join(curpath, "copy.cnf") 

config = configparser.ConfigParser()    #类中一个方法 #实例化一个对象

config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11':'yes'
                     }	#类似于操作字典的形式

config['bitbucket.org'] = {'User':'Atlan'} #类似于操作字典的形式

config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}

#通过字典创建
config.read_dict({
                'section1': {'key1': 'value1',
                              'key2': 'value2',
                              'key3': 'value3'},
                'section2': {'keyA': 'valueA',
                              'keyB': 'valueB',
                              'keyC': 'valueC'},
                 'section3': {'foo': 'x',
                              'bar': 'y',
                              'fun': 'z'}
                  })

config.read_file(open(path1, encoding="utf-8"))

with open(path2, 'w') as configfile: 
   config.write(configfile)	#将对象写入文件
