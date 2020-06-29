# -*- coding: utf-8 -*-
import scrapy


class OnelinersSpider(scrapy.Spider):
    name = 'oneliners'
    allowed_domains = ['onelinefun.com']
    start_urls = ['https://onelinefun.com/']

    def parse(self, response):
        for oneliner in response.css('div.o p::text').getall():
            yield {
                'oneliner': oneliner
            }
            
        nextpage = response.xpath('//a[contains(text(),"Next one liners →")]/@href').get()
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
