# coding=utf-8

import scrapy
import re
import czlscrape.loaders as loaders
import czlscrape.items as items

import czlscrape.helpers as helpers


class CulturaSpider(scrapy.Spider):

    """www.cultura.ro

   FIELDS CRAWLED:
   documents, title
    """

    name = 'cultura'
    def start_requests(self):
        url = 'http://www.cultura.ro/proiecte-acte-normative'
        yield scrapy.Request(url)

    def parse(self, response):
        for entry in response.css('#recomended-articles .recommended-title'):
            href = entry.css('a::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(href), self.parse_entry)

    def parse_entry(self, response):
        publication_loader = loaders.PublicationLoader(
            items.PublicationItem())

        post = response.css('.post-content')

        post_title = post.css('.post-title').xpath('.//text()').extract_first()
        publication_loader.add_value('title', post_title)

        documents = []
        for anchor in post.css('a'):
            href = anchor.css('::attr(href)').extract_first()
            url = response.urljoin(href)
            if helpers.checkers.is_document(url):
                name = anchor.css('::text').extract_first()
                document = {
                    name: name,
                    url: url
                }
                documents.append(document)
        publication_loader.add_value('documents', documents)

        yield publication_loader.load_item()
