import re

strd = '''odps.Schema {
  patient_type                    string      # 病人类型
  police_station                  string      # 户籍地派出所
  census_addr                     string      # 户籍地详址
  id                              string      # 序号
  id_card                         string      # 身份证号
  sync_insert_time                string      # 入库时间
}
Partitions {
  dt                              string      # 分区字段：yyyymmdd
}'''

<<<<<<< HEAD
tb_name = 'stg_person_photo' 
t = re.findall('(\w+)\s+(\w+)\s+#\s+(\S+)',strd)
c = 'create table %s\n(\n'%tb_name
s = ''
for x in t:
      if x[0]!='dt':
        c += '\t{} {},\n'.format(x[0],'varchar2(4000)')
        s += 'comment on column {}.{} is \'{}\';\n'.format(tb_name,x[0],x[2])
      
c += '''\tcreate_date date default sysdate,
        create_user varchar2(100) default 'pyodps'\n);\n\n'''
c += 'comment on table {} is \'{}\';'.format(tb_name,'表注释')   
      
print(c)
print('')
print(s)
=======
print(re.match(r'\s+',strd)) 
print(re.findall('(\w+)\s+(\w+)\s+#\s+(\S+)',strd))
>>>>>>> b47e55d18c45997bf4bd6e62449b072570fe8c9f
