# -*- coding: utf-8 -*-
import scrapy, json


class StoriesSpider(scrapy.Spider):
    name = 'stories'
    allowed_domains = ['www.scoopwhoop.com']
    start_urls = ['https://www.scoopwhoop.com/api/v4/read/all/?offset=0&limit=100']

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        
        nextoffset = jsonresponse['next_offset']
        
        if jsonresponse['status'] == 1:
        
            for i, data in enumerate(jsonresponse['data']):
                try:
                    yield {
                        'title' : data['title'],
                        'category': data['category'],
                        'slug': data['slug'],
                        'pub_date': data['pub_date']
                    }
                except:
                    with open(f"iter{nextoffset-1}-{i}.json", "w") as f:
                        json.dump(data, f)
        else:
            print('\n\n\n\n\n\n\n\n\n\n\nError\n\n\n\n\n\n\n\n\n\n\n')
        
        

        if nextoffset != -1:
            yield response.follow(
                url=f"https://www.scoopwhoop.com/api/v4/read/all/?offset={nextoffset}&limit=100", 
                callback=self.parse
            )