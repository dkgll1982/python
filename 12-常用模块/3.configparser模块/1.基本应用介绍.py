#参考链接：https://www.cnblogs.com/ming5218/p/7965973.html

import configparser,time,os

curpath = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(curpath, "setting.ini") 

config = configparser.ConfigParser() 
config.read(path, encoding="utf-8")

#获取所用的section节点
print(config.sections())

#获取指定section 的options。即将配置文件某个section 内key 读取到列表中： 
r = config.options("db")
print(r)
#运行结果
# ['db_host', 'db_port', 'db_user', 'db_pass', 'host_port']

#获取指点section下指点option的值
r = config.get("db", "db_host")
# r1 = config.getint("db", "k1")        #将获取到值转换为int型
# r2 = config.getboolean("db", "k2" )   #将获取到值转换为bool型
# r3 = config.getfloat("db", "k3" )     #将获取到值转换为浮点型
print(r)

#获取指点section的所用配置信息
r = config.items("db")
print(r)

#修改某个option的值，如果不存在则会出创建
config.set("db", "db_port", "2269")  #修改db_port的值为69
r = config.items("db")
print(r)
#写回文件的方式如下：（使用configparser的write方法）
config.write(open(path, "w"))

#检查section或option是否存在，bool值
print(config.has_section("concurrent"))               #是否存在该section
print(config.has_option("concurrent", "option"))      #是否存在该option

if not config.has_section("default"):                 # 检查是否存在section
    config.add_section("default")
if not config.has_option("default", "db_host"):       # 检查是否存在该option
    config.set("default", "db_host", "1.1.1.1")
    config.set('default','db_name','madam')

config["alex"]={}  
config["alex"]['name']='erdanw'
config["alex"]['pwd']='123'

config["suixin"]={
    'name':'suixin',
    'pwd':'1234'
} 

config.write(open(path, "w"))

time.sleep(2)

config.remove_section("default")                      #整个section下的所有内容都将删除
config.write(open(path, "w"))