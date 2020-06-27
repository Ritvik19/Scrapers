# -*- coding: utf-8 -*-
import scrapy


class ViralstoriesSpider(scrapy.Spider):
    name = 'viralstories'
    allowed_domains = ['viralstories.in']
    start_urls = ['http://viralstories.in/']


    def parse(self, response):
        for div in response.css('article a::text').getall()[2::4]:
            yield {
                'headline': div
            }
        
        try:
            older = response.css('.pagination a::attr(href)').getall()[0]
        except:
            older = None
            
        if older is not None:      
            yield response.follow(url=older, callback=self.parse)