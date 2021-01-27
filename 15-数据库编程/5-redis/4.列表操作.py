
from redis import StrictRedis

# Redis的地址、运行端口、使用的数据库和密码信息。在默认不传的情况下，这4个参数分别为localhost、6379、0和None。首先声明了一个StrictRedis对象
r = StrictRedis(host='localhost', port=6379, db=0, password=None)

key = 'list'
if not r.exists(key):
    #在键为name的列表末尾添加值为value的元素，可以传多个
    r.rpush(key, 1, 2, 3)
    #在键为name的列表头添加值为value的元素，可以传多个
    r.lpush(key, -1, -2, 23)

print('列表的长度；',r.llen(key),'元素：',sorted([int(x.decode()) for x in r.lrange(key, 0, r.llen(key))]))

# 将键为list的列表删除两个3
r.lrem(key, 2, 3)
print('列表的长度；',r.llen(key),'元素：',sorted([int(x.decode()) for x in r.lrange(key, 0, r.llen(key))]))
