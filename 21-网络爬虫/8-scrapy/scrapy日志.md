"""
logging :
    scrapy：
        settings中设置LOG_LEVEL="WARNING"
        settings中设置LOG_FILE="./log.log" #设置日志保存的位置，设置后在终端不会显示日志内容
        import logging 实例化一个logger的方式在任何文件中使用logger输出内容
                logger = logging.getLogger(__name__) #实例化
    普通项目中：
        import logging
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w') #设置日志输出格式
        实例化一个ogger = logging.getLogger(__name__)
        在任何py文件中调用logger即可
"""
参考链接：https://www.cnblogs.com/ywjfx/p/11079621.html