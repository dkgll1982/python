# hello.py
import numpy as np

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    path = bytes(map(ord, environ['PATH_INFO'][1:])).decode('utf-8')
    body = '<h1>Hello,GUOJUN, %s!</h1>' % (path or 'web')
    return [body.encode('utf-8')]

def avgscore(grads):
    first,*middle,last=grads
    print(middle)
    return np.mean(middle)

s = (11,2,3,4,5,6,7,8,99,1110)

print(avgscore(sorted(s)))