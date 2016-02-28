# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikilovesItem(scrapy.Item):
    # define the fields for your item here like:
    '''
    Nombre
    Código
    Fichas
    Provincia
    Coordenadas
    Superficie
    Categoría en Commons
    Imagen
    Sube tu foto
    '''
    nombre = scrapy.Field()
    codigo = scrapy.Field()
    fichas = scrapy.Field()
    provincia = scrapy.Field()
    coordenadas = scrapy.Field()
    superficie = scrapy.Field()
    categoria = scrapy.Field()
    imagen = scrapy.Field()



class WikilovesItemIndice(scrapy.Item):
    '''
    Comunidad autónoma
    Número de lugares de interés comunitario
    Superficie total protegida como LIC (ha)
    Superficie terrestre protegida como LIC (ha)
    Superficie marina protegida como LIC (ha)
    Superficie de la comunidad autónoma protegida como LIC (%)
    Superficie total c.a.
    '''
    ccaa = scrapy.Field()
    nlic = scrapy.Field()
    stotal = scrapy.Field()
    sterrestre = scrapy.Field()
    smarina = scrapy.Field()
    scalic = scrapy.Field()
    stotalca = scrapy.Field()



