# -*- coding: utf-8 -*-
import scrapy, json


class QodSpider(scrapy.Spider):
    name = 'qod'
    allowed_domains = ['quotes.rest']
    start_urls = ['http://quotes.rest/qod.json/']

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        
        yield {
            'title': jsonresponse['contents']['quotes'][0]['title'],
            'date': jsonresponse['contents']['quotes'][0]['date'],
            'qoute': jsonresponse['contents']['quotes'][0]['quote'],
            'author': jsonresponse['contents']['quotes'][0]['author'],
            'tags': jsonresponse['contents']['quotes'][0]['tags'],
            'category': jsonresponse['contents']['quotes'][0]['category'],
            'url': jsonresponse['contents']['quotes'][0]['permalink'],
            'background': jsonresponse['contents']['quotes'][0]['background'],
        }

