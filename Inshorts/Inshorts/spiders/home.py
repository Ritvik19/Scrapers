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

class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['inshorts.com/']
    start_urls = ['https://inshorts.com/en/read/']

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