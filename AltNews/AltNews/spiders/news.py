# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.altnews.in']
    start_urls = ['https://www.altnews.in/topics/news/']

    def parse(self, response):
        for a in response.xpath("//h2/a"):
            yield {
                'headline': a.xpath("./text()").get(),
                'url': a.xpath("./@href").get()
            }
        
        nextpage = response.css("a.next::attr(href)").get()
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
