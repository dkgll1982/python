from redis import StrictRedis, ConnectionPool
import datetime,time


# pool = ConnectionPool(host='localhost',
#                       port=6379,
#                       db=0,
#                       password=None
#                       )
# redis = StrictRedis(connection_pool=pool)

#另外，ConnectionPool还支持通过URL来构建。URL的格式支持有如下3种：
# redis://[:password]@host:port/db
# rediss://[:password]@host:port/db
# unix://[:password]@/path/to/socket.sock?db=db
# 这3种URL分别表示创建Redis TCP连接、Redis TCP+SSL连接、Redis UNIX socket连接。
# 我们只需要构造上面任意一种URL即可，其中password部分如果有则可以写，没有则可以省略。下面再用URL连接演示一下：
url = 'redis://:@localhost:6379/0'

pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)

print('name:',redis.get('name').decode('utf-8'))
print('myKey:',redis.get('myKey').decode('utf-8'))
print('V8:',redis.get('V8').decode('utf-8'))

print('*'*40)

key_name = 'newkey'
redis.set(key_name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
if redis.exists(key_name):
    print(redis.get(key_name))

key_name = 'nowdate'
for x in range(1000):
    redis.set(key_name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)
    
     