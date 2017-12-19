BOT_NAME = 'opensooq'

SPIDER_MODULES = ['opensooq.spiders']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'eweiwi',
    'password': '',
    'database': 'opensooq'
    }
IMAGE_STORE = '/images'

ITEM_PIPELINES = {'opensooq.pipeline.OpenSooqPipeline':10,
                  'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/Users/eweiwi/code/python/scrapy/opensooq/images'


DELTAFETCH_ENABLED = True
DELTAFETCH_DIR = '/Users/eweiwi/code/python/scrapy/opensooq/'

SPIDER_MIDDLEWARES = {
    'scrapy_deltafetch.DeltaFetch': 100,
}

#DOWNLOADER_MIDDLEWARES = {
    #'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    #'scrapy_proxies.RandomProxy': 100,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    #}

#PROXY_MODE = 0
#RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

#PROXY_LIST = '/Users/eweiwi/code/python/scrapy/opensooq/li.txt'

#USER_AGENT_CHOICES = [
    #'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0',
    #'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    #'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)',
    #'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
    #'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
    #'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0',
    #'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    #'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
#]

#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=True
