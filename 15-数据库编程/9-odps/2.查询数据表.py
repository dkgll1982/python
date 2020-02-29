#!/usr/local/anaconda3/bin/python3
# -*- coding: utf-8 -*-
# ###########################################################################################
# 执行环境：分析服务器
# 脚本: get_table_meta.py
# 调度: 每日早6点调度
# 日志: get_table_meta.log
# ###########################################################################################
 
import os
from datetime import datetime
from odps import ODPS
from odps.models import Schema, Column, Partition
 
start_tm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cur_path = os.path.split(os.path.realpath(__file__))[0]
 
odps = ODPS(access_id='HWqOnIUpeYhyd7BR', #登陆账号
         secret_access_key='0RG5GJpo2WjCCwpUkQzcwjGGzKX8Tn', #登陆密码
         project='hzdn_mplc_dev', #odps上的项目名称 
         endpoint='http://service.cn-huzhou-hzdsj-d01.odps.ops.cloud.huzhou.gov.cn/api') #官方提供的接口
 
to_table = 'meta_tables'
columns = [Column(name='tbl_name', type='string', comment='表名'),
           Column(name='tbl_comment', type='string', comment='表注释'),
           Column(name='tbl_owner', type='string', comment='作者'),
           Column(name='tbl_pt_name', type='string', comment='（如果是分区表）分区名'),
           Column(name='tbl_ddl_tm', type='datetime', comment='最近创建时间'),
           Column(name='tbl_mod_tm', type='datetime', comment='最近更新时间'),
           Column(name='etl_tm', type='datetime', comment='ETL时间')]
partitions = [Partition(name='pt', type='string', comment='按日期分区')]
schema = Schema(columns=columns, partitions=partitions)
 
records = []
try:
    for tbl in odps.list_tables():
        tm = datetime.now()
        records.append([tbl.name, tbl.comment, tbl.owner.split(':')[-1],
                        tbl.schema.partitions[0].name if tbl.schema.partitions else None,
                        tbl.last_meta_modified_time.strftime('%Y-%m-%d %H:%M:%S'),
                        tbl.last_modified_time.strftime('%Y-%m-%d %H:%M:%S'),
                        tm.strftime('%Y-%m-%d %H:%M:%S')])
    partition = '%s=%s' % (partitions[0].name, datetime.now().strftime('%Y%m%d'))
    to_tbl = odps.create_table(to_table, schema, if_not_exists=True)
    to_tbl.delete_partition(partition, if_exists=True)
    odps.write_table(to_table, records, partition=partition, create_partition=True)
 
except:
    status = 'failed'
    n = 0
else:
    status = 'succeed'
    n = len(records)
 
end_tm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log = {'status': status, 'n': n, 'start': start_tm, 'end': end_tm}
f = open(os.path.join(cur_path, 'get_table_meta.log'), 'a')
f.write("Update {status} with {n} tables from {start} to {end}\n".format(**log))
f.close()