# -*- coding: utf-8 -*-
import scrapy


class ViralnovaSpider(scrapy.Spider):
    name = 'viralnova'
    allowed_domains = ['viralnova.com']
    start_urls = ['https://viralnova.com/']

    def parse(self, response):
        for div in response.css('section div::text').getall():
            yield {
                'headline': div
            }
        
        try:
            older = response.css('.pagination a::attr(href)').getall()[0]
        except:
            older = None
            
        if older is not None:      
            yield response.follow(url=older, callback=self.parse)