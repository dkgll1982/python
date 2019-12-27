from multiprocessing import Pool
import time
from lxml import etree
import aiohttp
import asyncio
urls = [
    'https://www.cnblogs.com/ikct2017/p/9829048.html' 
]
htmls = []
titles = []
sem = asyncio.Semaphore(100) # 信号量，控制协程数，防止爬的过快
'''
提交请求获取AAAI网页html
'''
async def get_html(url):
    with(await sem):
        # async with是异步上下文管理器
        async with aiohttp.ClientSession() as session:  # 获取session
            async with session.request('GET', url) as resp:  # 提出请求
                html = await resp.read() # 直接获取到bytes
                htmls.append(html)
                print('异步获取%s下的html.' % url)

'''
协程调用方，请求网页
'''
def main_get_html():
    loop = asyncio.get_event_loop()           # 获取事件循环
    asyncio.set_event_loop(loop)
    tasks = [get_html(urls[0]) for i in range(10)]  # 把所有任务放到一个列表中
    loop.run_until_complete(asyncio.wait(tasks)) # 激活协程
    
    loop.close()  # 关闭事件循环
    
'''
使用多进程解析html
'''
def multi_parse_html(html,cnt):
    title = etree.HTML(html).xpath('//*[@id="title"]/text()')
    titles.append(''.join(title))
    print('第%d个html完成解析－title:%s' % (cnt,''.join(title)))
'''
多进程调用总函数，解析html
'''
def main_parse_html():
    p = Pool(4)
    i = 0
    for html in htmls:
        i += 1
        p.apply_async(multi_parse_html,args=(html,i))
    p.close()
    p.join()


if __name__ == '__main__':
    oldloop = asyncio.get_event_loop()
    start = time.time()
    main_get_html()   # 调用方
    asyncio.set_event_loop(oldloop)
    #main_parse_html() # 解析html
    print('总耗时：%.5f秒' % float(time.time()-start))
