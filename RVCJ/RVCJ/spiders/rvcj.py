# -*- coding: utf-8 -*-
import scrapy


class RvcjSpider(scrapy.Spider):
    name = 'rvcj'
    allowed_domains = ['www.rvcj.com']
    start_urls = [f'https://www.rvcj.com/page/{i}' for i in range(1, 783)]

    def parse(self, response):
        for h2 in response.css('h2::text').getall():
            yield{
                'headline': h2
            }
