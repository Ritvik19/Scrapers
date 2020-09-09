# -*- coding: utf-8 -*-
import scrapy, json


class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['www.reddit.com']
    
    def __init__(self, subreddit='', **kwargs):
        self.start_urls = [f'http://www.reddit.com/r/{subreddit}/new.json?sort=new/']
        self.subreddit = subreddit
        super().__init__(**kwargs)

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        name_of_last = None
        
        for post in jsonresponse['data']['children']:
            yield {
                'title': post['data'].get('title', ''),
                'text': post['data'].get('selftext', ''),
                'type': post['data'].get('post_hint', ''),
                'flairs': post['data'].get('link_flair_text', ''),
                'media': post['data'].get('url_overridden_by_dest', ''),
                'created': post['data'].get('created', '')
            }
            
            name_of_last = post['data'].get('name', None)
        
        if name_of_last is not None:    
            yield response.follow(url=f'http://www.reddit.com/r/{self.subreddit}/new.json?sort=new&after={name_of_last}', callback=self.parse)
