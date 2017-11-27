from scrapy.item import Item, Field

class OpenSooqCar(Item):
    city = Field()
    brand = Field()
    model = Field()
    model_year = Field()
    color = Field()
    status = Field()
    fuel_type=Field()
    gear_type = Field()
    payment_type = Field()
    description = Field()
    url = Field()
    
    
    
