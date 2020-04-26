# -*- coding: utf-8 -*-
import scrapy


class BeginnerSpider(scrapy.Spider):
    name = 'beginner'
    allowed_domains = ['www.codechef.com/problems/school']
    start_urls = ['https://www.codechef.com/problems/school']

    def parse(self, response):
    
        for tr in response.xpath("//table[@class='dataTable']/tbody/tr"):
            title = tr.xpath('.//td[1]/div/a/b/text()').get()
            code = tr.xpath('.//td[2]/a/text()').get()
            submissions = tr.xpath('.//td[3]/div/text()').get()
            accuracy = tr.xpath('.//td[4]/a/text()').get()
                
            yield{
                'title': title,
                'code': code,
                'submissions': submissions,
                'accuracy': accuracy
            }