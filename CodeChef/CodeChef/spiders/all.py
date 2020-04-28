import scrapy

class AllSpider(scrapy.Spider):
    name = 'all'

    allowed_domains = ['www.codechef.com/problems']
    start_urls = [
        'https://www.codechef.com/problems/school',
        'https://www.codechef.com/problems/easy/',
        'https://www.codechef.com/problems/medium/',
        'https://www.codechef.com/problems/hard/',
        'https://www.codechef.com/problems/challenge/',
        'https://www.codechef.com/problems/extcontest/'
    ]

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