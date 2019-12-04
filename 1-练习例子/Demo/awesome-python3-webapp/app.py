#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-10 15:56
# @Author  : guojun
# @Site    : https://user.qzone.qq.com/350606539/main
# @File    : app
# @Software: PyCharm

import logging; logging.basicConfig(level=logging.INFO)

import 异步asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@异步asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = 异步asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()