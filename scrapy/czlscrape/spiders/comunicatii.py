import scrapy

class ComunicatiiSpider(scrapy.Spider):
    name = 'comunicatii'
    def start_requests(self):
        url = 'http://www.comunicatii.gov.ro/?page_id=3517'
        yield scrapy.Request(url)

    def parse(self, response):
        for column in response.css('div.vc_column_container'):
            for p in column.css('p'):
                print(p.extract())
