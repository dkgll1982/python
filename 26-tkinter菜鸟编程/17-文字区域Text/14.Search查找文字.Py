from tkinter import *
root = Tk()
text = Text(root, width=30, height=5)
text.pack()
text.insert(INSERT, "I love FishC.com!")
# 将任何格式的索引号统一为元祖 (行,列) 的格式输出
def getIndex(text, index):
    return tuple(map(int, str.split(text.index(index), ".")))
    '''这句困扰我一大会，哎，基础没打好！~
    分解来理解：split()以拆分字符串得到list，
    然后map（）把list的每一项str转换为int，
    tuple（）把list转换为tuple。

    改为这样就好理解了：   
    b = text.index(index)
    a = b.split('.')
    return tuple(map(int, a))
    '''
start = 1.0
while True:
    #格式: pos = text.search(key,startindex,endindex)
    #pos：传回所找到的字符串的索引位置，如果查找失败则传回空字符串
    #key：所查找的字符串
    #startindex：查找起始位置
    #endindex：查找结束位置，如果查找到文档后可以使用END
    pos = text.search("o", start, stopindex=END)
    if not pos:
        break
    print("找到啦，位置是：", getIndex(text, pos))
    start = pos + "+1c"  # 将 start 指向下一个字符
mainloop()
