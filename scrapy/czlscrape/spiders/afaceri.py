import scrapy
import re
import czlscrape.loaders as loaders
import czlscrape.items as items


class AfaceriSpider(scrapy.Spider):

    """www.aippim.ro

   FIELDS CRAWLED:
   date, documents, institution, title
    """

    name = 'afaceri'
    def start_requests(self):
        url = str('http://www.aippimm.ro/categorie/'
                  'transparenta-decizionala---modificare-hg-96-2011/')
        yield scrapy.Request(url)

    def parse(self, response):
        for article in response.css('.article_container'):
            link = article.css('a.lead_subcat')
            title = ''.join(link.xpath('.//text()').extract())
            # TODO Log warning.
            if not title:
                continue
            date_extract = ''.join(article.xpath(
                './ul[contains(@class, \'lead\')]//text()').extract())
            date_match = re.search(
                r'(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})$',
                date_extract,
            )
            date = "{year}-{month}-{day}".format(**date_match.groupdict())

            documents = [{
                    'type': href.split('.')[-1],
                    'url': href,
                } for href in article.css('a.files::attr(href)').extract()]

            publication_loader = loaders.PublicationLoader(
                items.PublicationItem())

            publication_loader.add_value('date', date)
            publication_loader.add_value('documents', documents)
            publication_loader.add_value('institution', AfaceriSpider.name)
            publication_loader.add_value('title', title)

            yield publication_loader.load_item()
