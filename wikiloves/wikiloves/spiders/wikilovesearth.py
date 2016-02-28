# -*- coding: utf-8 -*-
import scrapy
from wikiloves.items import WikilovesItem, WikilovesItemIndice
from urlparse import urljoin


INDICE = 'ccaa nlic stotal sterrestre smarina scalic stotalca'.split()
ITEM = 'nombre codigo fichas provincia coordenadas superficie categoria imagen'.split()
BASE = 'https://es.wikipedia.org'

class WikilovesearthSpider(scrapy.Spider):
    name = "wikilovesearth"
    allowed_domains = ["es.wikipedia.org"]
    start_urls = (
        'https://es.wikipedia.org/wiki/Anexo:Lugares_de_importancia_comunitaria_de_Espa%C3%B1a',
    )

    def parse(self, response):
        for fila in response.xpath('//div[@id="mw-content-text"]//table/tr[td]'):
            item = WikilovesItemIndice()
            datos = [''.join(c.xpath('.//text()').extract()).strip() for c in fila.xpath('.//td')]
            for i, atributo in enumerate(INDICE):
                item[atributo] = datos[i]
            yield item
            url = ''.join(fila.xpath('td[1]//a/@href').extract()).strip()
            if url:
                request = scrapy.Request(urljoin(BASE, url), callback=self.parse_ccaa)
                yield request

    def parse_ccaa(self, response):
        for fila in response.xpath('//div[@id="mw-content-text"]//table[not(contains(@class, "collapsible"))]/tr[td]'):
            item = WikilovesItem()
            datos = [''.join(c.xpath('.//text()').extract()).strip() for c in fila.xpath('.//td')]
            for i, atributo in enumerate(ITEM):
                item[atributo] = datos[i]
            yield item
