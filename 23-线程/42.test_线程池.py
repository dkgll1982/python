from concurrent.futures import ThreadPoolExecutor
import time

def task(args):
    time.sleep(1)
    print(f"传入的参数：{args}")
    return f'{args}'

with ThreadPoolExecutor(max_workers = 2) as pool:
    # t1 = pool.submit(task,'第一个参数')
    # t2 = pool.submit(task,'第二个参数')
    # t3 = pool.submit(task,'第三个参数')
    # t4 = pool.submit(task,'第四个参数')
    
    # def get_result(future):
    #     print('回调函数：',future.result())
        
    # t4.add_done_callback(get_result)
    
    # time.sleep(1.1)
    # print(f'状态：{t1.done()}，结果：{t1.result()}\t')
    # print(f'状态：{t2.done()}，结果：{t2.result()}\t')
    # print(f'状态：{t3.done()}，结果：{t3.result()}\t')
    # print(f'状态：{t4.done()}，结果：{t4.result()}\t')
    results = pool.map(task,('第一个参数','第二个参数','第三个参数','第四个参数','第五个参数'))
    print('--------------')
    for r in results:
        print(r)