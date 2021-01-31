# -*- coding: utf-8 -*-

# Scrapy settings for meizitu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'

# 爬取深度
DEPTH_LIMIT = 3
# 图片存放位置
IMAGES_STORE = 'images'

#过滤小图片
#注意：这些尺寸的限制不会影响缩略图生成
#默认情况下，没有限制，所有的图片都会被处理。
# 图片最小宽度
IMAGES_MIN_WIDTH = 1920
# 图片最小高度
IMAGES_MIN_HEIGHT = 1000
# 图片过期时间
IMAGES_EXPIRES = 90
# 生成缩略图选项
# IMAGES_THUMBS = {
#  'small': (50, 50),
#  'big': (270, 270),
# }

#还有一些选项需要注意：
# 下载延迟，别把别人站点拖垮了，慢点
DOWNLOAD_DELAY = 0.2
# 爬虫并发数，默认是 16
CONCURRENT_REQUESTS = 20

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meinvtu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

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
#    'meinvtu.middlewares.MeinvtuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'meinvtu.middlewares.MeinvtuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'meizitu.pipelines.PicscrapyPipeline': 300,
}
LOG_LEVEL = "WARNING"
LOG_FILE = './log.log'  #设置日志保存的位置，设置后在终端不会显示日志内容
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
