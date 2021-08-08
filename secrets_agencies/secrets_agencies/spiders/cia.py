import scrapy

class CiaSpider(scrapy.Spider):
    name = 'cia'
    url = 'https://www.cia.gov/readingroom/historical-collections/'
    start_urls = [url]
    ustom_settings = {
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
                'item_export_kwargs': {
                    'export_empty_fields': True,
                },
            },
        },
    }

    def parse(self, response):
        url_cosntruct = 'https://www.cia.gov/'
        relative_links = response.xpath('//ul[@class="menu"]/li[@class="leaf"]/a/@href').getall()
        for l in relative_links:
            link = url_cosntruct  + l
            yield response.follow(link, callback=self.parse_link)


    def parse_link(self, response,**kwargs):
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]/p[not(@class)]/text()').getall()
        docs = response.xpath('//div[@class="views-field views-field-title"]/h4/a/text()').getall()
        yield {
            'title': title,
            'body': paragraph,
            'documents': docs
            }


