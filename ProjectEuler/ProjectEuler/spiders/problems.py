import scrapy

class ProblemsSpider(scrapy.Spider):
    name = 'problems'

    def start_requests(self):
        urls = ['https://projecteuler.net/problem='+str(i) for i in range(1,706)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'title': response.xpath('//h2[1]/text()').get(),
            'description': ' '.join(response.xpath('//div[@class="problem_content"]//text()').getall()),
        }
