# 写入csv文件
import csv,uuid

csvfile = open(r'backup\python写入.csv', 'a',newline='')
# 如果不指定newline='',有时则每写入一行将有一空行被写入
writer = csv.writer(csvfile)
writer.writerow(['主键','姓名','年龄','电话']) # 写入一行用writerow
 
data = [
    (uuid.uuid1(),'al', '25', '111111111111111111\t'),
    (uuid.uuid1(),'eg', '18', '134543534535367890800\t'),
    (uuid.uuid1(),'eg', '18', '13673534534543453890800\t'),
    (uuid.uuid1(),'eg', '18', '1367453535853535353535390800\t'),
    (uuid.uuid1(),'eg', '18', '13673535353535890800\t'),
    (uuid.uuid1(),'eg', '18', '13673535353535353890800\t'),
    (uuid.uuid1(),'eg', '18', '1367535353535353535890800\t'),
    (uuid.uuid1(),'eg', '18', '13678353535354353535390800\t'),
    (uuid.uuid1(),'eg', '18', '13678353553535353533535390800\t'),
    (uuid.uuid1(),'eg', '18', '13678535353535353590800\t')
]
writer.writerows(data)  # 多行用writerows
csvfile.close() 