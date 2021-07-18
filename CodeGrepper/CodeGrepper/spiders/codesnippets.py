# -*- coding: utf-8 -*-
import scrapy


class CodesnippetsSpider(scrapy.Spider):
    name = 'codesnippets'
    allowed_domains = ['www.codegrepper.com']
    start_urls = ['http://www.codegrepper.com/']

    def parse(self, response):
        for a in response.css('ul.code_language_large a'):
            link = a.css('::attr(href)').get()
            yield response.follow(url=link, callback=self.parse_list_of_snippets, meta={'title': ' '.join(a.css(' ::text').getall()).strip()})
            

    def parse_list_of_snippets(self, response):
        for a in response.css('div#language_snipper_cats_holder li a'):
            code_url =  a.css('::attr(href)').get()
            meta = {
                'language': response.meta['title'],
                'title': ' '.join(a.css(' ::text').getall()).strip()
            }
            yield response.follow(url=code_url, callback=self.parse_snippet, meta=meta)
            
    def parse_snippet(self, response):
        yield {
            'language': response.meta['language'],
            'title': response.meta['title'],
            'code': response.css('meta[name="description"]::attr(content)').get()
        }