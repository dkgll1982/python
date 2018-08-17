#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-11 14:18
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : test
# @Software: PyCharm

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库 engine 使用 utf8 编码
eng = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
Base = declarative_base()

# 创建 session 类，绑定engine
Session = sessionmaker(bind=eng)
session = Session()


class User(Base):
    '''
    用户类，对应数据库的 member 表
    '''
    __tablename__ = 'member'

    # 定义表字段
    mid = Column(Integer, primary_key=True)
    nickname = Column(String(50))
    email = Column(String(128))

    def __repl__(self):
        return '<User(name={}, email={}, nickname{}>'.format(mid,
                                                             email,
                                                             nickname)


class Article(Base):
    '''
    文章类，对应数据库中的 article 表
    '''
    __tablename__ = 'article'

    # 定义表字段
    arid = Column(Integer, primary_key=True)
    tags = Column(String(128))
    description = Column(String(256))
    title = Column(String(256))



class Article2(Base):
    '''
    文章类，对应数据库中的 article 表
    '''
    __tablename__ = 'article2'

    # 定义表字段
    arid = Column(Integer, primary_key=True)
    tags = Column(String(128))
    description = Column(String(256))
    title = Column(String(256))


def create_table():
    '''
    创建数据库表结构，导入初始数据
    '''
    # 创建表
    Base.metadata.create_all(eng)

    # 插入数据
    session.add_all([
        User(mid=1, nickname='测试数据 test hello', email='test@gmail.com'),
        User(mid=2, nickname='测试数据 china hello', email='test@gmail.com'),
        User(mid=3, nickname='测试数据 上海 hello', email='test@gmail.com'),
        User(mid=4, nickname='测试数据 北京 hello', email='test@gmail.com'),
        User(mid=5, nickname='测试数据 上海 hello', email='test@gmail.com'),
        User(mid=6, nickname='测试数据 山东 hello', email='test@gmail.com'),
        User(mid=7, nickname='测试数据 武夷山 hello', email='test@gmail.com'),
        User(mid=8, nickname='测试数据 黄山 hello', email='test@gmail.com'),

        Article(arid=1, tags='测试数据 test hello', title='销售额度', description='测试 test ok'),
        Article(arid=2, tags='测试数据 china hello', title='成功转型', description='测试 test ok'),
        Article(arid=3, tags='测试数据 上海 hello', title='蓝蓝的天上白云飘', description='测试 test ok'),
        Article(arid=4, tags='测试数据 背景 hello', title='在水一方', description='测试 test ok'),
        Article(arid=5, tags='测试数据 上海 hello', title='晴天，阴天，雨天，大风天', description='测试 test ok'),
        Article(arid=6, tags='测试数据 山东 hello', title='每年365天，每天24小时', description='测试 test ok'),
        Article(arid=7, tags='测试数据 武夷山 hello', title='高效工作的秘密', description='测试 test ok'),
        Article(arid=8, tags='测试数据 黄山 hello', title='战狼2', description='测试 test ok'),
    ]
    )

    # 提交到数据库
    session.commit()


def modify_data():
    '''
    测试修改数据
    '''

    # 查询用户表
    users = session.query(User).all()
    print(users)

    # 查询文章表
    # articles = session.query(Article).all()
    articles = session.query(Article).filter(Article.arid==2)
    print(articles)

    # 修改文章表
    articles[0].description = '程度，修改描述可以成功'
    print(session.dirty)

    # 提交到数据库
    session.commit()

modify_data();
#if __name__ == '__main__':
#    create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
#    modify_data()