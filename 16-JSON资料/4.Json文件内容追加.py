import json

with open(r'backup/test2.json','a+',encoding="utf-8") as f:
    f.seek(0)  # 因为是追加方式打开，默认偏移量再最后面，我们调整到开头
    if f.read() =='':  # 判断是否为空，如果为空的话创建一个新的字典格式
        print('执行了吗')
        data = {}
    else:
        f.seek(0)
        data = json.load(f)
    print(data['ee'],type(data['ee']))

    data['a']="我爸是赵四"
    data['b']="我爸是李刚"  # 可以在第二遍运行时修改一下看看效果
    data['e']="我爸是李刚"
    if data['ee']: 
        
        data['ee'].append({'a3':'嵌套'+str(len(data['ee']))}) 
    else:
        data['ee'] = [{'a3':'嵌套啊'}]
    print(data)

    f.seek(0)# 设置文件当前位置 0代表开始处 其实有两个参数 offset,whence （whence常用有三个参数0，1，2；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。）
    # 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
    f.truncate() # 从开头截断，截断文件为size个字符，无参代表 从当前位置截断，截断之后后面的所有字符都被删除
    json.dump(data,f,indent=2,ensure_ascii=False)
