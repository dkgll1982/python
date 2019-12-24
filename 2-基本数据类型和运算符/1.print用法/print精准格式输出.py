print('%-5s%-4s%-4s%-4s'%('姓名','语文','数学','英语'))
print('%-5s%-6d%-6d%-6d'%('张三',112,120,111))
print('%-4s%-6d%-6d%-6d'%('王倚天',22,120,111))

print('{}的物理成绩是{}'.format('郭君','100'))

print(r'e:/cmd'.replace(r'/',"\\"))
print(r'e:/cmd'.replace(r'/',r"\\"))

data = {1,2,3}
print(f"data:{data}")