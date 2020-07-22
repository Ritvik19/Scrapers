# -*- coding: utf-8 -*-
import scrapy, json
from distutils.version import LooseVersion

class PackagedependencySpider(scrapy.Spider):
    name = 'packagedependency'
    allowed_domains = ['pypi.org']

    def __init__(self, package='', **kwargs):
        self.start_urls = [f'https://pypi.org/pypi/{package}/json'] 
        self.package=package
        super().__init__(**kwargs)

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        
        for version in sorted(jsonresponse['releases'].keys(), key=LooseVersion, reverse=True):
            yield response.follow(
                url=f'https://pypi.org/pypi/{self.package}/{version}/json',
                callback=self.parse_dependencies, meta={'version': version}
            )
            
    def parse_dependencies(self, response):
        jsonresponse = json.loads(response.text)
        yield {
            'version': response.request.meta['version'],
            'dependencies': jsonresponse['info']['requires_dist']
        }
