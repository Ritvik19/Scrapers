# -*- coding: utf-8 -*-
import scrapy, json


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['thewire.in']
    start_urls = [
        'https://thewire.in/wp-json/thewire/v2/posts/category/politics/recent-stories/?per_page=10&page=0',
        'https://thewire.in/wp-json/thewire/v2/posts/category/economy/recent-stories/?per_page=10&page=0',
        'https://thewire.in/wp-json/thewire/v2/posts/category/external-affairs/recent-stories/?per_page=10&page=0',
        'https://thewire.in/wp-json/thewire/v2/posts/category/culture/recent-stories/?per_page=10&page=0',
        'https://thewire.in/wp-json/thewire/v2/posts/category/society/recent-stories/?per_page=10&page=0',
        'https://thewire.in/wp-json/thewire/v2/posts/category/law/recent-stories/?per_page=10&page=0',
        'https://thewire.in/wp-json/thewire/v2/posts/category/security/recent-stories/?per_page=10&page=0',
        'https://thewire.in/wp-json/thewire/v2/posts/opinion/all/recent-stories/?per_page=10&page=0'
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        
        for story in jsonresponse:
            yield {
                'title': story['post_title'],
                'excerpt': story['post_excerpt'],
                'categories': [x['name'] for x in story['categories']],
                'tags': story['tags'],                
            }
        
        if len(jsonresponse) == 10:
            url_chunks = response.request.url.split('=')
            next_url = '='.join(url_chunks[:2]+[str(int(url_chunks[2])+1)])
            
            yield response.follow(url=next_url, callback=self.parse)
        
