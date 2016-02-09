# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikilovesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    superficie = scrapy.Field()
    supterrestre = scrapy.Field()
    ccaa = scrapy.Field()
    provincia = scrapy.Field()
    coordenadas = scrapy.Field()



