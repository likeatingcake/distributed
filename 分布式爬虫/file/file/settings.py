# Scrapy settings for file project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "file"

SPIDER_MODULES = ["file.spiders"]
NEWSPIDER_MODULE = "file.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 2

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
   "cookie": "_ga=GA1.2.1160954745.1702971919; _gid=GA1.2.9256415.1702971919; _ga_CCMJLXNLX2=GS1.2.1702971919.1.1.1702973681.0.0.0"
}


# # 使用 scrapy-redis 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # 使用 scrapy-redis 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# # 允许暂停和恢复
SCHEDULER_PERSIST = True
#
# # 使用队列调度请求
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
#
# # Redis连接配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


ITEM_PIPELINES = {
    'file.pipelines.MongoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
FILES_STORE = "./Files"


MONGO_URI = 'localhost'
MONGO_DATABASE = 'python_file'
