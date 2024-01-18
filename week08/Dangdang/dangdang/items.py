import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    now_price = scrapy.Field()
    short_title = scrapy.Field()
    pre_price = scrapy.Field()