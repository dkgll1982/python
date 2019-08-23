#!/usr/bin/env python
# encoding: utf-8
"""
:author: xiaoxiaobai

:contact: 865816863@qq.com

:file: dataBaseOpr.py

:time: 2017/10/3 12:04

:@Software: PyCharm Community Edition

:desc: 连接oracle数据库，并封装了增删改查全部操作。

"""
import cx_Oracle


class OracleOpr:

    def __init__(self, username='dkgll', passname='dkgll', ip='localhost', datebasename='orcl', ipport='1521'):
        """
        :param username: 连接数据库的用户名
        :param passname: 连接数据库的密码
        :param ip: 数据库ip
        :param datebasename:数据库名
        :param ipport: 数据库端口
        :desc: 初始化函数用于完成数据库连接，可以通过self.connStatus判断是否连接成功，成功则参数为0，不成功则返回错误详情
        """
        try:
            self.connStatus = '未连接'    # 连接状态
            self.queryStatus = 0    # 查询状态
            self.updateStatus = 0   # 更新状态
            self.deleteStatus = 0   # 删除状态
            self.insertStatus = 0   # 插入状态
            self.__conn = ''
            self.__conStr = username+'/'+passname+'@'+ip+':'+ipport+'/'+datebasename
            self.__conn = cx_Oracle.connect(self.__conStr)
            self.connStatus = 0
        except cx_Oracle.Error as e:
            self.connStatus = e

    def closeconnection(self):
        try:
            if self.__conn:
                self.__conn.close()
                self.connStatus = '连接已断开'
        except cx_Oracle.Error as e:
            self.connStatus = e

    def query(self, table='groupinfo', queryby=''):
        """
        :param table: 查询表名
        :param queryby: 查询条件，支持完整where, order by, group by 字句
        :return:返回数据集，列名
        """
        self.queryStatus = 0
        result = ''
        cursor = ''
        title = ''
        try:
            sql = 'select * from '+table+' '+queryby
            print(sql)
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            title = [i[0] for i in cursor.description]
            cursor.close()
            cursor = ''
        except cx_Oracle.Error as e:
            self.queryStatus = e
        finally:
            if cursor:
                cursor.close()
            return result, title

    def insert(self, proc='insert_groupinfo', insertlist=[]):
        """
        :param proc: 过程名
        :param insertlist: 参数集合，主键不能为空，参数必须与列对应，数量一致
        :desc: 此方法通过调用过程完成插入，需要在sql上完成存储过程，可以通过insertstatus的值判断是否成功
        """
        self.insertStatus = 0
        cursor = ''
        try:
            cursor = self.__conn.cursor()
            cursor.callproc(proc, insertlist)
            cursor.close()
            cursor = ''
        except cx_Oracle.Error as e:
            self.insertStatus = e
        finally:
            if cursor:
                cursor.close()

    def update(self, proc='update_groupinfo', updatelist=[]):
        """
        :param proc: 存储过程名
        :param updatelist: 更新的集合，第一个为查询主键，后面的参数为对应的列，可以更新主键。
        :desc: 此方法通过调用存储过程完成更新操作，可以通过updatestatus的值判断是否成功
        """
        self.updateStatus = 0
        cursor = ''
        try:
            cursor = self.__conn.cursor()
            cursor.callproc(proc, updatelist)
            cursor.close()
            cursor = ''
        except cx_Oracle.Error as e:
            self.updateStatus = e
        finally:
            if cursor:
                cursor.close()

    def delete(self, deleteby: '删除条件,where关键词后面的内容,即列名=列值(可多个组合)', table='groupinfo'):
        """
        :param deleteby: 删除的条件，除where关键字以外的内容
        :param table: 要删除的表名
        :desc:可以通过deletestatus判断是否成功删除
        """
        self.deleteStatus = 0
        cursor = ''
        try:
            sql = 'delete ' + table + ' where ' + deleteby
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            cursor.close()
            cursor = ''
        except cx_Oracle.Error as e:
            self.deleteStatus = e
        finally:
            if cursor:
                cursor.close() 