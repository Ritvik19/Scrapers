# -*- coding: utf-8 -*-
import scrapy


class PoliticsSpider(scrapy.Spider):
    name = 'politics'
    allowed_domains = ['www.indiatvnews.com']
    start_urls = ['https://www.indiatvnews.com/politics/1']

    def parse(self, response):
        for li in response.css('li.p_news'):
            yield{
                'headline': li.css('h3.title a::text').get(),
                'description': li.css('p.dic::text').get(),
                'url': li.css('h3.title a::attr(href)').get(),
                'category': self.name
            }

        url_tokens = response.url.split('/')
        nextpage = '/'.join(url_tokens[:-1]+[str(int(url_tokens[-1])+1)])
        
        yield response.follow(url=nextpage, callback=self.parse)
