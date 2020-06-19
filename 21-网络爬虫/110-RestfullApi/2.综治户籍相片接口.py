#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-06-19 16:44:48 
# @Remark: 人生苦短，我用python！

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request 
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app = Flask(__name__)

def get_url(card_num):    
    #ORACLE连接参数
    conn = cx_Oracle.connect('test','esri@123','172.21.246.244:15211/xe')
    cursor = conn.cursor()  
    sql = f"select file_path from TEST.BASE_CARD_PHOTO where gmsfhm = '{card_num}' and rn = 1"
    cursor.execute(sql); 
    row = cursor.fetchone()  # 逐行得到数据集 
    cursor.close()
    conn.close()
    return row
        
@app.route('/hjxp/<string:card_num>', methods=['GET'])
def get_task(card_num):    
    if not 'Referer' in request.headers:    #防盗链
       abort(403)
    else:
        if request.headers['Referer']!='jczl.com':
           abort(403)
        elif len(card_num) == 0:
           abort(404)    
    task = {
        "success": "1",
        "data": []
    }
    row = get_url(card_num)
    if row is not None:
        data = {"cardnum": card_num,"filepath": row[0]}
        task["data"].append(data)
    return jsonify(task)

@app.errorhandler(403)
def not_task(error):
    return make_response(jsonify({"success": "0",'code':'4031004','msg': 'no Referer or invalid Referer header!!!'.format(error)}), 403)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"success": "0",'code':'404','msg': 'The tasks which card_num is Not found,{}!!!'.format(error)}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)