import pandas as pd
from pandas import DataFrame

#读
data = pd.read_excel(r'backup\excel\合并后的.xlsx')

#查看所有的值
print(data.values)

#查看第一行的值
print(data.values[0])

#查看某一列所有的值
print(data['企业名称'].values)

#新增列
data['标题列3'] = None

#新增行
data.loc[2] = ['王五', 100, '男', '男', '男', '男']

#删除行：axis=0
data = data.drop([0,1], axis=0)

#删除列：axis=1
data.drop('标题列3', axis=1)

#保存
DataFrame(data).to_excel(r'backup\excel\1.xlsx', sheet_name='Sheet1', index=False, header=True)