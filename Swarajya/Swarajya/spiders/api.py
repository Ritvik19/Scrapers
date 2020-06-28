# -*- coding: utf-8 -*-
import scrapy, json


class ApiSpider(scrapy.Spider):
    name = 'api'
    allowed_domains = ['swarajyamag.com']
    start_urls = [f'https://swarajyamag.com/api/v1/stories?offset={i}&limit=100&fields=id%2Cheadline%2Cslug%2Curl' for i in range(0, 45701, 100)]

    def parse(self, response):
        resjson = json.loads(response.text)
        stories = resjson['stories']
        for story in stories:
            yield {
                'headline': story['headline'],
                'url': story['url'],
                'slug': story['slug']
            }
