# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuperspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

    itemUrl = scrapy.Field()
    itemName = scrapy.Field()
    itemLocNo = scrapy.Field()
    itemLocation = scrapy.Field()




