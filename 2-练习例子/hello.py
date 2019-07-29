# hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    path = bytes(map(ord, environ['PATH_INFO'][1:])).decode('utf-8')
    body = '<h1>Hello,GUOJUN, %s!</h1>' % (path or 'web')
    return [body.encode('utf-8')]

