#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
# @Author: guojun 
# @Company: Aerospace Shenzhou Intelligent System Technology Co., Ltd 
# @Site: https://user.qzone.qq.com/350606539/main 
# @Date: 2020-04-16 12:36:39 
# @Remark: 人生苦短，我用python！
# 参考链接：https://www.jianshu.com/p/6e12c6a69f10
import execjs
import sys
import os   
import time

print(sys.stdout.encoding)
# 获取文件当前所在的目录，并返回完整文件全路径 
def realpath(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

print(execjs.get().name)

val1 = execjs.eval("'red yellow blue'.split(' ')") 

# 先编译、后调用
# 将js文件中的内容读取出来编译即可调用里面的方法了
ctx = execjs.compile(""" 
function add2(x, y) {
    return x + y;
};
function plus(x, y) {
    return x * y;
};
function validatePhone(e) {
    var phone = e.replace(/(^\s*)|(\s*$)/g, "");
    var regm = /^0{0,1}(13[0-9]?|15[0-3]?|15[5-9]?|145|147|18[0-9])[0-9]{8}$/;
    if (e.length == 11) {
        if (!e.match(regm)) {
            return "1:手机号码不正确。请重新输入!";
        }
        else {
            return true;
        }
    }
    else if (e.length > 0) {
        return "2:手机号码为11位数字，请重新输入!";
    }
    else {
        return "3:手机号码不能为空!";
    }
}; 
//获取距离当前时间的天,时，分，秒
function countdown(o) {
    this.d = Math.floor(o / (1000 * 60 * 60 * 24));
    this.h = Math.floor(o / (1000 * 60 * 60) - this.d * 24);
    this.m = Math.floor(o / (1000 * 60) - this.h * 60 - this.d * 24 * 60);
    this.s = Math.floor(o / 1000 - this.m * 60 - this.h * 60 * 60 - this.d * 24 * 60 * 60);
    this.d = this.d > 9 ? this.d : "0" + this.d;
    this.h = this.h > 9 ? this.h : "0" + this.h;
    this.m = this.m > 9 ? this.m : "0" + this.m;
    this.s = this.s > 9 ? this.s : "0" + this.s;
    return this.d
};
 """)
# 调用js方法  第一个参数是JS的方法名，后面的为js方法的参数  
val2 = ctx.call("add2", 1, 2) 
# 使用eval的写法同上，但是在传入字符串或者其他类型的数据时需要添加对应的格式,如下所示，具体可在程序中debug
#val3 = ctx.eval("add({0}, {1})").format(1,2) 
val4 = ctx.eval('add2("{0}", "{1}")').format("1","2")    
val5 = ctx.call("plus", 4, 2) 

print(val1,val2,val4,val5)
#如果打印中文乱码，参考：windows python运行execjs中出现编码问题 代码中是utf-8 但是运行环境就是gbk
#链接地址：https://blog.csdn.net/suwenlai/article/details/93047182
#全局搜一下 subprocess.py 文件的encoding，然后我这边初始值是encoding = None   然后改成‘utf-8’就行了  完美
print(ctx.call('validatePhone', '1232323218')) 
print(ctx.call('countdown', '111111111'))  

print('*'*50)

with open(realpath('test.js'),encoding='utf-8') as f:
    jsdata = f.read()
 
ctx = execjs.compile(jsdata)
print(ctx.call('add', '1', '2'),ctx.call('plus', 1.2, 1.8)) 
print(ctx.call('validatePhone', '11723212121')) 
print(ctx.call('validatePhone', '13362311111')) 

print('*'*50)

with open(realpath('product.js'),encoding='utf-8') as f:
    jsdata = f.read()

ctx = execjs.compile(jsdata)
print(ctx.eval('cookie'))
print(ctx.eval('security_verify_data'))