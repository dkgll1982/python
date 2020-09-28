import json

def json_append(file_name,key,json_data):  
    with open(file_name,'a+',encoding="utf-8") as f:
        # 因为是追加方式打开，默认偏移量再最后面，我们调整到开头
        f.seek(0)                       
        # 判断是否为空，如果为空的话创建一个新的字典格式 
        if f.read() =='':              
            data = {}
        else:
            f.seek(0)
            data = json.load(f) 
        if data != {}:  
            data[key][len(data[key]):len(data[key])] = json_data 
        else:
            data[key] = json_data 
        
        # 设置文件当前位置 0代表开始处 其实有两个参数 offset,whence （whence常用有三个参数0，1，2；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。）
        f.seek(0)                       
        # 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
        # 从开头截断，截断文件为size个字符，无参代表 从当前位置截断，截断之后后面的所有字符都被删除
        f.truncate()                    
        json.dump(data,f,indent=2,ensure_ascii=False)

if __name__ == "__main__":
    file_name = r'backup\test2.json'
    key = 'ee'
    json_data =[
        {'id': 'e8d0bc60-ff93-11e9-806b-a3b23f8b848b', 
         'placeName': '浙江来伊份食品有限公司湖州南街店', 
         'oldPlaceName': '浙江来伊份食品有限公司湖州南街店', 
         'placeAddr': '浙江省湖州市吴兴区江南工贸大街459号', 
         'isKeyPlace': '一般场所', 
         'displayName': '朝阳街道/北齐巷社区/北齐巷社区网格', 
         'checkDate': '2020-09-22', 
         'checkLevel': '县级检查', 
         'RN': 1, 
         'safeType': '小食杂店', 
         'task_num': ['PC2020092200002'], 
         'checkUserName': ['杨扶新'], 
         'description': ['灭火器有遮挡物，无每月检查表'], 
         'ill_list': ['未配备灭火器等基本消防器材；备注：灭火器遮挡物检查表']
         }
    ]
    json_append(file_name,key,json_data)