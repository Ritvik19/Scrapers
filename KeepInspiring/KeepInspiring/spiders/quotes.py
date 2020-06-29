# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.keepinspiring.me']
    start_urls = ['http://www.keepinspiring.me/category/quotes/']

    def parse(self, response):
        for url in response.css('h2.entry-title a::attr(href)').getall():
            yield response.follow(
                url=url, callback=self.parse_follow
            )
            
        nextpage = response.xpath('//a[contains(text(),"Next →")]/@href').get()
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
            
    def parse_follow(self, response):
        for div in response.css('div.author-quotes::text').getall():
            if div.strip() != '':
                yield {
                    'quote': div.strip()
                }
