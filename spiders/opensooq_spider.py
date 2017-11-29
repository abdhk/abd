from opensooq.items import OpenSooqCar
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from opensooq.items import OpenSooqCar


class Opensooq(BaseSpider):
    name = "opensooq"
    allowed_domains = ["opensooq.com"]
    start_urls = ("https://sa.opensooq.com/ar/%D8%AD%D8%B1%D8%A7%D8%AC-%D8%A7%D9%84%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9",)
    """
    "https://eg.opensooq.com/ar/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%88%D9%85%D8%B1%D9%83%D8%A8%D8%A7%D8%AA/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9",
                  "https://lb.opensooq.com/ar/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%88%D9%85%D8%B1%D9%83%D8%A8%D8%A7%D8%AA/%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA-%D9%84%D9%84%D8%A8%D9%8A%D8%B9"
    """
    
    cars_list_xpath = "//div[@class='galleryCont specialPost']"

    cars_menue_xpath = "//li[@class='rectLi ie relative mb15']/div/div/a/@href"

    item_fields = {'city' : ".//div[@class='customP']/ul/li[1]/a/text()",
                   'brand' : ".//div[@class='customP']/ul/li[2]/a/text()",
                   'model' : ".//div[@class='customP']/ul/li[3]/a/text()",
                   'model_year': ".//div[@class='customP']/ul/li[4]/a/text()",
                   'status' : ".//div[@class='customP']/ul/li[5]/a/text()",
                   'gear_type' :".//div[@class='customP']/ul/li[7]/a/text()",
                   'fuel_type': ".//div[@class='customP']/ul/li[8]/a/text()",
                   'color' : ".//div[@class='customP']/ul/li[9]/a/text()",
                   'payment_type' :  ".//div[@class='customP']/ul/li[10]/a/text()",
                   'description' : ".//div[@class='albumDet clear']/div[@class='postDesc']/p/text()"
                   }

    def parse(self,response):
        selector=HtmlXPathSelector(response)
        for car in selector.select(self.cars_menue_xpath):
            car_url = car.xpath('.//div/div/a/@href').extract()
            url_sub = urljoin(response.url, car_url)
            yield (url_sub, callback='parse_sub')


    def parse_sub(self, response):

        selector = HtmlXPathSelector(response)

        for deal in selector.select(self.cars_list_xpath):
            loader = XPathItemLoader(OpensooqCar(), selector = deal)

            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
            
            
            
            
                   

