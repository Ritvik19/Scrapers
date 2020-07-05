# -*- coding: utf-8 -*-
import scrapy, json


class StoriesSpider(scrapy.Spider):
    name = 'stories'
    allowed_domains = ['www.theweek.in']
    start_urls = [
        'https://www.theweek.in/content/week/news/india/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
        'https://www.theweek.in/content/week/news/world/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
        'https://www.theweek.in/content/week/news/biz-tech/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
        'https://www.theweek.in/content/week/news/sports/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
        'https://www.theweek.in/content/week/news/sci-tech/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
        'https://www.theweek.in/content/week/news/leisure/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
        'https://www.theweek.in/content/week/news/entertainment/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
        'https://www.theweek.in/content/week/news/health/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
        'https://www.theweek.in/content/week/news/education/_jcr_content/col_leftparaside/commonlisting.results.showmore.0.10.json',
    ]

    def parse(self, response):
        try:
            jsonresponse = json.loads(response.text)
            articles = json.loads(jsonresponse['articleList'])
            
            for article in articles:
                yield {
                    'title': article['pageTitle'],
                    'description': article['description'],
                    'url': article['url'],
                    'section': article['sectionName']
                }
            
            if jsonresponse['showMore'] == True:
                url_chunks = response.request.url.split('.')
                nextpage = '.'.join(url_chunks[:-3]+[str(int(url_chunks[-3])+10)]+url_chunks[-2:])
                yield response.follow(
                    url=nextpage,
                    callback=self.parse
                )
        except Exception as e:
            with open('errorlogs.txt', 'a') as f:
                    f.write(f'{e}: {response.request.url}')
