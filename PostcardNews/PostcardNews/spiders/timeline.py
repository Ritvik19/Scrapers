# -*- coding: utf-8 -*-
import scrapy


class TimelineSpider(scrapy.Spider):
    name = 'timeline'
    allowed_domains = ['postcard.news']
    start_urls = ['https://postcard.news/timeline/']

    def parse(self, response):
        for li in response.css('li.post-item'):
            yield {
                'headline': li.css('h3 a::text').get(),
                'url': li.css('h3 a::attr(href)').get(),
                'category': li.css('h5.post-cat-wrap span::text').get()
            }
                
        nextpage = response.css('li.current+li>a::attr(href)').get()
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
