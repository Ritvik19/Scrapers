# -*- coding: utf-8 -*-
import scrapy


class OpindiaSpider(scrapy.Spider):
    name = 'opindia'
    allowed_domains = ['www.opindia.com']
    start_urls = [
        'https://www.opindia.com/category/politics/',
        'https://www.opindia.com/category/opinions/',
        'https://www.opindia.com/category/fact-check/',
        'https://www.opindia.com/category/media/',
        'https://www.opindia.com/category/variety/',
        'https://www.opindia.com/category/explainer/',
        'https://www.opindia.com/category/virtual-world/',
        'https://www.opindia.com/category/entertainment/',
        'https://www.opindia.com/category/political-history-of-india/',
        'https://www.opindia.com/category/government-and-policy/',
        'https://www.opindia.com/category/economy-and-finance/',
        'https://www.opindia.com/category/sports/',
        'https://www.opindia.com/category/crime/',
        'https://www.opindia.com/category/law/',
    ]

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
