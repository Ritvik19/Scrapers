import scrapy

class Books(scrapy.Spider):
    name = 'books'

    def start_requests(self):
        urls = ['http://books.toscrape.com/catalogue/page-'+str(i)+'.html' for i in range(1,51)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'name': book.css('a::text').get(),
                'price': book.css('p.price_color::text').get(),
                'rating': book.css('p.star-rating::attr(class)').get().split()[1],
            }
