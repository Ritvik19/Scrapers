# -*- coding: utf-8 -*-
import scrapy


class FactcheckSpider(scrapy.Spider):
    name = 'factcheck'
    allowed_domains = ['www.opindia.com']
    start_urls = ['https://www.opindia.com/category/fact-check/']

    def parse(self, response):
        category = response.css('h1.tdb-title-text::text').get()
        
        for h in response.css('div.td_block_inner.tdb-block-inner.td-fix-index div.tdb_module_loop.td_module_wrap.td-animation-stack h3 a'):
            yield {
                'headline': h.css('::text').get(),
                'url': h.css('::attr(href)').get(),
                'category': category
            }

        nextpage = response.css('span.current+a::attr(href)').get()
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
