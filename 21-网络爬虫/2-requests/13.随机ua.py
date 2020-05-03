from fake_useragent import UserAgent

ua = UserAgent()
set = set()
for x in range(10000):
    set.add(ua.random)

for index,item in enumerate(set):
    print(f'{index}:{item}') 