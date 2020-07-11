# -*- coding: utf-8 -*-
import scrapy, json


class FinanceAccountsInvestmentBankingJobsSpider(scrapy.Spider):
    name = 'finance-accounts-investment-banking-jobs'
    allowed_domains = ['shine.com']
    start_urls = ['https://www.shine.com/api/v2/search/simple/?csrfmiddlewaretoken=wvVFtnOPyKpm1D2wDHPDR8qeh4hBXIfOkeTnR1rPHk5N0j7QtXkhBW4HM0ut5xw5&swsv=&swse=&page=2&active=&rectype=&sort=&q=&loc=&minexp=&minsal=&area=10007&ind=&rcount=256&rstart=1&best_matches_ajax=&search_type=simple&jobid=']

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
