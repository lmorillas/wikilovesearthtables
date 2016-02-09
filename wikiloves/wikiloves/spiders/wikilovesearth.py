# -*- coding: utf-8 -*-
import scrapy
from wikiloves.items import WikilovesItem
from scrapy import request
from urllib import urljoin


class WikilovesearthSpider(scrapy.Spider):
    name = "wikilovesearth"
    allowed_domains = ["es.wikipedia.org"]
    start_urls = (
        'https://es.wikipedia.org/wiki/Anexo:Lugares_de_importancia_comunitaria_de_Espa%C3%B1a',
    )

    def parse(self, response):

        tabla = response.xpath('//table/tr[td[1]//a]')
        for row in tabla:
            item = WikilovesItem()
            lic = row.xpath('td[1]//a//text()').extract()[0]
            url = row.xpath('td[1]//a/@href').extract()[0]
            request = scrapy.Request(urljoin(BASE, url),
                             callback=self.parse_ccaa)
            request.meta['lic'] = lic
            yield request

    def parse_ccaa(self, response):
        lic = response.meta['lic']





def parse_page1(self, response):
    item = MyItem()
    item['main_url'] = response.url
    request = scrapy.Request("http://www.example.com/some_page.html",
                             callback=self.parse_page2)
    request.meta['item'] = item
    return request

def parse_page2(self, response):
    item = response.meta['item']
    item['other_url'] = response.url
    return item