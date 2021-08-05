import scrapy


class CiaSpider(scrapy.Spider):
    name = 'cia'
    allowed_domains = ['https://www.cia.gov/readingroom/historical-collections']
    start_urls = ['http://https://www.cia.gov/readingroom/historical-collections/']

    def parse(self, response):
        
        # Usar la misma lógica de links para extraer en ho usar los wild cards.
        title = response.xpath('//div[@class="field-item even"]/h3/a/text()').getall()
        #response.xpath('//div[@class="field-item even"]/*/a/text()').getall()
        abstract = response.xpath('//div[@class="field-item even"]/h3/p/text()').getall()
        links = response.xpath('//a[starts-with(@href,"collection") and (parent::h3|parent::h2)]/@href').getall()


        pass
