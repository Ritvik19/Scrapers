# -*- coding: utf-8 -*-
import scrapy, json


class ApodSpider(scrapy.Spider):
    name = 'apod'
    
    API_KEY = open('E:/API-Credentials/NASA.txt').read().strip()
    
    allowed_domains = ['api.nasa.gov']
    start_urls = ['https://api.nasa.gov/planetary/apod?api_key='+API_KEY]

    def parse(self, response):
        yield json.loads(response.text)
