import scrapy


class FirstItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()
