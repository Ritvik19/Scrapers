import scrapy, json

class SnippetsSpider(scrapy.Spider):
    name = "snippets"

    def start_requests(self):
        urls = [
            'https://www.tutorialspoint.com/programming_examples/'+str(i) for i in range(1, 8402)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pagenum = response.url.split('/')[-1]
        for i, snippet in enumerate(response.css('div.qa_post')):
            dct = {}
            try:
                dct['code'] = snippet.css('pre::text').get()
            except Exception as e:
                dct['code'] = e
            try:
                dct['language'] = snippet.css('span::text').get()
            except Exception as e:
                dct['language'] = e
            try:
                dct['title'] = snippet.css('a::text').getall()
            except Exception as e:
                dct['title'] = e
            with open(pagenum+'-'+str(i)+'.json', 'w') as f:
                json.dump(dct, f)
            yield dct
