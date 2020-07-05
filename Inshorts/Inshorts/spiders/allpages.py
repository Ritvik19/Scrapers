# -*- coding: utf-8 -*-
import scrapy, re

striptext = lambda x: re.sub(r"\s+", ' ', x).strip()

def process(filterdata):
    processeddata = []
    i = 0
    while i < len(filterdata):
        if filterdata[i].strip() not in ['short', 'by', '/', 'on', 'read more at'] and filterdata[i-1].strip() != 'read more at':
            processeddata.append(filterdata[i])
        i += 1
    return processeddata   

class AllpagesSpider(scrapy.Spider):
    name = 'allpages'
    allowed_domains = ['inshorts.com']
    start_urls = [
        'https://inshorts.com/en/read/automobile',
        'https://inshorts.com/en/read/business',
        'https://inshorts.com/en/read/entertainment',
        'https://inshorts.com/en/read/hatke',
        'https://inshorts.com/en/read/',
        'https://inshorts.com/en/read/miscellaneous',
        'https://inshorts.com/en/read/national',
        'https://inshorts.com/en/read/politics',
        'https://inshorts.com/en/read/science',
        'https://inshorts.com/en/read/sports',
        'https://inshorts.com/en/read/startup',
        'https://inshorts.com/en/read/technology',
        'https://inshorts.com/en/read/world'
    ]

    def parse(self, response):
        data = response.css("div.news-card *::text").getall()
        stripdata = list(map(striptext, data))
        filterdata = list(filter(lambda x : x != '', stripdata))
        processdata = process(filterdata)
        for i in range(0, len(processdata), 8):
            yield {
                'Headline': processdata[i],
                'Author': processdata[i+1],
                'Time': processdata[i+2],
                'Date': processdata[i+3],
                'Article': processdata[i+4],
            }
