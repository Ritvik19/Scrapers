# -*- coding: utf-8 -*-
import scrapy


class SnippetsSpider(scrapy.Spider):
    name = 'snippets'
    allowed_domains = ['syntaxdb.com']
    start_urls = ['https://syntaxdb.com/reference/']

    def parse(self, response):
        dropdown = response.xpath("//ul[@id='language-dropdown']")
        for a in dropdown.xpath("./li/a"):
            yield response.follow(
                url=a.xpath(".//@href").get(), 
                callback=self.parse_language, 
                meta={'language': a.xpath("./text()").get()}
            )
            
    def parse_language(self, response):
        
        for ul_c in response.xpath("//ul[@class='collapsible']"):
            for li in ul_c.xpath("./li/div/ul/li"):
                yield response.follow(
                    url=li.xpath(".//@href").get(),
                    callback=self.parse_snippet,
                    meta={
                    'language': response.request.meta['language'],
                    'title': li.xpath(".//text()").get(),
                    }
                )
    
    def parse_snippet(self, response):
        code, example = response.xpath("//code[1]/text()").getall()
        
        yield {
            'title': response.request.meta['title'],
            'language': response.request.meta['language'],
            'code': code,
            'example': example,
            'notes': '\n'.join(response.css(".col.s12.m8.l8 p::text").getall())
        }