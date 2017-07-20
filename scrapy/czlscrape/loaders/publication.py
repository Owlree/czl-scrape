from scrapy.loader import ItemLoader
import scrapy.loader.processors as processors


class PublicationLoader(ItemLoader):
    default_output_processor = processors.TakeFirst()
