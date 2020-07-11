# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['tfipost.com']
    start_urls = [
        'https://tfipost.com/category/politics/',
        'https://tfipost.com/category/economy/',
        'https://tfipost.com/category/defmain/',
        'https://tfipost.com/category/geopolitics/',
        'https://tfipost.com/category/knowledge/',
        'https://tfipost.com/category/tfilounge/',
        'https://tfipost.com/category/newswire/'
    ]

    def parse(self, response):
        category = response.css('h1.jeg_cat_title::text').get()
        
        for post in response.css('div.jeg_inner_content h3.jeg_post_title a'):
            yield {
                'title': post.css('::text').get(),
                'url': post.css('::attr(href)').get(),
                'category': category
            }
            
        nextpage = response.css('span.page_number.active+a.page_number::attr(href)').get()
        
        if nextpage is not None:
            yield response.follow(
                url=nextpage,
                callback=self.parse
            )
        
