# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['aninews.in']
    start_urls = [
        'https://aninews.in/category/national/',
        'https://aninews.in/category/world/',
        'https://aninews.in/category/business/',
        'https://aninews.in/category/sports/',
        'https://aninews.in/category/lifestyle/',
        'https://aninews.in/category/entertainment/',
        'https://aninews.in/category/health/',
        'https://aninews.in/category/science/',
        'https://aninews.in/category/tech/',
        'https://aninews.in/category/environment/',
    ]

    def parse(self, response):
        category = response.url.split('/')[4]
        for div in response.css('div.col-sm-6.col-xs-12.extra-related-block'):
            yield {
                'headline': div.css('h6.title::text').get(),
                'description': div.css('p.text.small::text').get(),
                'url': div.css('a.read-more::attr(href)').get(),
                'category': category
            }
            
        nextpage = response.css('li.page-next a::attr(href)').get()
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
            
            