使用vs code环境调试scrapy框架程序
最近使用scrapy框架，因为我们使用scrapy框架一般都是通过命令行来执行的，所以对于我们调试就会出现很多的不便，上网查了一圈，发现很多都是一些pycharm软件的教程，vs code 很少，而且有的讲的不是很明白，先记录下来。

要想在vocode里进行调试，首先我们要先模拟一下，在vs code端进行运行scrapy，所以我们首先解决的是怎么在python端运行框架，而不是使用命令行来执行。解决办法如下：

1，在项目下面新建一个文件，比如：run.py，这个名字随意。这个文件是和setting.py在同一个级别即可。

2，在run.py下添加如下代码。

from scrapy.cmdline import execute
import sys
import os
# 获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))
print(dirpath)
# 添加环境变量
sys.path.append(dirpath)
# 启动爬虫,第三个参数为爬虫name
execute(['scrapy','crawl','XXX'])
XXX是你爬虫的名字，注意：这里的名字的不是你项目名字，而是你scrapy里爬虫里的name的值。

3，到这里我们就可以不使用命令行来执行里，可以直接运行这个run.py文件，就会直接执行scrapy框架了。

4，调试 按F5执行，如下图所示：
————————————————
版权声明：本文为CSDN博主「这孩子谁懂哈」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zhaomengszu/article/details/88885852