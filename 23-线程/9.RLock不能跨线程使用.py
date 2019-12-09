import threading

lock = threading.RLock()


def subThread(lock: threading.RLock):
    lock.release()


ret = lock.acquire()
print(ret)
ret = lock.acquire(timeout=3)
print(ret)
ret = lock.acquire(True)
print(ret)
ret = lock.acquire(False)
print(ret)

t = threading.Thread(target=subThread, args=(lock,))
t.start()

# 参考链接：https://www.cnblogs.com/i-honey/p/8067503.html
# acquire是在主线程获取了四个，新起了一次子线程，在子线程中release，抛出RuntimeError异常，说明RLock是线程级别的，
# 在哪个线程acquire的，就需要在这个线程release，其它无法release。也就是说RLock无法跨线程。需要跨线程就得使用Lock。
