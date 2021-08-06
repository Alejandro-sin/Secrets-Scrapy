import scrapy

class CiaSpider(scrapy.Spider):
    name = 'cia'
    url = 'https://www.cia.gov/readingroom/historical-collections/'
    url_cosntruct = 'https://www.cia.gov/readingroom'
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
        relative_links = response.xpath('//ul[@class="menu"]/li[@class="leaf"]/a/@href').getall()
        r = str(response)
        r = r.replace('200 ','')
        r = r.replace('/historical-collections/','')
        for r_link in relative_links:
            # response.urljoin(link) Construye el link del articulo del que queremos scrapear titulo y contenido.
            link = r.join(r_link)
            yield response.follow(link, callback=self.parse_link)


    def parse_link(self, response,**kwargs):
        # link =kwargs['url'] # Le digo que recibo diccionarios que tienen un key de 'url'.
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]/p[not(@class)]/text()').getall()
        yield {
            'title': title,
            'body': paragraph
            }
""" 
    def parse(self, response):
        links_declassified = response.xpath('//a[starts-with(@href,"collection") and (parent::h3|parent::h2)]/@href').getall()
        for link in links_declassified:
            # response.urljoin(link) Construye el link del articulo del que queremos scrapear titulo y contenido.
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})


    def parse_link(self, response,**kwargs):
        link =kwargs['url'] # Le digo que recibo diccionarios que tienen un key de 'url'.
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]/p[not(@class)]/text()').getall()
        yield {
            'url':link,
            'title': title,
            'body': paragraph
            }

 """

