# Scrapy settings for Crawl_sjwz project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Crawl_sjwz'

SPIDER_MODULES = ['Crawl_sjwz.spiders']
NEWSPIDER_MODULE = 'Crawl_sjwz.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Crawl_sjwz (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Crawl_sjwz.middlewares.CrawlSjwzSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Crawl_sjwz.middlewares.CrawlSjwzDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   #'Crawl_sjwz.pipelines.CrawlSjwzPipeline': 123,
   'Crawl_sjwz.pipelines.CrawlSjwz2Pipeline': 123,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 在Scrapy中实现是一个能将数据以Excel格式导出的Exporter。

# 共有3个步骤：
# ①自定义导出exporters方法。
# ②将自定义方法添加至配置文件中。(FEED_EXPORTERS)
# ③运行爬虫声明导出格式为自定义格式。 

# 用户自定义的EXPORTERS，自已实现数据转换。
FEED_EXPORTERS = {
   #说明：Crawl_sjwz是项目名称；exporters是文件名；ExcelItemExporter是自定义类名
   'excel':'Crawl_sjwz.exporters.ExcelItemExporter'
}

# 直接在配置文件中配置导出器相关属性
# 1.FEED_URI:导出文件路径
# FEED_URI='data\%(name)s.xls'

# # 2.FEED_FORMAT:导出文件的格式
# FEED_FORMAT='xls'

# # 3.FEED_EXPORT_ENCODING:导出文件的编码格式(默认情况下,json使用数字编码,其他格式使用'utf-8'编码)
# FEED_EXPORT_ENCODING='gbk'

# # 4.FEED_EXPORT_FIELDS:默认导出全部字段,对字段进行排序:
# FEED_EXPORT_FIELDS=['name','index','link','content']