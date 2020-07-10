#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-03-07 12:50:33 
# @Last Modified by: guojun 
# @Last Modified time: 2020-03-07 12:50:33 
# @Software: vscode  

import json
import pandas as pd

data = [] # 用于存储每一行的Json数据

j = json.load(open(r'backup/js/接口_13.json', 'r', encoding='utf-8')) 
data.append(j)
df = pd.DataFrame() # 最后转换得到的结果
for line in data:
    for i in line:  
        df1 = pd.DataFrame([i])
        df = df.append(df1)

# 在excel表格的第1列写入, 不写入index
df.to_excel(r'backup/excel/data.xlsx', sheet_name='Data', startcol=0, index=False)
