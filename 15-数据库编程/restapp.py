t# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 16:54
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : FlaskTest.py
from flask import Flask
from flask import request
import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

app = Flask(__name__)


@app.route('/',methods=['GET','POSt'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username3"></p>
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In </button></p>
    </form>
    '''

@app.route('/signin',methods=['POST'])
def signin():
    str2 = ""
    conn = cx_Oracle.connect('cigproxy/cigproxy@127.0.0.1/orcl')
    cursor = conn.cursor()

    cursor.execute("SELECT table_NAME,TO_CHAR(COMMENTS) FROM user_tab_comments where COMMENTS IS NOT NULL ORDER BY TABLE_NAME")
    rows = cursor.fetchall()  # 得到所有数据集
    for row in rows:
        str2 = str2 +'"'+ row[0] + '":"' + row[1] + '",'

    str2 = str2 + '"表数量": ' + str(cursor.rowcount)

    cursor.close()
    conn.close()

    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '{"data":{' + str2 + '}}';
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()