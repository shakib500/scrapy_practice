# -*- coding: utf-8 -*-
import scrapy
import scrapy
import os
import csv
import glob
import MySQLdb


class RaynsaggSpider(scrapy.Spider):
    name = 'raynsAgg'
    allowed_domains = ['ryanscomputers.com']
    start_urls = ['https://ryanscomputers.com/components/processor.html']

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
        yield scrapy.Request(next_page_url)

    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'),key=os.path.getctime)
        # print (csv_file)
        mydb = MySQLdb.connect(host='localhost',
                                user='root',
                                passwd='01923619725',
                                db='aggregator')
        cursor = mydb.cursor()
        csv_data = csv.reader(file(csv_file))

        row_count = 0
        for row in csv_data:
            if row_count != 0:
                pass
                # cursor.execute('INSERT IGNORE INTO  ')
            row_count += 1
        mydb.commit()
        cursor.close()
