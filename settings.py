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

ITEM_PIPELINES = {'opensooq.pipeline.OpenSooqPipeline':1,}

