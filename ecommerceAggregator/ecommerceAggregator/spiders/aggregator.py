# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class AggregatorSpider(scrapy.Spider):
    name = 'aggregator'
    allowed_domains = ['www.startech.com.bd']
    start_urls = ['https://startech.com.bd/component/processor','https://www.startech.com.bd/component/motherboard','https://www.startech.com.bd/component/graphics-card']

    def parse(self, response):
        processor_details = response.xpath('//*[@class="col-xs-12 col-md-4 product-layout grid"]')
        # motherboard_details = response.xpath('//*[@class="col-xs-12 col-md-4 product-layout grid"]')
        for processor in processor_details:
            name = processor.xpath('.//h4/a/text()').extract_first()
            price = processor.xpath('.//*[@class="price space-between"]/span/text()').extract_first()
            url = processor.xpath('.//h4/a/@href').extract_first()
            img = processor.xpath('.//*[@class="img-holder"]/a/img').extract_first()
            # print ('\n')
            # print (name)
            # print (price)
            # print ('\n')
            yield{'Name': name,
                  'Price': price,
                  'Url':url,
                  'Img' :img }
        # absolute_next_page_url = response.urljoin(next_page_url)
        next_page_url = response.css('.pagination li:last-child a::attr(href)').extract_first()

        if next_page_url:
            yield scrapy.Request(next_page_url)
