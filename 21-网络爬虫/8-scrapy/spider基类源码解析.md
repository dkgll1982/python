参考链接：https://blog.csdn.net/weixin_39810306/article/details/104475941

一旦spider的子类被实例化，__ init __ 中的代码就会被执行，所以需要设定name和 star_url 两个属性。
然而Spider 的子类被实例化后并不会马上被执行爬网，只有在 start_requests 被调用时，蜘蛛才会执行爬网。
如果想修改最初爬取某个网站的 REquests 对象，则可以重写（override）start_requests 函数。