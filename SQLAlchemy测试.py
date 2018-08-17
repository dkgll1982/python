#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-11 11:05
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : SQLAlchemy测试
# @Software: PyCharm

#导入模块
from sqlalchemy import Column,Integer,String,Date,Float,Text,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random
import uuid
import  os
from sqlalchemy.sql import func

os.environ["NLS_LANG"] = "SIMPLIFIED CHINESE_CHINA.ZHS16GBK"

# 1：创建对象的基类:
Base = declarative_base()
# 2：初始化数据库连接:
#DB_CONNECT_STRING = 'mysql+pymysql://root:123456@192.168.1.118:3306/testdb'

DB_CONNECT_STRING = 'oracle+cx_oracle://cigproxy:cigproxy@127.0.0.1:1521/orcl'

engine = create_engine(DB_CONNECT_STRING, echo=True)
# 3：创建DBSession类型:
DBSession = sessionmaker(bind=engine)
#:4：创建session对象:
session = DBSession()

#找到Base的所有子类，并在数据库中建立这些表
def init_db():
    Base.metadata.create_all(engine)

#找到Base的所有子类，并在数据库中删除这些表
def drop_db():
    Base.metadata.drop_all(engine)

# Model:定义实体对象
class Users(Base):
    # 表名
    __tablename__ = 'tbuser'

    # 表结构
    # Column：行声明，可指定主键 primary_key；约束：unique；数据类型 String；数据长度，可指定长度
    # 主键，序号(自增列)
    XH = Column(Integer,primary_key=True,autoincrement=True)
    # 用户ID
    UserID = Column(String(36))
    # 身份证号
    CardID = Column(String(18),unique=True,nullable=False)
    # 姓名
    Name = Column(String(45),nullable=False)
    # 年龄
    Age = Column(Integer,nullable=True)
    # 性别
    Sex = Column(String(20),nullable=True)
    # 家庭住址
    Address = Column(String(255),nullable=True)

    #自增列默认不需要传值，为空列也可以不传值
    def __init__(self,UserID,CardID,Name,XH = None,Age = None,Sex = None,Address = None):
        self.UserID = UserID
        self.CardID = CardID
        self.Name = Name

        if not XH is None:
            self.XH = XH
        if not Age is None:
            self.Age = Age
        if not Sex is None:
            self.Sex = Sex
        if not Address is None:
            self.Address = Address

#BLL：定义添加用户的方法
def AddUser(Users):
    try:
        # 添加到session:
        session.add(Users)
        # 提交即保存到数据库:
        session.commit()
        print("Add User sucesses！")
    except Exception as e:
        session.rollback()
        print("Add User error,%s！"+e)
    finally:
        # 关闭session:
        session.close()

#BLL：定义删除用户的方法,如通过主键删除用户
def DelUser(XH):
    session.query(Users).filter(Users.XH == XH).delete()
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

#BLL:定义修改（通过主键进行匹配）
def UpdateUser(User):
    singe_user = session.query(Users).filter(Users.XH == User.XH).first();
    if singe_user is not None:
        if not User.Name is None:
            singe_user.Name = User.Name
        if not User.Age is None:
            singe_user.Age = User.Age
        if not User.Sex is None:
            singe_user.Sex = User.Sex
        if not User.Address is None:
            singe_user.Address = User.Address

        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
        session.close()
    else:
        print('用户不存在')

#BLL：定义同步/更新用户（存在则更新，不存在则添加）的方法
def MergeUser(User):
    # 使用merge方法，如果存在则修改，如果不存在则插入
    session.merge(User)
    # 提交即保存到数据库:
    session.commit()
    session.close()

#BLL：定义查询用户的方法,如通过姓或者名模糊查询用户
def SelUser(UserName):
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    users = session.query(Users).filter(Users.Name.like('%'+UserName+'%')).all();
    for user in users:
        print("CardId:%s,Name=%s,Age:%d,Sex=%s,Address=%s"%(user.CardID,user.Name,user.Age,user.Sex,user.Address))

#删除表
#drop_db();

#创建表
init_db()

#Control:调用方法
# 创建新User对象:
# MAX_XH = session.query(Users.max(Users.XH)).first();
# print("MAX_XH:"+MAX_XH);
new_user = Users(
    XH=random.randint(10000000000,99999999999),     #随机数
    UserID=str(uuid.uuid1()),                                   #guid
    CardID=random.randint(4290011900000,4290012020000),     #随机数
    Name=random.choice(['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                        '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
                        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                        '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                        '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                        '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁'])+random.choice(['子涵','小伟','千千','二勇','天强','明明','大宝','玲玲','涛','昊天','明心','月如']),
    Age=random.randint(4,98),
    Sex=random.choice(['男性','女性','变性人','双性人','性别不明']),
    Address=random.choice(['湖北省','湖南省','河北省','山东省','河南省','浙江省'])
)
#调用添加的方法
AddUser(new_user);
AddUser(new_user);

#根据条件删除用户
#DelUser(input("please Input delete User-XH："));
#DelUser(12321);

#根据条件修改用户
mUser =  Users(
    XH = 12360,
    UserID = 12321,
    Name = '张君宝',
    CardID='4999999931',
    Age=18,
    Sex='男孩',
    Address='湖北省十堰武当山'
)
UpdateUser(mUser)

#同步/更新用户（通过主键匹配）
rUser = Users(
    XH = 12359,
    UserID = 12321,
    Name = '张三丰',
    CardID='4999999939',
    Age=138,
    Address='湖北省十堰武当山'
)
MergeUser(rUser);

#根据条件查询用户
SelUser('')
print("*"*100)
SelUser('张')

#删除符合条件的所有用户
session.query(Users).filter(Users.XH.in_([12376,12351,12352,12353,12354,12355,12356])).delete(synchronize_session=False);

session.commit();
session.close()