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

print(re.match(r'\s+',strd)) 
print(re.findall('(\w+)\s+(\w+)\s+#\s+(\S+)',strd))