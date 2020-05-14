# -*- coding: utf-8 -*-
import scrapy, re


class ProblemsSpider(scrapy.Spider):
    name = 'problems'
    allowed_domains = ['codeforces.com']
    start_urls = ['https://codeforces.com/problemset/']

    def parse(self, response):
        for tr in response.xpath('//table[@class="problems"]').xpath('//tr')[1:]:
            meta = {
                'ProblemCode': ' '.join(tr.xpath('.//td[1]//text()').getall()).strip(),
                'Url': tr.xpath('.//td[1]//a/@href').get(),
                'ProblemTitle': ' '.join(tr.xpath('.//td[2]//div[1]//text()').getall()).strip(),
                'Tags': re.sub('\s+', ' ', ' '.join(tr.xpath('.//td[2]//div[2]//text()').getall()).strip()).strip(),
            }
            if meta['Url'] is not None:
                yield response.follow(url=meta['Url'], callback=self.parse_problems, meta=meta)
        
        nextpage = response.xpath('//a[@class="arrow"]')[-1].xpath(".//@href").get()
        if nextpage:
            yield response.follow(url=nextpage, callback=self.parse)
            
    def parse_problems(self, response):
        yield{
                'ProblemCode': response.request.meta['ProblemCode'],
                'Url': response.request.meta['Url'],
                'ProblemTitle': response.request.meta['ProblemTitle'],
                'Tags': response.request.meta['Tags'],
                'Description': re.sub('\s+', ' ', 
                    ' '.join(response.xpath('//div[@class="problem-statement"]//p//text()').getall()).strip()).strip(),
        }
