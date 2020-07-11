# -*- coding: utf-8 -*-
import scrapy, json


class AccountingJobsSpider(scrapy.Spider):
    name = 'accounting-jobs'
    allowed_domains = ['shine.com']
    start_urls = ['https://www.shine.com/api/v2/search/simple/?csrfmiddlewaretoken=6G1Q9f2CZXmw31XZhD4ohpqT4upYCdZjUpZyxTFC8x2X2H2j7Tz21d4mzqCQK2gA&swsv=&swse=&page=1&active=&rectype=&sort=&q=accounting&loc=&minexp=&minsal=&area=&ind=&rcount=782&rstart=1&best_matches_ajax=&search_type=simple&jobid=']

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        
        for result in jsonresponse['results']:
            yield{
                'job_title': result['jJT'],
                'company': result['jCName'],
                'tag': result['jInd'],
                'min_salary': result['jSalMinID'],
                'max_salary': result['jSalMaxID'],
                'locations': ', '.join(result['jLoc']),
                'keywords': result['jKwd'],
                'experience': result['jExp'],
                'description': result['jJDT'],
                'slug': result['jSlug'],
                'exp_date': result['jExpDate']
            }
        
        nextpage = jsonresponse['next']
        
        if nextpage is not None:
            yield response.follow(url=nextpage, callback=self.parse)
