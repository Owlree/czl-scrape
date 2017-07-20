import scrapy


class PublicationItem(scrapy.Item):
    contact = scrapy.Field()
    date = scrapy.Field()
    description = scrapy.Field()
    documents = scrapy.Field()
    feedback_days = scrapy.Field()
    identifier = scrapy.Field()
    institution = scrapy.Field()
    max_feedback_date = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
