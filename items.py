from scrapy.item import Item, Field
from scrapy.loader.processors import Join, MapCompose

def replace_img(x):
    return x.replace('75x75', '700x0')

def join_img_names(x):
    return '|'.join(x)
def extract_img_name(x):
    return x.split('/')[-1]

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
    price = Field()
    images_names = Field(input_processor = MapCompose(extract_img_name),
                        output_processor= join_img_names)
    
    
    
class OpenSooqCarImage(Item):
    images = Field()
    image_urls = Field(input_processor=MapCompose(replace_img))
    
