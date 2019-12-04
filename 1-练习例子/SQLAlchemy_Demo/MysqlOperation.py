#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-11 14:40
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : MysqlOperation
# @Software: PyCharm
'''
    Demo：sqlalchemy对mysql数据库的操作
'''

from sqlalchemy import Column,Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

# 创建对象的基类:
Base = declarative_base()

# 定义Channel对象:
class Channel(Base):

    # 表名
    __tablename__ = 'playback'

    # 表结构
    # Column：行声明，可指定主键 Integer：数据类型 String：数据类型，可指定长度
    id = Column(Integer,primary_key=True,autoincrement=True)
    channel_name = Column(String(45),unique=True, nullable=False)
    address = Column(String(80),unique=True, nullable=False)
    service_name = Column(String(45),unique=True, nullable=False)

    def __init__(self,id,channel_name,address,service_name):
        self.id = id
        self.channel_name = channel_name
        self.address = address
        self.service_name = service_name

# 初始化数据库连接,
# 传入参数：数据库类型+连接库+用户名+密码+主机，字符编码，是否打印建表细节
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test',encoding='utf-8')

# 创建表
Base.metadata.create_all(engine)
# 删除表
# Base.metadata.drop_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()

try:
    # 添加操作
    item1 = Channel(id='1',channel_name='cctv8',address='http://10.10.10.1/cctv8',service_name='news')
    session.add(item1)
    item2 = Channel(id='2',channel_name='cctv10',address='http://10.10.10.1/cctv10',service_name='sports')
    session.add(item2)
    item3 = Channel(id='3',channel_name='cctv12',address='http://10.10.10.1/cctv12',service_name='economics')
    session.add(item3)
    #提交数据
    session.commit()
except Exception as e:
    session.rollback()
finally:
    #关闭
    session.close()

# 查操作
session1 = DBSession()

# 输出sql 语句
print("查询sql语句：%s"%session1.query(Channel).filter(Channel.id < '3'))
# 返回的是一个类似列表的对象
channel = session1.query(Channel).filter(Channel.id < '3').all()

for i in range(len(channel)):
    print(channel[i].id)
    print(channel[i].channel_name)
    print(channel[i].address)
    print(channel[i].service_name)
session1.close()

# 改操作
session2 = DBSession()
session2.query(Channel).filter(Channel.id == '2').update({Channel.service_name: 'movie',Channel.address: '127.0.0.1'}, synchronize_session=False)
session2.commit()
session2.close()

## 查看修改结果
session3 = DBSession()
print(session3.query(Channel).filter(Channel.id == '2').one().service_name)
session3.close()

# 删操作
session4 = DBSession()
session4.query(Channel).filter(Channel.id == '3').delete()
session4.commit()
session4.close()