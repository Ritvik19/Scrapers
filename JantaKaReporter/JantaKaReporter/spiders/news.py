# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.jantakareporter.com']
    start_urls = [
        'https://www.jantakareporter.com/business/',
        'http://www.jantakareporter.com/india/',
        'http://www.jantakareporter.com/politics/',
        'http://www.jantakareporter.com/world/',
        'http://www.jantakareporter.com/sports/',
        'http://www.jantakareporter.com/entertainment/',
        'http://www.jantakareporter.com/culture/',
        'http://www.jantakareporter.com/education/',
        'http://www.jantakareporter.com/in-pictures/',
        'http://www.jantakareporter.com/interview/',
        'http://www.jantakareporter.com/science/',
        'http://www.jantakareporter.com/society/',
        'http://www.jantakareporter.com/technology/',
        'http://www.jantakareporter.com/social-media-buzz/'
    ]

    def parse(self, response):
        category = response.css("h1.entry-title.td-page-title::text").get()
        for headline in response.css("div.td-block-span6 h3.entry-title.td-module-title a"):
            yield {
                'headline': headline.css("::text").get(),
                'url': headline.css("::attr(href)").get(),
                'category' : category
            }
            
        nextpage = response.css('span.current+a::attr(href)').get()
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
