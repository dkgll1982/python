# https://blog.csdn.net/Yunwubanjian/article/details/91411103?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control

FormRequest.from_response()
（1）FormRequest.from_response也可以进行设置 formdata，用来填写并提交表单，实现模拟登入。
（2）FormRequest.from_response相当于是自动识别post。
（3）FormRequest.from_response与FormRequest.http.from_response也没有区别。

scrapy.FormRequest与FormRequest.from_response 的区别##
1.什么情况下分别使用什么
先找到填写表单时发送的post请求的地址，下面以豆瓣登入为例子：

可以看见其post的地址为：https://accounts.douban.com/j/mobile/login/basic
然后用浏览器访问https://accounts.douban.com/j/mobile/login/basic

发现页面没有表单信息（也就是没有填写账号、密码的地方），所以，我们只能采用scrapy.FormRequest，手动的去发送post请求。
如果浏览器访问某post网址时，里面有表单信息，这时候你可以用FormRequest.from_response也可以用scrapy.FormRequest实现模拟登入

2.参数的不一样
scrapy.FormRequest的必填参数是目标网址，而FormRequest.from_response的必填参数是response

def parse(self, response):
        # 如果有验证码
        # 没有验证码，就进行登入
        # 设置要发送的post信息
        data = {
            'name': '18371417971',
            'password': 'wanghao211',
            'remember': 'false'
        }
        print("登入中...")
        return FormRequest(
            url='https://accounts.douban.com/j/mobile/login/basic',
            method='post',
            formdata=data,
            meta={'cookiejar':response.meta['cookiejar']},
            # 如果需要多次提交表单，且url一样，那么就必须加此参数dont_filter，防止被当成重复网页过滤掉了
            dont_filter=True,
            callback=self.next
        )
##############################
def parse(self, response):
        # 如果有验证码
        # 没有验证码，就进行登入
        # 设置要发送的post信息
        data = {
            'name': '18371417971',
            'password': 'wanghao211',
            'remember': 'false'
        }
        print("登入中...")
        return FormRequest(
            url=response,
            method='post',
            formdata=data,
            meta={'cookiejar':response.meta['cookiejar']},
            # 如果需要多次提交表单，且url一样，那么就必须加此参数dont_filter，防止被当成重复网页过滤掉了
            dont_filter=True,
            callback=self.next
            )

3.小结
总的来说，scrapy.FormRequest的功能更加强大，如果FormRequest.from_response 不能解决就用scrapy.FormRequest来解决模拟登入，毕竟是手动设置目标网址，比自动识别要精准。
 