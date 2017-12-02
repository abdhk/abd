from opensooq.items import OpenSooqCar
from scrapy.spiders import BaseSpider, CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.loader import XPathItemLoader, ItemLoader
from scrapy.loader.processors import Join, MapCompose
from scrapy.linkextractors import LinkExtractor
from opensooq.items import OpenSooqCar
import sqlalchemy as sa
import pandas as pd

class Opensooq(CrawlSpider):
    name = "opensooq"
    allowed_domains = ["opensooq.com"]
    cars_list_xpath = "//div[contains(@class, 'galleryCont')]"
    start_urls = [u"https://sa.opensooq.com/ar/%D8%AD%D8%B1%D8%A7%D8%AC-%D8%A7%D9%84%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9"]
    
    rules = [
        Rule(LinkExtractor(allow=('\S+/'),
                           restrict_xpaths='//li[@class="next"]/a'),
             follow=True),
        Rule(LinkExtractor(allow=('\S+/'),
                           restrict_xpaths='//div[@class="rectLiImg tableCell vTop pl15 relative"]'),
             follow=True,
             callback='parse_sub'),
        ]
             
    item_fields = {'city' : ".//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[1]/a/text()",
                   'brand' : "//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[2]/a/text()",
                   'model' : "//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[3]/a/text()",
                   'model_year': "//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[4]/a/text()",
                   'status' : "//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[5]/a/text()",
                   'gear_type' :"//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[7]/a/text()",
                   'fuel_type': "//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[8]/a/text()",
                   'color' : "//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[9]/a/text()",
                   'payment_type' :  "//div[contains(@class, 'galleryCont')]/div[@class='customP']/ul/li[10]/a/text()",
                   'description' : "//div[contains(@class, 'galleryCont')]/div[@class='albumDet clear']/div[@class='postDesc']/p/text()",
                   'price': '//span[contains(@class, "priceNo")]/text()'
                   }
    def __init__(self):
        super().__init__()
        
    
    def parse_sub(self, response):
        self.logger.info('----------IN FUNCTION------------')
        
        
        loader = ItemLoader(OpenSooqCar(), response=response)
        
        loader.default_input_processor = MapCompose(str.strip)
        loader.default_output_processor = Join()
        
        loader.add_value('url', response.url)
        
        for field, xpath in self.item_fields.items():
            self.logger.info(field)
            loader.add_xpath(field, xpath)
        
        yield loader.load_item()
