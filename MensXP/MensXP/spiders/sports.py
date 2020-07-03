# -*- coding: utf-8 -*-
import scrapy


class SportsSpider(scrapy.Spider):
    name = 'sports'
    allowed_domains = ['www.mensxp.com']
    start_urls = ['https://www.mensxp.com/sports-p1.html']

    def parse(self, response):
        for title, tag in zip(response.css('a.section-height'), response.css('a.section-tag::text').getall()):
            yield {
                'title':  title.css('span.color-link::text').get(),
                'url': title.css('::attr(href)').get(),
                'tag': tag,
                'category': 'sports'
            }

        nextpage = response.css('a.selected+a::attr(href)').get()
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
