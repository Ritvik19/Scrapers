# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta

def get_claps(claps_str):
    if (claps_str is None) or (claps_str == '') or (claps_str.split is None):
        return 0
    split = claps_str.split('K')
    claps = float(split[0])
    claps = int(claps*1000) if len(split) == 2 else int(claps)
    return claps

class PythonfeaturesSpider(scrapy.Spider):
    name = 'pythonfeatures'
    allowed_domains = ['medium.com']
    start_urls = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.sdate = map(int, self.sdate.split('-'))
        self.edate = map(int, self.edate.split('-'))
        self.sdate = date(*self.sdate)
        self.edate = date(*self.edate)
        delta = self.edate - self.sdate
        
        for i in range(delta.days + 1):
            day = self.sdate + timedelta(days=i)
            self.start_urls.append('https://medium.com/python-features/archive/'+day.strftime("%Y/%m/%d"))

    def parse(self, response):
        for article in response.css('div.postArticle.postArticle--short.js-postArticle.js-trackPostPresentation.js-trackPostScrolls'):
            title = article.css('h3.graf--title::text').get()
            subtitle = article.css('h4.graf--subtitle::text').get()
            url = article.css('a::attr(href)').getall()[3]
            claps = article.css('span button::text').get()
            readingtime = article.css('span.readingTime::attr(title)').get()
            if title is not None:
                yield {
                    'title': title,
                    'subtitle': subtitle,
                    'url': url,
                    'claps': get_claps(claps),
                    'readingtime': readingtime,
                    'publication': self.name
                }
