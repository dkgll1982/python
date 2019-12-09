import time

def show_process(total):
    received_size = 0
    current_percent = 0
    while received_size < total:
        if int((received_size / total) * 100) > current_percent:
            print('#',end='',flush=True)
            current_percent = int((received_size / total) * 100)
        new_size = yield
        received_size += new_size 

progress = show_process(102410241024)              #generator
progress.__next__()  
received_size = 0
while received_size < 102410241024: 
    received_size += 4096 
    try:
        progress.send(4096)
    except StopIteration as e:
        print('100%') 
                    