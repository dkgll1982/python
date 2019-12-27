import requests,time,gevent
starttime=time.time()
def f(url):
    print('get the url:',url)
    res=requests.get(url)
    data=res.text
    print('%s bytes' % len(data))
    with open(r'backup\drug.txt','w',encoding='utf8') as t:
        t.write(data)
# f('http://www.sina.cn')
# f('http://sina.com.cn')
# f('http://smzdm.com')
# f('https://blog.csdn.net/dengyuelin/article/details/54628774')
gevent.joinall([
gevent.spawn(f,'http://baidu.com'),
gevent.spawn(f,'http://sina.com.cn'),
gevent.spawn(f,'http://smzdm.com'),
gevent.spawn(f,'https://blog.csdn.net/dengyuelin/article/details/54628774')
 
])
 
print('cost time',time.time()-starttime)