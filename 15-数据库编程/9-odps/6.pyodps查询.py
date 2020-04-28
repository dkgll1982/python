#参考链接:https://blog.csdn.net/weixin_42261073/article/details/103199562

#执行SQL
odps.execute_sql('select * from ods_orders ') #同步方式
odps.run_sql('select * from ods_orders') #异步方式
print(instance.get_logview_address()) #获取logview地址
instance.wait_for_success() #阻塞直到完成
#设置参数
odps.execute_sql(sql,hints={'odps.sql.mapper.split.size':16}) #设置hints运行参数
或
from odps import options
options.sql.setting = {'odps.sql.mapper.split.size':16}
odps.execute_sql(sql)

#读取SQL执行结果
options.tunnel.use_instance_tunnel == True #控制通道
tunnel.limit_instance_tunnel = True #限制下载数据的规模

sql = "select * from ods_orders where pt='20191118' limit 10"
instance = odps.run_sql(sql)
with instance.open_reader(tunnel=True) as reader: #tunnel参数
    for record in reader:
        print(record['o_orderkey'])
或
with instance.open_reader() as reader:
    print(reader.raw)
    
#设置alias UDF引用的资源动态变化，可以将旧的资源名到新的资源，不需要重建删除或创建新的
from odps.models import Schema
myfunc = '''\ 
from odps.udf import annotate 
from odps.distcache import get_cache_file 
@annotate('bigint->bigint') 
class Example(object):
    def __init__(self):
        self.n = int(get_cache_file('test_alias_res1').read())    
    def evaluate(self, arg):        
        return arg + self.n '''
res1 = o.create_resource('test_alias_res1', 'file', file_obj='1')
o.create_resource('test_alias.py', 'py', file_obj=myfunc)
o.create_function('test_alias_func',
                  class_type='test_alias.Example',
                  resources=['test_alias.py', 'test_alias_res1'])
table = o.create_table('test_table',
                       schema=Schema.from_lists(['size'], ['bigint']),
                       if_not_exists=True )
data = [[1, ], ] # 写⼊⼀⾏数据，只包含⼀个值1。
o.write_table(table, 0, [table.new_record(it) for it in data])
with o.execute_sql('select test_alias_func(size) from test_table').open_reader() as reader:
    print(reader[0][0]) 
    res2 = o.create_resource('test_alias_res2', 'file', file_obj='2') 
#把内容为1的资源alias成内容为2的资源，您不需要修改UDF或资源。
with o.execute_sql( 'select test_alias_func(size) from test_table',
                    aliases={'test_alias_res1': 'test_alias_res2'}).open_reader() as reader:
    print(reader[0][0]) 
