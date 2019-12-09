#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: 航天神舟智慧系统技术有限公司 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2019-12-09 21:50:04 
# @Last Modified by: guojun 
# @Last Modified time: 2019-12-09 21:50:04 
# @Software: vscode 
# 参考链接：http://www.lemfix.com/topics/375

from ruamel.yaml import YAML

import os
 
curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "lovers.yaml") 

# 第一步: 创建需要保存的User类
class User:
    """
    定义用户类
    """
    def __init__(self, name, age, gender):
        self.name, self.age, self.gender = name, age, gender
        self.lovers = []

    def loved(self, user):
        self.lovers.append(user)


# 第二步: 创建YAML对象
yaml = YAML()

# 第三步: 注册用户类
yaml.register_class(User)

# 第四步: 保存用户对象
keyou = User("可优", 17, "油腻男")
lemon_little_girl = User("柠檬小姐姐", 16, "素颜小仙女")
orange_little_girl = User("橘子小姐姐", 18, "不会PS的靓妹")
keyou.loved(lemon_little_girl)
keyou.loved(orange_little_girl)

with open(yamlpath, mode='w', encoding='utf-8') as file:
    yaml.dump([keyou], file)