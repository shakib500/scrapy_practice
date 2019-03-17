# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class RaynsaggSpider(scrapy.Spider):
    name = 'raynsAgg'
    allowed_domains = ['ryanscomputers.com']
    start_urls = ['https://ryanscomputers.com/components/processor.html','https://ryanscomputers.com/components/mainboard.html','https://ryanscomputers.com/components/graphics-card.html']

    def parse(self, response):
        processor_details = response.xpath('//*[@class="item col-lg-4 col-md-4 col-sm-6"]')

        for processor in processor_details:
            name = processor.xpath('.//h2/a/text()').extract_first()
            price = processor.xpath('.//*[@class="price"]/text()').extract_first()
            url = processor.xpath('//*[@class="product-name"]/a/@href').extract_first()
            img = processor.xpath('//*[@class="product-image"]/img/@src').extract_first()
            # print ('\n')
            # print (name)
            # print (price)
            # print ('\n')
            yield{'Name': name,
                  'Price': price,
                  'Url': url,
                  'Img': img }

        next_page_url = response.xpath('//*[@class="next i-next"]/@href').extract_first()
        # yield scrapy.Request(next_page_url)
        if next_page_url:
            yield scrapy.Request(next_page_url)
