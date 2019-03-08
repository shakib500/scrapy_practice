# -*- coding: utf-8 -*-
import scrapy


class AggregatorSpider(scrapy.Spider):
    name = 'aggregator'
    allowed_domains = ['www.startech.com.bd']
    start_urls = ['https://startech.com.bd/component/processor']

    def parse(self, response):
        processor_details = response.xpath('//*[@class="col-xs-12 col-md-4 product-layout grid"]')
        for processor in processor_details:
            name = processor.xpath('.//h4/a/text()').extract_first()
            price = processor.xpath('.//*[@class="price space-between"]/span/text()').extract_first()
            print ('\n')
            print (name)
            print (price)
            print ('\n')
        # absolute_next_page_url = response.urljoin(next_page_url)
        next_page_url = response.css('.pagination li:last-child a::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(next_page_url)
        # yield scrapy.Request(next_page_url, callback=self.parse_next_page)

    # def parse_next_page(self, response):
    #     # next_page_url = response.xpath('//*[@class="pagination"]/li/a/@href').extract_first()
    #     self.logger.info("Visited %s", response.url)
    #     # yield scrapy.Request(next_page_url)
