# -*- coding: utf-8 -*-
import scrapy


class ProfileheatmapSpider(scrapy.Spider):
    name = 'profileheatmap'
    allowed_domains = ['github.com']
    
    def __init__(self, username='', **kwargs):
        self.start_urls = [f'http://github.com/{username}/']
        super().__init__(**kwargs)

    def parse(self, response):
        for rect in response.css('rect'):
            yield {
                'date':rect.css('::attr(data-date)').get(),
                'count': rect.css('::attr(data-count)').get(),
            }
