# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    rate = scrapy.Field()
    summary = scrapy.Field()
    type = scrapy.Field()
    actor = scrapy.Field()
    link =  scrapy.Field()

class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
