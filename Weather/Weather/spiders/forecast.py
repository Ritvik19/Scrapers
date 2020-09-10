# -*- coding: utf-8 -*-
import scrapy


class ForecastSpider(scrapy.Spider):
    name = 'forecast'
    allowed_domains = ['api.openweathermap.org']
    
    def __init__(self, city='', **kwargs):
        API_KEY = open('E:/API-Credentials/Weather.txt').read().strip()
        self.start_urls = [f'http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={API_KEY}']
        super().__init__(**kwargs)
    
    def parse(self, response):
        jsonresponse = json.loads(response.text)
        yield jsonresponse
