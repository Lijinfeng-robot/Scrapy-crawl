import scrapy
from fengniaops.items import FengniaopsItem


class FnpsSpider(scrapy.Spider):
    name = 'fengniao'
    allowed_domains = []
    start_urls = ['https://photo.fengniao.com']

    # def parse(self, response):
    #     for href in response.xpath('//div[@class="picList"]/ul/li[@class="noRight"]/a/@href').extract():
    #         yield scrapy.Request(url='https://photo.fengniao.com'+href, callback=self.get_parse, dont_filter=True)

    def parse(self, response):
        image = response.xpath('/html/body/div[@class="picList"]/ul/li[@class="noRight"]/a/@style').extract()
        for i in image:
            item = FengniaopsItem()
            img = i[23:-43]
            item['imgurl'] = [img]
            yield item

        # next_page = response.xpath('/html/body/div[@class="picList"]/ul/li[@class="noRight"]/a/@style').extract()
        #
        # if next_page:
        #     url = 'https://photo.fengniao.com' + next_page[0]
        #     yield scrapy.Request(url, callback=self.get_parse)
